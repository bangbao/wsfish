# coding: utf-8

# 不作版本校验的接口
IGNORE_API = set([
    'config.resource_version',
    'config.config_version',
    'config.all_config',
    'config.server_list',
    'user.register',
    'user.login',
    'user.loading',
    'user.rename',
    'user.game_enter',
    'user.guide',
    'user.guide_battle',
    'pve.gamerace',
    'pve.legendgamerace',
    'pve.dynasty_settlement',
    'pve.moneystage_settlement',
    'payment.refresh',
    'payment.index',
    'client.exception_info',
])

# 不作低版本限制的接口
IGNORE_RES_VER_LIMIT_API = set([
    'config.resource_version',
    'config.config_version',
    'config.all_config',
    'config.server_list',
    'user.register',
    'user.login',
    'user.platform_access',
    'pve.gamerace',
    'pve.legendgamerace',
    'pve.dynasty_settlement',
    'pve.moneystage_settlement',
    'payment.refresh',
    'payment.index',
    'client.exception_info',
])

# 校验背包中卡牌、装备是否超上限的接口
CARD_BAG_TOP_API = set([
    'pve.sweep',
    'pve.stage',
    'pve.gamefriend',
    'pve.gamerace_start',
    'pve.game1v1',
    'pve.legend_fight',
    'pve.dynasty_fight',
    'pve.moneystage_fight',
    'arena.fight',
    # 'rob.rob_patch',
    'rob.rob_money',
    'rob.rob_player',
    'item.open_treasure',
    'item.use_gacha_box',
    'gamevs.fight',
])

# 遇到报错需要重启游戏的接口
METHOD_NAME_ERROR_NEED_RESTART = set([
    'pve.game1v1',
    'pve.gamefriend',
    'pve.gamerace',
    'pve.legendgamerace',
    'pve.dynasty_settlement',
    'pve.moneystage_settlement',
    'card.levelup',
    'card.evolution',
    #'card.rebirth',
    'card.mix',
    'equip.evolution',
    #'equip.rebirth',
    'equip.mix',
])

