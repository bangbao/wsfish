# coding: utf-8

import time
import random
import datetime
import json

import settings
from lib.utils.helper import md5, merge_dict
from apps.public import timer
from apps.config import game_config
from . import logics
from . import consts
from .proxy import User, NPCUser
from .models import AccountToken, TokenServerUid, UserM, Footprint


def get_user_by_token(token, server_id, read_only=False, platform='', skip_salt=False):
    """由用户TOKEN获取用户对象
    Args:
        token: 用户TOKEN
        server: 分服ID
        read_only: 是否调用子模块pre_use方法
    Returns:
        user: 用户对象
    """
    flag, token = check_token_salt(token, skip_salt)
    if not flag:
        return None

    prefix = settings.UID_PREFIX
    obj = TokenServerUid.get_or_create(token, server_id or '00', prefix)
    user = get_user(obj.uid, server_id, read_only)
    if not user.user_m.token:
        user.user_m.setattr(token=obj.token)

    # 若被锁定, 不能取出用户对象
    if user.user_m.has_redis_lock():
        return None

    return user


def get_user(uid, server_id='', read_only=False):
    """获取用户代理对象
    Args:
        uid: 用户对象
        server_id: 分服ID, 不传从uid是截取
        read_only: 只读模块，加载子模块时不调用pre_use方法
    Returns:
        用户代理对象
    """
    if uid or not server_id:
        server_id = server_id
    return User(uid, server_id, read_only)


def get_npcuser(uid, server_id, **kwargs):
    """模拟npc用户对象
    """
    return NPCUser(uid, server_id, **kwargs)


def game_enter(user, leader=0, logo=0, force=False):
    """新用户初始化属性值
    TODO:
        测试数据
    """
    from apps import card as card_app

    if not user.is_new() and not force:
        return False

    leader = leader or min(game_config.user_select)
    logo = logo or min(game_config.logo)

    leader_detail = game_config.user_select[leader]
    player = []
    for pos_key, pos in leader_detail['default'].iteritems():
        cfg_id = leader_detail[pos_key][pos-1]
        player.append(cfg_id)

    strategy = leader_detail['strategy']
    init_team = player + leader_detail['player']
    new_team = user.card.team
    for i, cfg_id in enumerate(init_team):
        card_data = card_app.new_card(user, cfg_id, level=1)
        new_team[i] = card_data['id']

    now_timestamp = int(time.time())
    user.user_m.setattr(logo=logo, username='username', regist_time=now_timestamp)
    user.base_m.setattr(logo=logo, username='username', regist_time=now_timestamp)
    user.card.setattr(team=new_team, strategy=strategy)
    user.pve.pre_init()
    user.gacha.setattr(money_gacha_at=now_timestamp, coin1_gacha_at=now_timestamp)
    # 等级排名, 注册时间排行
    user.level_rank.zadd(user.user_m.level, weight=True)
    user.exp_rank.zadd(user.user_m.exp)
    user.regist_rank.zadd(user.user_m.regist_time)

    # 初始化用户数据
    user.add_gift(game_config.user_ini['ini_loot'])


def user_cache(user, method=None):
    """获取用户cache信息
    Args:
        user: 用户对象
        method: 指定接口
    Returns:
        用户cache信息
    """
    from apps.gamevs.consts import GAMEVS_FIRST_INIT_GUIDE_ID

    user_m = user.user_m
    config = game_config.user_info[user_m.level]

    if method in (None, 'user.home', 'user.main_index') or hasattr(user, 'task'):
        guide_task = user.task.get_guide_task()
    else:
        guide_task = None    # 为None时 前端不更新缓存

    guide = user_m.filter_guide()
    # 联赛新手引导不能进行的接口, 置为空
    if GAMEVS_FIRST_INIT_GUIDE_ID in guide and method.startswith('gamevs'):
        if not user.gamevs.is_open or not method.startswith(('gamevs.index', 'gamevs.fight')):
            guide.pop(GAMEVS_FIRST_INIT_GUIDE_ID, None)

    return {
        'username': user_m.username,
        'uid': user_m.uid,
        'logo': user_m.logo,
        'level': user_m.level,
        'exp': user_m.exp,
        'exp_top': config['exp'],
        'vip': user_m.vip,
        'vip_exp': user_m.vip_exp,
        'coin': user_m.coin,
        'money': user_m.money,
        'energy': user_m.energy,
        'honor': user_m.honor,
        'point': user_m.point,
        'energy_top': user_m.get_energy_top(),
        'battle': user_m.battle,
        'battle_top': user_m.get_battle_top(),
        'is_new': user.is_new(),
        'guide': guide,
        'max_step': user_m.get_first_max_step(),    # 第一类新手引导最大步数
        'ability': user_m.ability,
        'first_pay': user_m.has_first_pay(),               # 充值是否显示首充礼包
        'first_pay_show': user_m.has_first_pay(show=True), # 显示的首充倍数
        'foreign_expired': user_m.is_foreign_expired(),    # 外援是否到期
        'cards_top': user_m.get_cards_top(),               # 球员背包上限
        'equips_top': user_m.get_equips_top(),             # 道具背包上限
        'task': guide_task,                                # 引导任务
        'login_days': len(user_m.login_days),              # 已登陆天数
        'fill_item': get_item_info(user),                  # 常用的补充道具数据
        'exp_percent': user_m.exp_percent,                 # 经验加成值
        'open_strategys': user_m.strategy_list(),          # 开启的战术列表
    }


