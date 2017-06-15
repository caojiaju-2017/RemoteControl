#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  thread


dataAccessLock = thread.allocate_lock ()
socketAccessLock = thread.allocate_lock ()

imageSocketDictionary= {}
singleSocketDictionary= {}

ZoomRate = 0.5

ClientDictionarys= {}

# 视频
VideoPort = 6001

# Single Port
SinglePort = 6002

class SnapDatas(object):
    CurrentPhoto = None
    # Fps = 10
    # # PhotoDictionary = {}
    # # currentIndex = 0
    #
    # def getNewPhoto(self):
    #     pass
    #
    # def snapPhoto(self):
    #     pass