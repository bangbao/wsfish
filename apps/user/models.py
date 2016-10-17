# coding: utf-8

import time
import datetime

import settings
from lib.db import ModelBase
from lib.db.redisdb import RedisRankModelBase, RedisHashModelBase, make_redis_client
from lib.utils.generator import trans_uid, salt_generator
from apps.config import game_config
from . import consts
from . import logics


def get_redis_userd_memory(server_id):
    """获取分服数据库状态
    """
    # 创建新的分服没生效时，进程中servers配置没更新， 此时取不到redis, 所以跳出
    if server_id == '00':
        redis = AccountToken.get_redis_client('key', server_id)
    elif server_id in game_config.servers:
        redis = ModelBase.get_redis_client('key', server_id)
    else:
        return '0M/0M/0G'
    info = redis.info()
    return '%s/%s/%sG' % (info.get('used_memory_human'),
                          info.get('used_memory_peak_human'),
                          '%0.2f' % (info.get('used_memory_rss', 0) / 1024.0 ** 3))


class AccountToken(ModelBase):
    """用户注册账户account生成游戏唯一token
    Attributes:
        account: 用户注册用户名
        password: 用户密码（md5)
        token: 用户游戏TOKEN
    """
    DATABASE_NAME = 'master'

    def __init__(self, uid=None):
        self.uid = uid
        self._attrs = {
            'account': '',
            'password': '',
            'token': '',
        }
        super(AccountToken, self).__init__(self.uid)

    @classmethod
    def create(cls, account, password):
        """创建一个新账号对象
        """
        obj = super(AccountToken, cls).get(account)
        obj.account = account
        obj.password = password
        obj.token = account
        obj.save()
        return cls.get(account)

    @classmethod
    def get(cls, account):
        obj = super(AccountToken, cls).get(account)
        if obj.token:
            return obj

    @classmethod
    def get_or_create(cls, account, password):
        obj = cls.get(account)
        if not obj:
            obj = cls.create(account, password)
        return obj


class Footprint(ModelBase):
    """用户token对应的分服关系
    """
    DATABASE_NAME = 'master'

    def __init__(self, uid=None):
        self.uid = uid
        self._attrs = {
            'data': {},     # {server_id: access_time}
            'servers': {},  # {server_id: uid}
            'salt': '',     # 每次登录生成的salt值
            'award_sp_uid': '',   # 内测奖励对应的uid
            'award_sp_got': 0,   # 内测奖励领取code_id标识
            'award_sp2_pay_dates': [],    # 返还支付天数
            'award_sp2_pay_rmbs_got': 0,  # 支付返还
            'award_sp2_vip_item': 0,      # vip等级返还
            'award_sp3_pay_dates': [],    # 返还支付天数
            'award_sp3_pay_rmbs_got': 0,  # 支付返还
            'award_sp3_vip_item': 0,      # vip等级返还
            'award_sp4_vip_item': 0,      # vip等级返还
        }
        super(Footprint, self).__init__(self.uid)

    @classmethod
    def get_server_foot(cls, user_token):
        """获取存储数据
        """
        obj = cls.get(user_token)
        return obj.data

    @classmethod
    def mark_footprint(cls, user_token, server_id, uid):
        # 用户登陆服务器足迹
        obj = cls.get(user_token)
        obj.data[server_id] = int(time.time())
        obj.servers[server_id] = uid
        # 记录首次创建的用户uid
        if not obj.award_sp_uid:
            obj.award_sp_uid = uid
        obj.save()
        return obj

    @classmethod
    def get_footprint(cls, user_token, length=None, now=None):
        if not user_token:
            return []
        now = now or time.strftime('%Y-%m-%d %H:%M:%S')
        server_foot = cls.get_server_foot(user_token)
        # 按登陆时间倒序排序
        server_list = sorted(server_foot, key=lambda x: server_foot[x], reverse=True)
        if length:
            server_list = server_list[:length]

        return [game_config.servers[server_id] for server_id in server_list
                if server_id in game_config.servers and game_config.servers[server_id]['open_time'] < now]

    @classmethod
    def create_salt(cls, user_token):
        obj = cls.get(user_token)
        obj.setattr(salt=salt_generator())
        obj.save()
        return obj.salt

    @classmethod
    def get_salt(cls, user_token):
        obj = cls.get(user_token)
        return obj.salt


