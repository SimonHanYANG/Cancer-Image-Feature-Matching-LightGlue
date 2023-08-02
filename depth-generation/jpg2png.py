'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-02 13:52:28
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-02 13:53:39
FilePath: \\feature-matching\depth-generation\jpg2png.py
Description: jpg to png format
'''
import os
from PIL import Image

# 指定要转换的 JPEG 图像的目录
input_directory = 'data\\image\\'

# 指定要保存 PNG 图像的目录
output_directory = 'data\\image\\'

# 确保输出目录存在
os.makedirs(output_directory, exist_ok=True)

# 遍历输入目录中的所有文件
for filename in os.listdir(input_directory):
    # 检查文件是否是 JPEG 格式
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # 打开 JPEG 图像
        img = Image.open(os.path.join(input_directory, filename))
        # 更改文件扩展名为 '.png'
        png_filename = os.path.splitext(filename)[0] + '.png'
        # 保存为 PNG 图像
        img.save(os.path.join(output_directory, png_filename))

print("Conversion from JPG to PNG completed!")