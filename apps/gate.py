# coding: utf-8

import json
import time
from pprint import pformat

import settings
from lib.utils.helper import strftimestamp
from lib.utils.mail import ErrorMail
from apps import user as user_app
from apps import notify as notify_app
from apps.config import game_config
from apps.notify import consts as notices
from apps.user import consts as user_consts
from apps.admin.urls import URL_MAPPING
from apps.admin.decorators import require_permission
from .consts import IGNORE_API
from .consts import IGNORE_RES_VER_LIMIT_API
from .consts import CARD_BAG_TOP_API
from .consts import METHOD_NAME_ERROR_NEED_RESTART


API_SUCCESS = 0                     # 合法请求
API_FAILMSG = 1                     # 一般的不符合条件的请求
API_UPDATE_CONFIG_VERSION = 2       # 配置更新
API_UPDATE_RESOURCE_VERSION = 3     # 客户端资源更新
API_OVERFLOW_CARD_TOP = 4           # 球员背包超上限
API_OVERFLOW_EQUIP_TOP = 5          # 装备背包超上限
API_PLAYER_NOT_ENOUGH = 6           # 阵容不足10人
API_COIN_NOT_ENOUGH = 7             # 钻石不足
API_ENERGY_NOT_ENOUGH = 8           # 行动力不足
API_BATTLE_NOT_ENOUGH = 9           # 战斗力不足
API_MONEY_NOT_ENOUGH = 10           # 金钱不足
API_FAILURE_NEED_RESTART = 11       # 需要重启游戏
API_VIP_LEVEL_NOT_ENOUGH = 12      # vip等级不足

# 提示消息到购买次数限制的映射
NOTICES_USER_VIP_LEVEL_NOT_ENOUGH_MAP = {
    notices.PVE_LEGEND_FIGHT_BUY_OVER: 1,
    notices.ARENA_FIGHT_BUY_OVER: 2,
    notices.USER_FILL_CAPABILITY_ENERGY_COUNT_TOP: 3,
    notices.USER_FILL_CAPABILITY_BATTLE_COUNT_TOP: 4,
    notices.SHOP_BUY_NO_BUY_COUNT_DAILY_MONEY_TREE_TIME: 5,
    notices.PVE_DYNASTY_RESTART_NO_FIGHT_TIMES: 6,
    notices.PVE_STAGE_RESET_BUY_OVER: 7,
    notices.PVE_STAGE_MAX_FIGHT_NUM: 8,
    notices.PVE_HSTAGE_RESET_BUY_OVER: 9,
    notices.PVE_HSTAGE_MAX_FIGHT_NUM: 10,
    notices.EQUIP_LEVELUP_ONEKEY_VIP_LIMIT: 11,
    notices.VIP_LEVEL_NOT_ENGOUGH: 12,
}


def server_filter(env):
    """检测分服设置是否有效
    Args:
        env: 运行环境
    Returns:
        是否被filter
    """
    server_id = env.get_argument('server_id', '00')
    msg_rc = None
    server_data = game_config.servers.get(server_id)
    if not server_data:
        msg_rc = notices.SERVER_NOT_EXISTS
    elif server_data['status'] == user_consts.GAME_SERVER_STATUS_MAINTENANING:
        msg_rc = notices.SERVER_IS_MAINTAINING
    elif server_data['open_time'] > time.strftime('%Y-%m-%d %H:%M:%S'):
        msg_rc = notices.SERVER_IS_MAINTAINING

    # 停服更新维护控制, 只debug用户可以游戏
    if msg_rc == notices.SERVER_IS_MAINTAINING:
        if user_app.is_debug_user(env.user):
            msg_rc = None

    if msg_rc:
        env.errno = API_FAILURE_NEED_RESTART
        env.msg = notify_app.get_notify_content(msg_rc)
        return True
    return False


