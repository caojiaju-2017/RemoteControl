#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
import threading,struct
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

            tcpClientSock, addr = sock.accept()

            print "******Video Channel Open %s %s******" % (addr[0], addr[1])
            try:
                imageSocketDictionary.pop(addr[0])
            except:
                pass

            imageSocketDictionary[addr[0]] = tcpClientSock;
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
            tcpClientSock, addr = sock.accept()

            try:
                singleSocketDictionary.pop(addr[0])
            except:
                pass
            singleSocketDictionary[addr[0]] = tcpClientSock;

            commandListen = threading.Thread(target=NetWay.singleConnect, args=(tcpClientSock,addr))
            commandListen.daemon = True
            commandListen.start()
        pass

    @staticmethod
    def singleConnect(sock,addr):
        print "******Single Channel Open %s %s******" % (addr[0],addr[1])
        sock.send("aaa")
        while True:
            try:
                data = sock.recv(4096)
                print "**************Receive Command Code Is:%s**************" % data

                if data == "1001":
                    dataAccessLock.acquire()  # 从这里进入线程安全区
                    sendData = SnapDatas.CurrentPhoto
                    dataAccessLock.release()  #

                    if sendData:
                        print type(sendData)
                        if imageSocketDictionary.has_key(addr[0]):
                            # sendBytes = bytes(sendData)
                            dataLen = len(sendData)
                            # dataLen =   dataLen + 8
                            dataLenString = "%08d" % dataLen
                            print "send image length =%s"% dataLenString
                            socketAccessLock.acquire()
                            # imageSocketDictionary[addr[0]].send(struct.pack('<HH', dataLen,2) + sendData)
                            imageSocketDictionary[addr[0]].send(struct.pack('=HH', 8,2) + bytes("caojiaju"))
                            socketAccessLock.release()
                        else:
                            print "******Video Channel was not open; %s ******" % (addr[0])
            except Exception,ex:
                print "***********Exception===>" + ex.message
                print "******Connection was closed; %s ******" % (addr[0])
                imageSocketDictionary.pop(addr[0])
                singleSocketDictionary.pop(addr[0])
                break

    @staticmethod
    def runVideoUdp():
        print "runUdp"
        pass

    @staticmethod
    def runSingleUdp():
        print "runUdp"
        pass