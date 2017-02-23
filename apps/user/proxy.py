# coding: utf-8

import time
import weakref

import settings

from lib.utils.helper import strftimestamp
from apps import public as public_app
from apps.public import consts as pub_consts
from apps.config import game_config


def subclass_attr_generate(templates):
    """把一些模块挂载到user模块上
    """
    result = {}
    for name, classpath in templates.iteritems():
        modulename, classname = classpath.rsplit('.', 1)
        module = __import__(modulename, globals(), locals(), [classname])
        result[name] = getattr(module, classname)
    return result


# 定义子model映射关系
USER_SUBCLASS_ATTRS = {
    'base_m'          : 'apps.user.models.BaseM',
    'user_m'          : 'apps.user.models.UserM',
    'level_rank'      : 'apps.user.models.LevelRank',
    'exp_rank'        : 'apps.user.models.ExpRank',
    'ability_rank'    : 'apps.user.models.AbilityRank',
    'highest_ability_rank'          : 'apps.user.models.HighestAbilityRank',
    'today_highest_ability_rank'    : 'apps.user.models.TodayHighestAbilityRank',
    'online_rank'     : 'apps.user.models.OnlineRank',
    'regist_rank'     : 'apps.user.models.RegistRank',
    'ban_rank'        : 'apps.user.models.BanRank',
    'username_hash'   : 'apps.user.models.UsernameHash',
    'card'            : 'apps.card.models.Card',
    'card_train'      : 'apps.card.models.CardTrain',
    'foreign_aid'     : 'apps.card.models.ForeignAid',
    'team_mirror_image': 'apps.card.models.TeamMirrorImage',
    'team_formation'  : 'apps.card.models.TeamFormaction',
    'pve'             : 'apps.pve.models.PVE',
    'pve_ranking'     : 'apps.pve.models.PVERanking',
    'pve_legend'      : 'apps.pve.models.PVELegend',
    'pve_dynasty'     : 'apps.pve.models.PVEDynasty',
    'pve_money'       : 'apps.pve.models.PVEMoney',
    'pve_hstage'      : 'apps.pve.models.PVEHstage',
    'item'            : 'apps.item.models.Item',
    'patch'           : 'apps.item.models.Patch',
    'patch_rank'      : 'apps.item.models.PatchRank',
    'arena'           : 'apps.arena.models.Arena',
    'arena_rank'      : 'apps.arena.models.ArenaRank',
    'arena_award_rank': 'apps.arena.models.ArenaAwardRank',
    'payment'         : 'apps.payment.models.Payment',
    'subrecord'       : 'apps.subrecord.models.Subrecord',
    'code'            : 'apps.code.models.Code',
    'equip'           : 'apps.equip.models.Equip',
    'friend'          : 'apps.friend.models.Friend',
    'gacha'           : 'apps.gacha.models.Gacha',
    'handbook'        : 'apps.handbook.models.Handbook',
    'league'          : 'apps.league.models.League',
    'league_all'      : 'apps.league.models.LeagueId',
    'league_rank'     : 'apps.league.models.LeagueRank',
    'league_bidding_rank': 'apps.league.models.LeagueBiddingRank',
    'league_name_hash': 'apps.league.models.LeagueNameHash',
    'shop'            : 'apps.shop.models.Shop',
    'award'           : 'apps.award.models.Award',
    'pay_award'       : 'apps.award.models.PayAward',
    'mysticshop'      : 'apps.shop.models.MysticShop',
    'celebration_yao' : 'apps.active.models.CelebrationYao',
    'task'            : 'apps.task.models.Task',
    'public_task'     : 'apps.task.models.PublicTask',
    'notify'          : 'apps.notify.models.Notify',
    'gamevs'          : 'apps.gamevs.models.Gamevs',
    'active'          : 'apps.active.models.Active',
    'public_active'   : 'apps.active.models.PublicActive',
    'roulette'        : 'apps.active.models.Roulette',
    'fund_string'     : 'apps.active.models.FundString',
    'loot'            : 'apps.loot.models.Loot',
    'loot_hash'       : 'apps.loot.models.LootHash',
}


