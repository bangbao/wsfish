# coding: utf-8

import os
import sys
import time
import datetime
import itertools
import redis
import cPickle as pickle
from collections import defaultdict
from pprint import pprint as p

_s = time.time()
uid = 'b00aaa001'
static_config = False

argv = sys.argv[1:]
if len(argv) > 1:
    env_name = argv[0]
    s = argv[1]
    if s == 'config':
        static_config = True
    else:
        uid = s or uid
elif len(argv) == 1:
    env_name = argv[0]
else:
    env_name = 'local'


import settings
settings.set_env(env_name)


from apps.config import game_config
from apps.config.models import Config
from apps.user.models import *
from apps.user.proxy import User

try:
    from lib.db import cache
except ImportError:
    print 'import cache error'
    pass

apps_root = os.path.join(settings.BASE_ROOT, 'apps')
for root, dirs, files in os.walk(apps_root):
    for dname in dirs:
        exec_str = "from apps import %s as %s_app" % (dname, dname)
        try:
            exec(exec_str)
        except ImportError:
            pass

path = os.path.join(settings.BASE_ROOT, 'logs', 'upload_xls')
if static_config:
    game_config.static_import(path)
    print '-----static import config: success'

# 注意, 正式环境禁止启动此函数
if settings.DEBUG:
    def debug_sync_change_time():
        from lib.utils import change_time
        from lib.db import cache

        delta_seconds = cache.get('debug_sync_change_time')
        delta_seconds = int(float(delta_seconds)) if delta_seconds else 0
        real_time = int(change_time.REAL_TIME_FUNC())
        sys_time = real_time + delta_seconds
        if abs(sys_time - int(time.time())) > 5:
            change_time.change_time(sys_time)
            print 'debug_change_time: %s -- %s -- %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(real_time)),
                                                         time.strftime('%Y-%m-%d %H:%M:%S'),
                                                         delta_seconds)
    debug_sync_change_time()

now = datetime.datetime.now()
u = user = user_app.get_user(uid, False)


def dump_config(filepath, config_name=None):
    data = {}
    if config_name:
        obj = Config.get(config_name)
        data[config_name] = [obj.version, obj.value]
    else:
        for name, version, value in game_config.all():
            data[name] = [version, value]
            print name, version

    with open(filepath, 'wb') as f:
        pickle.dump(data, f, 1)

def load_config(filepath):
    with open(filepath, 'rb') as f:
        data = pickle.load(f)
        for name, (version, value) in data.iteritems():
            Config.set(name, value, version)
            print name, version


print time.time() - _s
print settings.ENV_NAME
