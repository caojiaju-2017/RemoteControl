#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Comminucation.BluthWay import *
from Comminucation.NetWay import *
from Snap.WndSnap import *
import threading,time

comminucationDictions = {1: NetWay.runTcp, 2: NetWay.runUdp, 3: BluthWay.run}

# 处理前端控制指令
def startCommandListen():
    commandListen = threading.Thread(target=startWorkThread, args=())
    commandListen.daemon = True
    commandListen.start()
    pass
def startWorkThread():
    print "***********Start Control Comman Listen***********"
    while True:
        print "adsf"
        time.sleep(1)
    pass
# 处理前端控制指令======================end


# 处理视频实时推送服务
def startVideoService():
    commandListen = threading.Thread(target=startVideoServiceChannel, args=())
    commandListen.daemon = True
    commandListen.start()
    pass
def startVideoServiceChannel():
    print "***********Start Video Send Service***********"
    while True:
        print "adsf"
        time.sleep(1)
    pass
# 处理视频实时推送服务======================end


# 启动定时截图功能
def startSnapService():
    startSnapThread(10)
    pass
# 启动定时截图功能====end

def startMain():
    runWay = 0
    while True:
        str = raw_input(u"请选启动方式：\n    输入1,Tcp模式 \n    输入2,UDP模式\n    输入3,蓝牙模式\n    输入q,退出程序\n你的输入：")
        if str.lower() == "1":
            runWay = 1
            break
        elif str.lower() == "2":
            runWay = 2
            break
        elif str.lower() == "3":
            runWay = 3
            break
        elif str.lower() == "q":
            exit()
        else:
            continue

    # 截屏服务
    startSnapService()

    # 视频推送服务
    startVideoService()

    #启动线程，监控前端控制指令
    startCommandListen()

    # 启动视频接入通信接口
    comminucationDictions[runWay]()



    pass

def waitTerminalSingal():
    while True:
        str = raw_input(u"请选择操作内容：\n    输入q,退出程序\n你的输入：")
        if str.lower() == "q":
            exit()

if __name__ == "__main__":
    startMain()
    waitTerminalSingal()