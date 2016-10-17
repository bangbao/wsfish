#  coding: utf-8

"""
注：模块间, ID间隔100, 避免覆盖
"""

USER_TOKEN_ERROR = 1000                     # 用户验证失败, 请重新登录
SYSTEM_ERROR = 1001                         # u'非法请求'
SERVER_NOT_EXISTS = 1002                    # u'服务器不存在'
SERVER_IS_MAINTAINING = 1003                # u'服务器维护中'
SERVER_CONFIG_UPDATE = 1004                 # u'客户端配置更新'
SERVER_RESOURCE_UPDATE = 1005               # u'客户端资源更新'
SERVER_RESOURCE_VERSION_LIMIT = 1006        # u'客户端已更新, 请更新游戏'
CHANNEL_ERROR = 1007                        # u'渠道错误, 请确认后在登陆'

USER_NOT_EXISTS = 1101                      # u'用户不存在'
USER_REGISTER_ACCOUNT_EXISTS = 1102         # u'用户账户已存在'
USER_REGISTER_ACCOUNT_NOT_MATCH = 1103      # u'用户账户格式不对: 只能使用以下字符: a-zA-Z0-9.-@, 长度4-20位'
USER_REGISTER_PASSWORD_NOT_MATCH = 1104     # u'用户密码格式不对: 长度4-20位'
USER_LOGIN_ACCOUNT_NOT_EXISTS = 1105        # u'用户登录时账户不存在, 请注册'
USER_LOGIN_PASSWORD_ERROR = 1106            # u'用户登陆时密码不对'
USER_RENAME_SENSITIVE_WORD = 1107           # u'用户昵称中有敏感词'
USER_RENAME_REDUPLICATE = 1108              # u'用户昵称与他人重复'
USER_GAME_ENTER_ERROR_LEADER = 1109         # u'游戏注册LEADER错误'
USER_GAME_ENTER_ERROR_LOGO = 1110           # u'游戏注册LOGO错误'
USER_FILL_CAPABILITY_ENERGY_COUNT_TOP = 1111 # u'今日回复行动力次数已达上限，请提升vip等级'
USER_PLATFORM_ACCESS_FAILTURE = 1112        # u'平台登录验证失败'
USER_FILL_CAPABILITY_BATTLE_COUNT_TOP = 1113 # u'今日回复战力点次数已达上限，请提升vip等级'
USER_RENAME_NOT_EMPTY = 1114                # u'亲，昵称不能为空哦'
USER_RENAME_MORE_LENGTH = 1115              # u'亲，昵称长度要限制在7位内哦'
USER_UID_ERROR = 1116                       # u'用户UID格式错误'
USER_IS_BAN = 1117                          # u'账号异常, 请联系客服'

LEVEL_NOT_ENGOUGH = 1201                    # u'等级不足'
VIP_LEVEL_NOT_ENGOUGH = 1202                # u'VIP等级不足'
MONEY_NOT_ENOUGH = 1203                     # u'金钱不足'
COIN_NOT_ENOUGH = 1204                      # u'钻石不足'
BATTLE_NOT_ENOUGH = 1205                    # u'战斗点数不足'
ENERGY_NOT_ENOUGH = 1206                    # u'行动力不足'
ENERGY_IS_TOP = 1207                        # u'行动力是满的'
BATTLE_IS_TOP = 1208                        # u'战力点是満的'
HONOR_NOT_ENOUGH = 1209                     # u'荣誉点（训练点）不足'
POINT_NOT_ENOUGH = 1210                     # u'积分不足'
NUM_INVALID = 1211                          # u'所选数量无效'
RANKING_NUM_ERROR = 1212                    # u'亲，甭拉了，到底了(排行榜中用)'

FRIEND_ADD_FRIEND_NOT_ADD_SELF = 1301       # u'不能加自己为好友'
FRIEND_IS_YOUR_FRIEND = 1302                # u'对方已经是你好友了'
FRIEND_IS_NOT_YOUR_FRIEND = 1303            # u'对方不是你好友'
FRIEND_HAD_APPLY = 1304                     # u'之前你已发出申请'
FRIEND_NOT_APPLY = 1305                     # u'对方未向你申请加好友'
FRIEND_CANNOT_SEND = 1306                   # u'今日赠送行动力次数已经到达上限。'
FRIEND_CANNOT_RECEIVE = 1307                # u'今日接受行动力次数已经到达上限。'
FRIEND_SENT = 1308                          # u'已赠送过体力给该好友，明天再送吧。'
FRIEND_RECEIVE_FAIL = 1309                  # u'该好友今日还未赠送体力给自己'
FRIEND_SEND_FAIL = 1310                     # u'没有可赠送的好友'
FRIEND_NO_RECEIVE = 1311                    # u'没有可接收的体力'
FRIEND_HAD_RECEIVE = 1312                   # u'已接收过该好友赠送的体力，明天再来吧。'
FRIEND_INVITE_FAIL = 1313                   # u'没有可邀请的好友'
FRIEND_NUM_MAX = 1314                       # u'您的好友数量已达上限'
FRIEND_TARGET_NUM_MAX = 1315                # u'对方的好友数量已达上限，邀请别人吧'

