# coding: utf-8

import time
import threading
import Queue
import tornado.ioloop
from apps.fight.game import FishFightGame


class UserLogin(object):
    def __init__(self, uid, is_login):
        self.uid = uid
        self.is_login = bool(is_login)


class AuthThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dataQueue = Queue.Queue()
        self.name = 'auth thread'

    def push_thread(self, data):
        self.dataQueue.put(data)

    def do_auth(self, message):
        """auth
        """
        result = None
        errno = 0
        errmsg = ''
        return result, errno, errmsg

    def run(self):
        print '%s: ready to work.' % self.name

        while True:
            try:
                data = self.dataQueue.get(True)
            except Queue.Empty:
                continue
            if data is None:
                print '%s: Got None, break thread' % self.name
                break

            handler, message = data['handler'], data['message']

            auth_result, errno, errmsg = self.do_auth(message)
            io_loop = tornado.ioloop.IOLoop.instance()
            io_loop.add_callback(handler.on_auth_finished,
                                 auth_result, errno, errmsg)


class GameThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dataQueue = Queue.Queue()
        self.name = 'game thread'

    def push_thread(self, data):
        self.dataQueue.put(data)

    def run(self):
        print '%s: ready to work.' % self.name

        fish_game = FishFightGame()
        next_update_time = 0
        while True:
            nowtime = time.time()
            if nowtime >= next_update_time:
                # 状态更新
                next_update_time = fish_game.update() or (nowtime + 1)

            try:
                data = self.dataQueue.get(True, 1)
            except Queue.Empty:
                continue
            if data is None:
                print '%s: Got None, break thread' % self.name
                break

            if isinstance(data, UserLogin):
                fish_game.handle_user_login(data.uid, data.is_login)
                continue

            uid, message = data['handler'], data['message']

            fish_game.handle_user_message(uid, message)
        del fish_game
