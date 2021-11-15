import os
import cv2
import numpy as np


imgpath = r'./spineweb\104'
savepath = r'./spineweb\104_180'

imglist = os.listdir(imgpath)
imglist.sort(key = lambda x:int(x.split('.png')[0]))

for i in range(180):
    if i<65 or i>115:
        temp = np.zeros((180,180),dtype=np.uint8)
        cv2.imwrite(os.path.join(savepath, str(i)+'.png'), temp)
    else:
        img = cv2.imread(os.path.join(imgpath, imglist[i-65]), 0)
        temp = img[10:190, 10:190]
        cv2.imwrite(os.path.join(savepath, str(i)+'.png'), temp)





# for i in imglist:
#     img = cv2.imread(os.path.join(imgpath, i), 0)
#     temp = img[10:190, 10:190]
#     cv2.imwrite(os.path.join(imgpath, i), temp)