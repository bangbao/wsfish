# coding: utf-8

from tornado.websocket import websocket_connect


class BaseWSClient(object):
    def __init__(self, url):
        self.url = url
        self.wsConn = None
        self.uid = None
        self.send_num = 0

    def do_connect(self):
        websocket_connect(self.url, callback=self.on_wsconnected)

    def dispose(self):
        pass

    def _close(self):
        if self.wsConn is not None:
            self.wsConn.close()
            self.wsConn = None
            self.dispose()

    def on_connect(self):
        print 'server connected'

    def on_connect_fail(self):
        pass

    def on_connect_broken(self):
        pass

    def send_request(self, dic, reqDomain='fightRequest'):
        self.send_num += 1
        try:
            d = {}
            d[reqDomain] = dic
            d['serial'] = self.send_num
            pbstr = d
            self.wsConn.write_message(pbstr, binary=True)
        except Exception as e:
            print e

    def on_wsconnected(self, connection):
        try:
            wsConn = connection.result()
            self.wsConn = wsConn
            self.wsConn.on_message = self.on_recv_message
            self.on_connect()
        except Exception as e:
            print 'server connect failed'
            self.on_connect_fail()
            self.dispose()

    def on_recv_message(self, message):
        if message is None:
            if self.wsConn is not None:
                print 'server connection broken.'
                self.on_connect_broken()
                self.dispose()
        else:
            response = message.response
            if response.val is not None:
                self.on_response(response)
            else:
                request = message.request
                if request.val is not None:
                    self.on_request(request)

    def on_request(self, request):
        pass

    def on_response(self, response):
        pass


class ClientStatus(object):
    INIT = 0
    AUTHING = 1
    SEATING = 2
    FIGHTING = 3


class WSClient(BaseWSClient):
    def __init__(self, url):
        BaseWSClient.__init__(self, url)
        self.client_status = ClientStatus.INIT

    def on_connect(self):
        BaseWSClient.on_connect(self)
        d = {'action': 'user.login', 'token': 'zyw'}
        self.send_request(d, 'authRequest')
        self.client_status = ClientStatus.AUTHING

    def on_response(self, response):
        if self.client_status == ClientStatus.AUTHING:
            playerinfo = response.playerinfo
            if playerinfo is not None:
                print 'uid=%s' % playerinfo['uid']

            tableSummary = response.tableSummary
            if tableSummary:
                tableIdx = None
                maxPlayerNumPerTable = tableSummary['maxPlayerNumPerTable']
                for idx, n in enumerate(tableSummary['tablePlayerNums']):
                    if n < maxPlayerNumPerTable:
                        tableIdx = idx
                        break
                if tableIdx is not None:
                    print '\tjoin table %s' % tableIdx
                    d = {'joinTable': {'tableIdx': tableIdx}}
                    self.send_request(d)
                self.client_status = ClientStatus.SEATING
        elif self.client_status == ClientStatus.SEATING:
            joinTable = response.joinTable
            if joinTable is not None:
                self.client_status = ClientStatus.FIGHTING
                print '\tplayer_num=%s' % len(joinTable['players'])
                print '\teverything is ok, go go go'

    def on_request(self, request):
        if self.client_status == ClientStatus.AUTHING:
            enterFight = request.enterFight
            if enterFight is not None:
                d = {'getTableSummary': {}}
                self.send_request(d)
                return
        elif self.client_status == ClientStatus.FIGHTING:
            joinTable = request.joinTable
            if joinTable is not None:
                print '\t player(uid=%s) join table' % joinTable['uid']

            leaveTable = request.leaveTable
            if leaveTable is not None:
                print '\t player(uid=%s) leave table' % leaveTable['uid']

            shotFish = request.shotFish
            if shotFish is not None:
                print '\t player(uid=%s) is shotting' % shotFish['uid']

            fishBorn = request.fishBorn
            if fishBorn is not None:
                print '\t fish born, num=%s' % len(fishBorn['fishes'])

            tableStatus = request.tableStatus
            if tableStatus is not None:
                print '\t please sync the table status, %s' % tableStatus

    def do_shot(self):
        if self.wsConn is None:
            print 'not connect the server, cannot do shot'
            return
        if self.client_status != ClientStatus.FIGHTING:
            print 'not ready, hold on'