CARD_NOT_EXISTS = 1401                      # u'卡牌不存在'
CARD_IN_TEAM = 1402                         # u'卡牌在编队中'
CARD_IN_TEAM_FIRST = 1403                   # u'不能选首发阵容中的球员'
CARD_IN_BACKUP = 1404                       # u'卡牌在助威阵容中'
CARD_IS_LOCK = 1405                         # u'卡牌被锁定'
CARD_IS_MAXLV = 1406                        # u'卡牌已到最高级'
CARD_NOT_MAXLV = 1407                       # u'卡牌没到最高级'
CARD_NOT_EATEN = 1408                       # u'卡牌不能被当做材料'
CARD_NOT_SELL = 1409                        # u'卡牌不能被卖出'
CARD_NOT_RETIRE = 1410                      # u'卡牌不能退役'
CARD_MATERIALS_NOT_ENOUGH = 1411            # u'卡牌材料不足'
CARD_NOT_EVOLUTION = 1412                   # u'卡牌不能进阶'
CARD_SET_TEAM_PRE_FIVE_POS_NOT_NONE = 1413      # u'编队时初始阵容不能有空位'
CARD_SET_TEAM_NOT_HAVE_SAMENAME = 1414          # u'编队中不能有相同名字的队员'
CARD_TRAIN_SKILL_MAX_TRAINTIMES = 1416          # u'卡牌技能洗练次数已用完'
CARD_TRAIN_SKILL_EMPTY_TRAIN_IDXS = 1417        # u'根据您的选择，没有要洗练的技能'
CARD_RETIRE_MAX_RETIRETIMES = 1418              # u'卡牌退役今赛季已到最大次数'
CARD_ADD_RENT_CARD_IN_RENTS = 1419              # u'此卡牌已经在租借列表中了'
CARD_ADD_RENT_POS_CARD_IS_RENTED = 1420         # u'此位置卡牌已经被借出了。不能替换'
CARD_ADD_RENT_CARD_CAN_NOT_RENTED = 1421        # u'此卡片不支持外援出租'
CARD_RENT_FOREIGN_ONE_DAY_ONE_TIMES = 1422      # u'每天只能对同一球员租借一次'
CARD_RENT_FOREIGN_IS_RENTED = 1423              # u'卡牌已被出租，请换一个'
CARD_SET_AUTO_RETIRED_NOT_IN_RENTS = 1424       # u'卡牌不在出租列表中'
CARD_STRATEGY_LEVELUP_STRATEGY_IS_MAXLV = 1425  # u'战术已到最高级'
CARD_BAG_OVERFLOW_CARDS_TOP = 1426              # u'背包中卡牌超出上限，不能装载队员'
CARD_HAD_AUTO_RETIRED = 1427                    # u'球员已在归队列表中'
CARD_RETIRE_EXCESS = 1428                       # u'球员退役数量超出上限'
CARD_RENT_FOREIGN_VIP_AID_NUM_LIMIT = 1429      # u'拥有外援数量已达上限'
CARD_EVOLUTION_UPTO_MAXLEVEL = 1432             # u'已是最高阶，不能进阶'
CARD_EVOLUTION_MATERAIL_STARTLEVEL = 1433       # u'进阶材料卡牌starlevel星级不符合'
CARD_EVOLUTION_MATERAIL_NOT_ENOUGH = 1434       # u'进阶材料卡牌不足'
CARD_PLAYER_NOT_ENOUGH = 1435                   # u'阵容不足十人，无法进行任何比赛'
CARD_SET_TEAM_PRE_FIVE_POS_NOT_FOREIGN = 1436   # u'外援无法进入首发名单'
CARD_SET_TEAM_MORE_FOREIGN = 1437               # u'阵容中只能有一个外援球员'
CARD_EVOLUTION_EXP_CARD_NOT_EATEN = 1438        # u'经验卡不能作为球员进阶材料'
CARD_NOT_REBIRTH = 1441                        # u'该球员不能重生'
CARD_NOT_MIX = 1442                            # u'该球员不能熔炼'
CARD_MIX_NOT_SAME_STAR = 1443                  # u'球员熔炼需要相同星级的材料'
CARD_REBIRTH_START_LOW = 1444                   # 紫色及以上品质的卡牌才能重生
CARD_REBIRTH_LEVEL_LOW = 1445                   # Starplus字段为0的且等级<10级的卡牌不能重生
CARD_EVOLUTION_MATERAIL_NOTSELF = 1446          # 进阶材料卡牌需要本卡 没有相同颜色的同名球员，快去选秀吧。
METERAIL_CART_NOT_IN_TEAM = 1447                # 材料卡牌不能进入主力阵容
METERAIL_CART_NOT_IN_BACKUP = 1448              # 材料卡牌不能进入助威阵容
METERAIL_CART_NOT_EVOLUTION = 1449              # 材料卡牌不能进阶
METERAIL_CART_NOT_LVUP = 1450                   # 材料卡牌不能升级
METERAIL_CART_NOT_FOREIGN = 1451                # 材料卡牌做外援
METERAIL_CART_NOT_TRAIN_SKILL = 1452            # 材料卡牌不能技能洗炼
METERAIL_CART_NOT_EVOLUTION_MATERAIL = 1453     # 此特殊材料卡牌不能做进阶材料
METERAIL_CART_NOT_LVUP_MATERAIL = 1454          # 此特殊材料卡牌不能做升级材料
METERAIL_CART_NOT_MIX = 1455                    # 特殊材料卡牌不能交换
CARD_STRATEGY_LEVELUP_PVESTAR_NOT_ENOUGH = 1456 # u'战术之星不足，无法升级战术'
CARD_STRATEGY_RESET_STRATEGY_LEVEL_LOW = 1457   # u'1级战术无法重置'
CARD_EVOLUTION_CARD_LEVEL_LOW = 1458            # 球员等级不足
CARD_TRAINING_TIME_SORT = 1459                  # 培养次数错误
CARD_TRAINING_SORT = 1460                       # 培养类型错误Cultivate Dan
CARD_TRAINING_ITEM_NOT_ENOUGH = 1461            # 特训卡数量不足
CARD_NOT_TRAINING = 1462                        # 球员未培养
CARD_TRAINING_UPTO_TOP = 1463                   # 所有属性已经培养到上限，请提升卡牌品质
CARD_ADD_RENT_CARD_NOT_IN_FOREIGN = 1464        # 对方已回收此球员，请租赁其他球员
CARD_MATERIAL_NOT_ENOUGH = 1465                 # 材料不足
CARD_JOINTLY_CID_NOT_EXIST = 1466               # 球员的联携ID不存在
CARD_REPEAT = 1467                              # 球员不能重复
CARD_NOT_CORRESPONDING_POSITION = 1468          # 球员不在skill_jointly配置相应的awakening_player或者upawakeing_player中
CARD_NOT_MATERIAL_CARD = 1469                   # 要觉醒的卡牌不能为材料卡
CARD_ONLY_CARD_JOINTLY = 1470                   # 只能为球员联携
CARD_UPAWAKENING_MAV_LEVEL = 1471               # 该组合已经满级无法继续强化


