'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-07-31 11:29:27
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-07-31 12:29:51
FilePath: \\feature-matching\ssim_matching.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt

# def get_image_segments(image, segments_per_side):
#     # 计算每个分区的大小
#     height, width = image.shape[:2]
#     seg_height = height // segments_per_side
#     seg_width = width // segments_per_side

#     # 切分图像
#     segments = []
#     for i in range(segments_per_side):
#         for j in range(segments_per_side):
#             segment = image[i*seg_height:(i+1)*seg_height, j*seg_width:(j+1)*seg_width]
#             segments.append(segment)

#     return segments

def get_image_segments(image, segments_per_side):
    # 计算每个分区的大小
    height, width = image.shape[:2]
    seg_height = height // segments_per_side
    seg_width = width // segments_per_side

    # 切分图像
    segments = []
    for i in range(segments_per_side):
        for j in range(segments_per_side):
            segment = image[i*seg_height:(i+1)*seg_height, j*seg_width:(j+1)*seg_width]
            segments.append(segment)

    # 展示每个分割
    num_segments = len(segments)
    cols = segments_per_side
    rows = num_segments // cols
    fig = plt.figure(figsize=(20, 20))

    for i, segment in enumerate(segments):
        ax = fig.add_subplot(rows, cols, i+1)
        ax.imshow(cv2.cvtColor(segment, cv2.COLOR_BGR2RGB))
        ax.title.set_text(f'Segment {i+1}')

    plt.show()

    return segments

def compare_segments(segments, ssim_threshold, mse_threshold):
    matches = []
    num_segments = len(segments)

    for i in range(num_segments):
        for j in range(i+1, num_segments):
            ssim_value = ssim(segments[i], segments[j], channel_axis=-1)
            mse_value = mse(np.ravel(segments[i]), np.ravel(segments[j]))

            if ssim_value >= ssim_threshold and mse_value <= mse_threshold:
                matches.append((i, j))
    return matches

def display_matches(matches, segments):
    for match in matches:
        plt.figure()

        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(segments[match[0]], cv2.COLOR_BGR2RGB))
        plt.title(f'Segment {match[0]}')

        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(segments[match[1]], cv2.COLOR_BGR2RGB))
        plt.title(f'Segment {match[1]}')

        plt.show()

# 读取图像
image = cv2.imread('LightGlue\\assets\\cancer1.png')

# 切分图像
segments_per_side = 4  # 4x4 = 16 分区
segments = get_image_segments(image, segments_per_side)

# 比较分区
ssim_threshold = 0.99
mse_threshold = 0.01
matches = compare_segments(segments, ssim_threshold, mse_threshold)

# 显示匹配的分区
display_matches(matches, segments)