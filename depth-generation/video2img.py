'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-17 13:54:08
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-17 13:55:53
FilePath: \depth-generation\\video2img.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import os

def save_frames(video_path, dir_path):
    # 确保目标保存目录存在
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
    # 读取视频文件
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    while success:
        # 保存当前帧为 JPEG 文件
        cv2.imwrite(os.path.join(dir_path, "frame%d.jpg" % count), image)
        success, image = vidcap.read()
        print('Saved frame number : ' + str(count))
        count += 1

# 使用函数
save_frames('data\\video\\Basler acA1920-155ucMED (40214438)_20230817_111734095.mp4', 'data\\video_image')