class TokenServerUid(ModelBase):
    """游戏TOKEN到游戏UID映射
    Attributes:
        uid: 用户游戏UID
        token: 用户TOKEN
        server_id: 用户分服ID
    """
    DATABASE_NAME = 'master'
    redis = make_redis_client(settings.DATABASES['master'])
    # set结构： server_id: token集合列表
    GAME_SERVER_TOKEN_SET_KEY = 'game_server_token_set'
    # hash结构： server_id: 人数
    GAME_USER_COUNT_KEY = 'game_user_count'

    def __init__(self, uid, token, server_id, account=''):
        self.uid = uid
        self.token = token
        self.server_id = server_id
        self.account = account

    @classmethod
    def all(cls, token=None, server_id=None):
        """根据token获取所有分服uid, 或者根据分服id获取此分服所有uid
        """
        if token:
            return (obj['uid'] for obj in cls.all_by_token(token))
        if server_id:
            return (obj['uid'] for obj in cls.all_by_server(server_id))
        return (obj['uid'] for obj in cls.all_obj())

    @classmethod
    def all_by_token(cls, token):
        """根据token获取所有用户
        """
        server_foot = Footprint.get_server_foot(token)
        for server_id in server_foot:
            key = cls.make_key(token, server_id)
            obj = cls.redis.hgetall(key)
            if obj:
                yield obj

    @classmethod
    def all_by_server(cls, server_id):
        """根据分服id获取此分服所有用户
        """
        server_token_key = cls.make_key(cls.GAME_SERVER_TOKEN_SET_KEY, server_id)
        members = cls.redis.smembers(server_token_key)
        for token in members:
            key = cls.make_key(token, server_id)
            obj = cls.redis.hgetall(key)
            if obj:
                yield obj

    @classmethod
    def all_obj(cls):
        """取出所有用户
        """
        for server_id in game_config.servers:
            server_token_key = cls.make_key(cls.GAME_SERVER_TOKEN_SET_KEY, server_id)
            members = cls.redis.smembers(server_token_key)
            for token in members:
                key = cls.make_key(token, server_id)
                obj = cls.redis.hgetall(key)
                if obj:
                    yield obj

    @classmethod
    def bind_token_server_uid(cls, token, server_id, uid):
        """
        """
        key = cls.make_key(token, server_id)
        obj = cls.redis.hgetall(key)
        if obj:
            obj['old_uid'] = obj['uid']
            obj['uid'] = uid
            cls.redis.hmset(key, obj)
            return True
        return False

    @classmethod
    def make_key(cls, token, server_id):
        return '%s%s||%s' % (settings.KEY_PREFIX, token, server_id)

    @classmethod
    def get(cls, token, server_id='00'):
        key = cls.make_key(token, server_id)
        obj = cls.redis.hgetall(key)
        if obj:
            return cls(obj['uid'], obj['token'], obj['server'], obj.get('account', ''))

    @classmethod
    def create(cls, token, server_id, prefix, account=''):
        if server_id not in game_config.servers:
            if server_id != '00':
                raise Exception('user.models: server_token: %s not exists' % server_id)

        cls.record_server_token(server_id, token)
        count = cls.incrby_user_count(server_id, prefix)
        uid = trans_uid(count, server_id, prefix)
        obj = {'uid': uid,
               'token': token,
               'server': server_id,
               'account': account}
        cls.redis.hmset(cls.make_key(token, server_id), obj)

        return cls.get(token, server_id)

    @classmethod
    def get_or_create(cls, token, server_id, prefix, account=''):
        obj = cls.get(token, server_id)
        if not obj:
            obj = cls.create(token, server_id, prefix, account)
        return obj

    @classmethod
    def record_server_token(cls, server_id, token):
        """记录分服所有的token
        """
        key = cls.make_key(cls.GAME_SERVER_TOKEN_SET_KEY, server_id)
        cls.redis.sadd(key, token)

    @classmethod
    def incrby_user_count(cls, server_id, prefix=None, amount=1):
        """分服用户记数
        """
        server_user_count = cls.redis.hincrby(cls.GAME_USER_COUNT_KEY, server_id, amount)
        if prefix:
            platform_key = '%s%s' % (prefix, server_id)
            cls.redis.hincrby(cls.GAME_USER_COUNT_KEY, platform_key, amount)
        return server_user_count

    @classmethod
    def get_user_count(cls, server_id=None, platform=None):
        """获取分服用户数量
        """
        if server_id and not platform:
            return cls.redis.hget(cls.GAME_USER_COUNT_KEY, server_id)
        if server_id and platform:
            platform_key = '%s%s' % (platform, server_id)
            return cls.redis.hget(cls.GAME_USER_COUNT_KEY, platform_key)
        return cls.redis.hgetall(cls.GAME_USER_COUNT_KEY)


class BaseM(ModelBase):
    """存储用户账号数据
    """
    def __init__(self, uid):
        self.uid = uid
        self._attrs = {
                'token': '',     # 对应的账号token
                'platform': '',  # 对应的平台标识
                'deviceid': '',    # 最新设备标识
                'leader': 1,     # 注册时选择的user_select索引
                'username': '',  # 昵称
                'logo': 1,       # 球队标志， 用户注册时选择
                'regist_time': 0,     # 注册时间戳
        }
        super(BaseM, self).__init__(uid)


