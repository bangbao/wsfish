# coding: utf-8

import time
import random


class Fish(object):
    __slots__ = ('fishID', 'lifeTime', 'createTime', 'isShoted', 'routeID')

    def __init__(self, **kwargs):
        for attr, value in kwargs.iteritems():
            if attr in Fish.__slots__:
                setattr(self, attr, value)

        self.createTime = time.time()
        self.isShoted = False
        self.routeID = self.getFishRouteID()

    def toBaseInfoDict(self):
        d = {}
        for key in Fish.__slots__:
            d[key] = getattr(self, key, None)

    def __repr__(self):
        return '<Fish(fishID=%s, curTime=%s, lifeTime=%s>' % (self.fishID,
                                                              self.curTime,
                                                              self.lifeTime)

    def isDead(self):
        if self.isShoted:
            return True
        return self.curTime >= self.lifeTime

    @property
    def curTime(self):
        passTime = time.time() - self.createTime
        if passTime >= self.lifeTime:
            passTime = self.lifeTime
        return passTime

    def setIsShoted(self, shot):
        self.isShoted = shot

    def getFishRouteID(self):
        return random.randint(1, 28)

    def on_request(self):
        pass

    def update(self):
        pass
