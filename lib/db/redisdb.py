# coding: utf-8

import sys
import time
import redis
import hashlib
import itertools
import cPickle as pickle

import settings
from lib.utils import md5, generate_rank_score
from lib.utils.debug import print_log_maker


REDIS_CLIENT_DICT = {}  # 每个db都有一个pool
REDIS_CONNECTIONPOOL_DICT = {}
REDIS_MAX_CONNECTIONS = 50  # redis池中最大连接数


def make_redis_client_cache_key(redis_config):
    return '_'.join([redis_config['host'], str(redis_config['port']), str(redis_config['db'])])


def make_redis_client(redis_config):
    """
    Args:
        redis_config:
                {'db': 4,
                 'host': '10.6.7.25',
                 'password': 'F8974044A778',
                 'port': 6379,
                 'socket_timeout': 5}
    Returns:
        0    ---
    """
    cache_key = make_redis_client_cache_key(redis_config)
    if cache_key not in REDIS_CONNECTIONPOOL_DICT:
        need_max_connections = settings.NUMPROCS * 2
        if need_max_connections > REDIS_MAX_CONNECTIONS:
            pool = redis.BlockingConnectionPool(max_connections=need_max_connections, **redis_config)
        else:
            pool = redis.BlockingConnectionPool(**redis_config)
        REDIS_CONNECTIONPOOL_DICT[cache_key] = pool
    redis_client = redis.Redis(connection_pool=REDIS_CONNECTIONPOOL_DICT[cache_key])
    return redis_client

# key-value使用的cache库
cache = make_redis_client(settings.DATABASES['redis'])


class ModelTools(object):
    """# ModelTools: 一堆工具"""
    DATABASE_NAME = 'servers'

    @classmethod
    def print_log(cls, *args, **kargs):
        print_log_maker(2)(*args, **kargs)

    @classmethod
    def get_redis_client(cls, key, server_name):
        """# get_redis_client: 获得一个redis客户端
        args:
            key, server_name:    ---    arg
        returns:
            0    ---
        """
        cache_config = settings.DATABASES[cls.DATABASE_NAME]
        if cls.DATABASE_NAME == 'servers':
            cache_config = cache_config[server_name]['cache_list'][0]
        client_key = make_redis_client_cache_key(cache_config)
        client = REDIS_CLIENT_DICT.get(client_key)
        if client is None:
            client = make_redis_client(cache_config)
            REDIS_CLIENT_DICT[client_key] = client
        return client

    @classmethod
    def _key_prefix(cls,):
        return "%s%s||%s" % (settings.KEY_PREFIX, cls.__module__, cls.__name__)

    @classmethod
    def _key_to_uid(cls, _key):
        return _key.repalce(cls._key_prefix() + '||', '')

    def make_key(self, uid=''):
        """# make_key: docstring
        args:
            :    ---    arg
        returns:
            0    ---
        """
        if not uid:
            uid = self.uid
        return self.__class__.make_key_cls(uid)

    @classmethod
    def make_key_cls(cls, uid):
        return cls._key_prefix() + "||%s" % str(uid)

    @classmethod
    def run_data_version_update(cls, _key, o):
        next_dv = o._data_version__ + 1
        data_update_func = getattr(o, 'data_update_func_%d' % next_dv, None)
        while data_update_func and callable(data_update_func):
            data_update_func()
            print '%s.%s complate' % (_key, data_update_func.__name__)
            o._data_version__ = next_dv
            next_dv += 1
            data_update_func = getattr(o, 'data_update_func_%d' % next_dv, None)


