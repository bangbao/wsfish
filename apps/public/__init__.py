# coding: utf-8

import os
import re
import copy

import settings
from lib.utils import hexie
from lib.utils import weight_choice
from apps.config import game_config
from apps import loot as loot_app
from . import celebration
from . import text
from . import consts
from . import xxtea


SERVER_ID_RE_COMPILE = re.compile(r'(?P<server_id>\d+)$')
PLATFORM_ID_RE_COMPILE = re.compile(r'(?P<platform_id>[a-z]+)(?:\d*)$')


def get_server_by_uid(user_id):
    """从游戏uid解析出server_id
    """
    s = SERVER_ID_RE_COMPILE.search(user_id[:-6])
    if s:
        server_id = s.group('server_id')
        return server_id
        #if server_id in game_config.servers:
        #    return server_id

    return '00'


def get_platform_by_uid(user_id):
    """从游戏uid解析出platform_id
    """
    s = PLATFORM_ID_RE_COMPILE.search(user_id[:-6])
    if s:
        platform_id = s.group('platform_id')
        return platform_id
        #if server_id in game_config.servers:
        #    return server_id


def is_npc(user_id):
    """判断是否是npc
    """
    return user_id.startswith(consts.NPC_UID_PREFIX)


def delimiter_list(value, func=None, delimiter=','):
    """转换字符串到列表
    Args:
        value:  逗号分隔的字符串
        func: 转换函数
        delimiter: 分割符
    Returns:
        转换后的列表
    """
    temp = value.split(delimiter)
    if func is not None:
        return map(func, temp)
    return temp


def delimiter_str(value, func=str, delimiter=','):
    """转换列表到字符串
    Args:
        value: 列表
        func: str
        delimiter: 分割符
    Returns:
        转换后的字符串
    """
    temp = map(str, value)
    return delimiter.join(temp)


def get_season(server_id):
    """获取游戏当前所在赛季
    Args:
        server: 分服id
    Returns:
        当前所在赛季
    """
    return celebration.get_season(server_id)


def get_gamevs_season(server_id):
    """获取联赛所在当前所在赛季
    Args:
        server: 分服id
    Returns:
        当前所在赛季
    """
    return celebration.get_gamevs_season(server_id)


def _check_sensitive_word():
    """检查昵称中是否有敏感词
    """
    words = game_config.text_hexie.get('name', [])
    if words:
        pof = text.PoFilter()
        pof.init(words)
        is_hexie = pof.check
    else:
        is_hexie = hexie.is_hexie
    return is_hexie

check_sensitive_word = _check_sensitive_word()


def format_loot(user, loot_id, double_sort=None, stage=None):
    """格式化loot配置统一处理
    loot配置中每一行只选一个{'loot': [[1,0,2, 1000],[2,1,1, 3000]]}
    Args:
        loot_id: loot配置ID
        game_config: 游戏配置
        double_sort: loot_double配置中的object_sort值
        stage: 关卡或章节ID
    Returns:
        用户加物品统一格式数据 [[1,0,2, 1000]]
    """
    loot_detail = game_config.loot[loot_id]

    user_loot_key = 'user_loot%d' % user.user_m.leader
    user_loot = loot_detail.get(user_loot_key) or loot_detail['loot']

    award = weight_choice(user_loot)
    goods = loot_app.replace_one_award(user, award, game_config.loot_server)

    if not double_sort:
        new_goods = copy.deepcopy([goods])
        return new_goods

    # 双倍掉落
    award = loot_app.loot_double_handle(user, goods, double_sort, stage)
    new_goods = copy.deepcopy([award])
    return new_goods


def trans_goods_list2dict(goods_list):
    """转换列表数据到字典
    Args:
        goods_list: loot配置里的掉落列表
    Returns:
        goods_data: 字典格式的数据
    """
    goods_data = {}

    for goods in goods_list:
        if not goods:
            continue
        goods_type = goods[0]   # 种类
        goods_type_name = consts.GOODS_TYPE_NAME_MAP[goods_type]

        if goods_type_name in consts.GOODS_NAME_INT_KEYS:
            goods_data.setdefault(goods_type_name, 0)
            goods_data[goods_type_name] += goods[2]
        elif goods_type_name == 'card':
            goods_data.setdefault('card', [])
            goods_data['card'].append((goods[1], goods[2], goods[3]))
        else:
            goods_data.setdefault(goods_type_name, [])
            goods_data[goods_type_name].append((goods[1], goods[2]))

    return goods_data


def format_loot_name_show_text(goods, symbol='x'):
    """格式化物品名称显示
    Args:
        goods: 物品loot格式配置
        symbol: 连接符号
    Returns:
        物品名x数量
    """
    goods_type = goods[0]
    goods_type_name = consts.GOODS_TYPE_NAME_MAP[goods_type]
    if goods_type_name in consts.GOODS_NAME_INT_KEYS:
        name = game_config.text_warning.get(goods_type, '')
        num = goods[2]
    elif goods_type == consts.GOODS_TYPE_CARD:
        cfg_id, num = goods[1], goods[3]
        name = game_config.player_detail[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_EQUIP:
        cfg_id, num = goods[1], goods[2]
        name = game_config.equip_detail[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_PATCH:
        cfg_id, num = goods[1], goods[2]
        name = game_config.robpatch[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_ITEM:
        cfg_id, num = goods[1], goods[2]
        name = game_config.item[cfg_id]['itemname']
    elif goods_type == consts.GOODS_TYPE_PATCHPLAYER:
        cfg_id, num = goods[1], goods[2]
        name = game_config.patchplayer[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_TREASURE:
        cfg_id, num = goods[1], goods[2]
        name = game_config.treasure[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_PATCHEQUIP:
        cfg_id, num = goods[1], goods[2]
        name = game_config.patchequip[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_GACHA_BOX:
        cfg_id, num = goods[1], goods[2]
        name = game_config.gacha_box[cfg_id]['name']
    elif goods_type == consts.GOODS_TYPE_PATCHITEM:
        cfg_id, num = goods[1], goods[2]
        name = game_config.patchitem[cfg_id]['name']
    else:
        name, num = goods_type, goods[2]

    return '%s%s%s' % (name, symbol, num)


def xxtea_encrypt(data, key=None):
    """用xxtea加密数据
    """
    key = key or settings.XXTEA_SIGNATURE_KEY

    return xxtea.encrypt(data, key, returnhex=True)


def xxtea_decrypt(data, key=None):
    """用xxtea解密数据
    """
    key = key or settings.XXTEA_SIGNATURE_KEY

    return xxtea.decrypt(data, key, ishex=True)


if __name__ == '__main__':
    for name in game_config.text_hexie['name']:
        print name, check_sensitive_word(name)


