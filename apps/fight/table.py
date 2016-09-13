# coding: utf-8

import copy
import time
import random
from apps.fight.gameglobal import GameGlobal
from apps.fight.fish import Fish


class Table(object):
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

    def player_leave(self, player, doresponse=False):
        """玩家离开
        """
        if player not in self.players:
            raise Exception('not sit down in table')

        if player.fishTable is not self:
            raise Exception('leave wrong table')

        if self.players[player.seatIdx] != player:
            raise Exception('invalid seat when leaving')

        self.players[player.seatIdx] = None
        player.set_table_seat(None, 0)

        if doresponse:
            GameGlobal.dispatch_error([player.uid], 0, 'errmsg')

        message = {'player leave table'}
        self.broadcast_request(message)

    def on_player_request(self, player, request):
        if player not in self.players:
            return
        if request.shotFish.val is not None:
            d = copy.copy(request.val)
            d['shotFish']['uid'] = player.uid
            self.broadcast_request(d, player.uid)

    def broadcast_request(self, message, excludeUID=-1):
        uids = [p.uid for p in self.players if p and p.uid != excludeUID]
        if not uids:
            return
        GameGlobal.dispatch_user_message(uids, message)
        for p in self.players:
            if p and p.uid != excludeUID:
                uids.append(p.uid)

    def update(self):
        # 更新状态
        if not self.playerNum:
            return

        for fish in list(self.fishes):
            if fish.isDead():
                self.fishes.remove(fish)

        fishConfig = GameGlobal._config
        delta = time.time() - self.startTime
        if delta < 1:
            print 'time is too short'
            return

        new_fishes = []
        for fid, fconf in fishConfig.iteritems():
            if not delta % fconf['bornRate']:
                for _ in xrange(fconf['bornCount']):
                    new_fish = Fish(fishID=fid, leifTime=fconf['lifeTime'])
                    self.fishes.append(new_fish)
                    new_fishes.append(new_fish.toBaseInfoDict())

        if new_fishes:
            message = {'fish born : %s' % new_fishes}
            self.broadcast_request(message)

    def dumpTableSeatPlayer(self, player):
        return dict(setIdx=player.seatIdx, gunLevel=player.gunLevel,
                    baseInfo=player.toBaseInfoDict())

    def getTableStatus(self):
        players = [self.dumpTableSeatPlayer(player)
                   for player in self.players if player]
        fishes = [fish.toBaseInfoDict()
                  for fish in self.fishes if not fish.isDead()]
        return {
            'tableIdx': self.tableIdx,
            'players': players,
            'fishes': fishes,
        }


class Tables(object):
    TABLE_NUM = 100

    def __init__(self):
        self.tables = [Table(idx) for idx in xrange(self.TABLE_NUM)]

    def dumpTablesSummary(self):
        return dict(tableNum=Tables.TABLE_NUM,
                    maxPLayerNumPerTable=Table.MAX_PLAYERS,
                    tablePlayerNums=[t.playerNum for t in self.tables])

    def on_player_request(self, player, request):
        if request.getTableSummary.val is not None:
            message = {'tableSummaryResponse': self.dumpTablesSummary()}
            GameGlobal.dispatch_user_message([player.uid], message)
        elif request.joinTable.val is not None:
            jointableidx = int(request.joinTable.tableIdx.val)
            if not 0 <= jointableidx < len(self.tables):
                raise Exception('invalid table idx: %s' % jointableidx)

            # 先从原来的桌子上推出来
            if player.fishTable is not None:
                player.fishTable.player_leave(player)
            targetTable = self.tables[jointableidx]
            targetTable.player_enter(player)

            if player.fishTable is not None:
                player.fishTable.on_player_request(player, request)

    def on_player_offline(self, player):
        # 下线， 将其从桌子上清除
        if player.fishTable is not None:
            player.fishTable.player_leave(player)

    def update(self):
        # 更新
        for t in self.tables:
            t.update()