class ModelBase(ModelTools):
    """# TestModel: docstring"""
    DATABASE_NAME = 'servers'
    _need_diff = ()  # 开关，判断是否需要对数据进行对比，如果需要，则元组中的元素为需要diff的key的名字
    def __new__(cls, *args, **kwargs):
        """# __new__: docstring
        args:
            cls, *args, **kwargs:    ---    arg
        returns:
            0    ---
        """
        cls._attrs_base = {
            '_data_version__': 0,
        }
        # 不对数据做diff
        # cls._old_data = {}  # attr_key: copy.deepcopy(data)
        # cls._diff = {  # 数据的变化
        #             # attr_key: {
        #             #     'update': {key: data}, # 新加入的和修改的数据
        #             #     'remove': set(keys),   # 删除的key
        # }

        return object.__new__(cls)

    def __init__(self, uid=None):
        if not self._attrs:
            raise ValueError, '_attrs_base must be not empty'
        self._attrs_base.update(self._attrs)
        self.__dict__.update(self._attrs_base)
        self.uid = str(uid)
        self.changed = False  # 显示判断model是否改变了
        self.need_insert = True  # 判断用户是否存在

        super(ModelBase, self).__init__()

    def _client_cache_update(self,):
        """# _client_cache_update: 前端cache更新机制中，数据的处理方法，有些数据是需要特殊处理的
        args:
            :    ---    arg
        returns:
            0    ---
        """
        return self._diff

    @classmethod
    def _all_model_keys(cls,):
        redis = cls.redis[cls.make_key_cls('-_-!!')]
        return redis.keys(cls._key_prefix() + '||*')

    def save(self):
        start_time = time.time()
        redis = self.redis
        _key = self._model_key
        r = {}

        for k in self._attrs_base:
            data = getattr(self, k)
            r[k] = data

        s = pickle.dumps(r, protocol=1)
        if settings.MIN_COMPRESS > 0 and len(s) >= settings.MIN_COMPRESS:
            s = s.encode("zip")

        # 新数据只作插入操作,避免覆盖数据
        if self.need_insert:
            flag = redis.setnx(_key, s)
            if not flag:
                raise Exception('redis setnx error: %s' % _key)
        else:
            redis.set(_key, s)
        self.changed = False  # 显示判断model是否改变了
        self.need_insert = False  # 保存后用户数据标识存在
        # print 'model save: %s--%s' % (_key, time.time()-start_time)

    @classmethod
    def get(cls, uid, server_id='00'):
        start_time = time.time()
        _key = cls.make_key_cls(uid)
        o = cls(uid)
        o.server_id = server_id
        o._model_key = _key
        o.redis = cls.get_redis_client(_key, o.server_id)
        r = o.redis.get(_key) or o.redis.get(_key)
        if not r:
            o.need_insert = True
            return o

        try:
            r = r.decode('zip')
        except:
            # 临时兼容, 以后全部走zip
            if r[0] == '\x01':
                r = r[1:].decode('zip')

        data = pickle.loads(r)
        for k in o._attrs_base:
            _v = o._attrs_base[k]
            v = data.get(k, _v)
            if _v is 0:
                v = int(v)
            setattr(o, k, v)

        cls.run_data_version_update(_key, o)
        # print 'model get: %s--%s' % (_key, time.time()-start_time)
        o.need_insert = False  # 取出数据表示用户是存在用户
        return o

    def pre_init(self):
        """初始化模块数据
        """
        pass

    def pre_use(self):
        """模块使用前自动修改数据
        """
        pass

    def setattr(self, **kwargs):
        """设定属性值
        """
        self.changed = True
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)

    def incr_attr(self, **kwargs):
        """增长属性值
        """
        self.changed = True
        for attr, value in kwargs.iteritems():
            new_value = getattr(self, attr) + value
            setattr(self, attr, new_value)

    def reset(self):
        # 直接删除key
        self.__dict__.update(self._attrs)
        self.redis.delete(self._model_key)
        # self.__dict__.update(self._attrs)
        # self.save()

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