EQUIP_NOT_EXISTS = 1501                         # u'装备不存在'
EQUIP_IN_TEAM = 1502                            # u'装备在编队中'
EQUIP_IS_LOCK = 1503                            # u'装备被锁定'
EQUIP_IS_MAXLV = 1504                           # u'强化等级已达上限'
EQUIP_LEVELUP_GT_USER_LEVEL = 1505              # u'强化等级已达上限，请提升球队等级'
EQUIP_NOT_MAXLV = 1506                          # u'强化等级没达上限'
EQUIP_NOT_EVOLUTION = 1507                      # u'装备不能进阶'
EQUIP_EVOLUTION_MATERIALS_NOT_ENOUGH = 1508     # u'装备材料不足'
EQUIP_EVOLUTION_ITEM_NOT_ENOUGH = 1509          # u'装备材料道具不足'
EQUIP_LOAD_HAD_LOADED_IN_OTHER_POS = 1510       # u'装备已在其它位置中'
EQUIP_LOAD_CAN_NOT_HAS_SAME_SIZE_EQUIP = 1511   # u'一个球队不能有重复的号码'
EQUIP_NOT_RETIRE = 1512                         # u'装备不能退役'
EQUIP_RETIRE_EXCESS = 1513                      # u'装备退役数量超出上限'
EQUIP_BAG_OVERFLOW_TOP = 1514                   # u'您的装备携带数量已达上限'
EQUIP_EVLUTION_UPTO_MAX = 1515                  # u'该装备已到最高阶，无法继续进阶'
EQUIP_EVLUTION_CONSUME_ERROR = 1516             # u'进阶需要吞噬一件相同部位，相同星级的装备'
EQUIP_EVLUTION_CANOT_SELF = 1517                # u'进阶需要吞噬的装备不能是进阶装备本身'
EQUIP_EVLUTION_EQUIP_USED = 1518                # u'进阶需要吞噬的装备已被球员装载'
EQUIP_NOT_MIX = 1519                            # u'该装备不能熔炼'
EQUIP_MIX_NOT_SAME_STAR = 1520                  # u'装备熔炼需要相同星级的材料'
EQUIP_MIX_MATERIAL_NOT_ENOUGH = 1521            # u'所需材料不足'
EQUIP_ALMIGHTY_NOT_EVOLUTION = 1522             # u'万能装备无法进阶'
EQUIP_ALMIGHTY_NOT_LEVELUP = 1523               # u'万能装备无法强化'
EQUIP_ALMIGHTY_NOT_LOAD = 1524                  # u'万能装备无法装备'
EQUIP_NOT_REBIRTH = 1525                        # u'该装备不能重生'
EQUIP_REBIRTH_LEVEL_LOW = 1526                  # 0阶强化且等级为1级的装备不能重生
EQUIP_LEVELUP_ONEKEY_MAX = 1527                 # 装备都达到满级，不能强化
EQUIP_LEVELUP_ONEKEY_NO = 1528                  # 球员身上无装备可强化
EQUIP_LOAD_ONEKEY_NO = 1529                     # 目前没有可用的装备，快去抽装备吧
EQUIP_EVOLUTION_ONLY_THIS_SORT = 1530           # u'只有饰品和号码才能进阶'
EQUIP_DEVELOP_ONLY_THIS_SORT = 1531             # u'只有球衣、短裤、球鞋和护具才能突破'
EQUIP_DEVELOP_STAR_NOT_ENOUGH = 1532            # u'橙色及以上装备才可进行突破'
EQUIP_LEVELUP_ONEKEY_VIP_LIMIT = 1533           # u'vip等级不足,不能一键强化'
EQUIP_DECORATION_ERROR = 1534                   # u'只能消耗同种类型的饰品或号码'
EQUIP_DECORATION_LIMIT = 1535                   # u'只有号码饰品才能通过吞噬同类型装备进行强化'

