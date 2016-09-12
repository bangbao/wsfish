# coding: utf-8

import time
import tornado.ioloop
from apps.fight.table import FishTables
from apps.fight.player import FishPlayer
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


class FishFightGame(object):
    def __init__(self):
        GameGlobal.init()
        self.players = {}
        self.tables = FishTables()

    def __del__(self):
        print 'fishfightgame del'

    def update(self):
        # 桌子更新
        self.tables.update()

        # 玩家更新
        for p in self.players.itervalues():
            p.update()
        return time.time() + 1

    def handle_user_login(self, uid, is_login):
        """处理玩家上下线
        """
        if is_login:
            if uid in self.players:
                print 'duplicated player uid=%s' % uid
                return
            p = FishPlayer.load_by_uid(uid)
            if not p:
                print 'fail to load player uid=%s' % uid
                return
            self.players[uid] = p
            print 'add player(uid=%s), num=%s' % (p.uid, len(self.players))
            message = {'aadsfsadfsad'}
            GameGlobal.dispatch_user_message([uid], message)
        else:
            if uid not in self.players:
                return
            p = self.players.pop(uid)
            print 'remove player(uid=%s), num=%s' % (p.uid, len(self.players))
            self.tables.on_player_offline(p)

    def handle_user_message(self, uid, message):
        """处理玩家具体消息
        """
        if uid not in self.players:
            print 'recv message from unlogin player(uid=%s)' % uid
            return

        # 取出消息和player实例
        p = self.players[uid]
        # 让桌子处理消息
        self.tables.on_player_request(p, message)
        # 让玩家处理消息
        p.on_request(message)

    def handle_gm_commond(self, commond):
        # 系统管理指令， 由外部管理接口传入
        pass

            return