#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  os,threading,time,io
from PIL import ImageGrab,Image
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np



FPS=10

def snapDesktop():
    print "***********Start video collection***********"
    timeSep = 1 / float(FPS)
    while True:
        im = ImageGrab.grab()
        out = im.resize((im.size[0] / 2, im.size[1] / 2), Image.ANTIALIAS)  # resize image with high-quality

        out.save(os.path.join(os.getcwd(), "abc.png"), "png")

        imgByteArr = io.BytesIO()
        out.save(imgByteArr,  "PNG")
        imgByteArr = imgByteArr.getvalue()

        time.sleep(timeSep)

        break

def startSnapThread(fps):
    FPS = fps
    commandListen = threading.Thread(target=snapDesktop, args=())
    commandListen.daemon = True
    commandListen.start()
    pass

if __name__ == "__main__":
    snapDesktop()