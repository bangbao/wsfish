# coding: utf-8

from apps import user as user_app
from apps.config import game_config
from apps.admin.user import consts


FIELD = 'notify'

def index(req, user=None, msg=''):
    """
    """
    if not user:
        uid = req.get_argument('uid')

        user = user_app.get_user(uid)
        if user.is_new():
            return 'admin/user/search.html', {'msg': 'user not exists'}

    return 'admin/%s/index.html' % FIELD, {
        'user': user,
        'user_field': consts.USER_FIELDS,
        'field': FIELD,
        'msg': msg,
        'friends': (user_app.get_user(friend_id) for friend_id in user.friend.get_friends()),
    }


def reset(req):
    """修改用户数据
    """
    uid = req.get_argument('uid')

    user = user_app.get_user(uid)
    if user.is_new():
        return 'admin/user/search.html', {'msg': 'user not exists'}

    user[FIELD].reset()

    return index(req, user=user, msg='reset success')


def modify(req):
    """修改用户数据
    """
    uid = req.get_argument('uid')
    msg_id = req.get_argument('msg_id')
    delete = req.get_argument('delete', False)

    user = user_app.get_user(uid)
    if user.is_new():
        return 'admin/user/search.html', {'msg': 'user not exists'}

    user.notify.del_message([msg_id])
    user.save_all()
    msg='modify success'

    return index(req, user=user, msg=msg)

