# -*- coding: utf-8 -*-
'''
Created on 2014-7-10

@author: Administrator
'''

'''
def module_funcname(env, args, returns):
    """# module_funcname: module中的funcname接口的统计方法, 此函数命名规则：views中模块名_函数名
                            比如views.cards.open的统计方法命名为：cards_open
    args:
        env:
        args: 请求参数
        returns: 比如views层函数处理后的result_data,
    returns:
        data:     需要记录的结果
    """
    data={}
    return data

'''

def gacha_player_gacha(env, args, returns):
    return {'loot': returns.get('loot', ''),
            '__gacha_sort': returns.get('__gacha_sort', ''),
            '__gacha_sort_pre': returns.get('__gacha_sort_pre', ''),}