def check_version(env, method):
    """检测客户端版本是否需要更新
    Args:
        env: 运行环境
        method: 接口名
    Returns:
        True: 目前是最新版本
        False: 版本过低需要更新
    """
    channel = env.get_argument('channel', '')
    version = env.get_argument('version', '')
    cfg_ver = env.get_argument('cfg_ver', '')
    res_ver = env.get_argument('res_ver', '')

    # 渠道不存在
    if channel and channel not in settings.ALL_PLATFORMS:
        msg_rc = notices.CHANNEL_ERROR
        env.errno = API_FAILMSG
        env.msg = notify_app.get_notify_content(msg_rc)
        return False

    channel_version = game_config.channel_version.get(channel, {})
    # 渠道版本维护控制
    if channel_version.get('maintaining', 0):
        msg_rc = notices.SERVER_IS_MAINTAINING
        env.errno = API_FAILURE_NEED_RESTART
        env.msg = notify_app.get_notify_content(msg_rc)
        return False

    # 渠道版本强制更新控制
    if channel_version.get('forceUpdate', 0) and version < channel_version['updateVersion']:
        msg_rc = notices.SERVER_RESOURCE_VERSION_LIMIT
        env.errno = API_UPDATE_RESOURCE_VERSION
        env.msg = channel_version['msg'] or notify_app.get_notify_content(msg_rc)
        return False

    # 停服更新维护控制
    resource_update_cfg = game_config.resource_update
    debug_server = resource_update_cfg.get('debug_server', 0)
    if debug_server:
        if not user_app.is_debug_user(env.user):
            msg_rc = notices.SERVER_IS_MAINTAINING
            env.errno = API_FAILURE_NEED_RESTART
            env.msg = notify_app.get_notify_content(msg_rc)
            return False

    # 打包版本太低, 请更新游戏
    if method not in IGNORE_RES_VER_LIMIT_API and \
            (res_ver and res_ver <= resource_update_cfg.get('res_ver') or \
             version and version <= resource_update_cfg.get('version')):
        env.errno = API_UPDATE_RESOURCE_VERSION
        msg_rc = notices.SERVER_RESOURCE_VERSION_LIMIT
        env.msg = notify_app.get_notify_content(msg_rc)
        return False

    if method in IGNORE_API:
        return True
    if settings.API_CONFIG_DEBUG:
        return True

    if env.user and env.user.user_m.is_in_guide():
        return True

    # 前端lua文件有更新
    if user_app.can_update_client_resource(env.user, res_ver, must=False):
        env.errno = API_UPDATE_RESOURCE_VERSION
        msg_rc = notices.SERVER_RESOURCE_UPDATE
        env.msg = notify_app.get_notify_content(msg_rc)
        return False

    # 配置过低
    current_cfg_ver = game_config.cfg_ver
    if game_config.api_check_version and cfg_ver != current_cfg_ver:
        env.errno = API_UPDATE_CONFIG_VERSION
        msg_rc = notices.SERVER_CONFIG_UPDATE
        env.msg = notify_app.get_notify_content(msg_rc)
        return False

    return True


def check_card_bag_top(env, method):
    """校验背包中卡牌、装备是否超出上限
    Args:
        env: 运行环境
        method: 接口名
    Returns:
        True:   未超上限
        False:  超出上限
    """
    if method not in CARD_BAG_TOP_API:
        return True, {}

    msg_rc = 0
    data = {}
    user = env.user
    if len(user.card.cards) >= user.user_m.get_cards_top():
        # 球员数量限制
        env.errno = API_OVERFLOW_CARD_TOP
        msg_rc = notices.CARD_BAG_OVERFLOW_CARDS_TOP
        data = user_app.get_fill_info(user, shop_consts.GOODS_DIAMOND_PLAYER)
    elif len(user.equip.equips) >= user.user_m.get_equips_top():
        # 装备数量限制
        env.errno = API_OVERFLOW_EQUIP_TOP
        msg_rc = notices.EQUIP_BAG_OVERFLOW_TOP
        data = user_app.get_fill_info(user, shop_consts.GOODS_DIAMOND_EQUIP)
    elif len(user.card.team)-user.card.team.count(None) < len(card_consts.CARD_TEAM_SEQ):
        # 阵容不足10人
        env.errno = API_PLAYER_NOT_ENOUGH
        msg_rc = notices.CARD_PLAYER_NOT_ENOUGH
    if msg_rc:
        env.msg = notify_app.get_notify_content(msg_rc)
        return False, data

    return True, {}


def user_functrl_filter(env, method):
    """校验用户是否开启了此功能
    Args:
        env: 运行环境
        method: 接口方法
    Returns:
        bool值
    """
    user = env.user
    if method not in user_consts.USER_FUNCTRL_METHODS:
        return False

    functrl_id = user_consts.USER_FUNCTRL_METHODS[method]

    # 函数返回的是文本
    text = user_app.check_user_functrl(user, functrl_id)
    if text:
        env.errno = API_FAILMSG
        env.msg = text
        return True

    return False