class RedisSTRINGModelBase(ModelTools):
    """REDIS string 结构
    """
    KEY_PREFIX = 'redis_string'

    @classmethod
    def get(cls, uid, server_id='00'):
        return cls(uid, server_id)

    @classmethod
    def make_key(cls, server):
        uid = '%s_%s' % (cls.KEY_PREFIX, server)
        return cls.make_key_cls(uid)

    def __init__(self, uid, server_id, key=None):
        self.uid = uid
        self.server_id = server_id
        self.key = key or self.make_key(server_id)
        self.name = self.key
        self.redis = self.get_redis_client(self.uid, self.server_id)
        self.changed = False

    def get_value(self):
        """ 获取值
        """
        value = self.redis.get(self.key)
        if value is None:
            return 0

        return int(value)

    def incr(self):
        """ 将自身积分增量 值递增1
        """
        self.redis.incr(self.key)

    def incrby(self, value):
        """ 将自身积分增量 值递增n
        Args:
            value: 增量数值
        """
        self.redis.incrby(self.key, value)

    def decr(self, value=1):
        """ 将自身积分值递减n
        Args:
            value: 减量数值
        """
        self.redis.decr(self.key, value)

    def delete(self):
        """清空排行榜
        """
        self.redis.delete(self.key)


class RedisRankModelBase(ModelTools):
    """排名用的基类
    """
    KEY_PREFIX = 'redis_sorted_set'
    score_cast_func = float

    @classmethod
    def get(cls, uid, server_id, key=None):
        return cls(uid, server_id, key)

    @classmethod
    def make_key(cls, server, new=False):
        if new:
            key = '%s_%s' % (cls.KEY_PREFIX, server)
            return cls.make_key_cls(key)
        return '%s%s_%s' % (settings.KEY_PREFIX, cls.KEY_PREFIX, server)

    def __init__(self, uid, server_id, key=None):
        self.uid = uid
        self.server_id = server_id
        self.key = key or self.make_key(server_id)
        self.redis = self.get_redis_client(self.uid, self.server_id)
        self.changed = False

    @property
    def rank(self):
        """实时排名
        """
        return self.get_rank(self.uid)

    @property
    def score(self):
        """实时分数
        """
        return self.get_score(self.uid)

    def get_rank(self, uid):
        rank = self.redis.zrevrank(self.key, uid)
        if rank is None:
            return 0
        rank += 1
        return rank

    def get_score(self, uid):
        score = self.redis.zscore(self.key, uid)
        if score is None:
            return 0
        return self.score_cast_func(score)

    def reset(self):
        """重置个人数据
        """
        self.redis.zrem(self.key, self.uid)

    def delete(self):
        """清空排行榜
        """
        self.redis.delete(self.key)

    def zcard(self):
        """ 获取当前key里所有的人数
        Returns:
            总人数
        """
        return self.redis.zcard(self.key)

    def snapshot_to(self, snapshot_key):
        """ 将redis数据快照到另一个key上
        Args:
           要快照的key
        """
        self.redis.zunionstore(snapshot_key, {self.key: 1}, aggregate=None)

    def incr(self, value, weight=False):
        """ 将自身积分增量
        Args:
           value: 增量数值
        """
        if weight:
            value = generate_rank_score(value)
        self.redis.zincrby(self.key, self.uid, value)

    def zadd(self, value, weight=False):
        """ 更改自身的积分数值
        """
        if weight:
            value = generate_rank_score(value)
        self.redis.zadd(self.key, self.uid, value)

    def zadd_multi(self, data):
        self.redis.zadd(self.key, **data)

    def zrevrange(self, min_rank, max_rank, withscores=False):
        """ 查找从指定名次到指定名次间的所有排名
        Args:
            min_rank: 最小排名
            max_rank: 最大排名
            withscores: 是否返回积分
        Returns:
            符合条件的列表
        """
        return self.redis.zrevrange(self.key, min_rank - 1, max_rank - 1,
                                    withscores=withscores)

    def zrevrangebyscore(self, max_score, min_score, num=None, withscores=False):
        """ 查找从指定分数到指定分数间的所有排名
        Args:
            max_score: 最大分数
            min_score: 最小分数
            num:  数量
            withscores: 是否返回积分
        Returns:
            符合条件的列表
        """
        return self.redis.zrevrangebyscore(self.key, max_score, min_score,
                                           start=0 if num else None,
                                           num=num,
                                           withscores=withscores)

    def pick_out_by_revrange(self, min_rank, max_rank, withscores=False):
        """查找从指定名次到指定名次间的所有排名
        """
        ranks = self.redis.zrevrange(self.key, min_rank - 1, max_rank - 1,
                                     withscores=withscores)
        return itertools.izip(xrange(min_rank, max_rank + 1), ranks)

    def pick_out_by_uid(self, uids, withscores=False):
        """查找从指定uid的分数
        """
        pipe = self.redis.pipeline(transaction=False)

        for uid in uids:
            pipe.zrevrank(self.key, uid)
            pipe.zscore(self.key, uid)

        data = pipe.execute()

        for i, uid in enumerate(uids):
            idx = i * 2
            rank, score = data[idx], data[idx + 1]
            rank = rank + 1 if rank is not None else 0
            score = self.score_cast_func(score) if score is not None else 0
            if withscores:
                yield (uid, rank, score)
            else:
                yield (uid, rank)

    def pick_out(self, ranks, withscores=False):
        """ 挑选排名用户的数据
        会尽量优化查询次数，当排名有连续的情况时，会使用一次命令
        所以当追求性能时，需要传入排序过的列表
        Args:
            ranks: 要挑选的排名列表
            withscores: 是否返回积分
        Returns:
            以排名为key的字典
        """
        all_ranks = []

        prev = ranks.pop(0)
        prev -= 1
        groups = [[prev, prev]]

        for value in ranks:
            rank = value - 1

            if rank - prev == 1:
                groups[-1][1] = rank
            else:
                start, end = groups[-1]
                all_ranks.append(xrange(start + 1, end + 2))
                groups.append([rank, rank])

            prev = rank

        start, end = groups[-1]
        all_ranks.append(xrange(start + 1, end + 2))

        pipe = self.redis.pipeline(transaction=False)
        for min_rank, max_rank in groups:
            pipe.zrevrange(self.key, min_rank, max_rank, withscores)

        data = pipe.execute()

        return dict(itertools.izip(itertools.chain(*all_ranks),
                                   itertools.chain(*data)))

    def nearby_pos(self, ahead, behind, withscores=False):
        """ 查找自身的前后多少名数据
        Args:
           ahead: 向前多少名
           behind: 向后多少名
           withscores: 是否返回积分
        Returns:
           符合条件的id列表
        """
        self_rank = self.rank
        min_rank = max(self_rank - ahead, 0)
        max_rank = self_rank + behind

        return self.redis.zrevrange(self.key, min_rank, max_rank,
                                    withscores=withscores)

    def nearby_score(self, ahead, behind, num=None, withscores=False):
        """ 查找自身的前后多少积分数据
        Args:
           ahead: 向前多少分
           behind: 向后多少分
           num: 数量控制
           withscores: 是否返回积分
        Returns:
           符合条件的id列表
        """
        self_score = self.score
        min_score = max(self_score - ahead, 0)
        max_score = self_score + behind

        return self.redis.zrevrangebyscore(self.key, max_score, min_score,
                                           start=0 if num else None,
                                           num=num,
                                           withscores=withscores)

    def transformation(self, target):
        """把本用户数据copy到另一用户上面
        """
        target.zadd(self.score)

    def all(self, min_rank=1, max_rank=0, withscores=False):
        """ 查找从指定名次到指定名次间的所有排名
        Args:
            server: 指定分服ID
            min_rank: 最小排名
            max_rank: 最大排名, 0表示全部
            withscores: 是否返回积分
        Returns:
            符合条件的列表
        """
        return self.redis.zrevrange(self.key, min_rank - 1, max_rank - 1,
                                    withscores=withscores)