def user_info(user=None, uid=None, **kwargs):
    """获取用户常用信息
    Args:
        user: 用户对象
        uid: 用户id, 当user为None时用此生成用户对象
    Returns:
        用户基本信息
    """
    user = user or get_user(uid)
    user_m = user.user_m

    info = {
        'username': user_m.username,
        'uid': user_m.uid,
        'level': user_m.level,
        'logo': user_m.logo,
        'ability': user_m.ability,           # 总实力
        'core_player': user_m.core_player,   # 核心位置中战斗力最大的球员cfg_id
    }
    info.update(kwargs)
    return info


def user_more_info(user=None, uid=None, **kwargs):
    """获取用户更多的数据信息
    Args:
        user: 用户对象
        uid: 用户id, 当user为None时用此生成用户对象
        kwargs: 动态添加的属性
    Returns:
        用户信息
    """
    from apps import league as league_app

    user = user or get_user(uid)
    user_m = user.user_m
    strategy_detail = game_config.strategy[user.user_m.strategy]
    strategy_core_pos = []

    for pos in strategy_detail['core_pos']:
        card_id = user.card.team[pos - 1]
        card_obj = user.card.cards.get(card_id)
        if card_obj:
            detail = game_config.player_detail[card_obj['cfg_id']]
            strategy_core_pos.append({'cfg_id': card_obj['cfg_id'],
                                      'from': detail['from']})

    info = {
        'username': user_m.username,
        'uid': user_m.uid,
        'level': user_m.level,
        'logo': user_m.logo,
        'strategy_name': strategy_detail['name'],
        'strategy_core_pos': strategy_core_pos,
        'arena_rank': user_m.arena_rank,
        'ability': user_m.ability,
        'gamevs_name': user.gamevs.get_gamevs_name(),
        'gamevs_rank': user.gamevs.section_rank.rank,
        'league_name': league_app.get_league_name(user),
    }
    info.update(kwargs)

    return info


def more_info(user, **kwargs):
    """用户详情
    Args:
        user: 用户对象
        kwargs: 动态添加的属性
    Returns:
        用户信息
    """
    return user_more_info(user,
                          cur_win=user.pve_ranking.cur_win,
                          all_win=user.pve_ranking.all_win,
                          arena_rank=user.arena_rank.rank,
                          **kwargs)


def user_levelup(user):
    """获取用户基本信息
    Args:
        user: 用户对象
    Returns:
        用户升级变化信息
    """
    user_m = user.user_m

    return {
        'level': user_m.level,
        'energy': user_m.energy,
        'battle': user_m.battle,
        'friend_top': user_m.user_info['friend_num'],
        'card_top': user_m.get_cards_top(),
    }


def update_user_levelup(old_levelup, levelup_backup):
    """更新用户基本信息
    Args:
        old_levelup: 旧的升级数据
        levelup_backup: 需要更新的数据
    Returns:
        用户升级变化信息
    """
    old_levelup.update(levelup_backup)

    return old_levelup


def item_cache(user):
    """用户道具缓存
    只有当item这类道具改变时才给返回值
    """
    if getattr(user, 'item_change', False):
        del user.item_change
        return {'items': user.item.item, 'patchitem': user.item.patchitem,
                'patchplayers': user.item.patchplayer,
                'patchequip': user.item.patchequip}


def patchplayer_cache(user, method_param):
    """用户球员碎片缓存
    当某动作使用户获得碎片时才给返回值
    """
    if getattr(user, 'patchplayer_change', []):
        cache = {}
        for patchplayer_id in user.patchplayer_change:
            cache[patchplayer_id] = user.item.patchplayer[patchplayer_id]
        del user.patchplayer_change
        return cache


def random_uid(user):
    """随机选择一个用户UID， 排除此用户好友
    Args:
        user: 用户对象
    Returns:
        随机的一个UID, 没找到，返回None
    """
    exclude_uid_sets = set(user.friend.friends)
    exclude_uid_sets.add(user.uid)
    friend_count = user.friend.real_count()
    # 上下5级选出对应的人
    uids = user.level_rank.nearby_score(5, 5, friend_count+2)
    diff = set(uids) - exclude_uid_sets
    # 没找出来， 就扩大用户范围中抓取
    if not diff:
        uids = user.level_rank.nearby_score(user.user_m.level, 50, friend_count+2)
        diff = set(uids) - exclude_uid_sets
    if not diff:
        uids = user.level_rank.nearby_score(user.user_m.level, 100, friend_count+2)
        diff = set(uids) - exclude_uid_sets
    if not diff:
        uids = user.level_rank.all()
        diff = set(uids) - exclude_uid_sets

    return random.sample(diff, 1)[0]


def create_test_user(user_id=None, user=None):
    user = user or get_user(user_id)

    # 初始化新用户数据
    if not user.exists():
        game_enter(user)

    # 添加测试道具
    if not user.item.item:
        for i in game_config.item:
            user.item.add('item', i, 10)

    # 测试级别排行
    user.level_rank.zadd(user.user_m.level, weight=True)
    user.exp_rank.zadd(user.user_m.exp)
    return user