PVE_CHAPTER_AWARD_ACCEPT_AWARD = 1601           # u'此章节已领奖'
PVE_CHAPTER_AWARD_NO_AWARD = 1602               # u'此章节不能领奖'
PVE_STAGE_NOT_OPEN = 1603                       # u'此关卡没开启'
PVE_STAGE_USER_LEVEL_NOT_ENOUGH = 1604          # u'等级不足，请升级后再来'
PVE_STAGE_MAX_FIGHT_NUM = 1605                  # u'此关卡今日挑战次数已用完， 请来日再战'
PVE_BLOCK_NOT_MATCH = 1606                      # u'请求地块与记录地块不匹配'
PVE_BLOCK_IS_DONE = 1607                        # u'此地块已完成，请继续前进吧'
PVE_BLOCK_SORT_NOT_MATCH = 1608                 # u'地块类型不对'
PVE_EXPLORE_BLOCK_NOT_DONE_NO_USE_DICE = 1610   # u'当前地块没完成，不能使用色子道具'
PVE_EXPLORE_DICE_ITEM_NOT_ENOUGH = 1611         # u'地块探索时使用色子道具不足'
PVE_SKIP_ITEM_NOT_ENOUGH = 1612                 # u'直达球场道具不足'
PVE_DYNASTY_RESTART_NO_FIGHT_TIMES = 1613       # u'今日重置次数已用完，请明日再来'
PVE_DYNASTY_PEEP_NOT_MATCH = 1614               # u'不要好高骛远啊'
PVE_DYNASTY_FIGHT_HIGHER = 1615                 # u'莫要好高骛远啊'
PVE_DYNASTY_FIGHT_LOWER = 1616                  # u'莫走回头路啊'
PVE_DYNASTY_FIGHT_STAMINA_DEAD = 1617           # u'首发有疲劳状态球员，无法继续王朝'
PVE_DYNASTY_FIGHT_NO_FORMATION = 1618           # u'请设定阵容后再来'
PVE_DYNASTY_GRADE_NOT_ENOUGH = 1619             # u'王朝积分不足'
PVE_DYNASTY_SET_TEAM_IS_DOING = 1620            # u'王朝之路中，不能调整阵容'
PVE_DYNASTY_SET_TEAM_NO_FOREIGN = 1621          # u'王朝之路中，不能调整阵容'
PVE_DYNASTY_FIGHT_LVLIMIT = 1622                # u'首发有等级不足球员，无法继续王朝'
PVE_MONEYSTAGE_NO_FIGHT_NUM = 1623              # u'金钱关卡没挑战次数了'
PVE_DYNASTY_STAR_LOWER = 1624                   # u'王朝之路当前关卡未达到三星评价无法扫荡'
PVE_DYNASTY_CANCEL_ERROR = 1625                 # u'王朝之路未使用突进功能'
PVE_DYNASTY_TO_MAX = 1626                       # u'当前可突进关卡已达最高，需重置到第一关进行突进'
PVE_STAGE_STAR_LOW = 1627                       # u'此关卡的星级太低，不能扫荡'
PVE_STAGE_FIGHT_HIGHER = 1628                   # u'挑战次数超上限， 不能扫荡'
PVE_LEGEND_MAX_FIGHT_NUM = 1629                 # u'今日挑战次数已用完， 请来日再战'
PVE_LEGEND_FIGHT_BUY_OVER = 1630                # u'今日球星传奇可购买次数已达上限，请来日再战'
PVE_DYNASTY_FIRST_DOING_NOT_RESTART = 1631      # 王朝模式至少通过一关才能重置
PVE_LEGEND_CHAPTER_NOT_OPEN = 1632              # u'球星传奇此章节未开启'
PVE_STAGE_NOT_MAX_FIGHT_NUM = 1633              # u'今日挑战次数还未用完,不能重置'
PVE_STAGE_HAVE_NO_RESET = 1634                  # u'此关卡没有重置功能'
PVE_STAGE_RESET_BUY_OVER = 1635                 # u'今日重置次数已用完'
PVE_MONEY_FIGHT_BUY_OVER = 1636                 # u'今日购买次数已使用完，请提升vip等级拥有更多购买次数'
PVE_HSTAGE_RESET_BUY_OVER = 1637                # u'今日重置次数已用完'
PVE_HSTAGE_STAR_LOW = 1638                      # u'此关卡的星级太低，不能扫荡'
PVE_HSTAGE_MAX_FIGHT_NUM = 1639                 # u'今日挑战次数已用完， 请来日再战'

ITEM_PEEP_USER_NOT_ENOUGH = 1701                # u'球探道具不足'
ITEM_FILL_ENERGY_NOT_ENOUGH = 1702              # u'佳得乐道具不足'
ITEM_FILL_BATTLE_NOT_ENOUGH = 1703              # u'红牛道具不足'
ITEM_GACHA_ITEM_NOT_ENOUGH = 1704               # u'GACHA道具不足'
ITEM_CARD_EVOLUTION_NOT_ENOUGH = 1705           # u'球员进阶道具不足'
ITEM_PATCHPLAYER_NOT_ENOUGH = 1706              # u'球员碎片不足'
ITEM_TREASURE_NOT_ENOUGH = 1707                 # u'礼包不足'
ITEM_PATCH_MERGE_PATCH_NOT_ENOUGH = 1708        # u'装备碎片合成碎片不足'
ITEM_USE_GACHA_BOX_NOT_ENOUGH = 1709            # u'宝箱不足'
ITEM_USE_ITEM_NOT_ENOUGH = 1710                 # u'道具不足'
ITEM_USE_LEGEND_NOT_ENOUGH = 1711               # u'巨星指南不足'
ITEM_PATCHEQUIP_NOT_ENOUGH = 1712               # u'装备护具碎片不足'
ITEM_USE_NOT_DIRECT_USE = 1713                  # u'该道具不能直接使用'

ROB_BATTLE_CAN_NOT_SELF = 1801                  # u'不能自己抢自己'
ROB_PATCH_TARGET_HAS_NOT_THIS_PATCH = 1802      # u'对手没这个碎片'
ROB_PLAYER_IN_SAFETIME = 1803                   # u'球员在保护期， 不能抢夺'
ROB_PLAYER_NOT_RENTED = 1804                    # u'球员没有被租出，不能抢夺'
ROB_PLAYER_CAN_NOT_ROB_SELF = 1805              # u'不能自己抢自己的外援'
#  ROB_PATCH_ROBBED = 1806                      # u'你来晚了，此碎片已被其他玩家夺取，无法抢夺该碎片。'
ROB_PATCH_CANNOT_ROB = 1807                     # u'该碎片无法抢夺'
ROB_PATCH_HAD = 1808                            # u'你已经有这个碎片了，不要太贪心'
ROB_PATCH_WAR_FREE = 1809                       # u'该玩家处于免战状态，无法抢夺'
ROB_PATCH_SYS_TIME = 1810                       # u'当前时段为系统免战时段，无法抢夺玩家'
ROB_PATCH_PATCH_SHORT = 1811                    # u'对手就这一个配方，手下留情吧'

ARENA_LEVEL_NOT_ENOUGH = 1901                   # u'7级开启全服排位赛功能'
ARENA_EXCHANGE_NOT_OPEN = 1902                  # u'此兑换没有开启'
ARENA_EXCHANGE_NO_EXCHANGE_COUNT = 1903         # u'今日兑换次数已达上限，请明日再来'
ARENA_FIGHT_NO_TIMES = 1904                     # u'今日战斗次数已用完'
ARENA_EXCHANGE_RANK_NOT_ENOUGH = 1905           # u'排名不足以兑换'
ARENA_FIGHT_BUY_OVER = 1906                     # u'今日购买战斗次数已达上限'
ARENA_EXCHANGE_NO_EXCHANGE_COUNT_SEASON = 1907  # u'赛季兑换次数已达上限，请下季再来'
ARENA_EXCHANGE_NO_EXCHANGE_COUNT_ARENA = 1908   # u'该排名奖励已经兑换完毕，再接再厉哦。'

