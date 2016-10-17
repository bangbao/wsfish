# coding: utf-8

from . import consts

URL_MAPPING = {}

# url配置在consts文件中详细定义， 这里自动生成url-views的映射
for url, settings in consts.URL_SETTINGS.iteritems():
    URL_MAPPING[url] = settings[0]



# URL_MAPPING = {
#     '/admin/': 'views.login',
#     '/admin/index/': 'views.index',
#     '/admin/left/': 'views.left',
#     '/admin/login/': 'views.login',
#     '/admin/add_admin/': 'views.add_admin',

#     '/admin/card/': 'card.index',
#     '/admin/card/modify/': 'card.modify',
#     '/admin/card/add/': 'card.add',
#     '/admin/card/reset/': 'card.reset',
# }
