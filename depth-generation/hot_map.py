'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-06 09:45:05
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-06 09:47:58
FilePath: \\feature-matching\depth-generation\hot_map.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 加载 RGB 图像和深度图
rgb_image = Image.open('rgb_image.png')
depth_map = Image.open('depth_map.png')

# 将深度图转换为数组
depth_array = np.array(depth_map)

# 创建一个新的图像以绘制热力图
plt.figure(figsize=(depth_map.size[0]/100, depth_map.size[1]/100), dpi=100)

# 使用 'hot' 颜色映射和深度图数据来绘制热力图
plt.imshow(depth_array, cmap='hot', interpolation='nearest')

# 将热力图保存为一个新的图像，移除额外的边框
plt.savefig('heatmap.png', bbox_inches='tight', pad_inches=0)

# 加载热力图
heatmap = Image.open('heatmap.png')

# 确保 RGB 图像和热力图具有相同的尺寸
rgb_image = rgb_image.resize(heatmap.size)

# 将热力图和原始 RGB 图像叠加在一起
result = Image.blend(rgb_image, heatmap, alpha=0.5)

# 显示结果
result.show()

# 保存结果
result.save('overlay.png')