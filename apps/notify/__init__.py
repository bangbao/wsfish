# coding: utf-8

import datetime

import settings
from apps.config import game_config
from apps.public import celebration as pub_celebration
from apps.public import consts as pub_consts
from . import consts


def get_notifies(user):
    """获取消息列表数据
    """
    messages = []
    battlelogs = []
    battlelog_sorts = set([user.NOTIFY_FROM_ARENA, user.NOTIFY_FROM_ROBPATCH,
                           user.NOTIFY_FROM_ROBFOREIGN])
    # 自动添加系统通知
    user.notify.add_message_by_system()

    for obj in sorted(user.notify.messages.itervalues(), key=lambda x:x['ts'], reverse=True):
        if obj['sort'] in battlelog_sorts:
            battlelogs.append(obj)
        else:
            messages.append(obj)
    return messages, battlelogs


def read_message(user, message_id):
    """读取消息
    """
    data = {}
    message = user.notify.messages.get(message_id)
    if message:
        # 有奖励且没有读取过
        if message['gift'] and not message['read']:
            data = user.add_gift(message['gift'], where=user.GOODS_FORM_NOTIFY)
        # 标记已读标识
        user.notify.mark_read([message_id])
        # 有奖励的领取完直接删除
        if message['gift']:
            user.notify.del_message([message_id])

    return data


def has_unread_notify(user):
    """是否有未读的消息
    """
    # 模块没变化时不判断小红点
    #if not hasattr(user, 'notify'):
    #    return 0

    # 自动添加系统通知
    user.notify.add_message_by_system()

    for obj in user.notify.messages.itervalues():
        if not obj['read']:
            return 1
    return 0


def get_notify_content(text_id, fmt=None):
    """获取配置中内容
    Args:
        text_id: text索引
        fmt: 要格式化的数据，为None表示不需要格式化
    Returns:
        配置文本
    """
    content = game_config.text_warning.get(text_id, text_id)
    if fmt:
        content = content % fmt

    return content


def notify_by_sort1(user, kwargs):
    """锦标赛对你的挑战
    """
    title = consts.ARENA_TITLE
    if kwargs['is_win']:
        content = get_notify_content(consts.ARENA_WIN_CONTENT, kwargs)
    else:
        content = get_notify_content(consts.ARENA_LOSE_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_ARENA, title, content, **kwargs)


def notify_by_sort2(user, kwargs):
    """装备碎片抢夺
    """
    title = get_notify_content(consts.ROBPATCH_TITLE)
    if kwargs['is_win']:
        content = get_notify_content(consts.ROBPATCH_WIN_CONTENT, kwargs)
    elif kwargs['lose_patch']:
        content = get_notify_content(consts.ROBPATCH_LOSE_CONTENT, kwargs)
    else:
        content = get_notify_content(consts.ROBPATCH_LOSE2_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_ROBPATCH, title, content, **kwargs)


def notify_by_sort3(user, kwargs):
    """租借的外援被抢夺
    """
    title = get_notify_content(consts.ROBFOREIGN_TITLE)
    if kwargs['is_win']:
        content = get_notify_content(consts.ROBFOREIGN_WIN_CONTENT, kwargs)
    else:
        content = get_notify_content(consts.ROBFOREIGN_LOSE_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_ROBFOREIGN, title, content, **kwargs)


def notify_by_sort4(user, kwargs):
    """租借的外援到期了
    """
    title = get_notify_content(consts.FOREIGN_TITLE)
    content = get_notify_content(consts.FOREIGN_EXPIRED_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_FOREIGN_EXPIRED, title, content, **kwargs)


def notify_by_sort5(user, kwargs):
    """出租的外援被租用了
    """
    title = get_notify_content(consts.FOREIGN_TITLE)
    content = get_notify_content(consts.FOREIGN_RENTED_CONTENT, kwargs)
    gift = [[pub_consts.GOODS_TYPE_MONEY, 0, kwargs['money']]]

    user.notify.add_message(user.NOTIFY_FROM_FOREIGN_RENTED, title, content, gift, **kwargs)


