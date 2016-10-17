# coding: utf-8

import datetime
import cPickle as pickle

import settings
from lib.utils import md5
from lib.db import make_redis_client
from . import consts


class Admin(object):
    """管理员
        permissions值
        0 - 无权限
        4 - 只读权限
        6 - 修改权限
        {
            'admin': 6,
            'change_password': 0,
            'code': 0,
            'config': 4,
            'server': 0,
            'super': 6,
            'test_api': 0,
            'tools': 0,
            'user': 6,
            'user_all': 0
        }
    """
    _client = make_redis_client(settings.DATABASES['master'])    # 获取一个指定的redis客户端
    ADMIN_PREFIX = 'admin_nba_'     # admin 存储hash表

    def __init__(self, username=''):
        self.username = username    # 管理员账号
        self.password = ''          # 管理员密码
        self.email = ''             # 邮件
        self.last_ip = '0.0.0.0'    # 登陆IP地址
        self.last_login = 0         #
        self.permissions = {}       # 管理员可用权限
        self.uid = self.username

    @classmethod
    def get(cls, username):
        obj_str = cls._client.hget(cls.ADMIN_PREFIX, username)
        if obj_str:
            o = cls(username)
            o.__dict__.update(pickle.loads(obj_str))
            return o

    @classmethod
    def all(cls):
        users = cls._client.hgetall(cls.ADMIN_PREFIX)
        for username, obj_str in users.iteritems():
            o = cls(username)
            o.__dict__.update(pickle.loads(obj_str))
            yield o

    def save(self):
        d = self.__dict__
        self._client.hset(self.ADMIN_PREFIX, self.username, pickle.dumps(d))

    def delete(self, username):
        self._client.hdel(self.ADMIN_PREFIX, username)

    def set_password(self, raw_password):
        "设置密码"
        self.password = md5(raw_password)

    def check_password(self, raw_password):
        "检查密码"
        return self.password == md5(raw_password)

    def set_permissions(self, perms):
        self.permissions.update(perms)

    def get_permission(self, perm_tp):
        """
        """
        return self.permissions.get(perm_tp, 0)

    def has_perm_path(self, path):
        """
        """
        if self.permissions.get('super'):
            return True

        perm_tp, perm_value = consts.PERM_URLS[path]
        if perm_tp and perm_value:
            has_value = self.permissions.get(perm_tp)
            return has_value >= perm_value
        return True

    def set_last_login(self, time, ip):
        self.last_login = time
        self.last_ip = ip