def get_expense_price(user, cost_id, times=1):
    """计算某一项商品需要花费的coin价格
    expense记录的是已经消费的次数，下次消费的价格需要加1
    Args:
        user: 用户对象
        cost_id: 消费类型ID
        times: 购买次数
    Returns:
        coin价格
    """
    count = user.user_m.expense.get(cost_id, 0)

    return get_expense_price_especial(user, cost_id, count, times)


def get_expense_price_especial(user, cost_id, count, times=1):
    """计算某一项商品需要花费的coin价格 -- 已购买次数作参数
    expense记录的是已经消费的次数，下次消费的价格需要加1
    Args:
        user: 用户对象
        cost_id: 消费类型ID
        count: 已购买的次数
        times: 购买次数
    Returns:
        coin价格
    """
    expense_config = game_config.cost_diamond[cost_id]
    max_count = max(expense_config)

    price = 0
    for _ in xrange(times):
        count = min(count+1, max_count)
        price += expense_config[count]

    return price

def get_gain_exp(user, expbase, explv):
    """计算用户实际能得的经验
    Args:
        user: 用户对象
        expbase: 基础经验
        explv: 等级加成
    Returns:
        经验
    """
    return int(expbase + user.user_m.user_info['lvexp'] * explv)


def get_rob_exp(user, robconfig, is_win):
    """计算用户实际能得的经验
    """
    if is_win:
        return get_gain_exp(user, robconfig['winexpbase'], robconfig['winexplv'])
    else:
        return get_gain_exp(user, robconfig['loseexpbase'], robconfig['loseexplv'])


def get_rob_money(user, robmoney, is_win):
    """计算胜利或者失败的钱
    is_win=True时， user为对方，  is_win=False, user为自方
    Args:
        user: 用户对象
        robmoney: 配置
        is_win: 是否胜利
    """
    if is_win:
        money = robmoney['robtop']
    else:
        money = robmoney['losetop']

    if not user.is_npc():
        money = min(user.user_m.money, money)

    return money


def sync_guide_status(user, guide_id):
    """api请求中同步新手引导状态
    Args:
        user: 用户对象
        guide_group: 引导分组
        guide_id: 引导id
    """
    if guide_id:
        user.user_m.do_guide(guide_id)


def create_account_token(account, password):
    """创建一个账号并生成对应的token
    Args:
        account: 账号
        password: 密码
    """
    obj = AccountToken.create(account, md5(password))
    return obj


def mark_footprint(user):
    """记录登陆分服
    Args:
        user: 用户对象
    """
    return Footprint.mark_footprint(user.user_m.token, user.server_id, user.uid)


def skip_guide(user):
    """跳过所有的新手引导步骤
    Args:
        user: 用户对象
    """
    for sort, config in game_config.guide.iteritems():
        max_step  = max(config)
        user.user_m.do_guide(max_step)


def check_user_functrl(user, functrl_id):
    """校验用户是否开启了此功能
    Args:
        user: 用户对象
        functrl_id: user_functrl类型ID
    Returns:
        提示消息(None表示不用中断请求)
    """
    # 配置有可能不存在
    user_functrl = game_config.user_functrl.get(functrl_id)
    if not user_functrl or user_functrl['lv'] == -1:
        return
    lv_limit = user_functrl['lv']
    if functrl_id <= 1000:
        # 校验level等级
        if user.user_m.level < lv_limit or \
            (user_functrl['stage'] and not user.pve.is_stage_done(user_functrl['stage'])):
            return user_functrl['text']
    else:
        # 校验vip等级
        if user.user_m.vip < lv_limit:
            return user_functrl['text']


def check_user_levelup_award(user, old_level, new_level):
    """检测用户升级给的奖励物品
    Args:
        user: 用户对象
        old_level: 旧级别
        new_level: 新级别
    Returns:
        奖励或者None
    """
    award = {}
    user_loot_key = 'user_loot%d' % user.user_m.leader
    for functrl_id, user_functrl in game_config.user_functrl.iteritems():
        if old_level < user_functrl['lv'] <= new_level:
            guide_loot = user_functrl.get(user_loot_key) or user_functrl['guide_loot']
            if guide_loot:
                result = user.add_gift(guide_loot,
                                       where=user.GOODS_FROM_FUNCTRL,
                                       ext=functrl_id)
                merge_dict(award, result)
            # 需要强制引导和弱引导
            if user_functrl['is_guide'] in (1, 2) and user_functrl['guide_id']:
                _, guide_id = user_functrl['guide_id']
                sync_guide_status(user, guide_id)

    return award


def yield_all_uid(server_id=None):
    """找出所有分服的注册用户的uid
    """
    from apps.user.models import RegistRank

    if server_id:
        regist_rank = RegistRank.get('', server_id)
        uids = regist_rank.all()
        for uid in uids:
            yield uid
    else:
        for server_id in game_config.servers:
            regist_rank = RegistRank.get('', server_id)
            uids = regist_rank.all()
            for uid in uids:
                yield uid


def yield_all_user(server_id=None):
    """找出所有分服的注册用户的user对象
    """
    from apps.user.models import RegistRank

    if server_id:
        regist_rank = RegistRank.get('', server_id)
        uids = regist_rank.all()
        for uid in uids:
            yield get_user(uid, server_id)
    else:
        for server_id in game_config.servers:
            regist_rank = RegistRank.get('', server_id)
            uids = regist_rank.all()
            for uid in uids:
                yield get_user(uid, server_id)


