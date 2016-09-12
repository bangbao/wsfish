# coding: utf-8

import time

import settings
from lib.db import ModelBase
from lib.utils import make_version
from . import consts


class Config(ModelBase):
    """Config: 游戏配置的模型
    """
    DATABASE_NAME = 'master'

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
            #'cfg_ver': '',       # 客户端配置总版本号
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


class GameConfig(object):
    """游戏配置装载对象
    """
    config_name_list = consts.config_name_list
    __configs = sorted([_i[0] for _i in config_name_list])
    __hooks = dict((_i[0], _i[1]) for _i in config_name_list)
    __clients = dict((_i[0], _i[-1]) for _i in config_name_list)

    def __init__(self):
        """
        """
        self.config_versions = {}           # 全部的配置号记录
        self.client_config_versions = {}    # 前端使用的配置号记录
        self.cfg_ver = ''                   # 前端使用的配置号记录的md5值
        self.reload_version = 0             # 自动加载时的时间戳
        self.api_check_version = 0          # API接口是否检测配置版本号cfg_ver(1校验，0不校验)
        # self.load_all()

    def all(self):
        for name in self.__configs:
            obj = getattr(self, name)
            yield name, self.config_versions[name], obj

    def load_all(self):
        """从数据库加载所有配置
        """
        for name in self.__configs:
            self.load_single(name)
        self.cfg_ver = make_version(self.client_config_versions)

        cv_obj = ConfigVersion.get()
        self.reload_version = cv_obj.reload_version
        self.api_check_version = cv_obj.api_check_version

    def load_single(self, name):
        """加载单个配置
        """
        obj = Config.get(name)

        value = obj.value
        if isinstance(value, basestring):
            value = eval(value)

        setattr(self, name, value)
        for hook_func in self.__hooks[name]:
            try:
                hook_func(self, name, value)
            except Exception as e:
                print 'hook func error: %s, %s, %s' % (name, hook_func, e)
                pass

        self.config_versions[name] = obj.version
        if self.__clients[name]:
            self.client_config_versions[name] = obj.version

    def auto_reload(self):
        """自动加载更新的配置
        """
        flag = False
        cv_obj = ConfigVersion.get()
        if cv_obj.reload_version and cv_obj.reload_version != self.reload_version:
            new_versions = cv_obj.versions
            old_versions = dict(self.config_versions)
            for name in self.__configs:
                version = old_versions.get(name, 0)
                new_version = new_versions.get(name, 0)
                if version != new_version:
                    flag = True
                    self.load_single(name)
                    print 'config_auto_reload: %s %s=>%s' % (name, version, new_version)
            self.cfg_ver = make_version(self.client_config_versions)
            self.reload_version = cv_obj.reload_version
            self.api_check_version = cv_obj.api_check_version
        return flag

    def get_raw_config(self, name):
        """获取数据库中的配置内容
        """
        obj = Config.get(name)

        value = obj.value
        if isinstance(value, basestring):
            value = eval(value)
        return value

    def set_config(self, key, value):
        """设定一个配置
        """
        Config.set(key, value)

    def notify_reload(self, api_check_version=0):
        """通知进程重新加载配置
        """
        ConfigVersion.update_reload_version(api_check_version)

    def get_monster_detail(self, monster_id):
        """根据id取不同配置
        """
        if 10000 <= monster_id <= 19999:
            return self.monster_op[monster_id]

        if 100000 <= monster_id <= 199999:
            return self.monster_robpatch[monster_id]

        if 200000 <= monster_id <= 209999:
            return self.monster_arena[monster_id]

        if 210000 <= monster_id <= 219999:
            return self.monster_system[monster_id]

        if 300000 <= monster_id <= 399999:
            return self.monster_vs[monster_id]

        if 1000000 <= monster_id <= 10999999:
            return self.monster_main[monster_id]

        if 11000000 <= monster_id <= 20999999:
            return self.monster_main11[monster_id]

        if 21000000 <= monster_id <= 30999999:
            return self.monster_main21[monster_id]

        if 31000000 <= monster_id <= 40999999:
            return self.monster_main31[monster_id]

        if 200000000 <= monster_id <= 299999999:
            return self.monster_legend[monster_id]

        if 300000000 <= monster_id <= 399999999:
            return self.monster_1v1[monster_id]

        if 500000000 <= monster_id <= 599999999:
            return self.monster_dynasty[monster_id]

        if 10020000000 <= monster_id <= 10029999999:
            return self.monster_money[monster_id]

    def has_monster_detail(self, monster_id):
        """是否在monster配置中
        """
        try:
            return bool(self.get_monster_detail(monster_id))
        except KeyError:
            return False

    def yield_open_servers(self):
        """返回已经开启的分服数据
        """
        now_str = time.strftime('%Y-%m-%d %H:%M:%S')
        for server_id, server_data in self.servers.iteritems():
            if server_data['open_time'] <= now_str:
                yield server_id, server_data


