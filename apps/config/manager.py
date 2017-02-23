# coding: utf-8

import os
import time
import xlrd
from lib.utils.helper import make_version
from . import consts
from . import convert
from .models import Config, ConfigVersion


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class ConfigManager(Singleton):
    """配置装载对象
    """
    __config_list = consts.CONFIG_LIST
    __configs = sorted([_i[0] for _i in __config_list])
    __clients = dict((_i[0], _i[-1]) for _i in __config_list)
    __hooks = dict((_i[0], _i[2]) for _i in __config_list)

    def __init__(self):
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
        self.reload_version = int(time.time())

        ConfigVersion.set(self.config_versions, self.reload_version)
        cv_obj = ConfigVersion.get()
        self.reload_version = cv_obj.reload_version
        self.api_check_version = cv_obj.api_check_version

    def load_single(self, name):
        """加载单个配置
        """
        obj = Config.get(name)
        value = obj.value

        setattr(self, name, value)
        if name in self.__hooks:
            hook_func = self.__hooks[name]
            try:
                hook_func(self, name, value)
            except Exception as e:
                print 'hook func error: %s, %s, %s' % (name, hook_func, e)

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

    def get_config(self, name):
        """获取一个配置
        """
        return Config.get(name)

    def set_config(self, name, value):
        """设定一个配置
        """
        Config.set(name, value)

    def notify_reload(self, api_check_version=0):
        """通知进程重新加载配置
        """
        ConfigVersion.update_reload_version(api_check_version)

    @classmethod
    def import_file(cls, filepath, save=True):
        """配置文件导入
        Args:
            filepath: 配置xlsx路径
            save: 是否要保存
        """
        xl = xlrd.open_workbook(filename=filepath)

        sheet_config_map = consts.SHEET_CONFIG_MAP
        done_list = []

        for sheet_name in xl.sheet_names():
            config_name = sheet_config_map.get(sheet_name)
            if not config_name:
                continue

            sheet = xl.sheet_by_name(sheet_name)
            data = convert.yield_xlrd_to_pyobj(sheet)
            value = convert.xls_to_config(config_name, data)

            if save:
                cls.set_config(config_name, value)
                done_list.append(sheet_name)
            else:
                return value

        return done_list

    @classmethod
    def import_dir(cls, dirpath, save=True):
        """导入目录下所有配置
        Args:
            dirpath: 目录路径
            save: 是否保存
        """
        error_files = []

        for filename in sorted(os.listdir(dirpath)):
            filepath = os.path.join(dirpath, filename)
            try:
                cls.import_file(filepath, save)
                print('success: %s' % filename)
            except Exception as e:
                error_files.append((filename, e))

        if error_files:
            print('error_files:')
            for f, e in error_files:
                print('\t%s %r' % (f, e))
            print()


if __name__ == '__main__':
    dirpath = r'E:\xlsx'
    config_manager = ConfigManager()
    config_manager.import_dir(dirpath, True)