def get_server_footprint(user_token):
    """获取服务器登录数据
    """
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    server_foot = Footprint.get_server_foot(user_token)
    footprints = {}
    for server_id, timestamp in server_foot.iteritems():
        if server_id in game_config.servers and game_config.servers[server_id]['open_time'] < now:
            token_obj = TokenServerUid.get(user_token, server_id)
            if token_obj:
                user = get_user(token_obj.uid, server_id)
                if user.exists():
                    footprints[server_id] = {'uid': user.uid,
                                             'level': user.user_m.level,
                                             't': timestamp}

    token_servers = {}
    for server_id, obj in game_config.servers.iteritems():
        if obj['open_time'] < now:
            uid, level = None, None
            if server_id in footprints:
                uid = footprints[server_id]['uid']
                level = footprints[server_id]['level']

            token_servers[server_id] = {
                'status': obj['status'],
                'server_id': server_id,
                'server_tag': obj['server_tag'],
                'server_name': obj['server_name'],
                'server_url': settings.SERVERS[server_id]['server_url'],
                'chat_host': settings.SERVERS[server_id]['chat_host'],
                'chat_port': settings.SERVERS[server_id]['chat_port'],
                'uid': uid,
                'level': level,
            }
    open_servers = sorted(token_servers.itervalues(), key=lambda x: x['server_tag'], reverse=True)

    footprints_len = len(footprints)
    footprints_sorted = sorted(footprints, key=lambda x: footprints[x]['t'], reverse=True)
    footprint = [token_servers[server_id] for server_id in footprints_sorted[:3]]
    if footprints_len >= 4:
        level_sorted = sorted(footprints_sorted[3:], key=lambda x: footprints[x]['level'], reverse=True)
        footprint.append(token_servers[level_sorted[0]])
    else:
        break_len = 3 if footprints_len == 1 else 4
        for server_obj in open_servers:
            if server_obj['server_id'] not in footprints:
                footprint.append(server_obj)
                if len(footprint) >= break_len:
                    break

    return {
        'servers': open_servers,      # 分服列表
        'footprint': footprint,       # token分服记录
    }


def create_token_salt(token, salt=None):
    """生成一个随机串标识是token上,加一层校验
    """
    salt = salt or Footprint.create_salt(token)
    return consts.TOKEN_SALT_HYPHEN.join((token, salt))


def check_token_salt(token, skip_salt=False):
    """校验token的salt值
    """
    HYPHEN = consts.TOKEN_SALT_HYPHEN
    if HYPHEN in token:
        token, salt = token.rsplit(HYPHEN)
        save_salt = Footprint.get_salt(token)
        if not skip_salt and salt != save_salt:
            return False, token
    return True, token


def charge_show(user):
    """返回用户能显示的几种商品
    Args:
        user: 用户对象
    """
    from apps import award as award_app
    from apps.award import consts as award_consts

    open_gifts = (award_consts.CHARGE_OPEN_GIFT_WEEK, award_consts.CHARGE_OPEN_GIFT_MONTH)
    show_ids = []
    for cfg_id, obj in game_config.charge.iteritems():
        if obj['is_show']:
            # 周卡月卡是否可以显示
            if obj['open_gift'] in open_gifts:
                award_info = award_app.get_pay_award_info(user, obj['open_gift'])
                if not award_info['can_buy']:
                    continue
            show_ids.append(cfg_id)

    show_ids.sort(key=lambda x: game_config.charge[x]['order'])
    return show_ids


def get_charge_config(user, charge_id=None, for_show=False):
    """获取用户充值相关状态
    Args:
        user: 用户对象
        charge_id: 充值项, 为None表示取所有, 有值时取此充值项
        for_show: 供前端使用
    Returns:
        充值详情
    """
    is_first_pay_func = user.user_m.is_first_pay
    can_first_pay_gift_func = user.user_m.can_first_pay_gift
    # 对应平台商品编号的映射, 有些平台在客户端支付时需要
    waresid_map = settings.PAYMENT_WARESID_MAP.get(user.user_m.platform, {})

    # 取charge_id此充值项返回
    if charge_id is not None:
        obj = game_config.charge[charge_id]
        first_pay = is_first_pay_func(obj)  # 首充状态
        can_first_gift = can_first_pay_gift_func(obj)  # 是否首充给予物品
        if first_pay == consts.CHARGE_CONFIG_FIRST_PAY_SP:
            first_diamond = obj['sp_diamond']
        else:
            first_diamond = obj['first_diamond']
        data = dict(obj, first_diamond=first_diamond, first_pay=first_pay,
                    is_first=0 if for_show and first_pay == 0 else obj['is_first'],
                    can_first_gift=can_first_gift,
                    waresid=waresid_map.get(charge_id))

        # 充值翻倍活动
        double_detail = charge_chargedouble(user, charge_id, first_pay)
        data.update(double_detail)

        return data

    # 取所有充值项返回
    charge_config = {}
    for cfg_id, obj in game_config.charge.iteritems():
        first_pay = is_first_pay_func(obj)  # 首充状态
        can_first_gift = can_first_pay_gift_func(obj)  # 是否首充给予物品
        if first_pay == consts.CHARGE_CONFIG_FIRST_PAY_SP:
            first_diamond = obj['sp_diamond']
        else:
            first_diamond = obj['first_diamond']

        charge_config[cfg_id] = dict(obj, first_diamond=first_diamond, first_pay=first_pay,
                                     is_first=0 if for_show and first_pay == 0 else obj['is_first'],
                                     can_first_gift=can_first_gift,
                                     waresid=waresid_map.get(cfg_id))
        # 充值翻倍活动
        double_detail = charge_chargedouble(user, cfg_id, first_pay)
        charge_config[cfg_id].update(double_detail)

    return charge_config


