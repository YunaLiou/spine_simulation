import cv2
import os
import numpy as np





imgpath = r'C:\Users\vision2110\Desktop\chinghui\All\104'
imglist = os.listdir(imgpath)
imglist.sort(key = lambda x:int(x.split('.png')[0]))

for x, i in enumerate(imglist):
    img = cv2.imread(os.path.join(imgpath, i), 0)
    cv2.imwrite(os.path.join(r'C:\Users\vision2110\Desktop\chinghui\All\104_2', str(x)+'.png'), img)