class UserM(ModelBase):
    """存储用户常用数据
    """
    def __init__(self, uid):
        self.uid = uid
        self._attrs = {
                'token': '',     # 对应的账号token
                'token_salt': '', # 平台登陆后的校验标识
                'platform': '',  # 对应的平台标识
                'deviceid': '',    # 最新设备标识
                'is_ban': 0,     # 是否封号， 0未封号， 1已封号
                'leader': 1,     # 注册时选择的user_select索引
                'username': '',  # 昵称
                'logo': 1,       # 球队标志， 用户注册时选择
                'level': 1,      # 等级
                'exp': 0,        # 经验
                'vip': 0,        # vip等级
                'vip_exp': 0,    # vip经验，即充值的coin数
                'coin': 0,       # 总钻石数
                'coin_type': {}, # 钻石来源 [1.充值获得 2.系统赠送 3.运营投放(激活码/礼包/邮件礼品/后台添加钻石)]
                'money': 0,      # 钱数（游戏内钱）
                'energy': 0,     # 体力，精力
                'battle': 0,     # 战力
                'lottery': 0,     # 奖券
                'energy_fill_at': 0,  # 体力恢复时间戳
                'battle_fill_at': 0,  # 战力恢复时间戳
                'point_fill_at': 0,   # 积分恢复时间戳
                'regist_time': 0,     # 注册时间戳
                'active_time': 0,     # 最后活跃时间戳
                'loading_time': 0,    # 进入主页时间戳
                'login_days': [],      # 登陆日期记录
                'continue_days': [],   # 连续登陆日期记录
                'last_date': '',      # 更新日期
                'robmoney': 0,    # 今日强夺的钱
                'honor': 0,       # 荣誉点
                'point': 0,       # 锦标赛点数(积分)
                'expense': {},    # 次数消费coin记录
                'guide': {},      # 新手引导
                'first_pays': {},    # 首充标识
                'potential_point': 0,       # 潜力点
                'cards_top_extend': 0,      # 卡牌背包数量上限扩展
                'equips_top_extend': 0,     # 装备背包数量上限扩展
                'exp_percent': 0.0,         # 昨天级别提供的经验百分比加成
                'strategy': 1,              # 当前战术
                'strategys': {1:1},         # 拥有的战术
                'alert_strategy': 0,        # 新战术是否解锁
                'low_lv_energy': 0,         # 等级升级前的体力
                'low_lv_battle': 0,         # 等级升级前的战力
                '_ability': 0,              # 缓存的实力
                '_max_ability': 0,          # 缓存的有史以来最大实力
                '_yestoday_max_ability': 0, # 缓存的昨日最大实力
                '_today_max_ability': 0,    # 缓存的今日最大实力
                '_core_player': {},         # 缓存的战术核心最牛队员配置ID
                '_arena_rank': 0,           # 缓存的竞技排名
                '_max_arena_rank': 0,       # 缓存的历史最高竞技排名
                '_foreign_id': None,        # 当前正在使用的外援id
                '_old_asj': None,           # 旧的编队激活的联携技能id, 赋值后为list
                '_new_asj': None,           # 新的编队激活的联携技能id, 赋值后为list
                #'_team_formation': '',      # 缓存的战斗编队
                '_pay_award': {},           # 支付时缓存定单数据
        }
        super(UserM, self).__init__(uid)

    @property
    def ability(self):
        if not self._ability:
            self.weak_user.update_user_cache_data()
        return self._ability

    @property
    def max_ability(self):
        return max(self._ability, self._max_ability)

    @property
    def yestoday_max_ability(self):
        return self._yestoday_max_ability

    @property
    def today_max_ability(self):
        return self._today_max_ability

    @property
    def core_player(self):
        if not self._core_player:
            self.weak_user.update_user_cache_data()
        return self._core_player

    @property
    def arena_rank(self):
        #if not self._arena_rank:
        #    self.changed = True
        #    self._arena_rank = self.weak_user.arena_rank.rank or 0
        return self._arena_rank

    @property
    def max_arena_rank(self):
        if not self._max_arena_rank:
            return self._arena_rank
        return self._max_arena_rank

    def set_arena_rank(self, arena_rank):
        self.changed = True
        self._arena_rank = arena_rank
        if not 0 < self._max_arena_rank < self._arena_rank:
            self._max_arena_rank = self._arena_rank

    def is_foreign_expired(self):
        # 外援是否到期了
        #return not self._foreign_id
        return not self.weak_user.foreign_aid.foreign_id

    def cache_active_skill_jointly(self, new_asj):
        # 缓存编队激活的联携id
        self.changed = True
        if self._old_asj is None or self._new_asj is None:
            self._old_asj = self._new_asj = new_asj
        else:
            self._old_asj = self._new_asj
            self._new_asj = new_asj

    def diff_active_skill_jointly(self):
        # 获取不同的联携id
        if self._new_asj is not None and self._old_asj is not None:
            diff = set(self._new_asj) - set(self._old_asj)
            return list(diff)
        return []

    # def cache_team_formation(self, team_formation):
    #     # 缓存战斗编队加成后数据
    #     self.changed = True
    #     self._team_formation = '' #repr(team_formation)
    #
    # def get_cache_team_formation(self):
    #     # 获取缓存的战斗编队数据
    #     if self._team_formation:
    #         return eval(self._team_formation)

    def cache_pay_award(self, obj, award={}):
        # 缓存充值的订单数据
        self.changed = True
        self._pay_award['order_data'] = {'goods_id': obj['product_id'], 'order_money': obj['order_money']}
        self._pay_award['award'] = award

    def pop_pay_award(self):
        # 取出并删除缓存的订单数据
        pay_award = dict(self._pay_award)
        self.changed = True
        self._pay_award = {}
        return pay_award

    def pre_use(self):
        """加载该模块时需要预先处理一部分数据
        """
        # 未注册用户不更新数据
        if not self.regist_time:
            return
        current_time = int(time.time())
        today = time.strftime('%Y-%m-%d')

        # 临时兼容 !!
        if self.coin > 0 and self.coin_type == {}:
            self.changed = True
            self.coin_type = {
                3: self.coin
            }

        if self.last_date != today:
            self.changed = True
            self.last_date = today
            self.robmoney = 0
            self.expense = {}
            self._yestoday_max_ability = self._today_max_ability
            self.exp_percent = self.calc_new_exp_percent()
        # 经验加成值
        if not self.exp_percent:
            self.changed = True
            self.exp_percent = self.calc_new_exp_percent()

        self.timed_fill_energy(current_time)
        self.timed_fill_battle(current_time)
        self.timed_fill_point(current_time)

    def calc_new_exp_percent(self):
        """计算新的经验加成
        Returns:
            经验加成值(转换成百分浮点数)
        """
        conf = game_config.user_functrl.get(consts.USER_FUNCTRL_TASK, {})
        open_level = conf.get('lv', 1)
        used_level = max(open_level, self.level)
        need_exp = game_config.user_info[used_level]['exp']
        return need_exp * 0.01

    def timed_fill_energy(self, current_time):
        """定时补充用户体力
        Args:
           current_time: 当前时间
        """
        energy_grow = game_config.user_ini['energy_grow']*60
        differ = current_time - self.energy_fill_at
        quotient, remainder = divmod(differ, energy_grow)
        energy_top = self.get_energy_top()

        if quotient > 0:
            if self.energy < energy_top:
                energy = self.energy + quotient * consts.ENERGY_HEAL_UNIT
                energy = min(energy, energy_top)
                self.setattr(energy=energy)
            self.setattr(energy_fill_at=current_time - remainder)

    def timed_fill_battle(self, current_time):
        """定时补充用户战力
        Args:
           current_time: 当前时间
        """
        battlepoint_grow = game_config.user_ini['battlepoint_grow']*60
        differ = current_time - self.battle_fill_at
        quotient, remainder = divmod(differ, battlepoint_grow)
        battle_top = self.get_battle_top()

        if quotient > 0:
            if self.battle < battle_top:
                battle = self.battle + quotient * consts.BATTLE_HEAL_UNIT
                battle = min(battle, battle_top)
                self.setattr(battle=battle)
            self.setattr(battle_fill_at=current_time - remainder)

    def timed_fill_point(self, current_time):
        """ 定时增加用户竞技奖励
        """
        from apps.arena.logics import get_award_detail
        from apps.arena.consts import DEFAULT_PER_DELTA_SECONDS

        if not self.arena_rank or not self.point_fill_at:
            return

        config = get_award_detail(self.arena_rank, game_config)
        differ = current_time - self.point_fill_at
        quotient, remainder = divmod(differ, DEFAULT_PER_DELTA_SECONDS)

        if quotient > 0:
            self.incr_attr(point=quotient * config['per_tp'],
                           money=quotient * config['per_money'])
            self.setattr(point_fill_at=current_time - remainder)

    def loads(self, data):
        exclude_keys = set(('token', 'platform', 'deviceid', 'is_ban', 'username'))
        super(UserM, self).loads(data, exclude_keys)

    def setattr(self, **kwargs):
        """设定属性值，有上限的自动处理
        """
        self.changed = True
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)

    def incr_attr(self, **kwargs):
        # 经验独立处理
        exp = kwargs.pop('exp', None)
        if exp:
            self.add_exp(exp)

        # 单独处理钻石的消耗
        coin = kwargs.pop('coin', None)
        if coin:
            self.incr_coin(coin)

        for attr, value in kwargs.iteritems():
            new_value = getattr(self, attr) + value
            if attr == 'battle':
                new_value = min(new_value, self.get_battle_real_top())
            elif attr == 'energy':
                new_value = min(new_value, self.get_energy_real_top())
            self.setattr(**{attr:new_value})

    def incr_coin(self, coin, where=0, gacha_times=0):
        """单独处理钻石的消耗
        Args:
            coint: 消耗的钻石数量
            where: 消耗的途径
            gacha_times: 选秀次数(分1次、10次)
        """
        self.changed = True
        self.coin += coin

        if coin == 0:
            return

        if coin < 0:
            # 任务: 消耗钻石
            self.weak_user.do_task('subrecord', expend_num=-coin)
            # 消费有礼: 累计消耗钻石
            self.weak_user.active.add_consume_coin(-coin)
            # 消耗各类钻石
            self.reduce_coin_type(-coin, where, gacha_times)

        else:
            if where in [self.weak_user.GOODS_FROM_CHARGE]:
                self.coin_type.setdefault(1, 0)
                self.coin_type[1] += coin
            elif where in [self.weak_user.GOODS_FROM_CODE, self.weak_user.GOODS_FROM_TREASURE, \
                           self.weak_user.GOODS_FORM_NOTIFY, self.weak_user.GOODS_FROM_ADMIN]:
                self.coin_type.setdefault(3, 0)
                self.coin_type[3] += coin
            else:
                self.coin_type.setdefault(2, 0)
                self.coin_type[2] += coin

    def reduce_coin_type(self, coin, where, gacha_times):
        """消耗不同种类的钻石
        Args:
            coint: 消耗的钻石数量
            where: 消耗的途径
            gacha_times: 选秀次数(分1次、10次)
        Return:
            返回最新的coin_type
        """
        from apps.gacha import consts as gacha_consts

        type_3 = self.coin_type.get(3, 0)
        type_2 = self.coin_type.get(2, 0)
        type_1 = self.coin_type.get(1, 0)
        user = self.weak_user
        coin_times = user.gacha.coin1_coin_times
        coin10_times = user.gacha.coin10_gacha_times
        equip_times = user.gacha.equip1_coin_times
        equip10_times = user.gacha.equip10_gacha_times
        coin_detail = game_config.gacha[gacha_consts.GACHA_SORT_COIN_MIDDLE]
        coin10_detail = game_config.gacha[gacha_consts.GACHA_SORT_COIN10_MIDDLE]
        equip_detail = game_config.gacha_equip[gacha_consts.GACHA_SORT_EQUIP_MIDDLE]
        equip10_detail = game_config.gacha_equip[gacha_consts.GACHA_SORT_EQUIP10_MIDDLE]

        # 状元秀和抽装备单抽、十连抽， N抽之后消耗顺序1-2-3(根据概率决定首先消耗钻石的种类)
        if (where == user.GOODS_FROM_GACHA and \
                    ((gacha_times == 1 and coin_times > coin_detail['sp_num'][1]) or (gacha_times == 10 and coin10_times > coin10_detail['sp_num'][1])) \
           ) or \
           (where == user.GOODS_FROM_GACHA_EQUIP and \
                    ((gacha_times == 1 and equip_times > equip_detail['sp_num'][1]) or (gacha_times == 10 and equip10_times > equip10_detail['sp_num'][1])) \
           ):
            coin_type_list, first_type = self.reduce_first_type()
            coin_type_num = self.coin_type.get(first_type, 0)
            if coin_type_num >= coin:
                self.coin_type[first_type] -= coin
                return

            self.coin_type[first_type] = 0
            type_len = len(coin_type_list)
            if type_len == 1:
                return

            diff_num = coin - coin_type_num
            idx = coin_type_list.index(first_type)
            next_idx = idx+1 if idx != type_len-1 else 0
            next_type = coin_type_list[next_idx]
            next_type_num = self.coin_type.get(next_type, 0)
            if next_type_num >= diff_num:
                self.coin_type[next_type] -= diff_num
                return

            self.coin_type[next_type] = 0
            if type_len == 2:
                return

            diff_num2 = diff_num - next_type_num
            last_idx = next_idx+1 if next_idx != type_len-1 else 0
            last_type = coin_type_list[last_idx]
            last_type_num = self.coin_type.get(last_type, 0)
            if last_type_num >= diff_num2:
                self.coin_type[last_type] -= diff_num2
                return

            self.coin_type[last_type] = 0
            return

        # 状元秀和抽装备前N抽 和 非gacha，消耗顺序3-2-1
        if type_3 >= coin:
            self.coin_type[3] -= coin
            return

        if type_3 > 0:
            self.coin_type[3] = 0
        diff_num = coin - type_3
        if type_2 >= diff_num:
            self.coin_type[2] -= diff_num
            return

        if type_2 > 0:
            self.coin_type[2] = 0
        diff_num2 = diff_num - type_2
        if type_1 > 0:
            self.coin_type[1] -= diff_num2

        return

    def reduce_first_type(self):
        """首先消耗的钻石种类
        Return:
            消耗顺序, 首先消耗的钻石种类
        """
        from lib.utils import weight_choice

        chance_conf = game_config.type_diamond['chance']
        coin_data = self.weak_user.user_m.coin_type

        # 消耗顺序1-2-3
        have_coin_type = []
        if coin_data.get(1, 0) > 0:
            have_coin_type.append(1)
        if coin_data.get(2, 0) > 0:
            have_coin_type.append(2)
        if coin_data.get(3, 0) > 0:
            have_coin_type.append(3)

        new_chance_list = []
        for _type, _w in chance_conf:
            if _type in have_coin_type:
                new_chance_list.append((_type, _w))

        coin_type, _ = weight_choice(new_chance_list)

        return have_coin_type, coin_type

    def set_platform_and_deviceid(self, platform, deviceid):
        if platform and platform != self.platform:
            self.changed = True
            self.platform = platform

        if deviceid and deviceid != self.deviceid:
            self.changed = True
            self.deviceid = deviceid

    def incr_expense(self, cost_id, times=1):
        """增长消费次数记录
        记录的是已经消费的次数，下次消费的价格需要加1
        """
        self.changed = True
        if cost_id not in self.expense:
            self.expense[cost_id] = times
        else:
            self.expense[cost_id] += times

    def update_login_stats(self, ts=None):
        """更新登录状态
        Args:
            ts: 更新时间戳
        """
        now = int(time.time())
        self.changed = True
        today_date = datetime.date.today()
        last_date = datetime.date.fromtimestamp(self.active_time)
        if today_date > last_date:
            today_str = today_date.strftime('%Y-%m-%d')
            if (today_date - last_date).days == 1:
                if today_str not in self.continue_days:
                    self.continue_days.append(today_str)
            else:
                self.continue_days = [today_str]

            if today_str not in self.login_days:
                self.login_days.append(today_str)

        # 48小时后回归奖励
        if self.active_time and now - self.active_time >= 3600*48:
            self.weak_user.add_notify(self.weak_user.NOTIFY_FROM_PUSH_AWARD,
                                      gift=game_config.user_ini['push_award'])

        self.active_time = ts or now
        # 记录在线时间
        self.weak_user.online_rank.zadd(self.active_time)

    def filter_guide(self, goto=False):
        """过滤要进行的新手引导步骤
        Args:
            goto: 若是登录操作，需要重置引导状态
        returns:
            {}: 所有需要进行引导的状态
        """
        if settings.SKIP_GUIDE:
            return {}

        # 初始化新手引导第一步
        if not self.guide:
            min_step = min(game_config.guide_raw)
            # 直接从105步开始
            if min_step < 105:
                min_step = 105
            min_group = game_config.guide_raw[min_step]['sectiongroup']
            self.changed = True
            self.guide[min_group] = min_step

        need_guide = {}
        for sectiongroup, step in self.guide.items():
            # 已完成的不再发送数据
            if step >= max(game_config.guide_sectiongroup[sectiongroup]):
                continue
            # 步骤容错
            if step not in game_config.guide_raw:
                step = min(game_config.guide_sectiongroup[sectiongroup])
            # 有可能会跳转到下一个group
            config = game_config.guide_raw[step]
            if goto and step in game_config.guide_raw:
                goto_step = config['save']
                goto_group = game_config.guide_raw[goto_step]['guidegroup']
                need_guide[goto_group] = goto_step
                self.changed = True
                self.guide[sectiongroup] = goto_step
            else:
                need_guide[config['guidegroup']] = step

        return need_guide

    def do_guide(self, step, force=False):
        """记录新手引导步骤
        args:
            group: 模块分类
            step: 已完成的步骤
        """
        if step not in game_config.guide_raw:
            return
        sectiongroup = game_config.guide_raw[step]['sectiongroup']
        if force or step >= self.guide.get(sectiongroup, 0):
            self.changed = True
            self.guide[sectiongroup] = step

    def is_in_guide(self, full=False):
        """判断是否在引导中
        """
        max_step = max(self.guide.itervalues()) if self.guide else 100
        if not full:
            return max_step < self.get_first_max_step()
        else:
            return max_step + 1 in game_config.guide_raw

    def get_first_max_step(self):
        """第一阶段新手引导最大步数值, 写死
        """
        sorted_groups = sorted(game_config.guide)
        for group in sorted_groups:
            max_step = max(game_config.guide[group])
            if max_step + 1 not in game_config.guide_raw:
                return max_step

        return getattr(settings, 'GUIDE_FIRST_MAX_STEP', 132)

    def add_exp(self, exp):
        """增加经验值
        Args:
            exp: 增加的经验值
        """
        # 到最高级别后不在加经验
        if self.level + 1 not in game_config.user_info:
            return

        new_exp = self.exp + exp
        new_level = self.level
        new_energy = low_lv_energy = self.energy
        new_battle = low_lv_battle = self.battle

        config = game_config.user_info[new_level]

        while new_exp >= config['exp'] and new_level+1 in game_config.user_info:
            new_level += 1
            new_exp -= config['exp']
            config = game_config.user_info[new_level]
            # 超出上限不恢复
            if new_energy < config['energy']:
                new_energy = min(new_energy + config['add_energy'], config['energy'])
            if new_battle < config['battlepoint']:
                new_battle = min(new_battle + config['add_battlepoint'], config['battlepoint'])

        # 到最高级别后不在加经验
        if new_level + 1 not in game_config.user_info:
            new_exp = 0

        sum_exp = logics.get_levelup_exp(1, new_level, game_config)
        self.weak_user.exp_rank.zadd(sum_exp+new_exp, weight=True)

        # 等级变化时修改等级排行
        if self.level != new_level:
            self.weak_user.level_rank.zadd(new_level, weight=True)
            # 限时冲级活动
            self.weak_user.active.update_xscj_level(new_level)
            self.setattr(low_lv_energy=low_lv_energy, low_lv_battle=low_lv_battle)

        # 先升级再修改行动力，战力值，否则上限不准确
        self.setattr(level=new_level, exp=new_exp)
        self.setattr(energy=new_energy, battle=new_battle)

    def can_first_pay_gift(self, charge_config=None):
        """是否有首充奖励物品, 只用户第一次充值才给
        """
        return not self.first_pays

    def has_first_pay(self, show=False):
        """是否有首充状态并返回
        """
        if not show and self.first_pays:
            return consts.CHARGE_CONFIG_FIRST_PAY_NONE

        for _, charge_config in game_config.charge.iteritems():
            first_pay = self.is_first_pay(charge_config)
            if first_pay:
                return first_pay
        return consts.CHARGE_CONFIG_FIRST_PAY_NONE

    def is_first_pay(self, charge_config):
        """是否首充
        0非首充, 1首充双倍, 2 首充三倍
        """
        flag = consts.CHARGE_CONFIG_FIRST_PAY_NONE
        # 充值时判定此商品是否可享受首充
        if not charge_config['is_first']:
            return flag
        server_id = self.weak_user.server_id
        config = game_config.serverctrl.get(server_id)
        now = time.strftime('%Y-%m-%d')
        if config and config['first_pay'] and config['first_pay'] <= now:
            pay_at = self.first_pays.get(charge_config['cfg_id'])
            if pay_at < config['first_pay']:
                flag = consts.CHARGE_CONFIG_FIRST_PAY_HAVE
                # 首测用户大于20级三倍
                if not pay_at and self.token in game_config.award_sp and game_config.award_sp[self.token]['level'] >= 20:
                    flag = consts.CHARGE_CONFIG_FIRST_PAY_SP
        return flag

    def set_first_pay(self, charge_config):
        """设定首充状态
        """
        # 充值时判定此商品是否可享受首充
        if not charge_config['is_first']:
            return False
        server_id = self.weak_user.server_id
        config = game_config.serverctrl.get(server_id)
        now = time.strftime('%Y-%m-%d')
        if config and config['first_pay'] and config['first_pay'] <= now:
            self.changed = True
            self.first_pays[charge_config['cfg_id']] = config['first_pay']
            return True
        return False

    def add_vip_exp(self, add_exp):
        """加vip经验
        """
        new_exp = self.vip_exp + add_exp
        new_level = self.vip
        levelup = False

        while new_level + 1 in game_config.vip_function:
            config = game_config.vip_function[new_level+1]
            if new_exp >= config['charge_count']:
                new_level += 1
                levelup = True
            else:
                break

        self.setattr(vip=new_level, vip_exp=new_exp)
        # vip升级了
        if levelup:
            user = self.weak_user
            user.add_notify(user.NOTIFY_FROM_VIP_LEVELUP, viplv=new_level)

    @property
    def vip_function(self):
        """ 用户VIP相关配置
        """
        return game_config.vip_function[self.vip]

    @property
    def user_info(self):
        """ 用户基本信息数据配置
        """
        return game_config.user_info[self.level]

    def get_rent_top(self):
        """出租球员开启数量
        """
        return self.user_info['rent_num']

    def get_energy_top(self):
        """自动恢复精力的上限
        """
        return self.user_info['energy'] + self.vip_function['energy_add']

    def get_energy_real_top(self):
        """真正的上限
        """
        return self.user_info['energytop']

    def get_battle_top(self):
        """战力点上限
        """
        return self.user_info['battlepoint'] + self.vip_function['battlepoint_add']

    def get_battle_real_top(self):
        """真正的战力点上限
        """
        return self.user_info['battlepointtop']

    def get_cards_top(self):
        """卡牌背包上限
        """
        return self.user_info['player_num'] + self.cards_top_extend

    def get_equips_top(self):
        """装备背包上限
        """
        return self.user_info['equip_num'] + self.equips_top_extend

    def get_arena_num(self):
        """增加的竞技次数
        """
        return self.vip_function['arena_num']

    def is_online(self):
        """判断用户是否在线(15分钟内有动作)
        Return:
            True    在线状态
            False   离线状态
        """
        now = int(time.time())
        diff = now - self.active_time
        return diff <= 60*15

    def active_time_diff(self):
        """用户上次活跃时间距现在的时间差(单位:秒)
        """
        now = int(time.time())
        diff = int(now - self.active_time)
        return max(diff, 0)

    def strategy_upgrade(self, new_strategy, is_ini=False):
        """升级战术
        Args:
            new_strategy: 新战术
            is_ini: 是否是初始值
        """
        self.changed = True

        samestrategy = game_config.strategy[new_strategy]['samestrategy']
        # 标识有新战术开启
        if samestrategy not in self.strategys:
            self.alert_strategy = 1
        self.strategys[samestrategy] = new_strategy

        if is_ini:
            self.strategy = new_strategy
        else:
            if samestrategy == game_config.strategy[self.strategy]['samestrategy']:
                self.strategy = new_strategy

    def strategy_reset(self, samestrategy):
        """战术重置
        """
        new_strategy = game_config.strategy_upgrade[samestrategy][1]
        self.strategy_upgrade(new_strategy)

    def strategy_list(self):
        """开启的战术列表
        """
        return sorted(self.strategys.itervalues())

    def has_redis_lock(self):
        key = 'lock_key||%s' % self.uid
        lock_key = self.make_key_cls(key)
        lock_time = float(self.redis.get(lock_key) or 0)
        return lock_time and time.time() - lock_time < 1

    def acquire_redis_lock(self):
        key = 'lock_key||%s' % self.uid
        lock_key = self.make_key_cls(key)
        # 设置2秒过期
        self.redis.set(lock_key, time.time(), ex=2)

    def release_redis_lock(self):
        key = 'lock_key||%s' % self.uid
        lock_key = self.make_key_cls(key)
        self.redis.delete(lock_key)

    def save(self, force=False):
        """重写保存方法
        """
        #if not force and self.has_redis_lock():
        #    raise Exception("Duplicate user_m save")
        super(UserM, self).save()


