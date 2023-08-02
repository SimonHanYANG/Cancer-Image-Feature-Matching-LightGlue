'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-02 10:25:12
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-02 12:02:57
FilePath: \\feature-matching\depth-generation\depth_value_generate_app.py
Description: 读取一个 rgb 图像并展示，然后通过鼠标点击获取图像中被点击的像素位置，并让我能够输入一个深度值。在 txt 文件中按照 rgb 图像像素顺序从左到右从上到下，
             如果程序结束时如果没有被点击到的像素位置储存 0，被点击到的像素位置储存输入的深度值，然后保存 txt 文件
'''
import cv2
import numpy as np

depth_path = f'data\\depth_value\\'

img_path = f'data\\image\\'
# image_0_1 ~ image_3_3
img_name = f'image_3_2'

# 读取 rgb 图像
img = cv2.imread(f'{img_path}{img_name}.jpg')
print("Image Shape: {}".format(img.shape))

# 创建一个与图像大小相同，但是所有元素为 0 的数组，用于储存深度信息
depth_array = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)

# 通过鼠标点击获取图像中被点击的像素位置
def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'你点击的像素位置是 ({x}, {y})')
        depth = input("请输入一个深度值：")
        depth_array[y, x] = depth
        depth_num = np.count_nonzero(depth_array)
        print(f"现在拥有的 Depth Information 数量为: {depth_num}")
        print('Depth Input Done! Please Select Next Pixel or Press Esc to Exit~')

# 创建一个名为 'image' 的窗口，并将 'get_position' 函数与鼠标点击事件绑定到这个窗口
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_position)

# 展示图像，直到用户按下 ESC 键
while True:
    cv2.imshow('image', img)
    
    # 如果用户按下 ESC 键，就退出循环
    if cv2.waitKey(20) & 0xFF == 27:
        print("APP FINISHED!")
        break

# 释放资源并关闭窗口
cv2.destroyAllWindows()

# 将深度数组的数据按照像素顺序（从左到右，从上到下）保存到 txt 文件中
np.savetxt(f'{depth_path}{img_name}_depth.txt', depth_array.flatten(), fmt='%.2f')
