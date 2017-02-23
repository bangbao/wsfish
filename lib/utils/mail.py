# coding: utf-8

import os
import time
import socket
import traceback
import urllib

from lib.utils.helper import md5
from collections import defaultdict

#                 正文       title  addrs
SYS_MAIL_CMD = """echo "%s" | mail -s "%s" %s"""

# 缓存服务器端报错信息
CLIENT_EXCEPTION_CACHES = defaultdict(int)
CLIENT_EXCEPTION_TIMES = 2


def send_sys_mail(addr_list, subject, body):
    """# send_sys_mail: 用系统名义给人发邮件
    Args:
        addr_list: 发件人的list
        subject: 邮件标题
        body: 邮件正文
    Returns:
        0
    """
    body = body.replace('"', '')
    addrs = ','.join(addr_list)

    # 编码便于显示中文
    if isinstance(subject, unicode):
        subject = subject.encode('utf-8')
    if isinstance(body, unicode):
        body = body.encode('utf-8')

    cmd = SYS_MAIL_CMD % (body, subject, addrs)
    return os.system(cmd)


class ErrorMail(object):
    """500错误发邮件
    Attributes:
       admins: 要发给的邮件地址
    """
    HTTP_500_ERROR = 'O_O'

    def __init__(self, mail_settings):
        """ 初始化实列
        Args:
            mail_settings: 要发给的邮件设置
        """
        if mail_settings.get('send', False):
            self.to_mails = mail_settings['admins']
            self.title = '[%s SERVER ERROR]' % mail_settings.get('title', '')
            self.debug = mail_settings.get('debug', False)
        else:
            self.to_mails = []
            self.title = ''
            self.debug = True

    @property
    def hostname(self):
        if not getattr(self, '_hostname', None):
            self._hostname = socket.gethostname()
        return self._hostname

    def __call__(self, view_func, *args, **kwargs):
        """ 装饰器方法
          @error_mail((('user', 'user@gmail.com'),))
          def foo(bar):
              pass
        Args:
            func: 要装饰的函数
        Returns:
             装饰器
        """
        def decorator(env, *args):
            """ 对指定的函数进行处理
            """
            try:
                result = view_func(env, *args)
            except:
                # 设定response返回http 500状态码
                env.req.set_status(500)
                env.errno = 1
                request = env.req.request
                error_uid = env.user.uid if env.user else None
                # 取自定义的header
                full_url = request.headers.pop('Real-Full-Url', request.full_url())
                full_url = urllib.unquote(full_url)
                body = request.body if len(request.body) < 5000 else 'BODY LARGER THAN 5Kb'
                tb = traceback.format_exc()
                error_msg = ("HTTP-500-ERROR:  %r\n\n"
                             "UID: %s\n\n"
                             "BODY: %r\n"
                             "%r\n\n"
                             "%s") % (full_url, error_uid, body, request, tb)
                subject = ("%s - [%s] - [%s]: %s") % (self.title, self.hostname, time.strftime('%Y-%m-%d %H:%M:%S'), tb.splitlines()[-1])

                # 发邮件(相同的报错内容一天只发5次)
                content_md5 = md5(tb)
                had_num = CLIENT_EXCEPTION_CACHES[content_md5] + 1
                if self.to_mails and had_num <= CLIENT_EXCEPTION_TIMES:
                    send_sys_mail(self.to_mails, subject, error_msg)
                    CLIENT_EXCEPTION_CACHES[content_md5] += 1

                print error_msg

                debug = env.get_argument('ddd', 0)
                if not debug and '/admin/' not in full_url:
                    error_msg = self.HTTP_500_ERROR

                return error_msg

            return result

        return decorator

error_mail = ErrorMail

