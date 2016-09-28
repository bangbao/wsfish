# coding: utf-8

import os

DEBUG = False
DEBUG_PRINT = False       # 是否打印接口返回数据
MAIL_SENDING = False      # 是否发送报错邮件
STATS_SWITCH = False      # 是否写动作日志
API_CONFIG_DEBUG = False  # 接口请求时跳过配置更新的校验
SKIP_GUIDE = False        # 是否跳过新手引导
IS_INREVIEW = False       # 是否是审核环境
SEND_LOG_TO_CMGE = False  # 是否发送日志给cmge
SEND_LOG_TO_REYUN = False # 是否发送日志给reyun
AD_CLICK_CALLBACK = False  # 是否需要广告回调

ADMINS = (
    'basketball_error@126.com',
)
# 客户端报错邮件接收人
CLIENT_DEVELOP = (
    'basketball_client@126.com',
)
DEFAULT_ADMIN_MANAGER = (
    ('yanwei.zhang', '1qwe32'),
    ('niuchanrong', '123465'),
    ('wangminying', '123465'),
    ('shuoquan.man', '123465'),
    ('shuai.zhang', '123465'),
    ('an.qin', '123465'),
    ('yiwei.zhang', '805500'),
    ('haoran.di', '805500'),
    ('chenguang.li', '805500'),
    ('fuhaiyang', '123465'),
)

URL_PREFIX = 'nba'
UID_PREFIX = 'b'
KEY_PREFIX = ''    # 数据库key生成时的前缀
ENV_NAME = None
DATABASES = None
# 进程数
NUMPROCS = 1
# 数据压缩阀值
MIN_COMPRESS = 50
# tornado handler 所开最大线程数
THREAD_POOL_EXECUTOR_MAX_WORKERS = 2
# 配置更新的延迟时间 (单位：秒)
CONFIG_UPDATE_DELAY_TIME = 10
SERVERS = {}
# xxtea加密解密key, 与前端同步
XXTEA_SIGNATURE_KEY = 'kqgmzzynzdyhcl'
# 上传版本数据时需要校验签名用的key
RESOURCE_SIGNATURE_KEY = 'kvksdfjasdDFDSJLKErrwef'
RESOURCE_DOWNLOAD_URL = 'http://dev.kaiqigu.net/nba/static'
CLIENT_CONFIG_NO_UPDATE = set([])
SERVER_TAG_DELTA = 0
# 发送邮件功能设置
MAIL_SETTINGS = {
    'send': MAIL_SENDING,
    'title': ENV_NAME,
    'admins': ADMINS,
    'debug': DEBUG,
}
# 推送设置
PUSH_NOTIFICATION = {}
# 热云统计平台appkey
STATS_REYUN_APPKEY = '3a2d6061147c69b7e766dba0de0ba45d'
# 所有接入的平台
ALL_PLATFORMS = ('zhengyueapp', 'appstore', 'android',
                 'pp', 'haima', 'zhengyue', '91', 'tongbu', 'kuaiyong',
                 'itools', 'xyzs', 'i4', 'zhengyueandroid', '360', 'baidu',
                 'uc', 'xiaomi', 'wandoujia', 'oppo', 'vivo', '37wan', 'lenovo',
                 'huawei', 'coolpad', 'jinli', '4399', 'pps', 'youku', 'anzhi',
                 'appchina', 'ewan', 'muzhiwan', 'downjoy', 'wanpu', 'zhangyue',
                 'ouwan', 'sougou', 'jinshan', 'hupu', 'cmge', 'xx', 'iiapple',
                 'zhuoyue', 'zhuoyueandroid')
# 平台支付回调地址们
PAYMENT_NOTIFY_URLS = {
    'haima': 'http://123.59.32.16/basketballiosbreak/pay-callback-haima/',
}
# 平台下定单的地址
PAYMENT_ORDER_URLS = {
    'vivo': 'http://123.59.32.17/basketballandroid/pay/?method=payment.get_vivo_order&',
    'jinli': 'http://123.59.32.17/basketballandroid/pay/?method=payment.get_jinli_order&',
}
# 已方charge表商品编号对应一些平台商品编号的映射
PAYMENT_WARESID_MAP = {
    'lenovo': {1: 2067, 2: 2068, 3: 2069, 4: 2071, 5: 2090, 6: 2070, 7: 2072,
               8: 2073, 9: 2074, 10: 2075, 11: 2076, 12: 2077, 13: 2078},
    'haima': {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
              8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13},
    'appchina': {1: 2, 2: 1, 3: 10, 4: 9, 5: 8, 6: 7, 7: 6,
                 8: 5, 9: 4, 10: 11, 11: 12, 12: 13, 13: 3},
    'coolpad': {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13},
}

PROJECT_NAME = 'wsapp'
BASE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOGS_ROOT = os.path.join(BASE_ROOT, 'logs')
TEMPLATE_ROOT = os.path.join(BASE_ROOT, 'templates')
STATIC_ROOT = os.path.join(BASE_ROOT, 'static')
SCRIPT_ROOT = os.path.join(BASE_ROOT, 'script')
# 自动创建日志目录
if not os.path.exists(LOGS_ROOT):
    os.makedirs(LOGS_ROOT)
    os.chmod(LOGS_ROOT, 511)

CMGE_LOG_ROOT = os.path.join(LOGS_ROOT, 'cmge_log')
# 默认加载本地的settings配置
execfile(os.path.join(BASE_ROOT, 'settings', 'local.py'), globals(), locals())

TORNADO_SETTINGS = {
    #'debug': DEBUG,
    'template_path': TEMPLATE_ROOT,
    'static_path': STATIC_ROOT,
    #'ui_modules': {},
    #'ui_methods': {},
    #'static_url_prefix': '/static/',
    #'static_handler_class': StaticFileHandler,
    #'static_handler_args': {},
    #'log_function': lambda handler: None,
    'cookie_secret': 'cookie_secret',
    #'template_loader': template.Loader,
    #'autoescape': True,
    #'login_url': '/login/',
    #'xsrf_cookies': True,
    'gzip': True,
}


def get_url(url, fmt=None):
    """获取完整路径
    """
    if fmt:
        return fmt % (URL_PREFIX, url)
    if URL_PREFIX:
        return '/%s%s' % (URL_PREFIX, url)
    return url


def get_mysqldb_cfg(table_prefix, serverid=''):
    """获取mysql配置
    """
    return DATABASES[table_prefix]


def set_env(env_name, numprocs=16):
    """设定当前使用的配置文件
    """
    execfile(os.path.join(BASE_ROOT, 'settings', '%s.py' % env_name),
             globals(), globals())
    globals()['ENV_NAME'] = env_name
    globals()['NUMPROCS'] = numprocs
    globals()['MAIL_SETTINGS'].update({
                                        'send': MAIL_SENDING,
                                        'title': ENV_NAME,
                                        'admins': ADMINS,
                                        'debug': DEBUG,
                                    })


def set_debug_print():
    """使print打印输出到logging输出文件中
    """
    # 让打印输出到logging.log中
    import sys
    import logging

    h = logging.getLogger('debug_print')
    h.write = h.critical
    old_stdout = sys.stdout
    sys.stdout = h