SHOP_BUY_NOT_OPEN = 2001                    # u'商店没有出售此商品'
SHOP_BUY_NO_BUY_COUNT = 2002                # u'商店购买次数已达上限'
SHOP_BUY_NO_BUY_COUNT_DAILY = 2003          # u'购买失败，今日已达购买上限'
SHOP_BUY_NO_BUY_COUNT_DAILY_MONEY_TREE_TIME = 2004    # u'购买失败，今日已达购买上限'

CODE_USE_CODE_INVALID = 2101                # u'该兑换码已失效'
CODE_USE_CODE_HAD_BEEN_USED = 2102          # u'该兑换码已被使用'
CODE_USE_CODE_HAD_GOT_AWARD = 2103          # u'您已经领取过此活动的奖励了'
CODE_USE_CODE_NOT_EXISTS = 2104             # u'该兑换码不存在'
CODE_GET_SP_AWARD_NONE = 2105               # u'您没有参与内测哦'
CODE_GET_SP_AWARD_DONE = 2106               # u'您已经领取过内测奖励了'
CODE_USE_CODE_INVALID_PLATFORM = 2107       # u'该兑换码只限指定渠道使用'

AWARD_GET_FAIL = 2201                       # u'不符合领奖条件'
AWARD_CAN_NOT_MAKEUP = 2202                 # u'剩余补签次数不足'
AWARD_TIME_ISNOT_UP = 2203                  # u'领奖时间未到'
AWARD_HAD_GOT = 2204                        # u'奖品已领奖，不能重复领取'
AWARD_YAO_TIME_ISNOT_UP = 2205              # 还未到领取时间呦
AWARD_YAO_HAD_GOT = 2206                    # 您已领完体力，不要太贪哦

TASK_NOT_OPEN = 2301                        # u'任务未开启'

GACHA_NOT_FREE = 2401                       # u'免费gacha时间未到'

