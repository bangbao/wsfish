# coding: utf-8

import time
import datetime
import hashlib
import random
import cPickle as pickle

import settings
from apps.config import game_config
from apps.user import consts as user_consts
from apps.user.models import TokenServerUid, OnlineRank, RegistRank, get_redis_userd_memory
from . import auth
from . import consts
from .models import Admin


def index(req):
    """后台首页
    """
    admin = auth.get_admin_by_request(req)

    if settings.DEBUG:
        left_herf_list = [(path, consts.URL_SETTINGS[path][1])
                          for path in consts.LEFT_HREF]
    else:
        left_herf_list = [(path, consts.URL_SETTINGS[path][1])
                          for path in consts.LEFT_HREF
                          if not consts.URL_SETTINGS[path][-1] or admin and admin.has_perm_path(path)]

    return 'admin/index.html', {'left_herf_list': left_herf_list, 'admin': admin}


def left(req):
    """左边视图
    """
    admin = auth.get_admin_by_request(req)

    if settings.DEBUG:
        left_herf_list = [(path, consts.URL_SETTINGS[path][1])
                          for path in consts.LEFT_HREF]
    else:
        left_herf_list = [(path, consts.URL_SETTINGS[path][1])
                          for path in consts.LEFT_HREF
                          if not consts.URL_SETTINGS[path][-1] or admin and admin.has_perm_path(path)]

    return 'admin/left.html', {'left_herf_list': left_herf_list}


def change_password(req):
    """
    """
    msg = ''
    if req.request.method == 'POST':
        old = req.get_argument('old_password').strip()
        pwd1 = req.get_argument('password1').strip()
        pwd2 = req.get_argument('password2').strip()

        if not pwd1 or not pwd2:
            msg = u'密码不能为空'
        elif pwd1 != pwd2:
            msg = u'两次输入密码不同'
        else:
            admin = auth.get_admin_by_request(req)
            if admin:
                if not admin.check_password(old):
                    msg = u'原始密码错误'
                else:
                    admin.set_password(pwd1)
                    admin.save()
                    msg = u'change password success'

    return 'admin/change_password.html', {'msg': msg}


def login(req):
    """
    """
    msg = req.get_argument('msg', '')
    if req.request.method == 'POST':
        username = req.get_argument('username', '').strip()
        password = req.get_argument('password', '').strip()
        admin = Admin.get(username)
        if not admin:
            return logout(req, msg=u'账号不存在')

        if not admin.check_password(password):
            return logout(req, msg=u'密码错误')

        auth.login(req, admin)
        return req.redirect(settings.get_url('/admin/index/'))

    return 'admin/login.html', {'msg': msg}

def logout(req, msg=''):
    auth.logout(req)
    req.current_user = None
    return req.redirect(settings.get_url('/admin/login/?msg=%s' % msg))


def admin_list(req, msg=''):
    """
    """
    admins = Admin.all()
    return 'admin/admin_list.html', {'admin_list': admins, 'msg': msg}


def admin_add(req):
    """新建管理员
    """
    result = {'consts': consts, 'msg': ''}

    if req.request.method == "POST":
        username = req.get_argument("username", '').strip()
        password = req.get_argument("password", '').strip()
        password1 = req.get_argument("password1", '').strip()
        #email = req.get_argument("email", '').strip()

        if not username or not password:
            result['msg'] = u'帐号、密码不能为空'
            return "admin/admin_add.html", result

        if not username.isalnum() or not password.isalnum():
            result['msg'] = u'帐号、密码只能由英文字母、数字组成'
            return "admin/admin_add.html", result

        admin = Admin.get(username)
        if admin:
            result['msg'] = u'帐号已存在'
            return "admin/admin_add.html", result

        if password != password1:
            result['msg'] = u'两次密码输入不同'
            return "admin/admin_add.html", result

        # 权限
        perms = {}
        for perm_key in consts.PERM_KEYS:
            perms[perm_key] = int(req.get_argument(perm_key, 0))

        auth.create_admin(username, password, perms)

        return req.finish('添加成功')

    else:
        return "admin/admin_add.html", result


def admin_delete(req):
    """删除管理员
    """
    mid = req.get_argument('mid')
    Admin().delete(mid)
    return admin_list(req, msg='delete success')


