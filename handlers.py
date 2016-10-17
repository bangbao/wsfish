# coding: utf-8

import tornado.ioloop
from tornado.websocket import WebSocketHandler


CONNECTION_STATUS_CLOSED = 0
CONNECTION_STATUS_CONNECTED = 1
CONNECTION_STATUS_AUTHING = 2
CONNECTION_STATUS_AUTHED = 3


class WSBaseHandler(WebSocketHandler):
    PING_INTERVAL = 5

    def __init__(self, application, request, **kwargs):
        WebSocketHandler.__init__(self, application, request, **kwargs)
        self.ping_timer = None
        self.io_loop = tornado.ioloop.IOLoop.instance()

    def open(self, *args, **kwargs):
        WebSocketHandler.open(self, *args, **kwargs)
        self.stream.set_nodelay(True)
        self.reset_ping_timer()

    def on_message(self, message):
        self.reset_ping_timer()

    def on_close(self, *args, **kwargs):
        WebSocketHandler.on_close(self, *args, **kwargs)
        self.clear_ping_timer()

    def write_message(self, message, binary=False):
        WebSocketHandler.write_message(self, message, binary=binary)
        self.reset_ping_timer()

    def clear_ping_timer(self):
        if self.ping_timer:
            self.io_loop.remove_timeout(self.ping_timer)

    def reset_ping_timer(self):
        self.clear_ping_timer()
        self.ping_timer = self.io_loop.call_later(self.PING_INTERVAL,
                                                  self.do_ping)

    def do_ping(self):
        self.ping('KL')
        self.ping_timer = None
        self.reset_ping_timer()

    def on_ping(self):
        pass

    def check_origin(self, origin):
        return True


class WSHandler(WSBaseHandler):
    CLIENTS = {}

    def __init__(self, application, request, **kwargs):
        WSBaseHandler.__init__(self, application, request, **kwargs)
        self.conn_status = CONNECTION_STATUS_CLOSED
        self.uid = None

    def open(self, *args, **kwargs):
        WSBaseHandler.open(self, *args, **kwargs)
        self.conn_status = CONNECTION_STATUS_CONNECTED

    def on_message(self, message):
        WSBaseHandler.on_message(self, message)
        if self.conn_status == CONNECTION_STATUS_CLOSED:
            # 连接已关闭， 不处理任何信息
            return
        elif self.conn_status == CONNECTION_STATUS_AUTHING:
            # 还在验证中， 不接收消息，否则直接关闭
            self.close()
            return

        elif self.conn_status == CONNECTION_STATUS_CONNECTED:
            # 收到的第一个包一定是验证请求
            self.application.push_auth_thread(self, message)
            self.conn_status = CONNECTION_STATUS_AUTHING
            return
        elif self.conn_status == CONNECTION_STATUS_AUTHED:
            # 推送到处理线程
            self.application.push_user_message(self, message)
            return
        else:
            print 'unknown conn_status=%s' % self.conn_status
            self.close()

    def on_close(self, *args, **kwargs):
        WSBaseHandler.on_close(self, *args, **kwargs)
        self.conn_status = CONNECTION_STATUS_CLOSED
        CLIENTS = WSHandler.CLIENTS
        if self.uid in CLIENTS:
            del CLIENTS[self.uid]
            self.application.push_user_login(self.uid, False)

    def on_auth_finished(self, auth_result, errno=0, errmsg=None):
        """验证结果
        """
        if auth_result is None:
            print 'auth failed, errno=%s, errmsg=%s' % (errno, errmsg)
            self.send_error(errno, errmsg)
            self.close()
            return

        self.uid = auth_result['uid']
        CLIENTS = WSHandler.CLIENTS
        if self.uid in CLIENTS:
            print 'duplicated login, uid=%s' % self.uid
            self.close()
            return

        CLIENTS[self.uid] = self
        self.conn_status = CONNECTION_STATUS_AUTHED
        self.send_response(auth_result)
        self.application.push_user_login(self.uid, True)

    def send_response(self, message, errno=0, errmsg=None):
        message['errno'] = errno
        pbdata = dict(response=message)
        self.write_message(pbdata, True)

    def send_request(self, message):
        pbdata = dict(request=message)
        self.write_message(pbdata, binary=True)

    def send_error(self, errno, errmsg):
        pbdata = dict(errno=errno, errmsg=errmsg)
        self.write_message(pbdata, binary=True)

    @staticmethod
    def send_message(message, uids=None):
        """发送消息
        """
        CLIENTS = WSHandler.CLIENTS
        if not message:
            return

        if not uids:
            for handler in CLIENTS.itervalues():
                handler.write_message(message)
        else:
            for uid in uids:
                if uid in CLIENTS:
                    handler = CLIENTS[uid]
                    handler.write_message(message)



class AdminHandler(tornado.web.RequestHandler):
    """ 后台统一 Handler
    全部后台处理公共接口
    """
    def initialize(self):
        """ 初始化操作
        创建全局环境和运行环境
        """
        self.logger = None

    def get_current_user(self, *args):
        """获取当前登陆用户对象
        """
        return admin_app.auth.get_admin_by_request(self)

    def render_to_response(self):
        """ 渲染模板
        """
        template_data = gate.admin_response(self.env)
        if isinstance(template_data, basestring):
            # 若返回字符串，标识报错了。直接写出错误
            self.write(template_data)
            self.set_header('Content-Type', 'text/plain')
        elif template_data and template_data[0]:
            self.render(template_data[0], **template_data[1])

    @tornado.web.addslash
    def get(self):
        """ 处理GET请求
        """
        self.render_to_response()

    @tornado.web.addslash
    def post(self):
        """ 处理POST请求
        """
        self.render_to_response()