def charge_chargedouble(user, charge_id, first_pay):
    """充值翻倍活动
    Args:
        user: 用户对象
        change_id: 商品配置id
        first_pay: 是否首充
    Returns:
        翻倍活动数据, 为空字典表示没有翻倍活动
    """
    from apps.active import consts as active_consts
    from apps.active import logics as active_logics
    from apps.public import celebration as pub_celebration

    # 首充不参与活动
    if first_pay in consts.CHARGE_CONFIG_FIRST_PAY_SP_HAVE_LIST:
        return {}

    server_id = user.server_id
    ctrl_cfg = game_config.serverctrl[server_id]

    # 活动未配置
    cel_id = ctrl_cfg.get(active_consts.ACTIVE_MARK_CHARGEDOUBLE2, 0)
    cel_detail = game_config.celebration.get(cel_id)
    if not cel_detail:
        return {}

    # 活动未开启
    if not active_logics.active_open(server_id, cel_detail,
                                     active_consts.ACTIVE_MARK_CHARGEDOUBLE2,
                                     active_consts.ACTIVE_TIME_CHARGEDOUBLE):
        return {}

    # 该商品不参与活动
    cfg_id = game_config.charge_double_charge_id.get(charge_id)
    if cfg_id not in ctrl_cfg[active_consts.ACTIVE_MARK_CHARGEDOUBLE]:
        return {}

    # 本服没有开启此活动
    detail = game_config.charge_double[cfg_id]
    if -1 not in detail['server_id'] and int(server_id) not in detail['server_id']:
        return {}

    # 此商品活动未开启
    s_open_time = game_config.servers[user.server_id]['open_time']
    if not pub_celebration.get_activity_status(detail, s_open_time):
        return {}

    # 超过充值翻倍使用次数了
    double_times = charge_double_data(user, cfg_id)
    if double_times >= detail['buylimit']:
        return {}

    return {
        'act_diamond': detail['act_diamond'],     # 实际赠送的钻石数
        'des_double': detail['des_double'],       # 活动描述文字
        'del_show': detail['del_show'],           # 划掉的原价
    }


def chargedouble_add_coin(user, charge_id, first_pay):
    """充值翻倍活动期间额外添加的钻石
    Args:
        user: 用户对象
        change_id: 商品配置id
        first_pay: 是否首充
    Returns:
        额外加的钻石
    """
    chargedouble_data = charge_chargedouble(user, charge_id, first_pay)

    return chargedouble_data.get('act_diamond', 0)


def charge_double_data(user, charge_double_id):
    """获取充值翻倍使用次数
    Args:
        user: 用户对象
        cfg_id: charge_double配置ID
    Returns:
        充值翻倍使用次数
    """
    from apps.active import consts as active_consts

    cel_id = game_config.serverctrl[user.server_id][active_consts.ACTIVE_MARK_CHARGEDOUBLE2]
    active_data = user.active.active_info(cel_id, active_consts.ACTIVE_KEY_CHARGEDOUBLE,
                                          user.active.chargedouble_temp)
    double_times = active_data['data'].get(charge_double_id, 0)

    return double_times


def get_level_users(user, rank_start):
    """获取用户当前排名数据列表
    Args:
        user: 用户对象
        rank: 获取该排名后面的人数
    Returns:
        排名数据列表
    """
    users_list = []
    rank_data = user.exp_rank.pick_out_by_revrange(rank_start, rank_start+20-1, True)
    for rank, (uid, score) in rank_data:
        if uid == user.uid:
            info = user_more_info(user, rank=rank, score=int(score))
        else:
            info = user_more_info(uid=uid, rank=rank, score=int(score))
        users_list.append(info)

    return users_list


def get_ability_users(user, rank_start):
    """获取用户当前排名数据列表
    Args:
        user: 用户对象
        rank: 获取该排名后面的人数
    Returns:
        排名数据列表
    """
    users_list = []
    rank_data = user.ability_rank.pick_out_by_revrange(rank_start, rank_start+20-1, True)
    for rank, (uid, score) in rank_data:
        if uid == user.uid:
            info = user_more_info(user, rank=rank, score=int(score))
        else:
            info = user_more_info(uid=uid, rank=rank, score=int(score))
        users_list.append(info)

    return users_list


