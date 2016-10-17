# coding: utf-8

TOKEN_SALT_HYPHEN = '||'
DEFAULT_TEST_USER_ID = 'test'

ENERGY_HEAL_UNIT = 1
BATTLE_HEAL_UNIT = 1

# cost_diamond配置中的cfg_id
USER_EXPENSE_FILL_ENERGY = 1
USER_EXPENSE_FILL_BATTLE = 2
USER_EXPENSE_TRAIN_SKILL = 3
USER_EXPENSE_ARENA_FIGHT = 4
USER_EXPENSE_PVE_EXPSTAGE_FIGHT = 11
USER_EXPENSE_PVE_MONEYSTAGE_FIGHT = 12
USER_EXPENSE_PVE_DYNASTY_REFRESH_SHOP = 16
USER_EXPENSE_PVE_DYNASTY_REFRESH_ACTIVISTS = 17
USER_EXPENSE_PVE_LEGEND_FIGHT = 100
USER_EXPENSE_PVE_STAGE_RESET = 300
USER_EXPENSE_PVE_DYNASTY_RESET = 400
USER_EXPENSE_PVE_HSTAGE_RESET = 500
USER_EXPENSE_QMZP_LUCKY_FRESH = 600
USER_EXPENSE_QMZP_LUXURY_FRESH = 601
USER_EXPENSE_SHOP_BUY_MONEY_REDUCE = 1000

# ('维护中', '热', '新', '满')
GAME_SERVER_STATUS_MAINTENANING = 0
GAME_SERVER_STATUS_HOT = 1
GAME_SERVER_STATUS_NEW = 2
GAME_SERVER_STATUS_FULL = 3
GAME_SERVER_STATUS_MAP = {
    GAME_SERVER_STATUS_MAINTENANING: u'维护中',
    GAME_SERVER_STATUS_HOT: u'热',
    GAME_SERVER_STATUS_NEW: u'新',
    GAME_SERVER_STATUS_FULL: u'满',
}

# 充值首充普通, 双倍, 三倍
CHARGE_CONFIG_FIRST_PAY_NONE = 0
CHARGE_CONFIG_FIRST_PAY_HAVE = 1
CHARGE_CONFIG_FIRST_PAY_SP = 2
CHARGE_CONFIG_FIRST_PAY_SP_HAVE_LIST = (1, 2)

USER_FUNCTRL_ARENA = 1
USER_FUNCTRL_ROB_PATCH_OPPONENT = 2
USER_FUNCTRL_RENT_FOREIGN = 3
USER_FUNCTRL_PVE_LEGEND = 4
USER_FUNCTRL_PVE_DYNASTY = 5
USER_FUNCTRL_CARD_BACKUP = 6
USER_FUNCTRL_CARD_TUTOR = 7
USER_FUNCTRL_EQUIP_DEVELOP = 8
USER_FUNCTRL_PVE_HSTAGE = 9
USER_FUNCTRL_EQUIP_EVOLUTION = 10
#USER_FUNCTRL_CARD_REBORN = 11
USER_FUNCTRL_SHOP_MYSTICSHOP = 12
USER_FUNCTRL_DECORATION_LEVELUP = 14
USER_FUNCTRL_CARD_EVOLUTION = 22
USER_FUNCTRL_CARD_TRAIN_SKILL = 23
USER_FUNCTRL_CARD_STRATEGY = 31
USER_FUNCTRL_PVE_MONEY = 30
USER_FUNCTRL_GAMEVS = 35
USER_FUNCTRL_LEAGUE = 36
USER_FUNCTRL_TRAINING = 37
USER_FUNCTRL_AWAKENING = 38
USER_FUNCTRL_PVE_SWEEP = 100
USER_FUNCTRL_TASK = 101
USER_FUNCTRL_TEAM_LOCK = 102
USER_FUNCTRL_EQUIP_LEVELUP_ONEKEY = 1001  #vip控制, 在接口内做判断, 方便vip等级不足统一弹板

USER_FUNCTRL_MAP = {
    USER_FUNCTRL_ARENA: ('arena.index', 'arena.target_peep', 'arena.fight',),
    USER_FUNCTRL_ROB_PATCH_OPPONENT: ('rob.patch_opponent',),
    USER_FUNCTRL_RENT_FOREIGN: ('card.rent_foreign',),
    USER_FUNCTRL_PVE_LEGEND: ('pve.legendchapter', 'pve.legendstage', 'pve.legendexplore',),
    USER_FUNCTRL_PVE_DYNASTY: ('pve.dynasty_index', 'pve.dynasty_shop'),
    USER_FUNCTRL_CARD_BACKUP: ('card.backup_set',),
    USER_FUNCTRL_CARD_TUTOR: ('card.tutor_info', 'card.tutor_load_materials', 'card.tutor_evolution',),
    USER_FUNCTRL_EQUIP_DEVELOP: ('equip.pre_develop', 'equip.develop'),
    USER_FUNCTRL_EQUIP_EVOLUTION: ('equip.pre_evolution', 'equip.evolution',),
    #USER_FUNCTRL_CARD_REBORN = 11
    USER_FUNCTRL_SHOP_MYSTICSHOP: ('shop.mysticshop_index',),
    USER_FUNCTRL_DECORATION_LEVELUP: ('equip.pre_decoration_levelup', 'equip.decoration_levelup'),
    USER_FUNCTRL_CARD_EVOLUTION: ('card.evolution',),
    USER_FUNCTRL_CARD_TRAIN_SKILL: ('card.train_skill',),
    USER_FUNCTRL_CARD_STRATEGY: ('card.strategy_index', 'card.strategy_setup', 'card.strategy_levelup',),
    USER_FUNCTRL_PVE_MONEY: ('pve.moneychapter', 'pve.moneystage_fight', 'pve.moneystage_settlement'),
    USER_FUNCTRL_PVE_SWEEP: ('pve.sweep',),
    USER_FUNCTRL_GAMEVS: ('gamevs.index', 'gamevs.fight', 'gamevs.open_gamevs', 'gamevs.fight', 'gamevs.rating_index'),
    USER_FUNCTRL_LEAGUE: ('league.index', 'league.create', 'league.league_list', 'league.league_apply', 'league.applied_leagues'),
    USER_FUNCTRL_TRAINING: ('card.training_index', 'card.training_preview', 'card.training_replace', 'card.training_cancel'),
    USER_FUNCTRL_AWAKENING: ('card.awakening',),
    #USER_FUNCTRL_EQUIP_LEVELUP_ONEKEY: ('equip.pre_levelup_onekey', 'equip.levelup_onekey'),
    USER_FUNCTRL_PVE_HSTAGE: ('pve.hchapter', 'pve.hstage_fight_ready', 'pve.hstage_fight'),
}
USER_FUNCTRL_METHODS = dict((m, k) for k, vs in USER_FUNCTRL_MAP.iteritems() for m in vs)
