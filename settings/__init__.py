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
    'error@126.com',
)
# 客户端报错邮件接收人
CLIENT_DEVELOP = (
    'client@126.com',
)
DEFAULT_ADMIN_MANAGER = (
    ('aaa.bbb', '1qwe32'),
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
STATS_REYUN_APPKEY = 'xsfasdfasdfaefdsfasd'
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
}
# 平台下定单的地址
PAYMENT_ORDER_URLS = {
}
# 已方charge表商品编号对应一些平台商品编号的映射
PAYMENT_WARESID_MAP = {
}

PROJECT_NAME = 'wsapp'
BASE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOGS_ROOT = os.path.join(BASE_ROOT, 'logs')
TEMPLATE_ROOT = os.path.join(BASE_ROOT, 'templates')
STATIC_ROOT = os.path.join(BASE_ROOT, 'statics')
SCRIPT_ROOT = os.path.join(BASE_ROOT, 'scripts')
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

