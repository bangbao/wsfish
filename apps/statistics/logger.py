# coding: utf-8

import os
import json
import time
import copy
import base64

import settings
from lib.utils import merge_dict_value2list
from . import logger_funcs
from . import reyun, reyun_utils
from . import cmge, cmge_utils

IGNORE_METHODS =  set([
    'config.all_config',
    'config.config_version',
    'config.resource_version',
    'client.exception_info',
    'user.get_bulletin',
    'battle.ready',
    'battle.settlement',
    'battle.fight',
])
LOG_PATH = os.path.join(settings.LOGS_ROOT, 'action')
LOGFILENAME_FORMAT = '%s_%s_%s.log' % (settings.ENV_NAME, '%s', '%s')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
    os.chmod(LOG_PATH, 511)

# 日志标准格式
LOG_FORMATTER = [
    'timestamp',
    'server',
    'uid',
    'platform',
    'method',
    'rc',
    'base',
    'args',
    'returns',
]

reyun_api = cmge_api = None
if settings.SEND_LOG_TO_REYUN:
    reyun_api = reyun.API(settings.STATS_REYUN_APPKEY)
if settings.SEND_LOG_TO_CMGE:
    cmge_api = cmge.API(settings.DATABASES['templog'])


class Logger(object):
    def __init__(self):
        """
        """
        self.STATS_SWITCH = getattr(settings, 'STATS_SWITCH', False)
        self.LOG_PATH = LOG_PATH
        self.formatter = LOG_FORMATTER

    def format(self, data,  delimiter='\t'):
        '''格式化数据'''
        record = []
        for item in self.formatter:
            d = json.dumps(data.get(item, ''))
            record.append(d.strip('"'))
        return delimiter.join(record)

    def write(self, data):
        '''将数据写到规定的渠道'''
        record = self.format(data)
        logfilename = LOGFILENAME_FORMAT % (time.strftime('%Y%m%d'), os.getpid())
        with open(os.path.join(self.LOG_PATH, logfilename), 'a+') as f:
            f.write(record)
            f.write('\n')

    def get_user_base_data(self, user):
        """获取用户常用的基本信息
        """
        if user:
            user_m = user.user_m
            guide = {}
            if user_m.guide:
                group = max(user_m.guide)
                guide[group] = user_m.guide[group]

            props = {'patch': copy.copy(user.patch.patchs)}
            for key in user.item.ITEM_TYPES:
                data = getattr(user.item, key, {})
                props[key] = copy.copy(data)
            return {
                'level': user_m.level,
                'exp': user_m.exp,
                'vip': user_m.vip,
                'vip_exp': user_m.vip_exp,
                'coin': user_m.coin,
                'money': user_m.money,
                'energy': user_m.energy,
                'battle': user_m.battle,
                'honor': user_m.honor,
                'point': user_m.point,
                'guide': guide,
                'props': props,
            }
        return {}

    def basecallback(self, env, args, returns):
        '''获取固定的数据，日志只是记录登陆用户的动作，如果没有登陆则标记此条日志为失败！！！
        '''
        args.pop('method', None)
        returns = base64.b64encode(repr(returns).encode('zip')) if returns else ''
        data = {
            'timestamp': time.strftime('%Y%m%d%H%M%S'),
            'server': '00',
            'uid': '',
            'platform': '',
            'method': self.method,
            'rc': env.errno,
            'base': {},
            'args': args,
            'returns': returns,
        }
        user = env.user
        if user:
            base = merge_dict_value2list(self.pre_userdata, self.post_userdata)
            data['server'] = user.server_id
            data['uid'] = user.uid
            data['platform'] = user.user_m.platform
            data['base'] = base
        return data

    def prepare_logger(self, env):
        """写日志前准备一些数据
        """
        try:
            api_method = env.get_argument('method', '')
            logger_func_name = api_method.replace('.', '_')
            self.method = api_method
            self.post_func = getattr(logger_funcs, logger_func_name, None)
            self.pre_userdata = self.get_user_base_data(env.user)
        except Exception as e:
            print repr(e)

    def handle_logger(self, env):
        """处理日志内容,写入数据库
        """
        # 非200的请求不做记录
        #if env.req.get_status() != 200:
        #    return
        # 跳过一些接口的日志记录
        if self.method in IGNORE_METHODS:
            return

        try:
            self.post_userdata = self.get_user_base_data(env.user)
            args = dict(env.req.summary_params())
            if self.post_func:
                returns = self.post_func(env, args, env.result)
            else:
                returns = {} #env.result

            # 写货币的消费日志
            self.write_economy_log(env, args, env.result)

            # 写接口日志
            if self.STATS_SWITCH:
                self.write_method_log(env, args, returns)

            if settings.SEND_LOG_TO_CMGE:
                self.send_log_to_cmge(env, args, env.result)

            # # 把日志发到reyun
            if settings.SEND_LOG_TO_REYUN:
                self.send_log_to_reyun(env, args, env.result)
        except Exception as e:
            print repr(e)


    def write_economy_log(self, env, args, returns):
        """coin, money的消费记录
        """
        old_coin = self.pre_userdata.get('coin', 0)
        new_coin = self.post_userdata.get('coin', 0)
        if old_coin != new_coin:
            env.user.subrecord.add_record_coin_api(env.user, self.method, old_coin, new_coin, args)

        # event  money消费记录
        old_money = self.pre_userdata.get('money', 0)
        new_money = self.post_userdata.get('money', 0)
        if old_money != new_money:
            env.user.subrecord.add_record_money_api(env.user, self.method, old_money, new_money, args)

    def write_method_log(self, env, args, returns):
        """每个接口动作的日志
        """
        rc = env.errno
        if rc == 0:
            self.write(self.basecallback(env, args, returns))

    def send_log_to_cmge(self, env, args, returns):
        """把日志发送给reyun
        """
        if env.errno != 0:
            return

        s = time.time()
        method = self.method
        deviceid = env.get_argument('deviceid', '') or ''
        version = env.get_argument('version', '') or ''
        clientip = env.req.request.headers.get('X-Real-IP') or ''

        if self.method in cmge_utils.METHOD_MAPPING:
            can_send = True
            # 未注册用户不发送登录数据
            if self.method == 'user.mark_login' and env.user.is_new():
                can_send = False

            if can_send:
                event_name = cmge_utils.METHOD_MAPPING[method]
                event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                     deviceid=deviceid, version=version,
                                                     clientip=clientip, method=method)
                cmge_api.produce(event_kwargs)
                #print 'send_log_to_cmge1:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # 新用户注册时直接登录
        if self.method == 'user.game_enter':
            event_name = 'role_login'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 deviceid=deviceid, version=version,
                                                 clientip=clientip, method=method)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge2:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        user = env.user
        if not user:
            return

        #get_item
        get_item_change = getattr(user, 'add_item_change', [])
        if get_item_change:
            event_name = 'get_item'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 get_item_change=get_item_change,
                                                 method=method)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge3:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # remove_item
        remove_item_change = getattr(user, 'reduce_item_change', [])
        if remove_item_change:
            event_name = 'remove_item'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 reduce_item_change=remove_item_change,
                                                 method=method)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge4:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # get_money, remove_money
        old_money = self.pre_userdata.get('money', 0)
        new_money = self.post_userdata.get('money', 0)
        if old_money != new_money:
            event_name = 'get_money' if old_money < new_money else 'remove_money'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 pre=old_money, after=new_money,
                                                 method=method, deviceid=deviceid)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge5:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # get_i_money, remove_i_money
        old_coin = self.pre_userdata.get('coin', 0)
        new_coin = self.post_userdata.get('coin', 0)
        if old_coin != new_coin:
            event_name = 'get_i_money' if old_coin < new_coin else 'remove_i_money'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 pre=old_coin, after=new_coin,
                                                 method=method, deviceid=deviceid)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge6:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # e_create
        add_equip_change = getattr(user, 'add_equip_change', [])
        if add_equip_change:
            event_name = 'e_create'
            for equip_data in add_equip_change:
                equip_cid = equip_data['cfg_id']
                event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                     deviceid=deviceid, version=version,
                                                     method=method, equip_cid=equip_cid)
                cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge7:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # get_exp
        old_exp = self.pre_userdata.get('exp', 0)
        new_exp = self.post_userdata.get('exp', 0)
        if old_exp < new_exp:
            event_name = 'get_exp'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 pre=old_exp, after=new_exp,
                                                 method=method, deviceid=deviceid)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge8:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # level_up
        old_level = self.pre_userdata.get('level', 0)
        new_level = self.post_userdata.get('level', 0)
        if old_level < new_level:
            event_name = 'level_up'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 pre_level=old_level, after_level=new_level,
                                                 pre_exp=old_exp, after_exp=new_exp,
                                                 method=method, deviceid=deviceid)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge9:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # newg
        guide_id = env.get_argument('guide_id', '')
        if guide_id and user.user_m.is_in_guide():
            event_name = 'newg'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 guide_id=int(guide_id),
                                                 method=method)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge10:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # h_create
        add_card_change = getattr(user, 'add_card_change', [])
        if add_card_change:
            event_name = 'h_create'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 add_card_change=add_card_change,
                                                 method=method)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge11:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # h_remove
        del_card_change = getattr(user, 'del_card_change', [])
        if del_card_change:
            event_name = 'h_remove'
            event_kwargs = cmge_utils.get_kwargs(event_name, env, args, returns,
                                                 del_card_change=del_card_change,
                                                 method=method)
            cmge_api.produce(event_kwargs)
            #print 'send_log_to_cmge12:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

    def send_log_to_reyun(self, env, args, returns):
        """把日志发送给reyun
        """
        if env.errno != 0:
            return

        s = time.time()
        deviceid = env.get_argument('deviceid', '') or 'unknown'
        serverid = env.get_argument('server_id', '') or 'unknown'
        channelid = env.get_argument('channel', '') or 'unknown'

        if self.method in reyun_utils.METHOD_MAPPING:
            can_send = True
            # 未注册用户不发送登录数据
            if self.method == 'user.mark_login' and env.user.is_new():
                can_send = False

            if can_send:
                event_name = reyun_utils.METHOD_MAPPING[self.method]
                event_kwargs = reyun_utils.get_kwargs(event_name, env, args, returns)
                event_kwargs['serverid'] = serverid
                event_kwargs['channelid'] = channelid
                event_func = getattr(reyun_api, event_name)
                event_func(deviceid, **event_kwargs)
                print 'send_log_to_reyun1:%s  %r, %.3f' % (event_name, event_kwargs, time.time()-s)

        # 新用户注册时直接登录
        if self.method == 'user.game_enter':
            event_name = 'loggedin'
            kwargs = reyun_utils.get_kwargs(event_name, env, args, returns)
            kwargs['serverid'] = serverid
            kwargs['channelid'] = channelid
            event_func = getattr(reyun_api, event_name)
            event_func(deviceid, **event_kwargs)
            print 'send_log_to_reyun4:%s  %r, %.3f' % ('loggedin_by_game_enter', kwargs, time.time()-s)

        # economy  coin消费记录
        old_coin = self.pre_userdata.get('coin', 0)
        new_coin = self.post_userdata.get('coin', 0)
        if old_coin > new_coin:
            kwargs = reyun_utils.get_kwargs_economy(env, args, returns,
                                                    method=self.method, cost=old_coin-new_coin)
            kwargs['serverid'] = serverid
            kwargs['channelid'] = channelid
            reyun_api.economy(deviceid, **kwargs)
            print 'send_log_to_reyun2:%s  %r, %.3f' % ('economy', kwargs, time.time()-s)

        # event  money消费记录
        old_money = self.pre_userdata.get('money', 0)
        new_money = self.post_userdata.get('money', 0)
        if old_money > new_money:
            kwargs = reyun_utils.get_kwargs_event(env, args, returns, what='money_cost',
                                                  method=self.method, cost=old_money-new_money)
            kwargs['serverid'] = serverid
            kwargs['channelid'] = channelid
            reyun_api.event(deviceid, **kwargs)
            print 'send_log_to_reyun3:%s  %r, %.3f' % ('event', kwargs, time.time()-s)


def auto_send_hearbeat_to_reyun(server_id):
    """发送心跳日志到热云
    """
    import gevent
    from apps.user import get_user
    from apps.user.models import OnlineRank

    def get_uid_hearbeat_kwargs(uid):
        user = get_user(uid, server_id)
        user_m = user.user_m
        if user_m.deviceid:
            kwargs = {'channelid': user_m.platform or 'unknown',
                      'deviceid': user_m.deviceid or 'unknown',
                      'who': uid, 'serverid': server_id, 'level': user_m.level}
            return kwargs

    online_rank = OnlineRank.get(server_id, server_id)
    uids = online_rank.get_onlines(delta=300)
    step = 5
    for delta in xrange(0, len(uids), step):
        jobs = []
        for uid in uids[delta:delta+step]:
            kwargs = get_uid_hearbeat_kwargs(uid)
            if kwargs:
                job = gevent.spawn(reyun_api.heartbeat, **kwargs)
                jobs.append(job)
        gevent.joinall(jobs)
    print('auto_send_hearbeat_to_reyun: %s--%s' % (server_id, len(uids)))

