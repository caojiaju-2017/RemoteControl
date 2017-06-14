#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
from GlobalDatas import *

class NetWay(object):
    def __init__(self):
        pass

    @staticmethod
    def runVideoTcp():
        print "***********Start Video Send Service***********"
        HOST = ''
        PORT = VideoPort
        BUFSIZ = 1024
        ADDR = (HOST, PORT)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(ADDR)

        sock.listen(5)
        while True:
            print('waiting for connection')
            tcpClientSock, addr = sock.accept()
            print('connect from ', addr)

        pass

    @staticmethod
    def runSingleTcp():
        print "***********Start Command Send Service***********"
        HOST = ''
        PORT = SinglePort
        BUFSIZ = 1024
        ADDR = (HOST, PORT)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(ADDR)

        sock.listen(5)
        while True:
            print('waiting for Command connection')
            tcpClientSock, addr = sock.accept()
            print('connect from ', addr)

        pass

    @staticmethod
    def runVideoUdp():
        print "runUdp"
        pass

    @staticmethod
    def runSingleUdp():
        print "runUdp"
        pass