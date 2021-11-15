import os
import cv2
import numpy as np
import nrrd


spinepath = r'D:\ChingHui\Data\Spineweb_dataset5\Spine DataBase for Public Use'
savepath = r'C:\Users\vision2110\Desktop\newchinghui'
spinelist = os.listdir(spinepath)
spinelist.sort(key = lambda x:int(x.split('Subject')[1]))
print(spinelist)

for w, i in enumerate(spinelist):
    bonepath = os.path.join(spinepath, i, 'Segmentation')
    print(bonepath)
    bonelist = os.listdir(bonepath)

    first_path = os.path.join(savepath, str(w+1))
    if not os.path.isdir(first_path):
        os.mkdir(first_path)
    print(bonelist)
    for v, j in enumerate(bonelist):

        second_path = os.path.join(first_path, str(v + 1))
        if not os.path.isdir(second_path):
            os.mkdir(second_path)

        nrrd_filename = os.path.join(bonepath, j)
        nrrd_data, nrrd_options = nrrd.read(nrrd_filename)
        for k in range(nrrd_data.shape[2]):
            img = nrrd_data[..., k]
            normalizedImg = np.zeros((nrrd_data.shape[0], nrrd_data.shape[1]))
            normalizedImg = cv2.normalize(img, normalizedImg, 0, 255, cv2.NORM_MINMAX)
            normalizedImg = cv2.resize(normalizedImg, (200,200))
            normalizedImg = np.where(normalizedImg>128,255,0)
            normalizedImg = normalizedImg.astype(np.uint8)

            cv2.imwrite(os.path.join(second_path, str(k) + '.png'), normalizedImg)


    # dirlist = os.listdir(second_path)
    # temp = np.zeros((200,200,200))
    # for p in dirlist:
    #
    #     img = cv2.imread(os.path.join(second_path, p))
    #     temp[..., 2]
    #
    #
    # all_path = os.path.join(first_path, str(v + 1))
    # if not os.path.isdir(second_path):
    #     os.mkdir(second_path)



