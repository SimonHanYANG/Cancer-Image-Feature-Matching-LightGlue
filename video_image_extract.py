'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-07-24 13:06:23
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-07-24 13:06:31
FilePath: \feature-matching\data_prepare.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import os

# 确保 image/ 文件夹存在
if not os.path.exists('image\\pic'):
    os.makedirs('image\\pic')

# 打开视频文件
video = cv2.VideoCapture('image\\tmp\\demo.mp4')

# 初始化帧数
frame_count = 0

while True:
    # 读取视频帧
    ret, frame = video.read()

    # 如果视频帧不能正确读取，我们就断开循环
    if not ret:
        break

    # 将图片保存到 image/ 文件夹
    cv2.imwrite(f'image\\pic\\frame_{frame_count}.jpg', frame)

    # 帧数增加
    frame_count += 1

    print(f'image\\pic\\frame_{frame_count}.jpg Done!', frame)

# 释放并关闭视频文件
video.release()
cv2.destroyAllWindows()
