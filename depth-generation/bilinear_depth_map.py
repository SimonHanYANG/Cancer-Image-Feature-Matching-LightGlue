'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-22 16:17:24
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-22 16:58:19
FilePath: \\feature-matching\depth-generation\\bilinear_depth_map.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取深度图
depth_map = cv2.imread('data\\depth\\image_3_2_sparse_depth_map.png', cv2.IMREAD_GRAYSCALE)

# 对深度图进行双线性插值
height, width = depth_map.shape
scaled_depth_map = cv2.resize(depth_map, (width*2, height*2), interpolation = cv2.INTER_LINEAR)

# 展示和保存双线性插值后的深度图
plt.imshow(scaled_depth_map, cmap='plasma')
plt.colorbar()
plt.savefig('data\\video_hot\\image_3_2_sparse_depth_map_bilinear.png')
plt.close()