def api_filter(env, module_name, method_name, need_server=False):
    """检查API请求是否合法，非法请求直接返回
    Args:
        env: 运行环境
        module_name: module_name
        method_name: method_name
        need_server: 是否需要检测server_id
    Returns:
        是否被过滤掉, 返回的其他数据
    """
    if need_server and server_filter(env):
        return True, {}

    # 检测客户端版本是否需要更新
    method = '%s.%s' % (module_name, method_name)
    if not check_version(env, method):
        return True, {}

    # 没有用户对象
    user = env.user
    if not user:
        env.errno = API_FAILURE_NEED_RESTART
        env.msg = notify_app.get_notify_content(notices.USER_TOKEN_ERROR)
        return True, {}

    # 被封号了
    if user.user_m.is_ban:
        env.errno = API_FAILMSG
        env.msg = notify_app.get_notify_content(notices.USER_IS_BAN)
        return True, {}

    # 球员容量、装备容量是否超出上限
    to_continue, data = check_card_bag_top(env, method)
    if not to_continue:
        return True, data

    # 此功能是否受限开启了
    if user_functrl_filter(env, method):
        return True, data

    try:
        filter_module = __import__('apps.apis.filters.%s' % module_name,
                                   globals(), locals(), [method_name])
        filter_func = getattr(filter_module, method_name, lambda x: None)
    except ImportError:
        return False, {}

    msg_rc = filter_func(env)
    if msg_rc:
        if msg_rc == notices.COIN_NOT_ENOUGH:
            # 钻石不足
            env.errno = API_COIN_NOT_ENOUGH

        elif msg_rc == notices.ENERGY_NOT_ENOUGH:
            # 行动力不足
            env.errno = API_ENERGY_NOT_ENOUGH
            data.update(user_app.get_item_info(env.user))

        elif msg_rc == notices.BATTLE_NOT_ENOUGH:
            # 战斗力不足
            env.errno = API_BATTLE_NOT_ENOUGH
            data.update(user_app.get_item_info(env.user))

        elif msg_rc == notices.MONEY_NOT_ENOUGH:
            # 金钱不足
            env.errno = API_MONEY_NOT_ENOUGH

        elif msg_rc in NOTICES_USER_VIP_LEVEL_NOT_ENOUGH_MAP:
            # vip等级不足
            limit_type = NOTICES_USER_VIP_LEVEL_NOT_ENOUGH_MAP[msg_rc]
            buy_times = env.params.get('buy_times', 0)
            env.errno = API_VIP_LEVEL_NOT_ENOUGH
            data.update(limit_type=limit_type, buy_times=buy_times)

        elif method in METHOD_NAME_ERROR_NEED_RESTART and \
                msg_rc != notices.CARD_EVOLUTION_CARD_LEVEL_LOW:
            # 需要重启游戏的报错
            env.errno = API_FAILURE_NEED_RESTART
        else:
            env.errno = API_FAILMSG

        env.msg = notify_app.get_notify_content(msg_rc)
        return True, data

    return False, {}


def api_method(env, method, need_server=False):
    """正常请求，返回接口数据
    Args:
        env: 运行环境
        method: method
        need_server: 是否需要检测server_id
    Returns:
        返回接口data数据
    """
    try:
        module_name, method_name = method.split('.')
    except ValueError:    # 过滤非法请求
        env.errno = API_FAILMSG
        env.msg = notify_app.get_notify_content(notices.SYSTEM_ERROR)
        return {}

    # 是否被过滤掉
    to_filter, data = api_filter(env, module_name, method_name, need_server)
    if to_filter:
        return data

    try:
        method_module = __import__('apps.apis.%s' % module_name,
                                   globals(), locals(), [method_name])
        method_func = getattr(method_module, method_name)
    except (ImportError, AttributeError):    # 过滤非法请求
        env.errno = API_FAILMSG
        env.msg = notify_app.get_notify_content(notices.SYSTEM_ERROR)
        return {}

    env.result = method_func(env)
    return env.result