# 联盟
LEAGUE_COIN_ERROR = 2501             # u'出价最低1钻石起'
LEAGUE_NOT_HAVE_LEAGUE = 2502        # u'当前还没有玩家建立联盟。'
LEAGUE_NOT_EXISTS = 2503             # u'该联盟不存在'
LEAGUE_NAME_EMPTY = 2504             # u'联盟名称不能为空'
LEAGUE_NAME_SENSITIVE_WORD = 2505    # u'联盟名称中有敏感词'
LEAGUE_LEVEL_NOT_ENGOUGH = 2506      # u'等级不足，无法建立联盟。'
LEAGUE_JOINED_OTHER_LEAGUE = 2509    # u'已在其他联盟中，无法建立联盟'
LEAGUE_IS_APPLYMAX = 2510            # u'最多只能申请10个联盟'
LEAGUE_IN_LEAGUE = 2511              # u'玩家已在联盟中'
LEAGUE_NOT_IN_LEAGUE = 2512          # u'您不是联盟成员'
LEAGUE_ONLY_OWNER_VC_CAN = 2513      # u'只有主席和副主席才有此权限'
LEAGUE_ONLY_OWNER_CAN = 2514         # u'只有主席才有此权限'
LEAGUE_NOT_APPLIED = 2515            # u'未申请过此联盟，不能取消联盟申请'
LEAGUE_HAD_APPLY = 2516              # u'已申请过此联盟，请耐心等待回应'
LEAGUE_APPLICANT_IN_LEAGUE = 2517    # u'申请者已在联盟中'
LEAGUE_APPLICANT_NO_APPLY = 2518     # u'对方未申请此联盟'
LEAGUE_HAD_APPLY_TO_AGREE = 2519     # u'对方已申请此联盟，快去"入盟申请"中同意吧'
LEAGUE_IS_MAXMEMBER = 2520           # u'联盟成员已达上限，快去升级吧'
LEAGUE_CANNOT_REMOVE_SUPER = 2521    # u'不能删除主席'
LEAGUE_CANNOT_RETIRE_SUPER = 2522    # u'主席不能被解职'
LEAGUE_IS_VC = 2523                  # u'此玩家之前已被任命为副主席'
LEAGUE_CANNOT_DELETE = 2524          # u'此联盟中还有其他成员，不能注销'
LEAGUE_NO_NEW_APPLY = 2525           # u'没有新玩家申请此联盟'
LEAGUE_NOT_INVITE = 2526             # u'未被邀请加入此联盟'
LEAGUE_HAVE_INVITE = 2527            # u'已邀请过此玩家，请耐心等待回应'
LEAGUE_NAME_TOO_LONG = 2528          # u'亲，联盟名长度要限制在8位内哦'
LEAGUE_NAME_REDUPLICATE = 2529       # u'亲，此名称已被占用'
LEAGUE_SLOGAN_SENSITIVE_WORD = 2531  # u'联盟口号中有敏感词'
LEAGUE_SLOGAN_TOO_LONG = 2532        # u'亲，联盟口号要限制在20位内哦'
LEAGUE_SLOGAN_SAME = 2533            # u'亲，联盟口号跟之前相同'
LEAGUE_NOTICE_SENSITIVE_WORD = 2534  # u'联盟公告中有敏感词'
LEAGUE_NOTICE_TOO_LONG = 2535        # u'亲，联盟公告要限制在52位内哦'
LEAGUE_NOTICE_SAME = 2536            # u'亲，联盟公告跟之前相同'
LEAGUE_NAME_SAME = 2537              # u'和之前名字相同，不用修改'
LEAGUE_UID_EMPTY = 2538              # 请输入玩家UID
LEAGUE_SLOGAN = 2530                 # 欢迎大家来到篮球英雄！
LEAGUE_DYNAMIC_JOIN_LEAGUE = 2539    # 玩家%(player)s加入联盟。
LEAGUE_DYNAMIC_USER_QUIT = 2540      # 玩家%(player)s退出联盟。
LEAGUE_DYNAMIC_OWNER_QUIT = 2541     # 主席%(player)s退出联盟，%(owner)s被提升为主席。
LEAGUE_DYNAMIC_APPOINT_VC = 2542     # %(player)s已被提升为副主席。
LEAGUE_DYNAMIC_REMOVE_VC = 2543      # %(player)s被解除副主席职务。
LEAGUE_DYNAMIC_USER_REMOVED = 2544   # %(player)s已被%(owner)s踢出联盟。
LEAGUE_DYNAMIC_SLOGAN = 2545         # %(player)s将联盟口号修改为：“%(slogan)s。
LEAGUE_DYNAMIC_NOTICE = 2546         # %(player)s将联盟公告修改为：“%(notice)s。
LEAGUE_DYNAMIC_NAME = 2547           # %(player)s将联盟名修改为：“%(name)s。
LEAGUE_OPP_NOT_IN_LEAGUE = 2548      # 对方不是本联盟成员
LEAGUE_CANNOT_REMOVE_MYSELF = 2549   # 不能踢出自己
LEAGUE_VC_CANNOT_REMOVE_VC = 2550    # 副主席没权限踢出其他副主席
LEAGUE_IS_MAXAPPLICATION = 2551      # 所选联盟申请人数已满
LEAGUE_IN_QUITLIMIT = 2552           # 退出联盟后24小时内不能加入和创建联盟
LEAGUE_DYNAMIC_EXP = 2553            # 玩家%(player)s提供了%(exp)s发展度。
LEAGUE_DONATE_CLOSE = 2554           # 此捐献项目尚未开启
LEAGUE_WORSHIP_LOCK = 2555           # 贡献值不足
LEAGUE_WORSHIP_CLOSE = 2556          # 膜拜大神未开启
LEAGUE_WORSHIP_USED = 2557           # 今日已膜拜完毕，请明日再来。
LEAGUE_IN_OTHER_LEAGUE = 2558        # 对方已是其他联盟成员
LEAGUE_DAILY_DONATE_TOP = 2559       # 今日捐献次数已用完，请明日再来。
LEAGUE_SHOP_LV_LOW = 2560                   # 商城等级不足，无法兑换
LEAGUE_SHOP_GOOODS_NOT_ENGOUGH = 2561       # 剩余兑换次数不足，无法兑换
LEAGUE_SHOP_DEVOTE_LOCK = 2562       # 个人贡献值不足，无法兑换
LEAGUE_EXP_NOT_ENGOUGH = 2563        # 联盟建设度不足，无法升级
LEAGUE_LV_MAX = 2564                 # 联盟大厅已是最高等级
LEAGUE_SHOP_LV_MAX = 2565            # 联盟商店已是最高等级
LEAGUE_WORSHIP_LV_MAX = 2566         # 联盟膜拜已是最高等级
LEAGUE_DYNAMIC_LV = 2567             # %(player)s将 联盟大厅 Lv%(old_lv)s 提升到 联盟大厅 Lv%(lv)s。
LEAGUE_DYNAMIC_SHOP_LV = 2568        # %(player)s将 联盟商店 Lv%(old_lv)s 提升到 联盟商店 Lv%(lv)s。
LEAGUE_DYNAMIC_DYNAMIC_LV = 2569     # %(player)s将 膜拜 Lv%(old_lv)s 提升到 膜拜 Lv%(lv)s。
LEAGUE_OTHER_OVER_LEAGUE_LV = 2570   # 联盟中其他建筑的等级，不得超过联盟大厅等级。
LEAGUE_SHOP_PLAYER_ONCE = 2571       # 每人只能兑换一次
LEAGUE_IN_JOINLIMIT = 2572           # 成员入盟12个小时内不能退出或被开除哦~
LEAGUE_UPLV = 2574                   # 联盟科技等级已达上限,无法继续升级


# gacha宝箱
GACHA_BOX_NOT_EXIST = 2601           # u'宝箱不存在'
GACHA_BOX_NUM_ERROR = 2602           # u'宝箱使用数量超出上限或下限'
GACHA_BOX_KEY_NOT_ENOUGH = 2603      # u'钥匙不足'

# active活动
ACTIVE_NOT_OPEN = 2701              # 活动未开启
ACTIVE_GOODS_SHOT = 2702            # 所需物品不足，无法兑换
LOTTERY_NOT_ENGOUGH = 2703          # u'奖券不足，抽奖可获得奖券'
ACTIVE_AWARD_TIME_NOT_OPEN = 2704   # 活动结束后才可以领奖
ACTIVE_ZSMTX_NO_TIMES = 2705        # u'活动没有次数了'
ACTIVE_LOTTERY_SHOP_NO_TIMES = 2706 # u'该物品已被兑换完毕'
ACTIVE_LUCKY_OBTAIN = 20002         # u'玩家[color=FFFF0000]%(name)s[/color]通过幸运抽奖获得[color=FFFF0000] %(num)s [/color]个[color=FFFF0000] %(loot)s [/color]！'
ACTIVE_LUXURY_OBTAIN = 20003        # u'玩家[color=FFFF0000]%(name)s[/color]通过豪华抽奖获得[color=FFFF0000] %(num)s [/color]个[color=FFFF0000] %(loot)s [/color]！'
ACTIVE_CZJJ_BUY_AGAIN = 2707        # 您已购买了成长基金，无须再买
ACTIVE_CZJJ_VIP_LEVEL_LOW = 2708    # 达到vip1即可购买成长基金
ACTIVE_CZJJ_NOT_BUY = 2709          # 购买成长基金后才可领奖
ACTIVE_IS_END = 2710                # 活动已结束

