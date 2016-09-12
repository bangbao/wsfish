# coding: utf-8

import os
import json
import xlrd

import settings
from . import xls_convert
from .models import Config, GameConfig

game_config = GameConfig()


def import_file(filepath, save=True):
    """配置文件导入
    Args:
        filepath: 配置xlsx路径
        save: 是否要保存
    """
    xl = xlrd.open_workbook(filename=filepath)

    config_name_sheet_map = dict((i[4], i[0]) for i in game_config.config_name_list if i[2])

    done_list = []

    for sheet_title in xl.sheet_names():
        config_name = config_name_sheet_map.get(sheet_title)
        if not config_name:
            continue
        sheet = xl.sheet_by_name(sheet_title)

        data = xls_convert.yield_xlrd_to_pyobj(sheet)
        str_config = xls_convert.to_config_string(config_name, data, filepath)
        eval_config = eval(str_config)

        if save:
            old_config = getattr(game_config, config_name, {})
            #print old_config == eval_config
            if old_config != eval_config:
                Config.set(config_name, eval_config)
                done_list.append(sheet_title)
                # 备份配置内容
                if not settings.DEBUG:
                    backup_config(config_name, eval_config)
        else:
            return str_config

    return done_list


def backup_config(config_name, config_value):
    """备份配置内容到json格式文件中
    """
    # 配置备份目录
    CONFIG_PATH = os.path.join(settings.LOGS_ROOT, 'config')
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
        os.chmod(CONFIG_PATH, 511)

    filepath = os.path.join(CONFIG_PATH, '%s.json' % config_name)
    with open(filepath, 'wb') as f:
        json.dump(config_value, f)


def static_import(dirpath, save=True):
    """导入目录下所有配置
    Args:
        dirpath: 目录路径
        save: 是否保存
    """
    error_files = []
    for filename in sorted(os.listdir(dirpath)):
        filepath = os.path.join(dirpath, filename)
        try:
            import_file(filepath, save)
            print 'success: %s' % filename
        except Exception as e:
            error_files.append((filename, e))
            print 'failure: %s, %s' % (filename, e)

    if error_files:
        print 'error_files:'
        for f, e in error_files:
            print '    %s %s' % (f, e)
        print


if __name__ == '__main__':
    dirpath = r'E:\xlsx'
    dirpath = r'/home/bangbao/kaiqigu/nba/trunk/Design/数据表/99.研发配置'
    filepath = os.path.join(dirpath, 'player_rebirth_exp.xlsx')
    #print import_file(filepath, False)
    static_import(dirpath, True)