@ErrorMail(settings.MAIL_SETTINGS)
def api_response(env):
    """组装API请求的返回数据, 必定会生成user对象
    Args:
        env: 运行环境
    Returns:
        返回response
    """
    user = env.user
    method_param = env.get_argument('method', '')

    # 用户等级提升
    if user and method_param:
        levelup = None
        levelup_award = None
        old_levelup = user_app.user_levelup(user)

    # 处理接口返回数据
    data = api_method(env, method_param, True)

    if user and method_param and not method_param.startswith(('config', 'client')):
        # 统一处理新手引导状态更新
        guide_id = env.get_argument('guide_id', '')
        if guide_id.isdigit() and env.errno == 0:
            guide_id = int(guide_id)
            # 新手中结算若guide_id 和 pve.gamerace_start 中一致,就说明步骤出错了. 加1修正
            if method_param == 'pve.gamerace' and user.user_m.is_in_guide():
                stage = int(env.get_argument('stage'))
                stage_guide_map = {101: 112, 102: 135, 103: 160, 201: 184}
                guide_id = stage_guide_map.get(stage, guide_id)
            user_app.sync_guide_status(user, guide_id)

        # 计算用户升级数据变化, 特殊接口返回levelup_backup值(dict)
        new_levelup = user_app.user_levelup(user)
        if new_levelup['level'] != old_levelup['level']:
            levelup_backup = {
                'energy': user.user_m.low_lv_energy,
                'battle': user.user_m.low_lv_battle,
            }
            user_app.update_user_levelup(old_levelup, levelup_backup)
            levelup = user_app.logics.merge_dict_value2list(old_levelup, new_levelup)
            levelup_award = user_app.check_user_levelup_award(user, old_levelup['level'], new_levelup['level'])

        # 若此时用户被锁定, 不保存数据
        if user.user_m.has_redis_lock():
            if method_param not in ('payment.refresh', 'user.fresh', 'user.home'):
                raise Exception('user %s had locked' % user.uid)
        else:
            # 操作完成后统一保存用户数据
            user.save_all()

        # 关于客户端数据缓存的更新
        #data['_client_cache_update'] = user.get_client_cache_update()

    if settings.DEBUG_PRINT and not method_param.startswith(('config', 'user.loading', 'user.game_enter')):
        uid = user.uid if user else 'none'
        print '%s, %s, %s, %s' % (method_param, env.errno, env.msg, uid), json.dumps(data, ensure_ascii=False)

    return_data = {
        'data': data,           # 接口返回数据
        'status': env.errno,    # 接口返回状态
        'msg': env.msg,         # 接口提示消息
        'caches': None,         # 接口cache数据, 若status不为0则不需要
    }
    if user and env.errno == 0 and not method_param.startswith(('config', 'client')):
        gamevs_status = gamevs_app.get_gamevs_status()
        return_data['caches'] = {
            'user': user_app.user_cache(user, method_param),      # 用户常用数据
            'levelup': levelup,                     # 用户等级变化数据
            'levelup_award': levelup_award,         # 用户等级变化时给的物品
            'item': user_app.item_cache(user),      # 用户道具缓存
            'patchplayers': user_app.patchplayer_cache(user, method_param), # 若本动作得到球员碎片, 返回该碎片新的数量
            'alerts': user_app.get_alerts(user, method_param),    # 小红点
            'gamevs_status': gamevs_status,         # 联赛状态, 0联赛,1评级赛
        }
        # 若此时用户被锁定, 不保存数据
        if user.user_m.has_redis_lock():
            if method_param not in ('payment.refresh', 'user.fresh', 'user.home'):
                raise Exception('user %s had locked' % user.uid)
        else:
            # 操作完成后统一保存用户数据
            user.save_all()

    return return_data


@ErrorMail(settings.MAIL_SETTINGS)
def loading_response(env):
    """配置，资源相关， 不生成user对象
    """
    method_param = env.get_argument('method')
    module_name, method_name = method_param.split('.')

    try:
        module_name, method_name = method_param.split('.')
        msg_rc = 0
    except ValueError:    # 过滤非法请求
        msg_rc = notices.SYSTEM_ERROR
    else:
        try:
            filter_module = __import__('apps.apis.filters.%s' % module_name,
                                       globals(), locals(), [method_name])
            filter_func = getattr(filter_module, method_name, lambda x: None)
            msg_rc = filter_func(env)
        except ImportError:
            msg_rc = 0

    if msg_rc:
        env.errno = API_FAILMSG
        env.msg = notify_app.get_notify_content(msg_rc)
        env.result = {}
    else:
        method_module = __import__('apps.apis.%s' % module_name,
                                   globals(), locals(), [method_name])
        method_func = getattr(method_module, method_name, lambda x: 'method_error')
        env.result = method_func(env)
        # 平台登录验证特殊处理
        if method_param in ('user.platform_access',):
            if not env.result or not env.result.get('token'):
                env.errno = API_FAILMSG
                env.msg = notify_app.get_notify_content(notices.USER_PLATFORM_ACCESS_FAILTURE)

    if settings.DEBUG_PRINT:
        if method_param not in ('config.all_config',):
            print '%s, %s, %s' % (method_param, env.errno, env.msg), json.dumps(env.result, ensure_ascii=False)

    return {
        'data': env.result,        # 接口返回数据
        'status': env.errno,       # 接口返回状态
        'msg': env.msg,            # 接口提示消息
    }


@ErrorMail(settings.MAIL_SETTINGS)
def admin_response(env):
    """后台数据处理
    """
    admin_pre = '/%s' % getattr(settings, 'ADMIN_PRE', 'nba')
    req = env.req
    path = req.request.path
    if path.startswith(admin_pre):
        path = path.replace(admin_pre, '')

    if path not in URL_MAPPING:
        req.finish('HTTPError 403: url=%s' % req.request.path)
        return

    func_path = URL_MAPPING[path]
    module_name, method_name = func_path.split('.')
    method_module = __import__('apps.admin.%s' % module_name,
                               globals(), locals(), [method_name])
    method_func = getattr(method_module, method_name)
    method_func = require_permission(method_func)
    template_and_data = method_func(req)
    template, data = template_and_data if template_and_data else (None, {})

    data['get_url'] = settings.get_url
    data['tformat'] = strftimestamp
    data['game_config'] = game_config
    data['json_dumps'] = json.dumps
    data['pformat'] = pformat
    data['settings'] = settings

    return template, data