# 联赛
GAMEVS_FRESH_OPPONENT_LIMIT = 2801    # u'刷新时间未到'
GAMEVS_FIGHT_NOT_OPEN = 2802          # u'联赛休息时间, 不能比赛'
GAMEVS_SECTION_NOT_OPEN = 2803        # u'新赛季没有开启, 不能看排行哦'
GAMEVS_EXCHANGE_SECTION_LIMIT = 2804  # u'没有达到指定联赛分级'
GAMEVS_EXCHANGE_NO_EXCHANGE_COUNT = 2805    # u'限购已达上限'
GAMEVS_RATING_NOT_OPEN = 2806               # u'未在评级赛时间内'
GAMEVS_RATING_NOT_JOIN_GAMEVS = 2807        # u'没有参与联赛，请等下赛季加油'
GAMEVS_RATING_FIHGT_NO_AWARD = 2808         # u'已经领取过该奖励了'
GAMEVS_BONUSREWARD_NO_REWARD = 2809         # u'进度奖励还未达到领取条件'
GAMEVS_BONUSREWARD_HAD_REWARD = 2810        # u'进度奖励已领取过了'
# 导师特训
ITEM_MATERIAL_NOT_ENOUGH = 2901                 # 没有合适的材料，去收集一些再来吧~
CARD_TUTOR_MATERIAL_LOADED = 2904               # 此道具已配备，不能重复配备
CARD_TUTOR_MATERIAL_NOT_LOADED = 2905           # 所有道具配置完毕后才能进阶
CARD_TUTOR_MAX_NOT_LOAD = 2906                  # 导师已是最高阶，无须配备道具


#  以下为邮件内容
ARENA_TITLE = 10000                 # u'锦标赛'
ARENA_LOSE_CONTENT = 10001          # u'玩家[color=FFFF0000] %(username)s [/color]在锦标赛中对你发起了挑战，你不幸被击败。落到了第%(arena_rank)s名。'
ARENA_WIN_CONTENT = 10002           # u'玩家[color=FFFF0000] %(username)s [/color]在锦标赛中对你发起了挑战，被你无情的打败了。你在积分榜的位置稳如泰山。'

ARENA_RANK_TITLE = 10003            # u'锦标赛排名结算'
ARENA_RANK_CONTENT = 10004          # u'今天的锦标赛排名结算中，你保持在第[color=FFFF0000] %(arena_rank)s [/color]名。获得锦标赛积分%(arena_point)s点。'

ROBPATCH_TITLE = 10005              # u'装备碎片'
ROBPATCH_LOSE_CONTENT = 10006       # u'玩家[color=FFFF0000] %(username)s [/color]在锦标赛中对你的[color=FFFF] %(patch_name)s [/color]碎片图谋不轨，成功获得了该装备碎片的所有权。'
ROBPATCH_LOSE2_CONTENT = 10007      # u'玩家[color=FFFF0000] %(username)s [/color]在争夺战中对你的[color=FFFF0000] %(patch_name)s [/color]碎片图谋不轨。你虽然被击败，但是机智地将它藏好,没有被抢走。'
ROBPATCH_WIN_CONTENT = 10008        # u'玩家[color=FFFF0000] %(username)s [/color]在锦标赛中对你的[color=FFFF0000] %(patch_name)s [/color]碎片图谋不轨，但是你在对决中证明了实力，捍卫了该品牌首席明星的荣耀。'

ROBFOREIGN_TITLE = 10009            # u'外援争夺'
ROBFOREIGN_LOSE_CONTENT = 10010     # u'玩家[color=FFFF0000] %(username)s [/color]竟然对你队的外援 %(foreign_name)s 横刀夺爱。目前你的外援库中还有%(foreign_length)s名外援。'
ROBFOREIGN_WIN_CONTENT = 10011      # u'玩家[color=FFFF0000] %(username)s [/color]竟然对你队的外援 %(foreign_name)s 图谋不轨，你证明了自己的实力，该球员表示愿为强者效忠。'

FOREIGN_TITLE = 10012               # u'外援租借'
FOREIGN_EXPIRED_CONTENT = 10013     # u'你租借[color=FFFF0000] %(foreign_name)s [/color]的外援已经到期了。目前你的外援库中还有%(foreign_length)s名外援。'
FOREIGN_RENTED_CONTENT = 10014      # u'你挂牌的[color=FFFF0000] %(foreign_name)s [/color]外援被玩家[color=FFFF0000] %(username)s [/color]租借走了。请注意查收你的佣金。（点击收取）'

PVE_RANKING_TITLE = 10015               # u'联盟球票收入'
PVE_RANKING_AWARD_CONTENT = 10016       # u'你上赛季的球票收入一直没有领取，只收到了未领取球票收入的50%。（点击收取）'

RENT_CUMULATE_MONEY_TITLE = 10017       # u'外援佣金'
RENT_CUMULATE_MONEY_CONTENT = 10018     # u'你挂牌的外援[color=FFFF0000] %(foreign_name)s [/color]已经成功归队，还带回一些佣金。'

GAMEVS_CON_WIN_AWARD_TITLE = 10401      # u'联赛连胜排名'
GAMEVS_CON_WIN_AWARD_CONTENT = 10402    # u'今天的连胜纪录中，你保持在本级联赛的第[color=FFFF0000] %(arena_rank)s [/color]名，获得积分%(arena_point)s点，有点给力哦。'

GAMEVS_SECTION_AWARD_TITLE = 10019         # u'联赛排名'
GAMEVS_SECTION_AWARD_UP_CONTENT = 10020    # u'上赛季联赛中你最终位列[color=FFFF0000]分区第%(rank)s[/color]，成功晋级！以下是排名奖励，点击收取。'
GAMEVS_SECTION_AWARD_KEEP_CONTENT = 10021  # u'上赛季联赛中你最终位列[color=FFFF0000]分区第%(rank)s[/color]，再接再励！以下是排名奖励，点击收取。'
GAMEVS_SECTION_AWARD_DOWN_CONTENT = 10022  # u'上赛季联赛中您位列[color=FFFF0000]分区第%(rank)s[/color]。虽然降级了，特送上一些奖励，重整旗鼓吧！'