class LevelRank(RedisRankModelBase):
    """等级排行
    """
    KEY_PREFIX = 'level_rank'


class ExpRank(RedisRankModelBase):
    """经验值排行
    """
    KEY_PREFIX = 'exp_rank'


class OnlineRank(RedisRankModelBase):
    """在线排行
    """
    KEY_PREFIX = 'online_rank'

    def get_onlines(self, delta=300, only_count=False):
        """获取在线人列表
        """
        max_score = int(time.time()) + 1
        min_score = max_score - delta

        if only_count:
            return self.redis.zcount(self.key, min_score, max_score)
        return self.redis.zrevrangebyscore(self.key, max_score, min_score)

    def get_today_onlines(self, only_count=False):
        """获取今日登陆过的人列表
        """
        today = datetime.date.today()
        min_score = time.mktime(today.timetuple())
        max_score = int(time.time()) + 1

        if only_count:
            return self.redis.zcount(self.key, min_score, max_score)
        return self.redis.zrevrangebyscore(self.key, max_score, min_score)


class RegistRank(OnlineRank):
    """注册时间排名， 方便查询每日新增
    """
    KEY_PREFIX = 'regist_rank'


class UsernameHash(RedisHashModelBase):
    """用户名字集合 - REDIS hash 结构
    """
    KEY_PREFIX = 'username_hash'


