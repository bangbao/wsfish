# coding: utf-8

import os
import sys
import time
import signal
import random
import socket
import logging
import psutil

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.log import access_log
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run at debug mode", type=bool)
define("maxmem", default=0, help="max memory use, overflow kill by self. (0 unlimit)", type=int)
define("env_name", default='local', help="settings file name", type=str)
define("numprocs", default=1, help="Forks multiple sub-processes num", type=int)


options.parse_command_line()
# 设定进程使用的配置文件
import settings
settings.set_env(options.env_name)
from handlers import WSHandler, AdminHandler
from threads import AuthThread, GameThread, UserLogin
from apps.config import game_config


def app_log(handler):
    status = handler.get_status()
    if status < 400:
        log_method = access_log.info
        uri = handler.request.uri
        if uri in ():
            return
    elif status < 500:
        log_method = access_log.warning
    else:
        log_method = access_log.error
    request_time = 1000 * handler.request.request_time()
    log_method('%d %s %.2fms', status, handler._request_summary(), request_time)


class Application(tornado.web.Application):
    def __init__(self, debug=False):
        handlers = [
            (r"/ws/", WSHandler),
            (r"/admin/.*", AdminHandler),
        ]
        super(Application, self).__init__(handlers, debug=debug,
                                          log_function=app_log,
                                          **settings.TORNADO_SETTINGS)

        self.auth_thread = AuthThread()
        self.auth_thread.start()
        self.game_thread = GameThread()
        self.game_thread.start()

    def stop_application(self):
        self.auth_thread.push_thread(None)
        self.auth_thread.join()
        self.game_thread.push_thread(None)
        self.game_thread.join()

    def push_auth_thread(self, handler, message):
        self.auth_thread.push_thread(dict(handler=handler, message=message))

    def push_user_message(self, uid, message):
        self.game_thread.push_thread(dict(uid=uid, message=message))

    def push_user_login(self, uid, is_login):
        self.game_thread.push_thread(UserLogin(uid, is_login))


def main_single():
    # 让打印输出到supervisor_err.log中
    settings.set_debug_print()

    # tornado多进程模式不支持debug模式中的autoreload
    debug = options.debug if options.numprocs == 1 else False
    app = Application(debug)
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    server.start(options.numprocs)
    process = psutil.Process(os.getpid())

    def shutdown():
        server.stop()
        deadline = int(time.time()) + 1
        io_loop = tornado.ioloop.IOLoop.instance()

        def stop_loop():
            now = int(time.time())
            if now < deadline and io_loop._callbacks:
                io_loop.add_timeout(now+1, stop_loop)
                logging.info('stop_loop delayed: pid=%s' % os.getpid())
            else:
                logging.info('stop_loop success: pid=%s' % os.getpid())
                io_loop.stop()
        stop_loop()

    def sig_handler(sig, frame):
        tornado.ioloop.IOLoop.instance().add_callback(shutdown)

    # 监控配置
    tornado.ioloop.PeriodicCallback(game_config.auto_reload,
                                    settings.CONFIG_UPDATE_DELAY_TIME*1000).start()

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)
    logging.info('start_single_loop success: pid=%s' % os.getpid())
    io_loop = tornado.ioloop.IOLoop.instance()
    io_loop.start()


if __name__ == "__main__":
    if options.numprocs == 1:
        print 'start server main_single()'
        main_single()
    else:
        print 'start server main()'
        main()
