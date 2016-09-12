# coding: utf-8

import redis
import hashlib

class ConnectPool(dict):
    def __init__(self, redis_config_list):
        self.redis_config_list = redis_config_list
        self.redis_config_list_len = len(self.redis_config_list)

    def __getitem__(self, name):
        sid = int(hashlib.md5(str(name)).hexdigest(), 16) % self.redis_config_list_len
        cache_config = self.redis_config_list[sid]
        cache_config['max_connections'] = 5
        obj = super(ConnectPool, self).get(sid)

        if not obj:
            pool = redis.ConnectionPool(**cache_config)
            obj = redis.Redis(connection_pool=pool)
            super(ConnectPool, self).__setitem__(sid, obj)

        return obj