class BanRank(RedisRankModelBase):
    """封号列表集合
    """
    KEY_PREFIX = 'ban_rank'


class AbilityRank(RedisRankModelBase):
    """战斗实力排行
    """
    KEY_PREFIX = 'ability_rank'


class HighestAbilityRank(RedisRankModelBase):
    """昨天最高战斗实力排行
    """
    KEY_PREFIX = 'highest_ability_rank'


class TodayHighestAbilityRank(RedisRankModelBase):
    """今日最高战斗实力排行
    """
    KEY_PREFIX = 'today_highest_ability_rank'


class Statistics(RedisHashModelBase):
    """用户数据统计字典
    日期  登陆用户 新增登陆 付费人数 新增登陆付费人数 新增付费人数 留存付费用户 付费金额 新增付费金额 付费率 付费ARPU 登陆ARPU
    注释
    登陆用户：当日登陆的总用户数量
    新增登陆：当日新增加的登陆用户数量
    付费人数：当日付费总人数
    新增登陆付费人数：当日新增的登陆用户中付费的人数
    新增付费人数：当日新增加的付费人数（之前没有过付费行为的用户产生付费）
    留存付费用户：今日登陆用户中所有有过付费行为的人数
    付费率：付费人数/登陆人数
    付费ARPU：付费金额/付费人数
    登陆ARPU：付费金额/登陆人数
    """
    KEY_PREFIX = 'user_statistics'

    @classmethod
    def get(cls, uid, server_id):
        uid = 'statistics'
        obj = super(Statistics, cls).get(uid, server_id)
        obj.today = time.strftime('%Y-%m-%d')
        obj.data = obj.hget(obj.today)
        return obj

    def add_login(self, user):
        today = time.strftime('%Y-%m-%d')
        pass

    def add_regist(self, user):
        pass