def get_user_detail(user):
    """获取用户详情
    """
    user_m = user.user_m
    config = game_config.user_info[user_m.level]

    current_time = int(time.time())
    energy = user_m.energy
    energy_top = user_m.get_energy_top()
    energy_delta = 0
    energy_grow_delta = game_config.user_ini['energy_grow']
    if energy < energy_top:
        energy_grow = energy_grow_delta * 60
        _, remainder = divmod(current_time - user_m.energy_fill_at, energy_grow)
        energy_delta = (energy_top - energy) * energy_grow - remainder
        energy_delta = max(0, energy_delta)

    battle = user_m.battle
    battle_top = user_m.get_battle_top()
    battle_delta = 0
    battle_grow_delta = game_config.user_ini['battlepoint_grow']
    if battle < battle_top:
        battlepoint_grow = battle_grow_delta * 60
        _, remainder = divmod(current_time - user_m.battle_fill_at, battlepoint_grow)
        battle_delta = (battle_top - battle) * battlepoint_grow - remainder
        battle_delta = max(0, battle_delta)

    strategy_detail = game_config.strategy[user.user_m.strategy]
    strategy_core_pos = []
    for pos in strategy_detail['core_pos']:
        card_id = user.card.team[pos - 1]
        card_obj = user.card.get_card(card_id)
        if card_obj:
            strategy_core_pos.append({'cfg_id': card_obj['cfg_id'],
                                      'from': card_obj['from']})

    return {
        'username': user_m.username,                   # 名字
        'uid': user_m.uid,                             # uid
        'vip': user_m.vip,                             # vip等级
        'logo': user_m.logo,                           # LOGO
        'level': user_m.level,                         # 等级
        'arena_rank': user_m.arena_rank,               # 锦标赛排名
        'cur_win': user.pve_ranking.cur_win,           # 赛季胜场
        'all_win': user.pve_ranking.all_win,           # 总胜场
        'pve_ranking_rank': user.pve_ranking.rank,     # 胜场排名
        'exp': user_m.exp,                             # 当前经验
        'exp_top': config['exp']-user_m.exp,           # 升下级还需要的经验
        'energy': energy,                              # 行动力
        'energy_top': energy_top,                      # 行动力上限
        'energy_filled_delta': energy_delta,           # 回満需要秒数
        'energy_grow_delta': energy_grow_delta,        # 恢复间隔的分钟
        'energy_grow_value': consts.ENERGY_HEAL_UNIT,  # 每次恢复的点数
        'battle': battle,                              # 战力点
        'battle_top': battle_top,                      # 战力点上限
        'battle_filled_delta': battle_delta,           # 回満需要秒数
        'battle_grow_delta': battle_grow_delta,        # 恢复间隔的分钟
        'battle_grow_value': consts.BATTLE_HEAL_UNIT,  # 每次恢复的点数
        'friend_num': user.friend.real_count(),        # 好友数
        'point': user_m.point,                         # 锦标赛积分
        'grade': user.pve_dynasty.grade,               # 王朝积分
        'ability': user_m.ability,                     # 球队实力
        'strategy': user.user_m.strategy,                # 战术
        'strategy_core_pos': strategy_core_pos,        # 核心位置
    }


def gamevs_time():

    conf = game_config.celebration
    item = {
        12: {'time_start': conf[12]['time_start'], 'time_end': conf[12]['time_end']},       # 12:{开始时间：结束时间}
        13: {'time_start': conf[13]['time_start'], 'time_end': conf[13]['time_end']},       # 13：{开始时间：结束时间}
    }
    return item


def get_inreview(user):
    """
    -1 表示关闭, None表示开启
    """
    from apps import active as active_app

    if settings.IS_INREVIEW:
        inreview = {
            'vip': -1,           # vip相关的屏蔽
            'user_center': -1,   # 用户中心
            #'charge': -1,        # 支付开关
            'bulletin': -1,      # 公告
            'signup': -1,        # 签到
            'activity': -1,      # 活动
            'unopen': -1,        # 敬请期待
            'chat': -1,          # 聊天
            'league': -1,        # 联盟
            'handbook': -1,      # 图鉴
            'gonglve': -1,       # 攻略
            'pve_ranking': -1,   # 胜场
            'notify': -1,        # 消息
            'strategy': -1,      # 战术
            'shop': -1,          # 商店
            'ad': None,          # 广告, 显示
            'opening_active': -1,   # 开服活动图标
            'ranking': -1,          # 排行榜
            'task': -1,             # 任务
            'achieve': -1,          # 成就
            'mix': -1,              # 交易所
            'extra_charge': None,   # 额外的充值按钮
            'guide_task': -1,       # 引导任务
            'pending': -1,          # 敬请期待
        }
    else:
        opening_active = active_app.show_opening_active_icon(user)
        inreview = {
            'ad': -1,        # 广告, 不显示
            'opening_active': opening_active,   # 开服活动图标
            'extra_charge': -1,                 # 额外的充值按钮
        }

        if user.user_m.level < 17:
            inreview['chat'] = -1

        # 临时屏蔽排行榜按钮显示
        if settings.ENV_NAME == 'appstore':
            now_time = time.strftime('%Y-%m-%d %H:%M:%S')
            if now_time < '2015-05-02 12:00:00':
                inreview['ranking'] = -1

    return inreview


def get_fill_info(user, item_id):
    """购买道具需要的信息
    Args:
        user: 用户对象
        item_id: 道具ID
    """
    detail = game_config.goods_diamond[item_id]

    return {
        'item_id': item_id,                                # 道具ID
        'item_num': user.item.get_num('item', item_id),    # 拥有道具数量
        'price': detail['cost'],                           # 购买价格
    }


