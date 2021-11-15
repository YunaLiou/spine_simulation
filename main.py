import os
import cv2
import numpy as np
# imgpath =r'C:\Users\vision2110\Desktop\ExampleImage2'
# savepath = r'C:\Users\vision2110\Desktop\testImage'
# imglist = os.listdir(imgpath)
#
# for i in imglist:
#     img = cv2.imread(os.path.join(imgpath, i), 1)
#     cv2.imwrite(os.path.join(savepath, i[:-3]+'bmp'), img)

# img = cv2.imread( ,0)
img = cv2.imread(r'C:\Users\vision2110\Desktop\new_1\ExampleImage2\salt-and-pepper-lena.bmp',0)
final = cv2.medianBlur(img, 3)

cv2.imwrite(r'C:\Users\vision2110\Desktop\1.bmp', final)


x = cv2.Sobel(final, cv2.CV_16S, 1, 0)
y = cv2.Sobel(final, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)  # 转回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


cv2.imwrite(r'C:\Users\vision2110\Desktop\2.bmp', dst)


temp = np.where(dst>130, 255, 0)
temp = temp.astype(np.uint8)
cv2.imwrite(r'C:\Users\vision2110\Desktop\3.bmp',temp)
cv2.waitKey(0)

