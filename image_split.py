'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-07-24 13:12:08
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-07-24 13:25:26
FilePath: \feature-matching\image_split.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PIL import Image
import os

# 确保 data/ 文件夹存在
if not os.path.exists('image\\data'):
    os.makedirs('image\\data')

# 打开图片
img = Image.open('image\\pic\\frame_8.jpg')

# 获取图片的宽度和高度
width, height = img.size

# 计算每个部分的尺寸
part_width = width // 2
part_height = height // 2

# 分割图片并保存
parts = [
    img.crop((0, 0, part_width, part_height)),  # 左上角
    img.crop((part_width, 0, width, part_height)),  # 右上角
    img.crop((0, part_height, part_width, height)),  # 左下角
    img.crop((part_width, part_height, width, height))  # 右下角
]

for i, part in enumerate(parts):
    part.save(f'image\\data\\part_{i}.jpg')
    print('image\\data\\part_{}.jpg saved!'.format(i))
    