# coding: utf-8

import os
import sys
import logging
from functools import wraps
import socket
import time
import datetime
from mail import send_sys_mail


def print_log_maker(frame_num):
    def print_log_embryo(*args):
        """# print: 将s打印至log_stdout
        """
        f = sys._getframe(frame_num)
        rv = (os.path.normcase(f.f_code.co_filename), f.f_code.co_name, f.f_lineno)
        logging.critical('='*10+'  LOG '+str(datetime.datetime.now())+' %f START  '%time.time()+'='*11)
        logging.critical('='*8+'  AT %s: %s: %d: '%rv+'='*8)
        l = [str(i) for i in args]
        logging.critical('|| '+', '.join(l))
        logging.critical('='*35+'  LOG END  '+'='*35+'\n\n')
    return print_log_embryo

print_log = print_log_maker(1)

def track_upon(n=5):
    """# track_upon: docstring
    args:
        n=3:    ---    arg
    returns:
        0    ---    
    """
    for i in xrange(2, n):
        print_log_maker(i)(i)
        

def trackback(msg='', exc_info=None):
    logging.critical(msg, exc_info=sys.exc_info())


def error_mail(addr_list):
    """ log exception decorator for a view,
    """
    def _decorator(self, *args, **kwargs):
        try:
            result = view_func(self, *args, **kwargs)
        except:
            import traceback, resource
            tb = traceback.format_exc()
            # get the view name from request
            form = ''
            if len(self.request.arguments) > 0:
                form_list = []
                for k, v in self.request.arguments.iteritems():
                    form_list.append('%s="%s"' % (k, v))
                form = '\n'+'\n'.join(form_list)
            log_dict = [
                ('date', datetime.datetime.utcnow()),
                ('hostname', socket.gethostname()),
                ('pid', int(os.getpid())),
                ('rss', int(resource.getrusage(resource.RUSAGE_SELF)[2])),
                ('', '\n\n'),
                ('url', self.request.full_url()),
                ('method', self.request.method),
                ('remote', self.request.remote_ip),
                ('form',  form),
                ('', '\n\n'),
                ('class_method', "%s.%s" % (self.__class__.__module__, self.__class__.__name__)),
                ('tb', tb),
            ]

            l = []
            for k, v in log_dict:
                l.append('%s: "%s"'%(k, v))
            s = '\n'.join(l)
            print_log(s)
            subject = '[ERROR MAIL] '+socket.gethostname()+': '+tb.splitlines()[-1]
            rc = send_sys_mail(addr_list, subject, s)
            print_log('error_mail rc: '+str(rc))
            raise
        return result
    return wraps(view_func)(_decorator)
