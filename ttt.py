from PIL import Image
import numpy as np
import nrrd
import os
import matplotlib.pylab as plt
import cv2

# nrrd圖片讀取
# nrrd圖片使用nrrd包gitHub中的data資料
# nrrd_filename = r'D:\ChingHui\Data\Spineweb_dataset5\Spine DataBase for Public Use\Subject 1\Segmentation\L5.nrrd'

# nrrd_filename = r'D:\ChingHui\Data\Spineweb_dataset5\Spine DataBase for Public Use\Subject 1\Segmentation\L5.nrrd'

nrrd_filename = 'D:\ChingHui\Data\Spineweb_dataset5\Spine DataBase for Public Use\Subject 1\Original.nrrd'
nrrd_data, nrrd_options = nrrd.read(nrrd_filename)

print(nrrd_options)
print(nrrd_data.shape)

# nrrd_image = Image.fromarray(nrrd_data[:,:,29]*1.5)
# #nrrd_data[:,:,29] 表示擷取第30張切片
# nrrd_image.show() # 顯示這圖片


for i in range(nrrd_data.shape[2]):
    img = nrrd_data[..., i]
    normalizedImg = np.zeros((nrrd_data.shape[0], nrrd_data.shape[1]))
    normalizedImg = cv2.normalize(img, normalizedImg, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(os.path.join(r'C:\Users\vision2110\Desktop\chinghui\subject1\original', str(i)+'.png'), normalizedImg)
#
#
#     plt.imshow(img, cmap='gray')
#
#     plt.savefig(os.path.join(r'C:\Users\vision2110\Desktop\test', str(i)+'.png'),
#                 bbox_inches='tight',
#                 pad_inches=0,
#                 format='png',
#                 dpi=300)
#
#     print('-----------------ok---', str(i))

# data = np.random.random((8, 8))
# plt.imshow(data, cmap='cool', interpolation='nearest')
# plt.show()


# import numpy as np
# import seaborn as sns
# import matplotlib.pylab as plt
#
# data = np.random.rand(8, 8)
# ax = sns.heatmap(data, linewidth=0.3)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# data = np.random.random((8, 8))
# plt.imshow(data, cmap='cool', interpolation='nearest')
# plt.show()
