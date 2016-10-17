# coding: utf-8

import time

from lib.db import ModelBase
from lib.utils.generator import timestamp_to_str62, salt_generator
from apps.config import game_config

MESSAGES_LEN = 40
KEEP_SECONDS = 7 * 24 * 3600


class Notify(ModelBase):
    """ 各种邮件通知
    """
    def __init__(self, uid=None):
        """
        mail = {
                'title': 消息标题,
                'content': 消息主体,
                'sort': 类型,
                'gift': 奖励列表数据,
                'read': 是否已读,
                'ts': 时间戳,
                'id': _id,
                'uid': 触发人的uid,
                'level': 触发人的level,
                'username': 触发人的username,
                'logo': 触发人的logo, 0表示没有触发人,
        }
        """
        self.uid = uid
        self._attrs = {
               'messages': {},    # 各种信息
               '_systems': {},    # 系统消息记录
        }
        super(Notify, self).__init__(uid)

    def pre_use(self):
        self.auto_delete_expired_message()

    def add_message_by_system(self):
        """把系统消息自动放置在用户身上
        """
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        user_uid = self.uid
        user_level = self.weak_user.user_m.level
        platform_id = self.weak_user.user_m.platform
        server_id = self.weak_user.server_id
        sort = self.weak_user.NOTIFY_FROM_SYS

        for sid, obj in game_config.system_notify.iteritems():
            if sid not in self._systems and \
                    obj['open'] <= now <= obj['close'] and \
                    obj['levels'][0] <= user_level <= obj['levels'][1] and \
                    (not obj['platforms'] or platform_id in obj['platforms']) and \
                    (not obj['servers'] or server_id in obj['servers']) and \
                    (not obj['uids'] or user_uid in obj['uids']):
                self._systems[sid] = now
                self.add_message(sort, obj['title'], obj['content'], obj['gift'])

    def auto_delete_expired_message(self):
        """自动删除过期的消息
        """
        if 1: #len(self.messages) > MESSAGES_LEN:
            delete_id_list = []
            now = time.time()
            d = sorted(self.messages.iteritems(), key=lambda x:x[1]['ts'], reverse=True)
            for idx, (mid, obj) in enumerate(d):
                # 有奖励的消息读取完直接删除
                if obj['gift']:
                    if obj['read']:
                        delete_id_list.append(mid)
                # 超过7天直接删除
                elif now - obj['ts'] >= KEEP_SECONDS:
                    delete_id_list.append(mid)
                # 超过长度直接删除
                elif idx >= MESSAGES_LEN and obj['read']:
                    delete_id_list.append(mid)

            if delete_id_list:
                self.del_message(delete_id_list)

    def add_message(self, sort, _title, _content, _gift=None, **kwargs):
        """添加消息
        """
        self.changed = True
        # 生成id, 若传时间，伪装下发送的时间
        ts = kwargs.get('ts', int(time.time()))
        id_list = [timestamp_to_str62(ts), salt_generator(), sort]
        gift = _gift or []
        for one_gift in gift[:3]:
            id_list.extend(one_gift)
        _id = '_'.join(str(m) for m in id_list)

        self.messages[_id] = {
                'title': _title,
                'content': _content,
                'sort': sort,
                'gift': gift,
                'read': False,
                'ts': ts,
                'id': _id,
                'uid': kwargs.get('uid', ''),
                'level': kwargs.get('level', 1),
                'username': kwargs.get('username', ''),
                'logo': kwargs.get('logo', 0),
            }

    def del_message(self, message_id_list=None, message_id_all=False):
        """删除消息
        Args:
            message_id_list: 消息ID列表
            message_id_all: 是否删除全部
        """
        self.changed = True
        if message_id_all:
            self.messages.clear()
        elif message_id_list is not None:
            for _id in message_id_list:
                self.messages.pop(_id, None)

    def mark_read(self, message_id_list):
        """标记是否已读取状态
        """
        self.changed = True
        for _id in message_id_list:
            self.messages[_id]['read'] = True