def get_item_info(user):
    """行动力、战斗力不足时，弹框需要的数据
    Args:
        env: 运行环境
    """
    from apps.item import logics as item_logics
    from apps.item import consts as item_consts

    fill_battle_price = get_expense_price(user, consts.USER_EXPENSE_FILL_BATTLE)
    fill_energy_price = get_expense_price(user, consts.USER_EXPENSE_FILL_ENERGY)

    item_id = item_logics.get_item_from_sort(item_consts.ITEM_SORT_FILL_ENERGY, game_config)
    fill_energy = {'item_id': item_id, 'item_num': user.item.get_num('item', item_id)}

    item_id = item_logics.get_item_from_sort(item_consts.ITEM_SORT_FILL_BATTLE, game_config)
    fill_battle = {'item_id': item_id, 'item_num': user.item.get_num('item', item_id)}

    return {
        'fill_battle_price': fill_battle_price,      # 补充战力点的价格
        'fill_energy_price': fill_energy_price,      # 补充行动力的价格
        'fill_battle': fill_battle,                  # 补充战力点的数据
        'fill_energy': fill_energy,                  # 补充行动力的数据
    }


def get_alerts(user, method=None):
    """获取各种小红点
    Args:
        user: 用户对象
        method: 指定接口, 不传判断所有
    """
    from apps.chat.models import ChatMsg
    from apps import award as award_app
    from apps import task as task_app
    from apps import arena as arena_app
    from apps import item as item_app
    from apps import friend as friend_app
    from apps import active as active_app
    from apps import gacha as gacha_app
    from apps import notify as notify_app
    from apps import pve as pve_app
    from apps import card as card_app
    from apps import league as league_app
    from apps import gamevs as gamevs_app

    alerts = {
        'chat': 0,                      # 是否有私聊内容
        'award': 0,                     # 签到：有任意未领取的登陆奖励时1
        'task_award': 0,                # 任务：有任意未领取的任务奖励时2
        'achieve': 0,                   # 成就: 有任意未领取的成就奖励时
        'arena': 0,                     # 锦标赛有排名奖励3
        'patch' : 0,                    # 碎片包可合成4
        'friend': 0,                    # 好友送体力 和 好友邀请5,6
        'active': 0,                    # 普通活动是否有奖励
        'opening_active': 0,            # 开服活动是否有奖励
        'notify': 0,                    # 有新消息时，玩家还未读时13
        'pve': 0,                       # 探索度奖励没领取 14
        'pve_money': 0,                 # 探索度奖励没领取 15
        'pve_dynasty': 0,               # 探索度奖励没领取 16
        'ranking_award': 0,             # 有未领取的球票收入时17
        'strategy': 0,                  # 解锁新战术时18
        'backup': 0,                    # 解锁新陪练阵容时19
        #'pve_legend': 0,,              # 球星传奇 20
        'rent_foreign': 0,              # 挂牌外援为空 21
        'league': 0,                    # 联盟 22
        'gamevs_rating': 0,             # 评级赛开始后，玩家还有比赛未评级
        'free_gacha': 0,                # 任意一种免费抽卡没使用时11
        'patch_merge': 0,               # 争夺战碎片可合成 12
    }
    alert_all_methods = set((None, 'user.home', 'user.main_index'))

    if method in alert_all_methods:
        alerts.update({
            'chat': 1 if ChatMsg.get(user.uid) else 0,
            'award': award_app.alert_award(user),
            'task_award': task_app.has_task_award(user),
            'achieve': task_app.has_achieve_award(user),
            'arena': arena_app.alert_arena(user),
            'patch' : item_app.alert_patch_merge(user),
            'friend': friend_app.alert_friend_tips(user),
            'active': active_app.alert_active_award(user),
            'opening_active': active_app.alert_active_award(user, opening=True),
            'free_gacha': gacha_app.has_free_gacha(user),
            'patch_merge': item_app.can_patch_merge(user),
            'notify': notify_app.has_unread_notify(user),
            'pve': pve_app.alert_pve_award(user),
            'ranking_award': pve_app.has_ranking_award(user),
            'strategy': card_app.alert_strategy_unlock(user),
            'backup': card_app.alert_backup_unlock(user),
            'rent_foreign': card_app.alert_rent_foreign(user),
            'league': league_app.alert_league(user),
            'gamevs_rating': gamevs_app.alert_gamevs_rating(user),
        })
    else:
        alerts.update({
            'friend': friend_app.alert_friend_tips(user),
            'free_gacha': gacha_app.has_free_gacha(user),
            'patch_merge': item_app.can_patch_merge(user),
        })

    return alerts


def can_update_client_resource(user, res_ver='', must=True):
    """是否可以更新前端资源
    """
    # 不强制更新时不做判断
    if not must and not game_config.resource_update.get('update_type', 0):
        return False

    can_update = False
    # 通过后台开关控制用户的更新
    debug_mode = game_config.resource_update.get('debug', 0)
    # 全部用户正常更新
    if debug_mode == 0:
        can_update = True
    # debug用户更新
    elif debug_mode == 1:
        if is_debug_user(user):
            can_update = True

    # 最新版本先不做热更
    if res_ver == 'm1.1.01':
        can_update = False
        if debug_mode != 2 and is_debug_user(user):
            can_update = True

    return can_update and res_ver in game_config.resource_versions


