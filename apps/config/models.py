# coding: utf-8

import time
import json
import hashlib
from lib.db import ModelBase


def make_version(value):
    """计算配置内容版本号
    """
    datastr = json.dumps(value, sort_keys=True)
    return hashlib.md5(datastr).hexdigest()


class ConfigFile(object):
    """配置文件
    """
    def __init__(self, key=None, value=None, version=None):
        self.key = key
        self.value = value if value is not None else {}
        self.version = version


class Config(ModelBase):
    """Config: 游戏配置的模型
    """
    def __init__(self, uid=None):
        self.uid = uid
        self._attrs = {
            'value': {},
            'version': 0,
        }
        super(Config, self).__init__(self.uid)

    @classmethod
    def set(cls, key, value, version=0):
        obj = cls.get(key)
        obj.value = value
        obj.version = version or int(time.time())
        obj.save()
        ConfigVersion.update_single(key, obj.version)


class ConfigVersion(ModelBase):
    """ConfigVersion: 这货是为了纪录config版本的
    """
    DATABASE_NAME = 'master'

    def __init__(self, uid=None):
        self.uid = 'config_version'
        self._attrs = {
            'versions': {},       # 所有的配置版本们
            'reload_version': 0,  # 自动更新的版本，时间戳
            'api_check_version': 0,     # API接口是否检测配置版本号 1表示检测
        }
        super(ConfigVersion, self).__init__(self.uid)

    @classmethod
    def get(cls, uid='config_version'):
        uid = 'config_version'
        return super(ConfigVersion, cls).get(uid)

    @classmethod
    def update_single(cls, field, version):
        obj = cls.get()
        obj.versions[field] = version
        obj.save()

    @classmethod
    def update_reload_version(cls, api_check_version):
        obj = cls.get()
        obj.reload_version = int(time.time())
        obj.api_check_version = api_check_version
        obj.save()
