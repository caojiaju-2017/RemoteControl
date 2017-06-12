#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Comminucation.BluthWay import *
from Comminucation.NetWay import *

operatorDict = {1: NetWay.runTcp, 2: NetWay.runUdp, 3: BluthWay.run}

def startCommandList():
    pass

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

    # 启动服务
    operatorDict[runWay]()


    #启动线程，监控前端控制指令
    startCommandList()
    
    pass

if __name__ == "__main__":
    startMain()