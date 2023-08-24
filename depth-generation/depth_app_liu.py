import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import random
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib import cm

# 初始化
drawing = False
ix, iy = -1, -1
points = []
depth_mask = None
root = tk.Tk()
root.withdraw()

def draw_polygon(event, x, y, flags, param):
    global ix, iy, drawing, img, points, depth_mask
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        points = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (ix, iy), (x, y), (0,255,255), 1)
            ix, iy = x, y
            points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), points[0], (0,255,255), 1)
        points.append(points[0])
        cv2.fillPoly(img, [np.array(points)], (0,0,255))
        
        correct_input = False

        while not correct_input:
            depth_type = simpledialog.askstring('Input', '请输入深度类型（low 或 high）')
            
            if depth_type == "low":
                # 20-60
                max_depth = random.randint(40, 60)
                correct_input = True
            elif depth_type == "high":
                # 80-255
                max_depth = random.randint(50, 70)
                correct_input = True
            else:
                messagebox.showinfo('Error', '输入错误，请输入 low 或 high')
        
        # 生成高斯分布的深度值
        mask = cv2.fillPoly(np.zeros_like(depth_mask), [np.array(points)], 1)
        
        # 为整个 mask 设置一个固定的深度值
        depth_values = np.full_like(depth_mask, max_depth)

        # 将深度值归一化到 0-1 范围
        #depth_values = (depth_values - np.min(depth_values)) / (np.max(depth_values) - np.min(depth_values))

        # 将深度值映射到 0 到 max_depth 范围
        #depth_values = depth_values * max_depth
        
        # 输出 depth_values 中的最大值和最小值
        print("depth_values Max depth value: ", np.max(depth_values))
        print("depth_values Min depth value: ", np.min(depth_values))

        # 将 depth_mask 的数据类型转换为 float32
        # 这样，depth_mask 就可以处理更大的数值，且不会被截断到 0-255 的范围。
        depth_mask = depth_mask.astype(np.float32)
        
        depth_mask[mask == 1] = depth_values[mask == 1]
        print("depth_mask Max depth value: ", np.max(depth_mask))
        print("depth_mask Min depth value: ", np.min(depth_mask))
        print(depth_mask.dtype)

        # 提示用户可以选择其他区域
        messagebox.showinfo('提示', '可以选择其他区域')
        points = []
        
def draw_ellipse(event, x, y, flags, param):
    global ix, iy, drawing, img, depth_mask, temp_img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        temp_img = img.copy()

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = temp_img.copy()
            axes_length = (abs(x - ix) // 2, abs(y - iy) // 2)
            center = ((x + ix) // 2, (y + iy) // 2)
            angle = np.degrees(np.arctan2((y - iy), (x - ix)))
            cv2.ellipse(img, center, axes_length, angle, 0, 360, (0,255,255), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        mask = np.zeros_like(depth_mask)
        axes_length = (abs(x - ix) // 2, abs(y - iy) // 2)
        center = ((x + ix) // 2, (y + iy) // 2)
        angle = np.degrees(np.arctan2((y - iy), (x - ix)))
        cv2.ellipse(img, center, axes_length, angle, 0, 360, (0,255,255), 1)
        cv2.ellipse(mask, center, axes_length, angle, 0, 360, 1, -1)

        correct_input = False

        while not correct_input:
            depth_type = simpledialog.askstring('Input', '请输入深度类型（low 或 high）')

            if depth_type == "low":
                # 20-60
                max_depth = random.randint(100, 150)
                correct_input = True
            elif depth_type == "high":
                # 80-255
                max_depth = random.randint(200, 255)
                correct_input = True
            else:
                messagebox.showinfo('Error', '输入错误，请输入 low 或 high')

        # 生成高斯分布的深度值
        depth_values = np.full_like(depth_mask, max_depth)
        depth_mask = depth_mask.astype(np.float32)
        depth_mask[mask == 1] = depth_values[mask == 1]

        # 提示用户可以选择其他区域
        messagebox.showinfo('提示', '可以选择其他区域')
        
def get_filename_from_path(img_path):
    base_name = os.path.basename(img_path)  # 获取路径中的文件名，例如 "frame0.jpg"
    file_name = os.path.splitext(base_name)[0]  # 从文件名中去掉扩展名，得到 "frame0"
    return file_name

# 加载 RGB 图像
img_path = "data\\video_image\\frame0.jpg"
file_name = get_filename_from_path(img_path)
print(file_name)

img = cv2.imread(img_path)
img_height, img_width = img.shape[:2]
depth_mask = np.zeros((img_height, img_width))

cv2.namedWindow("image")
# cv2.setMouseCallback("image", draw_polygon)
cv2.setMouseCallback("image", draw_ellipse)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

# 对 depth_mask 进行高斯滤波平滑处理
# smoothed_depth_mask = cv2.GaussianBlur(depth_mask, (5, 5), 0)

# 创建保存深度图像和热力图的文件夹
os.makedirs('data\\video_depth', exist_ok=True)
os.makedirs('data\\video_hot', exist_ok=True)

# # 保存深度图和深度值
depth_mask[depth_mask == 0] = 90  # 将深度为 0 的区域设置为 60，以便在热力图中将其显示为白色
np.savetxt("data\\video_depth\\{}_depth_txt_liu.txt".format(file_name), depth_mask, fmt="%.2f")
plt.imsave("data\\video_depth\\{}_depth_img_liu.png".format(file_name), depth_mask, cmap='hot')

# 生成并保存热力图
# 'viridis': 这是 Matplotlib 的默认颜色映射。它是一种线性的、亮度递增的颜色映射，颜色从蓝色变为黄色。这种映射是为了在数据可视化中最大程度地区分不同的值，并且对色盲友好。

# 'plasma': 这是一种从深蓝色变为亮粉色的颜色映射，亮度线性增加。

# 'inferno': 这是一种从黑色变为黄色的颜色映射，亮度线性增加。

# 'magma': 这是一种从黑色变为亮粉色的颜色映射，亮度线性增加。

# 'cividis': 这是一种从深蓝色变为黄色的颜色映射，亮度线性增加。这种映射特别设计为对色盲友好。
plt.imshow(depth_mask, cmap='plasma')
plt.colorbar()
plt.savefig("data\\video_hot\\{}_hot_img_liu.png".format(file_name))
plt.close()
