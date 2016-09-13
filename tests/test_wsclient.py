# coding: utf-8

import os
import sys
import signal
import threading
import tornado.ioloop
from tornado.options import define, options
from wsclient import WSClient


define('app_name', default='[wsclint robot]', type=str)
define('host', default='ws://127.0.0.1:808/ws/', type=str)
define('username', default='test1', type=str)
define('password', default='1111', type=str)
define('token', default='', type=str)


keepRunning = True
fishClient = None


def start_tornado():
    global fishClient
    io_loop = tornado.ioloop.IOLoop.instance()
    fishClient = WSClient(options.host)
    fishClient.do_connect()
    io_loop.start()


def stop_tornado(sig, frame):
    global serviceApp
    global keepRunning
    print 'shutdown'
    io_loop = tornado.ioloop.IOLoop.instance()
    io_loop.add_callback(io_loop.stop)
    keepRunning = False
    print 'ioloop thread stopped'


def do_shot():
    global fishClient
    fishClient.do_shot()


def main():
    os.system('cls')
    options.parse_command_line()
    print 'starting %s...' % options.app_name

    t = threading.Thread(target=start_tornado)
    t.start()
    signal.signal(signal.SIGTERM, stop_tornado)
    signal.signal(signal.SIGINT, stop_tornado)
    try:
        print 'when robot ready, enter do shot'
        while keepRunning:
            raw_input('enter do shot:')
            tornado.ioloop.IOLoop.instance().add_callback(do_shot)
    except KeyboardInterrupt as e:
        stop_tornado(0, 0)
    except Exception as e:
        print e

    print 'wait tornaod main thread to exit...'
    t.join()
    print '%s stopped .' % options.app_name


if __name__ == '__main__':
    main()