class RedisSetModelBase(ModelTools):
    """REDIS set集合
    """
    KEY_PREFIX = 'redis_set'

    @classmethod
    def get(cls, uid, server_id='00'):
        return cls(uid, server_id)

    def __init__(self, uid, server_id):
        self.uid = uid
        self.server_id = server_id
        self.changed = False
        self.redis = self.get_redis_client(self.uid, self.server_id)

    def make_key(self, patch_id):
        uid = '%s_%s_%s' % (self.KEY_PREFIX, self.server_id, patch_id)
        return self.make_key_cls(uid)

    def sadd(self, patch_id):
        key = self.make_key(patch_id)
        self.redis.sadd(key, self.uid)

    def scard(self, patch_id):
        key = self.make_key(patch_id)
        return self.redis.scard(key)

    def smembers(self, patch_id):
        key = self.make_key(patch_id)
        return self.redis.smembers(key)

    def sismember(self, patch_id):
        key = self.make_key(patch_id)
        return self.redis.sismember(key, self.uid)

    def srandmember(self, patch_id, num):
        key = self.make_key(patch_id)
        return self.redis.srandmember(key, num)

    def srem(self, patch_id):
        key = self.make_key(patch_id)
        self.redis.srem(key, self.uid)

    def reset(self):
        # TODO 不能用keys，在子类复写此方法
        keys = self.redis.keys(self.KEY_PREFIX + '_*')
        pipe = self.redis.pipeline(transaction=False)
        for key in keys:
            pipe.srem(key, self.uid)
        pipe.execute()