class User(object):
    """用户类，现在当作所有model的数据容器
    NOTE:
        修改子model任何存储数据， 需显示使该model的changed属性为True, 保存统一用user.save_all()方法
    """
    GOODS_FROM_BLOCK = 1
    GOODS_FROM_EVOLUTION = 2
    GOODS_FROM_ADMIN = 3
    GOODS_FROM_ARENA = 4
    GOODS_FROM_GACHA = 5
    GOODS_FROM_RETIRE = 6
    GOODS_FROM_CUPNUM = 7
    GOODS_FROM_SHOP = 8
    GOODS_FROM_PATCH = 9
    GOODS_FROM_TREASURE = 10
    GOODS_FROM_CODE = 11
    GOODS_FROM_RANKING = 12
    GOODS_FROM_AWARD = 13
    GOODS_FROM_MYSTICSHOP = 14
    GOODS_FROM_TASK = 15
    GOODS_FROM_GACHA_BOX = 16
    GOODS_FROM_LEGEND = 17
    GOODS_FORM_NOTIFY = 18
    GOODS_FROM_DYNASTY = 19
    GOODS_FROM_REBIRTH = 20
    GOODS_FROM_MONEYSTAGE = 21
    GOODS_FROM_MIX = 22
    GOODS_FROM_WEEK = 23
    GOODS_FROM_MONTH = 24
    GOODS_FROM_FUNCTRL = 25
    GOODS_FROM_ACTIVE = 26
    GOODS_FROM_PAYMENT = 27
    GOODS_FROM_GOODS_VS = 28
    GOODS_FROM_LEAGUE = 29
    GOODS_FROM_HSTAGE = 30
    GOODS_FROM_MERGE = 31
    GOODS_FROM_GAMEVS = 32
    GODOS_FROM_QMZP = 33
    GOODS_FROM_DEVELOP = 34
    GOODS_FROM_CHARGE = 35
    GOODS_FROM_GACHA_EQUIP = 36
    GOODS_FROM_LEVELUP = 37
    GOODS_FROM_DECORATION = 38

    NOTIFY_FROM_SYS = 0
    NOTIFY_FROM_ARENA = 1
    NOTIFY_FROM_ROBPATCH = 2
    NOTIFY_FROM_ROBFOREIGN = 3
    NOTIFY_FROM_FOREIGN_EXPIRED = 4
    NOTIFY_FROM_FOREIGN_RENTED = 5
    NOTIFY_FROM_PVE_RANKING = 6
    NOTIFY_FROM_ARENA_RANK = 7
    NOTIFY_FROM_RECYCLE_RENT = 8
    NOTIFY_FROM_GAMEVS_CON_WIN = 9
    NOTIFY_FROM_GAMEVS_SECTION = 10
    NOTIFY_FROM_FIRST_PAY = 11
    NOTIFY_FROM_VIP_LEVELUP = 12
    NOTIFY_FROM_LEAGUE = 13
    NOTIFY_FROM_PUSH_AWARD = 14
    NOTIFY_FROM_AWARD_SP = 15
    NOTIFY_FROM_ACTIVE = 16
    NOTIFY_FROM_LEVELRANK = 17
    NOTIFY_FROM_ABILITYRANK = 18
    NOTIFY_FROM_LEAGUERANK = 19
    NOTIFY_FROM_ACTIVE_XSJX = 20

    def __init__(self, uid, server_id, read_only=True):
        self.uid = uid
        self.read_only = read_only
        self.server_id = server_id or public_app.get_server_by_uid(uid)
        self._client_cache_update = {}

    def __getattr__(self, name):
        if name in USER_SUBCLASS_ATTRS:
            return self.__getitem__(name)
        return self.__getattribute__(name)

    def __getitem__(self, name):
        obj = self.__dict__.get(name, None)
        if obj is None:
            classpath = USER_SUBCLASS_ATTRS[name]
            modulename, classname = classpath.rsplit('.', 1)
            module = __import__(modulename, globals(), fromlist=[classname])
            class_obj = getattr(module, classname)
            obj = class_obj.get(self.uid, self.server_id)
            obj.weak_user = weakref.proxy(self)
            self.__dict__[name] = obj
            if not self.read_only and getattr(obj, 'need_insert', False) and hasattr(obj, 'pre_init'):
                obj.pre_init()
            if not self.read_only and hasattr(obj, 'pre_use'):
                obj.pre_use()
        return obj

    def reset_all(self):
        """重置用户所有模块
        """
        read_only = self.read_only
        self.read_only = True
        for name in USER_SUBCLASS_ATTRS:
            obj = self.__getitem__(name)
            if hasattr(obj, 'reset'):
                obj.reset()
        self.read_only = read_only

    def save_all(self):
        """统一保存数据入口
        """
        attrs = USER_SUBCLASS_ATTRS
        for name, obj in self.__dict__.iteritems():
            if name in attrs and obj.changed:
                obj.save()

    def is_new(self):
        """判断用户是否存在
        """
        return not self.user_m.regist_time and not self.base_m.regist_time

    def exists(self, server_id=None):
        """判断用户是否在server_id存在
        """
        server_id = server_id or self.server_id
        if self.server_id not in game_config.servers:
            return False

        father_server = settings.get_father_server(server_id)
        self_father_server = settings.get_father_server(self.server_id)
        regist_time = self.user_m.regist_time or self.base_m.regist_time
        return father_server == self_father_server and regist_time

    def dumps(self):
        """把本用户数据全部取出来
        """
        data = {}
        for name in USER_SUBCLASS_ATTRS:
            obj = self.__getitem__(name)
            if hasattr(obj, 'dumps') and getattr(obj, 'uid', '') == self.uid:
                data[name] = obj.dumps()
        return data

    def loads(self, data):
        """把数据分发到各模块
        """
        for name in USER_SUBCLASS_ATTRS:
            if name in data:
                obj = self.__getitem__(name)
                if hasattr(obj, 'loads') and getattr(obj, 'uid', '') == self.uid:
                    obj.loads(data[name])

    def add_goods(self, goods_data, where=0, ext=0, times=1):
        """添加一组礼物
        Args:
            goods_data = {
                'money': 0,    # 金钱
                'coin': 0,     # 钻石
                'exp': 0,      # 经验
                'energy': 0,   # 行动力
                'battle': 0,   # 战力
                'honor': 0,    # 荣誉点
                'point': 0,    # 积分
                'item': [(id, num), (id, num)],     # 道具
                'equip': [(id, num), (id, num)],    # 装备
                'patch': [(id, num), (id, num)],    # 装备碎片
                'treasure': [(id, num), (id, num)], # 固定宝箱
                'card': [(id, level, num), (id, level, num)] 或者 [(id, num), (id, num)],
                'patchequip': [(id, num)],          # 护具装备碎片
                'patchplayer': [(id, num)],         # 球员碎片
                'gacha_box': [(id, num)],           # gacha宝箱
                'patchitem': [(id, num)],           # 道具碎片
                'grade': 0,    # 王朝积分
                'stamina': 0,  # 王朝体力
                'lottery': 0,   # 奖券
                'activeness': 0,  #任务
            }
            where:  奖励来源
            ext:    奖励扩展标识
            times:  奖品物品数量的倍数(支持float)

        Returns:
            {
                'card': [{'id': 'aaaa', 'card': {...}}],
                'equip': [{'id': 'aaaa', 'equip': {...}}],
                'patch': [[1, 1], [2, 2]],
                'item': [[1, 1], [2, 2]],
                'money': 0,
                'honor': 0,
                'point': 0,
                'patchplayer': [[1, 1], [2, 2]],
                'treasure': [[1, 1], [2, 2]],
                'gacha_box': [[1, 1], [2, 2]],
                'patchitem': [[10001, 1]],
                'coin': 0,
                'exp': 0,
                'energy': 0,
                'battle': 0,
                'stamina': 0,
                'grade': 0,
                'lottery': 0,
                'activeness': 0,
            }
        """
        from apps.card import new_card
        from apps.equip import new_equip
        from apps.item.models import Item

        ITEM_TYPES = Item.ITEM_TYPES
        times = float(times)
        result = {}
        for goods_type, value in goods_data.iteritems():
            if not value: continue

            if goods_type in ('money', 'energy', 'battle', 'honor', 'point', 'exp', 'lottery'):
                new_num = int(value*times)
                self.user_m.incr_attr(**{goods_type: new_num})
                result[goods_type] = new_num

            if goods_type == 'coin':
                new_num = int(value*times)
                self.user_m.incr_coin(new_num, where)
                result[goods_type] = new_num

            elif goods_type == 'exp_percent':
                new_num = int(value*times)
                exp = int(self.user_m.exp_percent * new_num)
                self.user_m.add_exp(exp)
                result['exp'] = result.get('exp', 0) + exp

            elif goods_type == 'activeness':
                new_num = int(value*times)
                self.task.incr_attr(activeness=new_num)
                result[goods_type] = new_num

            elif goods_type in ITEM_TYPES:
                result[goods_type] = []
                new_value = []
                for _id, num in value:
                    new_num = int(num*times)
                    self.item.add(goods_type, _id, new_num, where=where)
                    new_value.append((_id, new_num))
                result[goods_type].extend(new_value)

            elif goods_type == 'patch':
                result['patch'] = []
                new_value = []
                for _id, num in value:
                    new_num = int(num*times)
                    self.patch.add(_id, new_num)
                    new_value.append((_id, new_num))
                result['patch'].extend(new_value)

            elif goods_type == 'equip':
                result['equip'] = []
                for item in value:
                    goods_id, num = item[0], item[-1]
                    level = item[1] if len(item) == 3 else 1
                    new_num = int(num*times)
                    for _ in xrange(new_num):
                        equip = new_equip(self, goods_id, level=level, where=where, ext=ext)
                        result['equip'].append(equip)

            elif goods_type == 'card':
                result['card'] = []
                for item in value:
                    goods_id, num = item[0], item[-1]
                    level = item[1] if len(item) == 3 else 1
                    new_num = int(num*times)
                    for _ in xrange(new_num):
                        card = new_card(self, goods_id, level=level, where=where, ext=ext)
                        result['card'].append(card)

            elif goods_type in ('stamina', 'grade'):
                new_num = int(value*times)
                if goods_type == 'stamina':
                    self.pve_dynasty.recover_stamina(new_num)
                else:
                    self.pve_dynasty.incr_attr(**{goods_type: new_num})
                result[goods_type] = new_num

        return result

    def add_gift(self, award_list, where=0, ext=0, times=1):
        """添加一组礼物
        Args:
            where:  奖励来源
            ext:    奖励扩展标识
            times:  奖品物品数量的倍数(支持float)
            award_list = [[5,0,1000], [100,0,100]]
            每个奖品列表中的首元素代表的内容
                1       card           [种类,id,等级,数量]    奖励的球员
                2       equip          [种类,id,数量]         奖励的装备
                3       patch          [种类,id,数量]         奖励的护具碎片
                4       item           [种类,id,数量]         奖励的道具
                5       money          [种类,0,现金数量]      奖励的金钱
                6       honor          [种类,0,荣誉数量]      奖励的荣誉
                7       point          [种类,0,积分数量]      奖励的积分
                8       patchplayer    [种类,id,数量]         奖励的球员碎片
                9       treasure       [种类,id,数量]         奖励的宝箱id
                11      grade          [种类,0,数量]          王朝积分
                18      patchequip     [种类,id,数量]         装备碎片
                19      gacha_box      [种类,id,数量]         gacha宝箱
                20      energy         [种类,0,恢复行动力]     恢复行动力
                24      patchitem      [种类,id,数量]         道具碎片
                100     coin           [种类,0,钻石数量]       奖励的钻石数量
                200     stamina        [种类,0,恢复体力值]     王朝模式回体力【专用】
                2000    exp            [种类,0,数量]          经验点
                # 后端自定义的几种类型
                1001    energy    [种类,0,数量]   体力点
                1002    battle    [种类,0,数量]   战力点
        Returns:
            同add_goods
        """
        goods_data = public_app.trans_goods_list2dict(award_list)

        return self.add_goods(goods_data, where, ext, times)

    def loot_list_integration(self, goods_list):
        """loot同种物品数量整合
        Args:
            award_list: 同add_gift
            [[1,10001,1,1,4000],
            [1,10001,1,3,4000],
            [5,0,300,1667],
            [5,0,200,1667],
            [4,100,1,1000],
            [4,100,2,1000]]
        return:
            [[1,10001,1,4],
            [5,0,500],
            [4,100,3]]
        """
        goods_data = []

        for goods in goods_list:
            if not goods:
                continue

            had = False
            goods_type = goods[0]
            goods_type_name = pub_consts.GOODS_TYPE_NAME_MAP[goods_type]

            if goods_type_name == 'card':
                for goods1 in goods_data:
                    if goods[:3] == goods1[:3]:
                        had = True
                        goods1[3] += goods[3]
                        break
                if not had:
                    goods_data.append(goods[:4])
                continue

            for goods1 in goods_data:
                if goods[:2] == goods1[:2]:
                    had = True
                    goods1[2] += goods[2]
                    break
            if not had:
                goods_data.append(goods[:3])

        return goods_data

    def reduce_goods(self, goods_list):
        """消耗一组物品
        Args:
            goods_list: 每个物品列表中的首元素代表的内容
                3       patch          [种类,id,数量]         奖励的护具碎片
                4       item           [种类,id,数量]         奖励的道具
                5       money          [种类,0,现金数量]      奖励的金钱
                8       patchplayer    [种类,id,数量]         奖励的球员碎片
                9       treasure       [种类,id,数量]         奖励的宝箱id
                18      patchequip     [种类,id,数量]         装备碎片
                19      gacha_box      [种类,id,数量]         gacha宝箱
                100     coin           [种类,0,钻石数量]       奖励的钻石数量
        Returns:
            同add_goods
        """
        from apps.item.models import Item

        ITEM_TYPES = Item.ITEM_TYPES
        result = {}
        goods_data = public_app.trans_goods_list2dict(goods_list)   # list to dict

        for goods_type, value in goods_data.iteritems():
            if not value: continue

            if goods_type in ('money', 'coin'):
                self.user_m.incr_attr(**{goods_type: -value})
                result[goods_type] = value

            elif goods_type in ITEM_TYPES:
                result[goods_type] = []
                for _id, num in value:
                    self.item.reduce(goods_type, _id, num)
                result[goods_type].extend(value)

            elif goods_type == 'patch':
                result['patch'] = []
                for _id, num in value:
                    self.patch.reduce(_id, num)
                result['patch'].extend(value)

        return result

    def check_goods_enough(self, goods_list):
        """校验一组物品是否充足
        Args:
            goods_list: 每个物品列表中的首元素代表的内容
                3       patch          [种类,id,数量]         奖励的护具碎片
                4       item           [种类,id,数量]         奖励的道具
                5       money          [种类,0,现金数量]      奖励的金钱
                8       patchplayer    [种类,id,数量]         奖励的球员碎片
                9       treasure       [种类,id,数量]         奖励的宝箱id
                18      patchequip     [种类,id,数量]         装备碎片
                19      gacha_box      [种类,id,数量]         gacha宝箱
                100     coin           [种类,0,钻石数量]       奖励的钻石数量
        Returns:
            True: 充足
            False: 不足
        """
        from apps.item.models import Item

        ITEM_TYPES = Item.ITEM_TYPES

        if not goods_list:
            return False

        goods_data = public_app.trans_goods_list2dict(goods_list)   # list to dict

        for goods_type, value in goods_data.iteritems():
            if not value:
                return False

            if goods_type in ('money', 'coin'):
                if getattr(self.user_m, goods_type, 0) < value:
                    return False

            elif goods_type in ITEM_TYPES:
                for _id, num in value:
                    if self.item.get_num(goods_type, _id) < num:
                        return False

            elif goods_type == 'patch':
                for _id, num in value:
                    if self.patch.get_num(_id) < num:
                        return False

            else:
                return False

        return True

    def goods_own_info(self, goods_list):
        """获取一组物品是否充足的信息
        Args:
            goods_list: 物品列表 例: [[5,0,1000], [100,0,100]...]
        Returns:
            own_goods list 物品拥有的情况(0不足，1充足) 例: [1,0]
        """
        own_goods = []
        for goods in goods_list:
            if self.check_goods_enough([goods]):
                had = 1
            else:
                had = 0
            own_goods.append(had)

        return own_goods

    def gift_loot_double(self, award_list, double_detail):
        """双倍掉落功能，指定类型翻倍
        Args:
            award_list = [[5,0,1000], [100,0,100]] 同add_gift函数
            double_detail:  loot_double配置详情
        """
        if not double_detail:
            return award_list

        new_list = []
        for goods in award_list:
            if goods[0] == 2000:
                num = int(goods[2]*double_detail['exp_times'])
                new_list.append([goods[0], goods[1], num])
            elif goods[0] == 5:
                num = int(goods[2]*double_detail['money_times'])
                new_list.append([goods[0], goods[1], num])
            elif goods[0] == 100:
                num = int(goods[2]*double_detail['diamond_times'])
                new_list.append([goods[0], goods[1], num])
            elif goods[0] == 1:
                num = int(goods[3]*double_detail['other_times'])
                new_list.append([goods[0], goods[1], goods[2], num])
            else:
                num = int(goods[2]*double_detail['other_times'])
                new_list.append([goods[0], goods[1], num])

        return new_list

    def add_pay_award(self, open_gift, order_money, charge_config, order_done):
        """充值活动记录相关
        Args:
            open_gift: 是否能开启周卡, 月卡
            order_money: 实际充值的钱
            charge_config: charge配置详情
            order_done: 此订单是否完成
        """
        # 开启周卡月卡
        self.pay_award.add_pay_award(open_gift)
        # 记录每天的充钱数
        self.pay_award.add_daily_rmb(order_money)
        # 充值活动
        self.active.add_charge_rmb(order_money, charge_config, order_done)

    def add_notify(self, sort, **kwargs):
        """添加各种通知消息
        Args:
            sort: 类型
            kwargs: 此类型需要的一些变量数据
        Note:
            在正式环境, 此操作不会解发异常,防止中断其它动作(充值动作)
        """
        from apps import notify as notify_app

        func_name = 'notify_by_sort%d' % sort
        func = getattr(notify_app, func_name)
        #return func(self, kwargs)
        try:
            return func(self, kwargs)
        except Exception as e:
            print 'add_notify_error:%r uid=%s, sort=%s, kwargs=%s' % (e, self.uid, sort, kwargs)
            if settings.DEBUG:
                raise e
            return False

    def do_task(self, sort, **kwargs):
        """添加各种通知消息
        Args:
            sort: 类型
            kwargs: 此类型需要的一些变量数据
        """
        from apps.task import dotask

        func_name = 'do_task_%s' % sort
        func = getattr(dotask, func_name)
        #return func(self, kwargs)
        try:
            return func(self, kwargs)
        except Exception as e:
            print 'do_task_error: sort=%s, kwargs=%s' % (sort, kwargs)
            if settings.DEBUG:
                raise e
            return False

    def update_user_cache_data(self, team_formation=None):
        """缓存一些不需要实时计算的数据
            ability: 总实力值
            core_player: 核心位置中最牛队员ID
        Args:
            user: 用户对象
            team_formation: 编队数据
        """
        from apps import card as card_app
        from apps.battle import utils as battle_utils

        team_formation = team_formation or card_app.get_effect_team_formation(self)
        team_ability = battle_utils.calc_team_ability(team_formation, game_config)
        core_player = card_app.get_max_core_player(self, team_formation)
        active_skill_jointly = battle_utils.get_active_skill_jointly(team_formation)

        history_ability = max(team_ability, self.user_m._max_ability)
        # 缓存一些编队数据
        self.user_m.setattr(_ability=team_ability, _core_player=core_player,
                            _max_ability=history_ability)
        self.user_m.cache_active_skill_jointly(active_skill_jointly)
        # 缓存原始的战斗编队数据
        self.team_formation.cache_team_formation(team_formation)
        if team_ability:
            self.ability_rank.zadd(team_ability, weight=True)

            # 开服活动
            self.active.opening_active_handle(team_ability, team_formation)

            # 今日历史最高战斗力排行榜
            if team_ability > self.user_m._today_max_ability:
                today = time.strftime('%Y-%m-%d')
                regist_date = strftimestamp(self.user_m.regist_time, fmt='%Y-%m-%d')
                # 新用户同时更新昨天、今天的排行榜
                if today == regist_date:
                    self.highest_ability_rank.zadd(team_ability, weight=True)
                    self.user_m.setattr(_yestoday_max_ability=team_ability)
                self.today_highest_ability_rank.zadd(team_ability, weight=True)
                self.user_m.setattr(_today_max_ability=team_ability)
                # 保存此时的球员阵容
                card_app.team2formation_special(self, team_formation)
                self.team_mirror_image.update_team_formation(team_formation)

        # 任务: 阵容变化时，完成一些任务
        self.do_task('update_team', team_formation=team_formation)
        return team_formation

    # def get_client_cache_update(self):
    #     """获取前端需要缓存的数据
    #     """
    #     return self._client_cache_update
    #
    # def add_client_cache_update(self, tp, act, args=None, kwargs=None):
    #     """添加前端需要缓存的数据
    #     """
    #     data = self._client_cache_update.setdefault(act, {})
    #     if act == 'update' and kwargs:
    #         data.setdefault(tp, {}).update(kwargs)
    #     elif act == 'remove' and args:
    #         data.setdefault(tp, []).extend(args)
    #     elif act == 'replace':
    #         data.setdefault(tp, {}).update(kwargs)

    def is_npc(self, uid=None):
        """判断用户是否是机器人
        Args:
            uid: 用户uid
        Return:
            True    机器人
            False   真实用户
        """
        uid = uid or self.uid
        return public_app.is_npc(uid)


class NPCUser(User):
    """NPC模拟用户对象
    """
    def __init__(self, uid, server_id, username=None):
        self.uid = uid
        self.server_id = server_id
        self.read_only = True
        self.user_m = EmptyObject()
        self.user_m.username = username

    def reset_all(self):
        """重置用户所有模块
        """
        pass

    def save_all(self):
        """统一保存数据入口
        """
        pass

    def is_npc(self, uid=None):
        """判断用户是否是机器人
        Args:
            uid: 用户uid
        Return:
            True    机器人
            False   真实用户
        """
        uid = uid or self.uid
        return public_app.is_npc(uid)


class EmptyObject(object):
    pass

