# coding: utf-8

PERM_NONE = 0           # 无权限
PERM_READ = 4           # 只读权限
PERM_READ_WRITE = 6     # 修改权限
PERM_VALUES = (PERM_NONE, PERM_READ, PERM_READ_WRITE)

URL_SETTINGS = {
    # 路径           : (视图函数,      中文描述,  权限分类， 权限值)
    '/admin/'       : ('views.login', u'登陆', None, PERM_NONE),
    '/admin/login/' : ('views.login', u'登陆', None, PERM_NONE),
    '/admin/logout/': ('views.logout', u'登出', None, PERM_NONE),
    '/admin/left/'  : ('views.left', u'左视图', None, PERM_NONE),
    '/admin/index/' : ('views.index', u'首页', None, PERM_NONE),
    '/admin/upload/' : ('views.upload', u'上传', None, PERM_NONE),

    '/admin/admin_list/'     : ('views.admin_list', u'管理员们', 'admin', PERM_READ),
    '/admin/admin_add/'      : ('views.admin_add', u'添加管理员', 'admin', PERM_READ_WRITE),
    '/admin/admin_delete/'   : ('views.admin_delete', u'删除管理员', 'admin', PERM_READ_WRITE),
    '/admin/admin_manage/'   : ('views.admin_manage', u'设置管理员', 'admin', PERM_READ_WRITE),
    '/admin/change_password/': ('views.change_password', u'修改密码', 'change_password', PERM_READ_WRITE),
    '/admin/server_list/'      : ('views.server_list', u'分服列表', 'server', PERM_READ),
    '/admin/create_new_server/': ('views.create_new_server', u'创建服务器', 'server', PERM_READ_WRITE),
    '/admin/modify_server/'    : ('views.modify_server', u'修改服务器', 'server', PERM_READ_WRITE),
    '/admin/tools/'              : ('tools.tools_index', u'控制工具', 'tools', PERM_READ),
    '/admin/tools/notify_index/' : ('tools.notify_index', u'系统通知', 'tools', PERM_READ),
    '/admin/tools/notify_modify/': ('tools.notify_modify', u'修改系统通知', 'tools', PERM_READ_WRITE),
    '/admin/tools/code_index/'   : ('tools.code_index', u'兑换码', 'tools', PERM_READ),
    '/admin/tools/code_create/'  : ('tools.code_create', u'生成兑换码', 'tools', PERM_READ_WRITE),
    '/admin/tools/code_show/'    : ('tools.code_show', u'部分兑换码', 'tools', PERM_READ),
    '/admin/tools/code_history/' : ('tools.code_history', u'历史兑换码', 'tools', PERM_READ),
    '/admin/tools/code_export/' : ('tools.code_export', u'导出兑换码', 'tools', PERM_READ),
    '/admin/tools/code_inject/' : ('tools.code_inject', u'导入兑换码', 'tools', PERM_READ_WRITE),
    '/admin/tools/sys_time_index/' : ('tools.sys_time_index',  u'系统时间',    'tools', PERM_READ),
    '/admin/tools/sys_time_modify/': ('tools.sys_time_modify', u'修改系统时间', 'tools', PERM_READ_WRITE),
    '/admin/tools/push_index/' : ('tools.push_index', u'推送页面', 'tools', PERM_READ),
    '/admin/tools/push_send/'  : ('tools.push_send',  u'发送推送', 'tools', PERM_READ_WRITE),
    '/admin/tools/virtual_index/'  : ('tools.virtual_index', u'虚拟页面', 'tools', PERM_READ),
    '/admin/tools/virtual_pay/'    : ('tools.virtual_pay',   u'虚拟充值', 'tools', PERM_READ_WRITE),

    '/admin/tools/random_index/': ('tools.random_index', u'概率测试', 'tools', PERM_READ),
    '/admin/tools/random_loot/' : ('tools.random_loot', u'概率测试-loot', 'tools', PERM_READ),
    '/admin/tools/random_block/': ('tools.random_block', u'概率测试-block', 'tools', PERM_READ),
    '/admin/tools/random_fight/': ('tools.random_fight', u'概率测试-fight', 'tools', PERM_READ),
    '/admin/tools/random_card_mix/': ('tools.random_card_mix', u'概率测试-球员交换', 'tools', PERM_READ),
    '/admin/tools/resource_index/' : ('tools.resource_index', u'资源更新', 'tools', PERM_READ),
    '/admin/tools/resource_update/': ('tools.resource_update', u'资源更新', 'tools', PERM_READ_WRITE),

    '/admin/data/'                : ('data.statistics_index',     u'查看数据', 'data', PERM_READ),
    '/admin/data/payinfo_index/'  : ('data.payinfo_index',  u'充值详情', 'data', PERM_READ),
    '/admin/data/analysis_index/' : ('data.analysis_index', u'数据分析', 'data', PERM_READ),
    '/admin/data/payday_index/'   : ('data.payday_index', u'日期详情',  'data', PERM_READ),
    '/admin/data/paydayuid_index/': ('data.paydayuid_index', u'单人详情', 'data', PERM_READ),
    '/admin/data/statistics_index/' : ('data.statistics_index', u'实时统计', 'data', PERM_READ),
    '/admin/data/statistics_channel/' : ('data.statistics_channel', u'渠道统计', 'data', PERM_READ),
    '/admin/data/retention_index/'  : ('data.retention_index', u'留存统计', 'data', PERM_READ),
    '/admin/data/retention_channel/': ('data.retention_channel', u'渠道留存统计', 'data', PERM_READ),
    '/admin/data/league_index/': ('data.league_index', u'联盟', 'data', PERM_READ),

    '/admin/config/'                    : ('config.index',          u'游戏配置', 'config', PERM_READ),
    '/admin/config/index/'              : ('config.index',          u'游戏配置', 'config', PERM_READ),
    '/admin/config/upload/'             : ('config.upload',         u'上传配置', 'config', PERM_READ_WRITE),
    '/admin/config/notify_reload/'      : ('config.notify_reload',  u'重载配置', 'config', PERM_READ_WRITE),
    '/admin/config/get_all_config/'     : ('config.get_all_config', u'下载配置', 'config', PERM_READ_WRITE),
    '/admin/config/check/'              : ('config.check',          u'配置校验', 'config', PERM_READ_WRITE),
    '/admin/config/lua_client_version/' : ('config.lua_client_version', u'LUA配置版本', 'config', PERM_READ_WRITE),

    '/admin/user/'       : ('user.search', u'用户数据', 'user', PERM_READ),
    '/admin/user_all/'   : ('user.user_all', u'分服用户', 'user', PERM_READ),
    '/admin/user/show/'  : ('user.show', u'用户数据', 'user', PERM_READ),
    '/admin/user/modify/': ('user.modify', u'修改用户', 'user', PERM_READ_WRITE),
    '/admin/user/skip_guide/': ('user.skip_guide', u'跳过引导', 'user', PERM_READ),
    '/admin/user_reset/' : ('user.user_reset', u'重置用户', 'user', PERM_READ_WRITE),
    '/admin/user_token/show/': ('user.showtoken', u'分服用户', 'user', PERM_READ),
    '/admin/user/ban_user/': ('user.ban_user', u'封号', 'user', PERM_READ_WRITE),
    '/admin/user/export/': ('user.export', u'导出数据', 'user', PERM_READ),
    '/admin/user/inject/': ('user.inject', u'注入数据', 'user', PERM_READ_WRITE),
    '/admin/username/show/': ('user.show_username', u'分服用户昵称', 'user', PERM_READ),

    '/admin/pve/show/'  : ('pve.index', u'PVE数据', 'user', PERM_READ),
    '/admin/pve/modify/': ('pve.modify', u'修改PVE', 'user', PERM_READ_WRITE),
    '/admin/pve/reset/' : ('pve.reset', u'重置PVE', 'user', PERM_READ_WRITE),
    '/admin/pvelegend/modify/': ('pve.modify_legend', u'修改PVE_legend', 'user', PERM_READ_WRITE),
    '/admin/pvedynasty/modify/': ('pve.modify_dynasty', u'修改PVE_dynasty', 'user', PERM_READ_WRITE),

    '/admin/item/show/' : ('item.index', u'道具数据', 'user', PERM_READ),
    '/admin/item/add/'  : ('item.add', u'添加道具', 'user', PERM_READ_WRITE),
    '/admin/item/reset/': ('item.reset', u'重置道具', 'user', PERM_READ_WRITE),
    '/admin/item/add_patch/'  : ('item.add_patch', u'添加碎片', 'user', PERM_READ_WRITE),
    '/admin/item/reset_patch/': ('item.reset_patch', u'重置碎片', 'user', PERM_READ_WRITE),

    '/admin/card/show/'    : ('card.index', u'卡牌数据', 'user', PERM_READ),
    '/admin/card/add/'     : ('card.add', u'添加卡牌', 'user', PERM_READ_WRITE),
    '/admin/card/modify/'  : ('card.modify', u'修改卡牌', 'user', PERM_READ_WRITE),
    '/admin/card/reset/'   : ('card.reset', u'重置卡牌', 'user', PERM_READ_WRITE),
    '/admin/card/batch_delete/': ('card.batch_delete', u'批量删除', 'user', PERM_READ_WRITE),
    '/admin/card/set_team/': ('card.set_team', u'设定编队', 'user', PERM_READ_WRITE),
    '/admin/card/set_backup/': ('card.set_backup', u'设定助威', 'user', PERM_READ_WRITE),
    '/admin/card_train/show/'    : ('card.train_index', u'卡牌数据', 'user', PERM_READ),
    '/admin/card_train/modify/'  : ('card.train_modify', u'修改卡牌', 'user', PERM_READ_WRITE),
    '/admin/card_train/reset/'   : ('card.train_reset', u'重置卡牌', 'user', PERM_READ_WRITE),
    '/admin/card/delete/'   : ('card.delete', u'清除非阵容中所有球员', 'user', PERM_READ_WRITE),

    '/admin/foreign/show/' : ('card.foreign_index', u'外援数据', 'user', PERM_READ),
    '/admin/foreign/add/'     : ('card.foreign_add', u'添加外援', 'user', PERM_READ_WRITE),
    '/admin/foreign/modify/'  : ('card.foreign_modify', u'修改外援', 'user', PERM_READ_WRITE),
    '/admin/foreign/reset/'   : ('card.foreign_reset', u'重置外援', 'user', PERM_READ_WRITE),

    '/admin/equip/show/'  : ('equip.index', u'装备数据', 'user', PERM_READ),
    '/admin/equip/add/'   : ('equip.add', u'添加装备', 'user', PERM_READ_WRITE),
    '/admin/equip/modify/': ('equip.modify', u'修改装备', 'user', PERM_READ_WRITE),
    '/admin/equip/reset/' : ('equip.reset', u'重置装备', 'user', PERM_READ_WRITE),
    '/admin/equip/load_equip/' : ('equip.load_equip', u'装载装备', 'user', PERM_READ_WRITE),
    '/admin/equip/batch_delete/': ('equip.batch_delete', u'批量删除', 'user', PERM_READ_WRITE),
    '/admin/equip/delete/': ('equip.delete', u'清除未装载的装备', 'user', PERM_READ_WRITE),

    '/admin/handbook/show/'  : ('handbook.index', u'图鉴数据', 'user', PERM_READ),
    '/admin/handbook/modify/': ('handbook.modify', u'修改图鉴', 'user', PERM_READ_WRITE),
    '/admin/handbook/reset/' : ('handbook.reset', u'重置图鉴', 'user', PERM_READ_WRITE),

    '/admin/gacha/show/'  : ('gacha.index', u'GACHA数据', 'user', PERM_READ),
    '/admin/gacha/modify/': ('gacha.modify', u'修改GACHA', 'user', PERM_READ_WRITE),
    '/admin/gacha/reset/' : ('gacha.reset', u'重置GACHA', 'user', PERM_READ_WRITE),

    '/admin/friend/show/'  : ('friend.index', u'好友数据', 'user', PERM_READ),
    '/admin/friend/modify/': ('friend.modify', u'修改好友', 'user', PERM_READ_WRITE),
    '/admin/friend/reset/' : ('friend.reset', u'重置好友', 'user', PERM_READ_WRITE),
    '/admin/friend/be_invited_modify/': ('friend.be_invited_modify', u'被邀请好友修改', 'user', PERM_READ_WRITE),
    '/admin/friend/to_invite_modify/' : ('friend.to_invite_modify', u'主动邀请好友修改', 'user', PERM_READ_WRITE),

    '/admin/arena/show/'  : ('arena.index', u'锦标赛数据', 'user', PERM_READ),
    '/admin/arena/modify/': ('arena.modify', u'修改锦标赛', 'user', PERM_READ_WRITE),
    '/admin/arena/reset/' : ('arena.reset', u'重置锦标赛', 'user', PERM_READ_WRITE),

    '/admin/subrecord/show/': ('subrecord.index', u'消费数据', 'user', PERM_READ),
    '/admin/subrecord_money/show/': ('subrecord.money_index', u'消费数据', 'user', PERM_READ),

    '/admin/payment/show/': ('payment.index', u'充值数据', 'user', PERM_READ),

    '/admin/notify/show/'  : ('notify.index', u'系统通知', 'user', PERM_READ),
    '/admin/notify/modify/': ('notify.modify', u'修改系统通知', 'user', PERM_READ_WRITE),
    '/admin/notify/reset/' : ('notify.reset', u'重置系统通知', 'user', PERM_READ_WRITE),

    '/admin/award/show/'  : ('award.index', u'奖励系统', 'user', PERM_READ),
    '/admin/award/modify/': ('award.modify', u'修改奖励系统', 'user', PERM_READ_WRITE),
    '/admin/award/reset/' : ('award.reset', u'重置奖励系统', 'user', PERM_READ_WRITE),

    '/admin/active/show/'           : ('active.index', u'活动内容', 'user', PERM_READ),
    '/admin/active/modify/'         : ('active.modify', u'修改活动内容', 'user', PERM_READ_WRITE),
    '/admin/active/reset/'          : ('active.reset', u'重置活动内容', 'user', PERM_READ_WRITE),
    '/admin/active/modify_yao/'     : ('active.modify_yao', u'修改姚餐厅', 'user', PERM_READ_WRITE),
    '/admin/active/modify_consume/' : ('active.modify_consume', u'修改消费有礼', 'user', PERM_READ_WRITE),
    '/admin/active/modify_exchange/': ('active.modify_exchange', u'修改限时兑换', 'user', PERM_READ_WRITE),
    '/admin/active/modify_charge/'  : ('active.modify_charge', u'修改充值有礼', 'user', PERM_READ_WRITE),

    '/admin/league/show/'           : ('league.index', u'联盟首页', 'user', PERM_READ),
    '/admin/league/modify/'         : ('league.modify', u'修改个人联盟内容', 'user', PERM_READ_WRITE),
    '/admin/league/quit_league/'    : ('league.quit_league', u'退出联盟', 'user', PERM_READ_WRITE),

    '/admin/task/show/'             : ('task.index', u'任务数据', 'user', PERM_READ),
    '/admin/task/modify/'      : ('task.modify', u'修改任务数据', 'user', PERM_READ_WRITE),
    '/admin/task/reset/'            : ('task.reset', u'重置任务数据', 'user', PERM_READ_WRITE),

}

# 左视图连接配置
LEFT_HREF = [
    '/admin/user/',
    '/admin/config/',
    '/admin/server_list/',
    '/admin/tools/',
    '/admin/data/',
    '/admin/admin_list/',
    '/admin/change_password/',
    '/admin/logout/',
]

# 权限们
PERM_URLS = {}
PERM_KEYS = set(['super'])
PERM_ITEMS = {'super': u'超级权限'}
for url, value in URL_SETTINGS.iteritems():
    PERM_URLS[url] = (value[2], value[3])
    if value[2]:
        PERM_KEYS.add(value[2])
        if value[2] not in PERM_ITEMS:
            PERM_ITEMS[value[2]] = value[1]

