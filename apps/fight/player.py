# coding: utf-8


class BasePlayer(object):
    __slots__ = ('uid', 'username', 'nickname', 'accountType', 'chipCount')

    def __init__(self, **kwargs):
        for key in BasePlayer.__slots__:
            setattr(self, key, kwargs[key])

        self.uid = int(self.uid)
        self.chipCount = int(self.chipCount)
        self.accountType = int(self.accountType)

    def toBaseInfoDcit(self):
        d = {}
        for key in BasePlayer.__slots__:
            d[key] = getattr(self, key)
        return d


class Player(BasePlayer):
    __slots__ = ('fishTable', 'seatIdx', 'gunLevel')

    def __init__(self, **kwargs):
        BasePlayer.__init__(self, **kwargs)

        self.fishTable = None
        self.seatIdx = 0
        self.gunLevel = 100

    def __repr__(self):
        return '<Player(uid=%s>' % self.uid

    def set_table_seat(self, table, seatIdx):
        self.fishTable = table
        self.seatIdx = seatIdx

    def on_request(self, request):
        pass

    def update(self):
        pass

    @classmethod
    def load_by_username(cls, username, password):
        return cls()
        raise Exception('username or password error')

    @classmethod
    def load_by_uid(cls, uid):
        pass

    @classmethod
    def load_by_token(cls, token):
        pass
