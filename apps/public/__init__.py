# coding: utf-8

import os
import re
import copy

import settings
from lib.utils import weight_choice
from apps.config import game_config
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


def _check_sensitive_word():
    """检查昵称中是否有敏感词
    """
    words = []
    pof = text.PoFilter()
    pof.init(words)
    is_hexie = pof.check
    return is_hexie

check_sensitive_word = _check_sensitive_word()



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


