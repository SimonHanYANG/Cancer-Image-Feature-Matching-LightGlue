'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-24 14:13:02
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-24 14:39:27
FilePath: \\depth-generation\\2D3D_generation.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取RGB图像和深度图
rgb = cv2.imread('E:\\Paper1-Contact_Detection_Dataset\\results\\image_res\\rgb.jpg')
depth = cv2.imread('E:\\Paper1-Contact_Detection_Dataset\\results\\image_res\\depth.png', cv2.IMREAD_GRAYSCALE)

# 将RGB图像和深度图调整到相同的大小
depth = cv2.resize(depth, (rgb.shape[1], rgb.shape[0]))

print(depth.shape)
print(rgb.shape)

# 将深度图转换为3D坐标
h, w = depth.shape
x, y = np.meshgrid(range(w), range(h))
z = -depth

# 创建一个新的图像窗口
fig = plt.figure(figsize=(10, 10))

# 创建3D坐标系
ax = fig.add_subplot(111, projection='3d')

# 使用RGB图像的颜色来渲染表面
rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)  # OpenCV读取的颜色是BGR, 转换为RGB
colors = rgb.reshape(-1, 3) / 255.0  # 重塑并归一化颜色

# 绘制表面
surf = ax.plot_surface(x, -y, z, facecolors=colors.reshape(h, w, 3), rstride=1, cstride=1)

# 设置坐标轴的标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图像
plt.show()