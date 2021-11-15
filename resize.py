from PIL import Image
import numpy as np
import nrrd
import os
import matplotlib.pylab as plt
import cv2



imgdir = r'C:\Users\vision2110\Desktop\chinghui\subject1\bone_resize\L5'
imglist = os.listdir(imgdir)

for i in imglist:
    img = cv2.imread(os.path.join(imgdir,i), 0)
    img = cv2.resize(img, (200, 200))
    img = np.where(img>128, 255, 0)
    img = img.astype(np.uint8)
    cv2.imwrite(os.path.join(r'C:\Users\vision2110\Desktop\chinghui\subject1\bone_resize\L5',i), img)