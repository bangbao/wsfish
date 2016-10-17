# coding: utf-8

import time
import functools
import traceback


def job_func_decorater(func):
    """包装函数,在函数执行前自动更新配置
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import settings
        from lib.utils.mail import send_sys_mail
        from apps.config import game_config

        now_str = time.strftime('%Y-%m-%d %H:%M:%S')
        # 没开服的不执行任务
        server_id = args[0] if args else None
        if server_id and server_id in game_config.servers:
            if game_config.servers[server_id]['open_time'] > now_str:
                print '--server %s is not opening, do job %s break!' % (server_id, func.__name__)
                return

            if not settings.is_father_server(server_id):
                print '--server %s is not father server, do job %s break!' % (server_id, func.__name__)
                return

        try:
            return func(*args, **kwargs)
        except Exception:
            tb = traceback.format_exc()
            error_msg = ("FUNC_NAME: %s:%s\n\n"
                         "%s") % (func.__name__, server_id, tb)
            subject = ("[%s RUN_TIMER ERROR] - [%s]") % (settings.ENV_NAME, now_str)
            if not settings.DEBUG:
                send_sys_mail(settings.ADMINS, subject, error_msg)
            print error_msg
    return wrapper


def timer_error_mail(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import settings
        from lib.utils.mail import send_sys_mail

        now_str = time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            return func(*args, **kwargs)
        except Exception:
            tb = traceback.format_exc()
            error_msg = ("FUNC_NAME: %s%s\n\n"
                         "%s") % (func.__name__, tuple(args), tb)
            subject = ("[%s RUN_TIMER ERROR] - [%s]") % (settings.ENV_NAME, now_str)
            if not settings.DEBUG:
                send_sys_mail(settings.ADMINS, subject, error_msg)
            print error_msg
    return wrapper