def notify_by_sort6(user, kwargs):
    """排名赛的收入
    """
    title = get_notify_content(consts.PVE_RANKING_TITLE)
    content = get_notify_content(consts.PVE_RANKING_AWARD_CONTENT, kwargs)
    gift = kwargs['gift']

    user.notify.add_message(user.NOTIFY_FROM_PVE_RANKING, title, content, gift, **kwargs)


def notify_by_sort7(user, kwargs):
    """arena的排名结算
    """
    title = get_notify_content(consts.ARENA_RANK_TITLE)
    content = get_notify_content(consts.ARENA_RANK_CONTENT, kwargs)
    gift = kwargs['gift']

    user.notify.add_message(user.NOTIFY_FROM_ARENA_RANK, title, content, gift, **kwargs)


def notify_by_sort8(user, kwargs):
    """球员租借的累积收益结算
    """
    title = get_notify_content(consts.RENT_CUMULATE_MONEY_TITLE)
    content = get_notify_content(consts.RENT_CUMULATE_MONEY_CONTENT, kwargs)
    gift = [[pub_consts.GOODS_TYPE_MONEY, 0, kwargs['cumulate_money']]]

    user.notify.add_message(user.NOTIFY_FROM_RECYCLE_RENT, title, content, gift, **kwargs)


def notify_by_sort9(user, kwargs):
    """联赛连胜排名奖励
    """
    title = get_notify_content(consts.GAMEVS_CON_WIN_AWARD_TITLE)
    content = get_notify_content(consts.GAMEVS_CON_WIN_AWARD_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_GAMEVS_CON_WIN, title, content, gift, **kwargs)


def notify_by_sort10(user, kwargs):
    """联赛连胜排名奖励
    """
    advance = kwargs['advance']
    gift = kwargs.pop('gift', None)
    title = get_notify_content(consts.GAMEVS_SECTION_AWARD_TITLE)
    if advance == -1:
        content = get_notify_content(consts.GAMEVS_SECTION_AWARD_DOWN_CONTENT, kwargs)
    elif advance == 1:
        content = get_notify_content(consts.GAMEVS_SECTION_AWARD_UP_CONTENT, kwargs)
    else:
        content = get_notify_content(consts.GAMEVS_SECTION_AWARD_KEEP_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_GAMEVS_SECTION, title, content, gift, **kwargs)


def notify_by_sort11(user, kwargs):
    """首充礼包
    """
    title = get_notify_content(consts.PAYMENT_FIRST_PAY_TITLE)
    content = get_notify_content(consts.PAYMENT_FIRST_PAY_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_FIRST_PAY, title, content, gift, **kwargs)


def notify_by_sort12(user, kwargs):
    """VIP礼包限购解锁
    """
    viplv = kwargs['viplv']
    title = get_notify_content(consts.VIP_LEVELUP_TITLE)
    content = get_notify_content(consts.VIP_LEVELUP_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_VIP_LEVELUP, title, content)


def notify_by_sort13(user, kwargs):
    """联盟申请的回复
    """
    result = kwargs['result']
    title = content = u''

    if result == 'league_agree':
        title = get_notify_content(consts.LEAGUE_AGREE_TITLE)
        content = get_notify_content(consts.LEAGUE_AGREE_CONTENT, kwargs)
    elif result == 'league_refuse':
        title = get_notify_content(consts.LEAGUE_REFUSE_TITLE)
        content = get_notify_content(consts.LEAGUE_REFUSE_CONTENT, kwargs)
    elif result == 'user_accept':
        title = get_notify_content(consts.LEAGUE_USER_ACCEPT_TITLE)
        content = get_notify_content(consts.LEAGUE_USER_ACCEPT_CONTENT, kwargs)
    elif result == 'user_refuse':
        title = get_notify_content(consts.LEAGUE_USER_REFUSE_TITLE)
        content = get_notify_content(consts.LEAGUE_USER_REFUSE_CONTENT, kwargs)
    elif result == 'league_dissolve':
        title = get_notify_content(consts.LEAGUE_DISSOLVE_TITLE)
        content = get_notify_content(consts.LEAGUE_DISSOLVE_CONTENT, kwargs)
    elif result == 'player_removed':
        title = get_notify_content(consts.LEAGUE_REMOVE_MEMBER_TITLE)
        content = get_notify_content(consts.LEAGUE_REMOVE_MEMBER_CONTENT, kwargs)

    user.notify.add_message(user.NOTIFY_FROM_LEAGUE, title, content)


