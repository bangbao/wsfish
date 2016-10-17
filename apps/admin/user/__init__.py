# coding: utf-8

import time
import itertools
import cPickle as pickle

import settings
from apps import user as user_app
from apps.config import game_config
from apps.user.models import TokenServerUid, Footprint, UsernameHash, LevelRank
from . import consts


def user_all(req, msg=''):
    """显示部分用户基本信息
    """
    server_id = req.get_argument('server_id')
    sort = req.get_argument('sort')
    page = int(req.get_argument('page', 1))
    next_page = req.get_argument('next_page', '')
    if next_page:
        page += 1
    delta = 50

    start, end = (page-1)*delta+1, page*delta
    temp_user = user_app.get_user('', server_id)
    rank_obj = temp_user['%s_rank' % sort]
    uids = rank_obj.all(start, end)
    users = ((rank, user_app.get_user(uid, server_id))
             for rank, uid in itertools.izip(xrange(start, end+1), uids))

    return search(req, users=users, msg=msg, select_page=page,
                  select_server=server_id, select_sort=sort)


def user_reset(req):
    """
    """
    uid = req.get_argument('uid').encode('utf-8')
    redirect = req.get_argument('redirect', '')

    if settings.DEBUG:
        user = user_app.get_user(uid)
        user.reset_all()
        msg = 'reset success'
        if redirect:
            req.redirect(redirect)
            return None, {}
    else:
        msg = 'not debug mode, can not delete user!'

    return user_all(req, msg=msg)


def search(req, msg='', select_page=1, users=[], select_server='00', select_sort=''):
    """
    """
    return 'admin/user/search.html', locals()


def show(req):
    """显示用户数据
    """
    uid = req.get_argument('uid').encode('utf-8')
    field = req.get_argument('field', 'user')

    user = user_app.get_user(uid)
    if not uid.isalnum() or user.is_new():
        return search(req, msg='user not exists: %s' % uid)

    return 'admin/%s/index.html' % field, {
        'user': user,
        'user_field': consts.USER_FIELDS,
        'field': field,
        'msg': '',
    }

def show_username(req):
    """根据用户昵称查询分服用户数据
    """
    username = req.get_argument('username').strip()
    server_id = req.get_argument('server_id', '0')
    field = req.get_argument('field', 'user')

    if not username:
        return search(req, msg='username is empty')
    if server_id not in game_config.servers:
        return search(req, msg='server not exists: %s' % server_id)

    uid = UsernameHash.get('', server_id).hget(username)
    if not uid:
        return search(req, msg='user not exists: %s' % username)
    user = user_app.get_user(uid)
    if user.is_new():
        return search(req, msg='user not exists: %s' % username)

    return 'admin/%s/index.html' % field, {
        'user': user,
        'user_field': consts.USER_FIELDS,
        'field': field,
        'msg': '',
    }

def index(req, user=None, msg=''):
    """用户数据首页
    """
    if user is None:
        uid = req.get_argument('uid')
        user = user_app.get_user(uid)
        if not uid.isalnum() or user.is_new():
            return search(req, msg='user not exists: %s' % uid)

    return 'admin/user/index.html', {
        'user': user,
        'user_field': consts.USER_FIELDS,
        'field': 'user',
        'msg': msg,
    }


def showtoken(req):
    """显示分服用户数据
    """
    user_token = req.get_argument('user_token', '')
    owner_user = None
    if not user_token:
        uid = req.get_argument('uid')
        owner_user = user_app.get_user(uid)
        user_token = owner_user.user_m.token

    footprint = Footprint.get_footprint(user_token)
    if not user_token or not footprint:
        return search(req, msg='token not exists')

    users = []
    for obj in footprint:
        user = user_app.get_user_by_token(user_token, obj['server_id'], read_only=True)
        if not user.is_new():
            users.append(user)

    if not owner_user and users:
        owner_user = users[0]

    if not owner_user:
        return search(req, msg='no users, retry the search!')

    return 'admin/user/user_token_show.html', {
        'users': users,
        'msg': '',
        'user': owner_user,
        'user_field': consts.USER_FIELDS,
        'field': 'user_token',
    }

