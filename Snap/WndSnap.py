#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  os,threading,time,io,datetime
from PIL import ImageGrab,Image
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np

from GlobalDatas import *

FPS=1

def snapDesktop():
    print "***********Start Video collection***********"
    timeSep = 1 / float(FPS)
    while True:
        im = ImageGrab.grab()
        out = im.resize((int(im.size[0]*ZoomRate), int(im.size[1]*ZoomRate)), Image.ANTIALIAS)  # resize image with high-quality

        # out.save(os.path.join(os.getcwd(), "%s.png"%time.mktime(datetime.datetime.now().timetuple())), "png")

        imgByteArr = io.BytesIO()
        out.save(imgByteArr,  "PNG")
        imgByteArr = imgByteArr.getvalue()

        dataAccessLock.acquire()  # 从这里进入线程安全区
        CurrentPhoto = imgByteArr
        dataAccessLock.release()  #
        time.sleep(timeSep)

        # print "next snap"


def startSnapThread(fps):
    FPS = fps
    commandListen = threading.Thread(target=snapDesktop, args=())
    commandListen.daemon = True
    commandListen.start()
    pass

if __name__ == "__main__":
    snapDesktop()