def notify_by_sort14(user, kwargs):
    """48小时后首次登录奖励
    """
    title = get_notify_content(consts.USER_LOGIN_AWARD_TITLE)
    content = get_notify_content(consts.USER_LOGIN_AWARD_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_PUSH_AWARD, title, content, gift)


def notify_by_sort16(user, kwargs):
    """邮件补发active活动中未领取的奖品
    """
    title = get_notify_content(consts.ACTIVE_UNCLAIMED_GIFT_TITLE)
    content = get_notify_content(consts.ACTIVE_UNCLAIMED_GIFT_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_PUSH_AWARD, title, content, gift)


def notify_by_sort17(user, kwargs):
    """等级排行榜定时发奖品
    """
    title = get_notify_content(consts.LEVEL_RANK_TITLE)
    content = get_notify_content(consts.LEVEL_RANK_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_LEVELRANK, title, content, gift)


def notify_by_sort18(user, kwargs):
    """实力排行榜定时发奖品
    """
    title = get_notify_content(consts.ABILITY_RANK_TITLE)
    content = get_notify_content(consts.ABILITY_RANK_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_ABILITYRANK, title, content, gift)


def notify_by_sort19(user, kwargs):
    """联盟排行榜定时发奖品
    """
    title = get_notify_content(consts.LEAGUE_RANK_TITLE )
    content = get_notify_content(consts.LEAGUE_RANK_CONTENT, kwargs)
    gift = kwargs.pop('gift', None)

    user.notify.add_message(user.NOTIFY_FROM_LEAGUERANK, title, content, gift)


def notify_by_sort20(user, kwargs):
    """活动限时巨星发奖品
    """
    tp = kwargs['tp']
    config = kwargs['config']

    if tp == 'rank':
        title = config['text2']
        content = config['text1'] % {'rank': kwargs['rank']}
        gift = config['reward']
    else:
        title = config['text2']
        content = config['text1']
        gift = config['reward']

    user.notify.add_message(user.NOTIFY_FROM_ACTIVE_XSJX, title, content, gift)


def push_notification_celeyao():
    """姚餐厅时间开始，提前1分钟
    """
    from apps.platform import jpush

    if not settings.PUSH_NOTIFICATION:
        print 'settings.PUSH_NOTIFICATION is empty'
        return

    now = datetime.datetime.now()
    if now.hour <= 14:
        content = get_notify_content(consts.PUSH_NOTIFICATION_CELEYAO_LUNCH)
    else:
        content = get_notify_content(consts.PUSH_NOTIFICATION_CELEYAO_DINNER)

    # 有效1.5小时
    time_to_live = 1.5 * 3600
    result = jpush.send_notification(content, audience='all', time_to_live=time_to_live)
    if result:
        print 'push_notification_celeyao succes'
    else:
        print 'push_notification_celeyao failure'


def push_notification_pve_ranking():
    """PvE好友排行结算排名结算时间到了的前1小时
    """
    from apps.platform import jpush

    if not settings.PUSH_NOTIFICATION:
        print 'settings.PUSH_NOTIFICATION is empty'
        return

    tag = []
    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d %H:%M:%S')
    for server_id, obj in game_config.yield_open_servers():
        if obj['open_time'] < today:
            season_conf = pub_celebration.get_season_conf(server_id)
            stime, etime = pub_celebration.get_activity_datetime(season_conf['cid'], now)
            # 只在最后一天才发推送
            if now.date() == etime.date():
                tag.append(server_id)

    if not tag:
        print 'push_notification_pve_ranking failure: no server tag'
        return

    content = get_notify_content(consts.PUSH_NOTIFICATION_CELEYAO_LUNCH)
    # 有效1小时
    time_to_live = 3500
    # TODO不支持tag, 所以暂时全部发
    tag = None
    result = jpush.send_notification(content, tag=tag, time_to_live=time_to_live)
    if result:
        print 'push_notification_pve_ranking success: %s' % tag
    else:
        print 'push_notification_pve_ranking failure: %s' % tag

