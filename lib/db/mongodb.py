# coding: utf-8

import copy
from pymongo import MongoClient

import settings


mongo_client = None


def get_mongo_client():
    global mongo_client
    if mongo_client is None:
        host = settings.DATABASES['mongo']['host']
        port = settings.DATABASES['mongo']['port']
        mongo_client = MongoClient(host, port)
    return mongo_client


class ModelBase(object):
    _mongo_client = get_mongo_client()
    _db = _mongo_client[settings.DATABASES['mongo']['db']]

    COLLECTION_NAME = None

    def __new__(cls, *args, **kwargs):
        cls._attrs_base = {
            '_data_version': 0,
        }
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, uid=None):
        if not self._attrs:
            raise ValueError('_attrs must be not empty')
        self._attrs_base.update(self._attrs)
        self.__dict__.update(self._attrs_base)
        self.uid = uid
        self.changed = True
        self.need_insert = True

    @classmethod
    def get(cls, uid, server_id='00'):
        o = cls(uid)
        o.server_id = server_id
        o._coll = cls._db[cls.COLLECTION_NAME or cls.__name__.lower()]

        data = o._coll.find_one({'_id': uid})

        if not data:
            o.need_insert = True
            return o

        for k, _v in o._attrs_base.iteritems():
            v = data.get(k, _v)
            setattr(o, k, v)
        o._old_data = copy.deepcopy(data)
        o.need_insert = False
        return o

    def save(self):
        if self.need_insert:
            r = {'_id': self.uid}
            for k in self._attrs_base:
                r[k] = getattr(self, k)
            self._coll.insert_one(r)
        else:
            r = {'$inc': {}, '$set': {}}
            for k, _v in self._attrs_base.iteritems():
                v = getattr(self, k)

                if isinstance(_v, (int, float)):
                    old_v = self._old_data.get(k, 0)
                    r['$inc'][k] = v - old_v
                else:
                    old_v = self._old_data.get(k)
                    if v != old_v:
                        r['$set'][k] = v
            self._coll.update_one({'_id': self.uid}, r)

    def pre_init(self):
        pass

    def pre_use(self):
        pass

    def inc_attr(self, **kwargs):
        self.changed = True
        for attr, value in kwargs.iteritems():
            new_value = getattr(self, attr) + value
            setattr(self, attr, new_value)

    def set_attr(self, **kwargs):
        self.changed = True
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)

    def reset(self):
        # 直接删除key
        self.__dict__.update(self._attrs)
        self._coll.delete({'_id': self.uid})

    def dumps(self):
        """dump数据
        """
        data = {}
        for k in self._attrs_base:
            data[k] = getattr(self, k)
        return data

    def loads(self, data, exclude=None):
        """load数据
        """
        self.changed = True
        exclude = exclude or set()
        for k in self._attrs_base:
            if k in data and k not in exclude:
                setattr(self, k, data[k])


    def __repr__(self):
        return '<%s(%s)>' % (self.__class__.__name__, self.uid)