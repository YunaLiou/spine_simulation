import cv2
import os
import numpy as np


imgpath = r'C:\Users\vision2110\Desktop\chinghui\All\102_2'
imglist = os.listdir(imgpath)
imglist.sort(key = lambda x:int(x.split('.png')[0]))

for i in imglist:
    img = cv2.imread(os.path.join(imgpath, i), 0)
    img = cv2.resize()