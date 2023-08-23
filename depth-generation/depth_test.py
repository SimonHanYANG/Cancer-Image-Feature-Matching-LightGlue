'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-08-21 16:05:17
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-08-21 17:38:37
FilePath: \\feature-matching\depth-generation\depth_test.py
Description: python 读取一个 txt，txt 文件存储是深度图的深度值，判断其中不为 0 的有多少个并输出
'''
# Open the file in read mode
# data\\video_depth\\frame0_depth_txt.txt

# The number of non-zero depth values is 271716.
# The minimum non-zero depth value is 60.0.
# The maximum depth value is 6045.0.
with open('data\\video_depth\\frame0_depth_txt.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Initialize a counter for non-zero values
non_zero_count = 0
# Initialize variables for the minimum and maximum non-zero values
min_value = float('inf')
max_value = float('-inf')

# Iterate over all lines
for line in lines:
    # Split the line into values (assuming space-separated values)
    values = line.split()
    # Convert values to floats and check if they are non-zero
    for value in values:
        float_value = float(value)
        if float_value != 0:
            non_zero_count += 1
            min_value = min(min_value, float_value)
            max_value = max(max_value, float_value)

# Print the results
print(f'The number of non-zero depth values is {non_zero_count}.')
print(f'The minimum non-zero depth value is {min_value}.')
print(f'The maximum depth value is {max_value}.')