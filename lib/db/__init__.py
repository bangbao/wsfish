# coding: utf-8

import settings
from .mongodb import ModelBase
from .redisdb import make_redis_client


# key-value使用的cache库
cache = make_redis_client(settings.DATABASES['redis'])
