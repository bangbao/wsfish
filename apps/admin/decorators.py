# coding:utf-8

import os
import datetime

import settings
from apps.public.logger import get_logger
from . import consts


def require_permission(view_func):
    """装饰器，用于判断管理后台的帐号是否有权限访问
    """
    def wrapped_view_func(request, *args, **kwargs):
        path = request.request.path
        need_perm = consts.URL_SETTINGS[path][-1]
        admin = request.current_user

        # 所有不进行登录直接访问后续页面的请求都踢回登录页面
        if not settings.DEBUG and need_perm and admin is None:
            return request.redirect(settings.get_url("/admin/login/"))
        # 视图权限
        # 请求的路径需要在用户自己的视图列表里查找
        if admin and not admin.has_perm_path(path):
            return request.finish(u'没权限')

        result = view_func(request, *args, **kwargs)
        writeLog(request, path , 1)

        return result

    return wrapped_view_func


def writeLog(request, path, flag=0):
    action = log_contrast(request, path)
    uname = request.current_user.username if request.current_user else 'default'
    if action and uname:
        strLog = u'<' + uname + u'>' + action
        if flag == 1:
            strLog = u'success__' + strLog
        elif flag == 2:
            strLog = u'faile__' + strLog
        elif flag == 3:
            strLog = u'Permission denied__' + strLog
        else:
            strLog = '<flag=' + flag + '>' + strLog
        writeFile(strLog)
    else:
        pass


def log_contrast(request, path):
    try:
        if path == '/admin/index/':
            return 'login<' + u'>'
        elif path == '/admin/config/upload/':
            config_name = request.request.arguments.get('config_name')
            return u'修改游戏配置<' + config_name + u'>'
        elif path == '/admin/upload/':
            upload_type = request.request.arguments.get('type')
            return u'upload<' + upload_type + u'>'
        else:
            params = dict(request.request.arguments.iteritems())
            return path + '<' + params.__str__() + '>'
    except:
        params = dict(request.request.arguments.iteritems())
        return path + '<' + params.__str__() + '>'


def writeFile(log):
    now = datetime.datetime.now()
    fdir = os.path.join(settings.LOGS_ROOT, 'admin_logs')
    if not os.path.exists(fdir):
        os.makedirs(fdir)
        os.chmod(fdir, 511)

    fname = datetime.datetime.strftime(now, '%Y%m%d') + '.log'
    fd = os.path.join(fdir, fname)

    logger = get_logger(fd)
    logger.debug(log)

    # 删掉30天前的记录
    dir_list = os.listdir(fdir)
    if len(dir_list) > 30:
        for fname_t in dir_list:
            try:
                fname_t_list = fname_t.split('.')
                if len(fname_t_list) != 2 or fname_t_list[1] != 'log':
                    continue
                fname_date = datetime.datetime.strptime(fname_t_list[0], '%Y%m%d')
            except:
                continue
            if (now - datetime.timedelta(days=30)).date() > fname_date.date():
                os.remove(os.path.join(fdir, fname_t))


