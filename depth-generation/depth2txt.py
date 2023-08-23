'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-17 14:04:30
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-17 14:12:51
FilePath: \depth-generation\depth2txt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import numpy as np

# VOID Depth Information
# Minimum Depth:  0
# Maximum Depth:  6045

# Cancer Cell
# (2.55 μm vs. 6.12 μm)
# 2550 vs. 6120

# 读取深度图像
depth_img = cv2.imread("data\\depth\\1552097915.8256.png", cv2.IMREAD_UNCHANGED)

# 计算并打印最大深度和最小深度
min_depth = np.min(depth_img)
max_depth = np.max(depth_img)

print("Minimum Depth: ", min_depth)
print("Maximum Depth: ", max_depth)


# 保存数据到txt文件中
# np.savetxt('data\\\depth_value\\552097915.8256_depth_data.txt', depth_img)
