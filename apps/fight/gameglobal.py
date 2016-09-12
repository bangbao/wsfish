# coding: utf-8

import time
import tornado.ioloop
from handlers import WSHandler


class GameGlobal(object):
    _mongo = None
    _redis = None
    _config = None

    @staticmethod
    def init():
        GameGlobal._mongo = None
        pass

    @staticmethod
    def dispatch_user_message(uids, message):
        # 发送消息支client
        io_loop = tornado.ioloop.IOLoop.instance()
        io_loop.add_callback(WSHandler.send_message, message, uids)

    @staticmethod
    def dispatch_error(uids, errno, errmsg):
        # 发送错误到client
        message = dict(errno=errno, errmsg=errmsg)
        io_loop = tornado.ioloop.IOLoop.instance()
        io_loop.add_callback(WSHandler.send_message, message, uids)
