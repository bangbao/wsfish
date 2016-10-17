# coding: utf-8

import datetime


def merge_dict_value2list(a_dict, b_dict):
    """合并两个字典， value组成list
    Args:
        a_dict: 字典a
        b_dict: 字典b
    Returns:
        合并后的字典
    """
    new_dict = {}

    for k, v in a_dict.iteritems():
        new_dict[k] = (v, b_dict[k])

    return new_dict


def get_server_bulletin(server_id, game_config):
    """获取此分服的公告
    Args:
        server_id: 分服标识
        game_config: 游戏配置
    Returns:
        该分服的公告
    """
    from apps.public import celebration as pub_celebration

    bulletins = []
    server_data = game_config.servers[server_id]
    server_id_int = int(server_id)
    s_open_time = server_data['open_time']
    open_time = datetime.datetime.strptime(s_open_time, '%Y-%m-%d %H:%M:%S')

    for _, obj in sorted(game_config.bulletin.iteritems()):
        if not obj['server'] or -1 in obj['server'] or server_id_int in obj['server']:
            if obj['text'] and \
                    (obj.get('cycle_detail', None) is None or pub_celebration.get_activity_status(obj, s_open_time)):
                day1 = open_time + datetime.timedelta(days=obj['day1'])
                day2 = open_time + datetime.timedelta(days=obj['day2'])
                new_text = obj['text'] % {'day1': day1.strftime('%Y.%m.%d'), 'day2': day2.strftime('%Y.%m.%d')}
                bulletins.append({'title': obj['title'], 'text': new_text})

    return bulletins


def get_levelup_exp(old_lv, new_lv, game_config):
    """获取升级所需要的经验
    Args:
        old_lv: 低等级
        new_lv: 高等级
        game_config: 游戏配置
    Returns:
        获取升级所需要的经验
    """
    return sum(game_config.user_info[lv]['exp'] for lv in xrange(old_lv, new_lv))

