'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-02 15:20:58
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-02 16:23:11
FilePath: \\feature-matching\depth-generation\hot_depth_map.py
Description: 使用matplotlib库来生成一个热力图。下面是一个例子，它使用二维数组作为深度图，并使用'hot'颜色映射来生成热力图。然后，它将热力图和原始RGB图像叠加在一起
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np

depth_map_name = 'image_3_3'

# Load the depth map
depth_map = cv2.imread(f'res\\{depth_map_name}.png', cv2.IMREAD_GRAYSCALE)

# Normalize the depth map
max_depth = np.max(depth_map)
depth_map = depth_map / max_depth

# Apply the colormap
depth_color = plt.get_cmap('viridis')(depth_map)

# Remove the alpha channel
depth_color = (depth_color[:, :, :3] * 255).astype(np.uint8)

# Save the depth color map
cv2.imwrite(f'res\\color\\{depth_map_name}_depth_color.png', cv2.cvtColor(depth_color, cv2.COLOR_RGB2BGR))

# Display the depth color map
plt.imshow(depth_color)
plt.show()