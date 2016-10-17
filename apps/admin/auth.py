#i coding: utf-8

import time
import urllib
import hashlib
import datetime

import settings
from apps.admin.models import Admin
import consts

COOKIE_AUTH_KEY = 'kqgadmin'


def build_signature(*args):
    """生成auth签名"""
    sign_str = '&'.join(str(k) for k in args)

    return hashlib.md5(sign_str).hexdigest()


def login(request, admin):
    """管理员登陆"""
    login_time = int(time.time())
    login_ip = request.request.remote_ip
    admin.set_last_login(login_time, login_ip)
    admin.save()

    sign = build_signature(admin.username, admin.last_login, admin.last_ip)
    cookie_value = "%s|%s" % (admin.username, sign)

    # cookie有效期为1天
    request.set_secure_cookie(COOKIE_AUTH_KEY, cookie_value, expires_days=1)


def logout(request):
    request.clear_cookie(COOKIE_AUTH_KEY)


def get_admin_by_request(request):
    """通过request获取admin"""
    cookie_value = request.get_secure_cookie(COOKIE_AUTH_KEY)
    if cookie_value is None:
        return None

    mid, sign = cookie_value.split('|')
    admin = Admin.get(mid)
    if not admin:
        return None

    new_sign = build_signature(mid, admin.last_login, admin.last_ip)
    if sign != new_sign:
        return None

    return admin


def create_admin(username, password='admin', perms={'super': 1}):
    """创建后台管理员
    """
    admin = Admin(username)
    admin.set_password(password)
    admin.set_permissions(perms)
    admin.save()


def create_default_admin(force=False):
    """默认创建后台管理员
    """
    default = getattr(settings, 'DEFAULT_ADMIN_MANAGER', [])
    for account, password in default:
        if force or not Admin.get(account):
            create_admin(account, password)

create_default_admin()


