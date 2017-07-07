# coding: utf-8

import os
import time

import settings
from apps.config import game_config
from apps.config import consts as config_consts
from . import consts


def index(req, config_key=None, msg=''):
    """显示配置相关信息
    """
    field = req.get_argument('field', 'index')
    config_name_list = config_consts.CONFIG_LIST

    config_name_list_new = []
    l_len = len(config_name_list)
    line_n = l_len/5
    i = 0
    while i <= line_n:
        left = i*5
        right = (i+1)*5
        if right < l_len:
            config_name_list_new.append(config_name_list[left:right])
        else:
            config_name_list_new.append(config_name_list[left:])
        i+=1

    config_key = config_key or req.get_argument('config_key', config_name_list[0][0])
    config_cn = config_key

    return 'admin/config/index.html', {
        'config_name_list': config_name_list_new,
        'config_key': config_key,
        'config_cn': config_cn,
        'config_data': getattr(game_config, config_key, {}),
        'config_versions': game_config.config_versions,
        'config_update_ats': game_config.client_config_versions,
        'msg': msg,
        'user_field': consts.USER_FIELDS,
        'field': field,
    }


def get_all_config(req):
    """下载所有配置
    """
    from test.get_all_configs import get_all_config

    file_name = get_all_config()
    file_obj = open(file_name, 'r')

    req.write(file_obj.read())
    req.set_header('Content-Type','application/txt')
    req.set_header('Content-Disposition','attachment;filename=local_config.py')

    return None, {}


def upload(req):
    """上传配置文件
    """
    file_obj = req.request.files.get('xls', None)

    if not file_obj:
        return 'admin/config/notice.html', {'msg': 'error file !!!'}

    upload_xls = os.path.join(settings.LOGS_ROOT, 'upload_xls')
    if not os.path.exists(upload_xls):
        os.makedirs(upload_xls)
        os.chmod(upload_xls, 511)

    file_name = os.path.join(upload_xls, file_obj[0]['filename'])

    filebody = file_obj[0]['body']
    hfile = open(file_name, 'wb+')
    hfile.write(filebody)
    hfile.close()

    done_list = game_config.import_file(file_name)
    msg = 'done: %s' % ', '.join(done_list)
    config_key = done_list[0].lower() if done_list else ''

    return index(req, config_key=config_key, msg=msg)


def notify_reload(req):
    """自动加载配置
    """
    api_check_version = int(req.get_argument('api_check_version', '0'))

    game_config.notify_reload(api_check_version)
    msg = u'%s秒内配置会自动加载' % settings.CONFIG_UPDATE_DELAY_TIME

    return index(req, msg=msg)


def check(req):
    """配置校验
    """
    from script import rectify_config
    content = rectify_config.main()

    field = req.get_argument('field', 'check')
    msg = 'check end'

    return 'admin/config/check.html', {
        'msg': msg,
        'content': content,
        'user_field': consts.USER_FIELDS,
        'field': field,
    }


def lua_client_version(req):
    """把前端配置文件版本转成lua供前端下载
    """
    from apps.public.py2lua import PY2LUA

    new_client_versions = {}
    for name, _version in game_config.client_config_versions.iteritems():
        new_client_versions[name] = str(_version)

    py2lua = PY2LUA()
    result = py2lua.encode(new_client_versions)

    filename = '%s_client_version.lua' % settings.ENV_NAME
    req.write(result.encode('utf-8'))
    req.set_header('Content-Type','application/txt')
    req.set_header('Content-Disposition','attachment;filename=%s' % filename)

    return None, {}


