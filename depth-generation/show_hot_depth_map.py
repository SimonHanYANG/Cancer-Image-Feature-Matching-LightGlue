'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-02 15:20:58
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-23 12:14:11
FilePath: \\feature-matching\depth-generation\hot_depth_map.py
Description: 通过热力图展示一个深度图
'''

import cv2
import matplotlib.pyplot as plt

# 读取深度图像，这里假设图像是灰度图像，每个像素的值表示深度
# depth_image = cv2.imread('data\\depth\\1552097915.8256.png', cv2.IMREAD_GRAYSCALE)

depth_image = cv2.imread('data\\depth\\1552097915.5921.png', cv2.IMREAD_GRAYSCALE)


# 使用热力图颜色映射显示图像
plt.imshow(depth_image, cmap='plasma')

# 显示颜色条
plt.colorbar()

# 显示图像
plt.show()