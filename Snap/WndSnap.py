#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  os
from PIL import ImageGrab
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np


def snapDesktop():
    im = ImageGrab.grab()
    im.save(os.path.join(os.getcwd(),"abc.png"),"png")
    lena = mpimg.imread(os.path.join(os.getcwd(),"abc.png"))
    lena.shape #(512, 512, 3)
    plt.imshow(lena) # 显示图片
    plt.axis('off') # 不显示坐标轴
    plt.show()

if __name__ == "__main__":
    snapDesktop()