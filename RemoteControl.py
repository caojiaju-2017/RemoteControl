#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Comminucation.BluthWay import *
from Comminucation.NetWay import *

from GlobalDatas import *

from Snap.WndSnap import *
from Comminucation.WayInfo import *
from GlobalDatas import *
import threading,time,socket
from socket import *

# 处理前端控制指令
def startCommandListen():
    commandListen = threading.Thread(target=NetWay.runSingleTcp, args=())
    commandListen.daemon = True
    commandListen.start()
    pass
# 处理前端控制指令======================end


# 处理视频实时推送服务
def startVideoService():
    commandListen = threading.Thread(target=NetWay.runVideoTcp, args=())
    commandListen.daemon = True
    commandListen.start()
    pass
# 处理视频实时推送服务======================end

def startMain():
    runWay = 0
    while True:
        str = raw_input(u"请选启动方式：\n    输入1,Tcp模式 \n    输入2,UDP模式\n    输入3,蓝牙模式\n    输入q,退出程序\n你的输入：\n")
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
    startSnapThread(10)

    if str == "1":
        # 视频推送服务
        startVideoService()
        #启动线程，监控前端控制指令
        startCommandListen()

    # # 启动视频接入通信接口
    # comminucationDictions[runWay]()



    pass

def waitTerminalSingal():
    while True:
        str = raw_input(u"请选择操作内容：\n    输入q,退出程序 \n    输入s,显示二维码\n你的输入：\n")
        if str.lower() == "q":
            exit()
        elif str.lower() == "s":
            WayInfo().make_qr("192.168.1.101:8009", os.path.join(os.getcwd(), "test.png"))

if __name__ == "__main__":
    startMain()
    waitTerminalSingal()