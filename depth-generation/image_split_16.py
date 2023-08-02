'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-02 10:51:37
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-02 10:58:58
FilePath: \\feature-matching\depth-generation\image_split_16.py
Description: 将图像分成 16 份并保存
'''
import cv2

# 读取图片
img = cv2.imread('ref\\frame_16.jpg')

# 获取图片的高度和宽度
height, width, _ = img.shape

# 计算每一份图像的高度和宽度
height_step = height // 4
width_step = width // 4

# 分割并保存图像
for i in range(4):
    for j in range(4):
        # 计算分割的矩形区域
        y_start = i * height_step
        y_end = (i + 1) * height_step
        x_start = j * width_step
        x_end = (j + 1) * width_step
        
        # 对图像进行分割
        sub_img = img[y_start:y_end, x_start:x_end]
        
        # 保存分割的图像
        cv2.imwrite(f'data\\image\\image_{i}_{j}.jpg', sub_img)
        
        