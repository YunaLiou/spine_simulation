import torch



import cv2
import numpy as np
import os
import torch.nn.functional as F

filepath = r'C:\Users\vision2110\Desktop\chinghui\All\102_2'
savepath = r'C:\Users\vision2110\Desktop\bbb'
file_folder = os.listdir(filepath)
file_folder.sort(key=lambda x: int(x.split('.png')[0]))
file_len = len(file_folder)
maskvolume_array = np.zeros((61, 200, 200))
print('okkkkkkkk11111111')
for i, x in enumerate(file_folder):
    img = cv2.imread(os.path.join(filepath, x), 0)
    maskvolume_array[i] = img
    print(i)
    print('----------------')
print('okkkkkkkk11111111')
img_tensor = torch.from_numpy(maskvolume_array)
img_tensor = img_tensor.unsqueeze(0)
img_tensor = img_tensor.unsqueeze(0)
img_interporlate_tensor = F.interpolate(img_tensor, scale_factor=2, mode='nearest')
img_interporlate_tensor = img_interporlate_tensor.squeeze(0)
img_interporlate_tensor = img_interporlate_tensor.squeeze(0)
img_interporlate_array = img_interporlate_tensor.numpy()

print(img_interporlate_array.shape)
w=0
for j in range(0,122,2):
    temp = img_interporlate_array[j]
    temp = temp.astype(np.uint8)
    print(temp.shape)
    iii = cv2.resize(temp, (200,200))
    print(iii.shape)
    a = np.zeros((200,200,3))
    a[..., 2]=iii
    a[..., 1]=maskvolume_array[w]
    w+=1
    a=a.astype(np.uint8)
    cv2.imwrite(os.path.join(savepath,str(w)+'.png'), a)

