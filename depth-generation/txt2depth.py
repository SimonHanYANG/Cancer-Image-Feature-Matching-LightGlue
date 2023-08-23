'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-02 12:45:25
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-22 16:52:29
FilePath: \\feature-matching\depth-generation\depth_map_generate.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import cv2

depth_map_path = f'data\\depth\\'

depth_path = f'data\\depth_value\\'

img_path = f'data\\image\\'
# image_0_1 ~ image_3_3
img_name = f'image_3_2'

# 读取 rgb 图像
rgb_img = cv2.imread(f'{img_path}{img_name}.jpg')
print("Image Shape: {}".format(rgb_img.shape))

height, width, _ = rgb_img.shape

# 从 txt 文件中读取深度数据
depth_data = np.loadtxt(f'{depth_path}{img_name}_depth.txt')

# 将深度数据调整为原始图像的形状
depth_array = depth_data.reshape((height, width))

# 将深度数据归一化到 0-255
depth_array = ((depth_array - depth_array.min()) / (depth_array.max() - depth_array.min()) * 255).astype(np.uint8)

# 保存深度图像
cv2.imwrite(f'{depth_map_path}{img_name}_sparse_depth_map.png', depth_array)
