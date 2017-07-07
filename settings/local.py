# coding: utf-8

DEBUG = True
DEBUG_PRINT = True       # 是否打印接口返回数据
STATS_SWITCH = False      # 是否写动作日志
API_CONFIG_DEBUG = False  # 接口请求时跳过配置更新的校验
SKIP_GUIDE = False        # 是否跳过新手引导
IS_INREVIEW = False       # 是否是审核环境
MAIL_SENDING = False      # 是否发送报错邮件
SEND_LOG_TO_CMGE = False  # 是否发送日志给cmge
SEND_LOG_TO_REYUN = False   # 是否发送日志给reyun

URL_PREFIX = ''

MYSQL_DEFAULT = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': '390dc437551c62', 'db': 'basketball'}
REDIS_DEFAULT = {'host': 'localhost', 'port': 6379, 'db': 0, 'socket_timeout': 5}
HOST_LIST = [
    # sid, server_host, web_local_port, redis_ip, redis_port, redis_db
    ('00', '127.0.0.1:8888', (2500, 2507), 'localhost', 6379, 0, URL_PREFIX),
    ('01', '127.0.0.1:8888', (2500, 2507), 'localhost', 6379, 0, URL_PREFIX),
    ('02', '127.0.0.1:8888', (2500, 2507), 'localhost', 6379, 2, URL_PREFIX),
    ('03', '127.0.0.1:8888', (2500, 2507), 'localhost', 6379, 3, URL_PREFIX),
    ('04', '127.0.0.1:8888', (2500, 2507), 'localhost', 6379, 4, URL_PREFIX),
    ('05', '127.0.0.1:8888', (2500, 2507), 'localhost', 6379, 5, URL_PREFIX),
]
# 聊天系统
CHAT_SERVERS = {
    'host': '127.0.0.1',
    'port': 9990,
    'chat_host': '127.0.0.1',
}
SERVERS = {}
for sid, host, _, redis_ip, redis_port, redis_db, url_prefix in HOST_LIST:
    fmt = 'http://%s/%s' if url_prefix else 'http://%s%s'
    SERVERS[sid] = {'server_url': fmt % (host, url_prefix),
                    'chat_host': CHAT_SERVERS['chat_host'],
                    'chat_port': CHAT_SERVERS['port'],
                    'cache_list': [dict(REDIS_DEFAULT, host=redis_ip, port=redis_port, db=redis_db)]}

DATABASES = {
    'master'          : dict(REDIS_DEFAULT, db=0),    # TOKEN与UID的转换
    'goods_code'      : dict(REDIS_DEFAULT, db=1),    # 兑换码
    'chat'            : dict(REDIS_DEFAULT, db=2),    # 聊天系统的私聊内容
    'redis'           : dict(REDIS_DEFAULT, db=3),    # t各种排名
    'templog'         : dict(REDIS_DEFAULT, db=15),   # 临时日志数据
    'payment'         : dict(MYSQL_DEFAULT, table_prefix='payment'),    # 支付数据
    'subrecord'       : dict(MYSQL_DEFAULT, table_prefix='subrecord'),    # 消费数据
    'subrecord_money' : dict(MYSQL_DEFAULT, table_prefix='subrecord_money'),    # money消费数据
    'servers'         : SERVERS,                      # 用户游戏分服数据
    'mongo'           : dict(host='127.0.0.1', port=27017, db='wsweb'),
}
