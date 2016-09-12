# coding: utf-8

import copy
import time
import random
from apps.fight.gameglobal import GameGlobal
from apps.fight.fish import Fish


class FishTable(object):
    MAX_PLAYERS = 4
    __slots__ = ('players', 'tableIdx', 'startTime', 'fishes')

    def __init__(self, tableIdx):
        self.players = [None] * self.MAX_PLAYERS
        self.tableIdx = tableIdx
        self.startTime = 0
        self.fishes = []

    @property
    def playerNum(self):
        num = 0
        for p in self.players:
            if p:
                num += 1
        return num

    def player_enter(self, player):
        """玩家坐下
        """
        if player in self.players:
            raise Exception('already in table')

        empty_seats = []
        for idx in range(self.MAX_PLAYERS):
            if self.players[idx] is None:
                empty_seats.append(idx)

        if not empty_seats:
            raise Exception('no avaliable seat in table')

        idx = random.choice(empty_seats)
        self.palyers[idx] = player
        self.startTime = self.startTime or time.time()

        player.set_table_seat(self, idx)

        # 发送进入桌子响应给玩家
        seatplayers = [self.dumpTableSeatPlayer(p) for p in self.players if p]
        tablefishes = [fish.toBaseInfoDict() for fish in self.fishes
                       if not fish.isDead()]
        message = dict(tableIdx=self.tableIdx, players=seatplayers,
                       fishes=tablefishes)
        GameGlobal.dispatch_user_message([player.uid], message)