def is_debug_user(user):
    """是否是debug用户
    """
    debug_users = game_config.resource_update.get('debug_users', [])
    if user and (user.uid in debug_users or user.user_m.token in debug_users):
        return True
    return False


def random_name(user):
    """随机一个名字
    Args:
        user: 用户对象
    Returns:
        随机名字
    """
    conf = game_config.random_name
    first_names = conf['first_name']
    middles = conf['middle']
    last_names = conf['last_name']

    first_name = random.choice(first_names)
    middle = random.choice(middles)
    last_name = random.choice(last_names)

    if middle == '%':
        middle = ''

    name = '%s%s%s' % (first_name, middle, last_name)

    while check_reduplicate(user, name):
        first_name = random.choice(first_names)
        middle = random.choice(middles)
        last_name = random.choice(last_names)
        if middle == '%':
            middle = ''
        name = '%s%s%s' % (first_name, middle, last_name)

    return name


def check_reduplicate(user, username):
    """检查昵称是否重复
    Args:
        user: 用户对象
        username: 用户昵称
    Return:
        True    此昵称已被使用
        False   此昵称还未使用
    """
    return user.username_hash.hexists(username)


@timer.job_func_decorater
def timer_update_highest_ability_rank(server_id):
    """每日0点将更新昨日最高战斗实力排行榜
    将今日最高战斗实力排行榜的内容全部转移到昨日最高战斗实力排行榜中
    """
    default_user = get_user('', server_id)

    redis_key = default_user.highest_ability_rank.key
    default_user.today_highest_ability_rank.snapshot_to(redis_key)


@timer.job_func_decorater
def timer_level_ranking_award(server_id):
    """个人等级排行发奖
    """
    level_log = []
    level_error_log = []
    active_time = time.strftime("%Y-%m-%d %H:%M:%S")
    today = time.strftime('%Y-%m-%d')
    print 'timer_level_ranking_award fun, server_id: %s, now: %s' % (server_id, active_time)

    open_time = game_config.servers[server_id]['open_time']
    time_values = datetime.datetime.strptime(open_time, "%Y-%m-%d %H:%M:%S")
    time_values += datetime.timedelta(days=6)
    time_value = datetime.datetime.strftime(time_values, '%Y-%m-%d')
    if today != time_value:
        return

    data = []
    default_user = get_user('', server_id)
    exp_rank = default_user.exp_rank.pick_out_by_revrange(1, 20)

    for rank, uid in exp_rank:
        if rank == 1:
            gift = [[100, 0, 10000]]
        elif rank == 2:
            gift = [[100, 0, 8000]]
        elif rank == 3:
            gift = [[100, 0, 5000]]
        elif rank in range(4, 11):
            gift = [[100, 0, 2000]]
        else:
            gift = [[100, 0, 1000]]
        data.append([rank, uid, gift])

    for rank, uid, gift in data:
        temp = {'rank': rank, 'uid': uid, 'gift': gift}
        try:
            user = get_user(uid, server_id)
            user.add_notify(default_user.NOTIFY_FROM_LEVELRANK, gift=gift)
            user.notify.save()
            level_log.append(temp)
        except:
            level_error_log.append(temp)

    print 'send award end:'
    print 'level_log:%s' % json.dumps(level_log)
    print 'level_error_log:%s' % json.dumps(level_error_log)


@timer.job_func_decorater
def timer_ability_ranking_award(server_id):
    """个人实力排行发奖
    """
    ability_log = []
    ability_error_log = []
    active_time = time.strftime("%Y-%m-%d %H:%M:%S")
    today = time.strftime('%Y-%m-%d')
    print 'timer_ability_ranking_award fun, server_id: %s, now: %s' % (server_id, active_time)

    open_time = game_config.servers[server_id]['open_time']
    time_values = datetime.datetime.strptime(open_time, "%Y-%m-%d %H:%M:%S")
    time_values += datetime.timedelta(days=13)
    time_value = datetime.datetime.strftime(time_values, '%Y-%m-%d')
    if today != time_value:
        return

    data = []
    default_user = get_user('', server_id)
    exp_rank = default_user.ability_rank.pick_out_by_revrange(1, 20)

    for rank, uid in exp_rank:
        if rank == 1:
            gift = [[100, 0, 10000]]
        elif rank == 2:
            gift = [[100, 0, 8000]]
        elif rank == 3:
            gift = [[100, 0, 5000]]
        elif rank in range(4, 11):
            gift = [[100, 0, 2000]]
        else:
            gift = [[100, 0, 1000]]
        data.append([rank, uid, gift])

    for rank, uid, gift in data:
        temp = {'rank': rank, 'uid': uid, 'gift': gift}
        try:
            user = get_user(uid, server_id)
            user.add_notify(default_user.NOTIFY_FROM_ABILITYRANK, gift=gift)
            user.notify.save()
            ability_log.append(temp)
        except:
            ability_error_log.append(temp)

    print 'send award end:'
    print 'ability_log:%s' % json.dumps(ability_log)
    print 'ability_error_log:%s' % json.dumps(ability_error_log)