class RedisHashModelBase(ModelTools):
    """REDIS hash 结构
    """
    KEY_PREFIX = 'redis_hash'

    @classmethod
    def get(cls, uid, server_id='00'):
        return cls(uid, server_id)

    @classmethod
    def make_key(cls, server):
        uid = '%s_%s' % (cls.KEY_PREFIX, server)
        return cls.make_key_cls(uid)

    def __init__(self, uid, server_id, key=None):
        self.uid = uid
        self.server_id = server_id
        self.key = key or self.make_key(server_id)
        self.name = self.key
        self.redis = self.get_redis_client(self.uid, self.server_id)
        self.changed = False

    def hdel(self, *sub_keys):
        self.redis.hdel(self.name, *sub_keys)

    def hexists(self, sub_key):
        return self.redis.hexists(self.name, sub_key)

    def hget(self, key):
        return self.redis.hget(self.name, key)

    def hgetall(self):
        return self.redis.hgetall(self.name)

    def hincrby(self, key, amount=1):
        self.redis.hincrby(self.name, key, amount)

    def hincrbyfloat(self, key, amount=1.0):
        self.redis.hincrbyfloat(self.name, key, amount)

    def hkeys(self):
        return self.redis.hkeys(self.name)

    def hlen(self):
        return self.redis.hlen(self.name)

    def hset(self, key, value):
        return self.redis.hset(self.name, key, value)

    def hsetnx(self, key, value):
        return self.redis.hsetnx(self.name, key, value)

    def hmset(self, mapping):
        return self.redis.hmset(self.name, mapping)

    def hmget(self, keys, *args):
        return self.redis.hmget(self.name, keys, *args)

    def hvals(self):
        return self.redis.hvals(self.name)

    def delete(self):
        self.redis.delete(self.name)


class RedisListModelBase(ModelTools):
    """REDIS list 结构
    """
    KEY_PREFIX = 'redis_list'

    @classmethod
    def get(cls, uid, server_id='00'):
        return cls(uid, server_id)

    @classmethod
    def make_key(cls, server):
        uid = '%s_%s' % (cls.KEY_PREFIX, server)
        return cls.make_key_cls(uid)

    def __init__(self, uid, server_id, key=None):
        self.uid = uid
        self.server_id = server_id
        self.key = key or self.make_key(server_id)
        self.name = self.key
        self.redis = self.get_redis_client(self.uid, self.server_id)
        self.changed = False