def modify(req):
    """修改用户数据
    """
    uid = req.get_argument('uid')
    save = req.get_argument('save', False)

    user = user_app.get_user(uid)
    if user.is_new():
        return search(req, msg='user not exists')

    if save:
        changes = {}
        for attr, init_value in user.user_m._attrs.iteritems():
            value = req.get_argument(attr, '')
            if value and isinstance(init_value, (int, float)):
                value = int(float(value))

            if attr == 'coin':
                coin = value - user.user_m.coin
                user.user_m.incr_coin(coin, where=user.GOODS_FROM_ADMIN)

            elif value or value == 0:
                if attr == 'vip':
                    value = min(value, max(game_config.vip_function))
                elif attr == 'level':
                    min_lv = min(game_config.user_info)
                    max_lv = max(game_config.user_info)
                    value = value if min_lv <= value <= max_lv else user.user_m.level
                changes[attr] = value

        # 不直接修改等级， 走加经验方式
        if changes['level'] > user.user_m.level:
            need_exp = user_app.logics.get_levelup_exp(user.user_m.level, changes['level'], game_config)
            user.user_m.add_exp(need_exp)

        user.user_m.setattr(**changes)
        user.save_all()
        msg = 'save success'
    else:
        if settings.DEBUG:
            user.user_m.reset()
            msg = 'reset success'
        else:
            msg = 'not debug mode, can not delete user!'

    return index(req, user, msg=msg)


def skip_guide(req):
    """跳过新手引导
    """
    uid = req.get_argument('uid')
    skip = req.get_argument('skip', '')
    goto = req.get_argument('goto', '')
    step = int(req.get_argument('step', 1))

    user = user_app.get_user(uid)
    if user.is_new():
        return search(req, msg='user not exists')

    msg = ''
    if skip:
        user_app.skip_guide(user)
        msg = 'skip guide success'
    elif goto:
        group = game_config.guide_raw[step]['guidegroup']
        # 跳转到指定步数需要把高于group的步数清除
        for g in user.user_m.guide.keys():
            if g > group:
                user.user_m.guide.pop(g, None)
        user.user_m.do_guide(step, force=True)
        msg = 'goto guide success'
    user.save_all()

    return index(req, user, msg=msg)


def ban_user(req):
    """封号/解封
    """
    uid = req.get_argument('uid')
    is_ban = int(req.get_argument('is_ban'))

    user = user_app.get_user(uid)
    if user.is_new():
        return search(req, msg='user not exists')

    user.user_m.setattr(is_ban=is_ban)
    user.user_m.save()

    if is_ban:
        user.ban_rank.zadd(int(time.time()))
    else:
        user.ban_rank.reset()
    return index(req, user, msg='ban_user success')


def export(req):
    """导出用户数据到文件
    """
    uid1 = req.get_argument('export_uid')

    user = user_app.get_user(uid1)
    if user.is_new():
        return search(req, msg='user not exists')

    data = user.dumps()
    pickle_data = pickle.dumps(data, 1).encode('zip')

    req.set_header('Content-Type', 'application/txt')
    req.set_header('Content-Disposition', 'attachment;filename=%s.pickle' % uid1)
    req.write(pickle_data)
    return None, {}


def inject(req):
    """从文件注入数据到用户
    """
    uid1 = req.get_argument('inject_uid')
    file_obj = req.request.files.get('user_file', None)

    user = user_app.get_user(uid1, read_only=True)
    if user.is_new():
        return search(req, msg='user not exists')

    content = file_obj[0]['body']
    user.loads(pickle.loads(content.decode('zip')))
    user.save_all()

    return index(req, user, msg='inject data success')