def admin_manage(req):
    """修改管理员
    """
    mid = req.get_argument('mid')
    msg = ''
    admin = Admin.get(mid)

    if admin is None:
        return admin_list(req, msg='admin [%s] not exists' % mid)

    if req.request.method == "POST":
        perms = {}
        for perm_key in consts.PERM_KEYS:
            perms[perm_key] = int(req.get_argument(perm_key, 0))
        admin.set_permissions(perms)
        admin.save()
        msg = 'set perms success'

    return 'admin/admin_manage.html', {
        'consts': consts,
        'admin': admin,
        'msg': msg,
    }


def server_list(req, msg=''):
    """服务器配置
    """
    servers = game_config.get_config('servers')
    new_server_id = ('%02d' % (int(max(servers)) + 1)) if servers else '01'
    user_counts = TokenServerUid.get_user_count()
    now = datetime.datetime.now()
    new_open_time = now + datetime.timedelta(days=1)
    return 'admin/game_servers.html', {'new_server_id': new_server_id,
                                       'new_open_time': new_open_time.strftime('%Y-%m-%d %H:00:00'),
                                       'server_status': user_consts.GAME_SERVER_STATUS_MAP,
                                       'user_counts': user_counts,
                                       'OnlineRank': OnlineRank,
                                       'RegistRank': RegistRank,
                                       'servers': servers,
                                       'get_payment_count': lambda x: '0 / 0',
                                       'get_redis_userd_memory': get_redis_userd_memory,
                                       'now_time': now.strftime('%Y-%m-%d %H:%M:%S'),
                                       'msg': msg}


def create_new_server(req):
    """新加一个新服
    """
    server_id = req.get_argument('server_id')
    server_name = req.get_argument('server_name')
    open_time = req.get_argument('open_time')
    status = int(req.get_argument('status', 1))
    uid_start_num = int(req.get_argument('uid_start_num', 0))
    uid_start_num = uid_start_num or random.randint(610, 800)

    servers = game_config.get_config('servers')
    if server_id in servers:
        msg = 'error: server_id exists'
    elif not server_name:
        msg = 'error: server_name can not be empty'
    elif server_id not in settings.DATABASES['servers']:
        msg = 'error: server_db not ready'
    else:
        # server_tag仅供前端显示使用
        server_tag = int(server_id)
        if server_tag > settings.SERVER_TAG_DELTA > 0:
            server_tag -= settings.SERVER_TAG_DELTA
        servers[server_id] = {
            'open_time': open_time,        # 开服时间
            'status': status,              # 分服状态
            'server_id': server_id,        # 分服ID
            'server_tag': server_tag,      # 排序权重
            'server_name': server_name,    # 分服名称
        }
        game_config.set_config('servers', servers)
        game_config.servers.update(servers)
        # 分服开启时初始化竞技场npc
        TokenServerUid.incrby_user_count(server_id, amount=uid_start_num)
        arena_app.init_arena_rank(server_id)
        gamevs_app.init_gamevs_section_rank(server_id)
        msg = 'create new server success'

    return server_list(req, msg=msg)


def modify_server(req):
    """修改服务配置
    """
    server_id = req.get_argument('server_id')
    server_name = req.get_argument('server_name')
    open_time = req.get_argument('open_time', '')
    status = int(req.get_argument('status', 1))

    servers = game_config.get_config('servers')
    if open_time:
        try:
            time.strptime(open_time, '%Y-%m-%d %H:%M:%S')
        except:
            msg = 'open_time error'
        else:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S')
            old_open_time = servers[server_id]['open_time']
            if old_open_time <= now_time:
                msg = 'server %s is opened, can not be changed open_time!' % server_id
            else:
                servers[server_id].update(server_name=server_name, status=status, open_time=open_time)
                msg='modify_server success'
    else:
        servers[server_id].update(server_name=server_name, status=status)
        msg='modify_server success'

    game_config.set_config('servers', servers)

    return server_list(req, msg=msg)


def upload(req):
    """上传一些数据
    Args:
        type: 类型， 1resource_version
    """
    tp = int(req.get_argument('type', 0))
    sign = req.get_argument('sign', '')
    data = req.request.body

    sign_data = '%s:%s:%s' % (settings.RESOURCE_SIGNATURE_KEY, tp, data)
    new_sign = hashlib.md5(sign_data).hexdigest()
    if new_sign == sign:
        result = {'rc': 0, 'msg': 'empty'}
        if tp == 1:
            resource_versions = pickle.loads(data.decode('zip'))
            game_config.set_config('resource_versions', resource_versions)
            resource_update = dict(game_config.resource_update, debug=2)
            game_config.set_config('resource_update', resource_update)
            game_config.notify_reload()
            result['msg'] = 'resource_versions upload success'
    else:
        result = {'rc': 1, 'msg': 'sign error'}

    return req.finish(result)