# 首充礼包
PAYMENT_FIRST_PAY_TITLE = 10501      # u'首充礼包'
PAYMENT_FIRST_PAY_CONTENT = 10502    # u'您的首充礼包已经发送到位，请点击领取。'
# VIP礼包限购解锁
VIP_LEVELUP_TITLE = 10503            # VIP礼包限购解锁
VIP_LEVELUP_CONTENT = 10504          # 恭喜您提升到VIP%(viplv)s，已经解锁了新的VIP礼包购买权限，请在商城-礼包中浏览。

# 联盟
LEAGUE_AGREE_TITLE = 10601                  # 联盟消息
LEAGUE_AGREE_CONTENT = 10602                # 恭喜你，%(name)s接受了您的联盟申请！
LEAGUE_REFUSE_TITLE = 10603                 # 联盟消息
LEAGUE_REFUSE_CONTENT = 10604               # 很遗憾，%(name)s拒绝了您的联盟申请！
LEAGUE_USER_REFUSE_TITLE = 10605            # 联盟消息
LEAGUE_USER_REFUSE_CONTENT = 10606          # 玩家%(name)s拒绝了你的邀请
LEAGUE_DISSOLVE_TITLE = 10607               # 联盟消息
LEAGUE_DISSOLVE_CONTENT = 10608             # %(name)s联盟已解散！
LEAGUE_REMOVE_MEMBER_TITLE = 10609          # 联盟消息
LEAGUE_REMOVE_MEMBER_CONTENT = 10610        # 你已被%(username)s踢出%(league_name)s
LEAGUE_USER_ACCEPT_TITLE = 10611            # 联盟消息
LEAGUE_USER_ACCEPT_CONTENT = 10612          # 玩家%(name)s接受了你的邀请


# 48小时后首次登录奖励
USER_LOGIN_AWARD_TITLE = 10701      # 回归奖励
USER_LOGIN_AWARD_CONTENT = 10702    # 您终于回来了，200钻石送上。
# 补发active活动中未领取的奖品
ACTIVE_UNCLAIMED_GIFT_TITLE = 10703      # 未领取活动奖励
ACTIVE_UNCLAIMED_GIFT_CONTENT = 10704    # 您今天的活动奖励没有领取哦，特为您奉上未领取的奖励。下次不要忘记啦


#个人等级排行
LEVEL_RANK_TITLE = 10801               # 个人等级排行奖励
LEVEL_RANK_CONTENT = 10802              # 恭喜您在个人等级排行活动中获得奖励！以下是您的奖励，请您及时领取。祝您游戏愉快。
#个人实力排行
ABILITY_RANK_TITLE = 10803               # 个人实力排行
ABILITY_RANK_CONTENT = 10804            # 恭喜您在个人实力排行活动中获得奖励！以下是您的奖励，请您及时领取。祝您游戏愉快
#联盟排行
LEAGUE_RANK_TITLE = 10805                # 联盟排行奖励
LEAGUE_RANK_CONTENT = 10806              # 恭喜您在联盟排行活动中获得奖励！以下是您的奖励，请您及时领取。祝您游戏愉快


# 发送消息到世界频道
GAMEVS_CON_WIN_NO1_MSG_SID_1 = 10201    # u'玩家[color=FFFF0000] %(username)s [/color]在SS级联赛中取得了%(wins_rank)s连胜，势不可挡，谁来阻止他！'
GAMEVS_CON_WIN_NO1_MSG_SID_2 = 10202
GAMEVS_CON_WIN_NO1_MSG_SID_3 = 10203
GAMEVS_CON_WIN_NO1_MSG_SID_4 = 10204
GAMEVS_CON_WIN_NO1_MSG_SID_5 = 10205
GAMEVS_CON_WIN_NO1_MSG_SID_6 = 10206
GAMEVS_CON_WIN_NO1_MSG_SID_7 = 10207
GAMEVS_CON_WIN_NO2_MSG_SID_1 = 10301    # 玩家[color=FFFF0000] %(username)s [/color]在B级联赛迎头赶上，打破了[color=FFFF0000] %(username2)s [/color]的垄断！
GAMEVS_CON_WIN_NO2_MSG_SID_2 = 10302
GAMEVS_CON_WIN_NO2_MSG_SID_3 = 10303
GAMEVS_CON_WIN_NO2_MSG_SID_4 = 10304
GAMEVS_CON_WIN_NO2_MSG_SID_5 = 10305
GAMEVS_CON_WIN_NO2_MSG_SID_6 = 10306
GAMEVS_CON_WIN_NO2_MSG_SID_7 = 10307

# 钻石满天星活动动态文本
ACTIVE_ZSMTX_DYNAMIC_CONTENT = 20001    # [color=FFFF0000]%(name)s[/color]玩家拼手气获得[color=FFFF0000] %(diamond)s [/color]钻石！
# 全民转盘活动动态文本
ACTIVE_QMZP_LOG_CONTENT = 20004      #   # 获得：[color=FFFF0000] %(loot)s [/color]   时间：[color=FFFF0000] %(time)s [/color]
LOOT_NAME_MONEY = 5
LOOT_NAME_HONOR = 6
LOOT_NAME_POINT = 7
LOOT_NAME_GRADE = 11
LOOT_NAME_COIN = 100
LOOT_NAME_LOTTERY = 500
LOOT_NAME_LUCKY = 100000


# 推送的一些内容
PUSH_NOTIFICATION_CELEYAO_LUNCH = 400001    # u'Yao餐厅午饭开马上开始了哦，赶紧来吃吧！'
PUSH_NOTIFICATION_CELEYAO_DINNER = 400002   # u'Yao餐厅晚饭开马上开始了哦，赶紧来吃吧！'
PUSH_NOTIFICATION_PVE_RANKING = 400003      # u'本赛季的战绩排名马上出炉了，赶快领取球票分红吧。'

