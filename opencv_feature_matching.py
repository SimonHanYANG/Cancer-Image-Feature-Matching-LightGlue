'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-07-31 11:21:37
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-01 11:55:45
FilePath: \\feature-matching\opencv_feature_matching.py
Description: 使用 ORB (Oriented FAST and Rotated BRIEF) 描述符和 Brute-Force 匹配器来比较两张图像的特征是否相似
            ORB 是一种高效的特征描述符，由 OpenCV 实验室提出。它是一种融合了 FAST 关键点检测器和 BRIEF 描述符的算法，同时加入了一些改进使其更为强大。
            ORB 的主要优点是其高效性和性能，它可以在不牺牲太多精度的情况下，达到或超过了更复杂的描述符（如 SIFT 和 SURF）的性能。
            ORB 的工作流程主要包括以下步骤：
                使用 FAST 关键点检测器找到图像中的关键点。
                计算关键点的方向。
                根据关键点的方向，使用旋转的 BRIEF 描述符来描述关键点。
                对描述符进行哈密顿距离匹配。
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 读取图像
img1 = cv2.imread('LightGlue\\assets\\cancer1.png',0)  # queryImage
img2 = cv2.imread('LightGlue\\assets\\cancer2.png',0)  # trainImage


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

    # 保存图像
    plt.savefig(f'matching_res\\image_split_16_res.png')
    
    plt.show()

    return segments


def orb_matching(img1, img2):
    # 初始化 ORB 描述符
    orb = cv2.ORB_create()

    # 寻找关键点和描述符
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # 创建 BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 进行匹配
    matches = bf.match(des1,des2)

    # 根据距离排序
    matches = sorted(matches, key = lambda x:x.distance)
    
    # 获取 match 到了多少个点
    match_count = len(matches)

    # 绘制前15个匹配
    result = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20], None, flags=2)

    # Show Matching Results
    # cv2.imshow('Feature Matching',result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return result
    

def compare_segments(segments):
    num_segments = len(segments)

    for i in range(num_segments):
        results = []
        for j in range(num_segments):
            # type(segments[i]): np.ndarray
            # print(segments[i].shape == segments[j].shape)
            if i == j:
                pass
            else:
                # ORB matching
                result = orb_matching(segments[i], segments[j])
                if result is not None:
                    results.append(result)
                
        # 创建一个新的 matplotlib 图形
        fig, axs = plt.subplots(4, 4, figsize=(15, 15))

        # 在第一行显示原图
        axs[0, 0].imshow(cv2.cvtColor(segments[i], cv2.COLOR_BGR2RGB))
        axs[0, 0].set_title(f'Original Segment {i+1}')
        axs[0, 0].axis('off')

        # 对于每个结果
        for k, result in enumerate(results):
            # 在新的一行中显示结果
            row = (k + 1) // 4
            col = (k + 1) % 4
            axs[row, col].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
            if k < i:
                axs[row, col].set_title(f'Match with Segment {k+1}')  
            elif k > i:
                axs[row, col].set_title(f'Match with Segment {k+2}')  
            else:
                axs[row, col].set_title(f'Match with Segment {k+2}')  
                
            axs[row, col].axis('off')  # 关闭坐标轴

        # 调整子图的间距
        plt.tight_layout()
        
        # 保存图像
        plt.savefig(f'matching_res\\output_original{i}_res.png')
        
        plt.show()
        
        
def main():
    # 读取图像
    # type(image): np.ndarray
    image = cv2.imread('ref\\cancer.jpg', 0)

    # 切分图像
    segments_per_side = 4  # 4x4 = 16 分区
    segments = get_image_segments(image, segments_per_side)
    
    # 比较分区
    compare_segments(segments)

if __name__ == "__main__":
    main()
