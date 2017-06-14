#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  thread

CurrentPhoto = None
dataAccessLock = thread.allocate_lock ()

ZoomRate = 0.5

ClientDictionarys= {}

# 视频
VideoPort = 6001

# Single Port
SinglePort = 6002

class SnapDatas(object):
    Fps = 10
    # PhotoDictionary = {}
    # currentIndex = 0

    def getNewPhoto(self):
        pass

    def snapPhoto(self):
        pass