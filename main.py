# -*- coding=utf-8 -*-
import logging
from cos_upload import upload_folder
from webp_convert import webp_convert
import os

# 设置目录路径
directory_path = r''  # 这里填写本地路径
cos_dir = r''  # 这里填写COS路径

# 获取目录下的所有子目录
subdirectories = [
    d for d in os.listdir(directory_path)
    if os.path.isdir(os.path.join(directory_path, d))
]

# 输出子目录名
for subdirectory in subdirectories:

    local_folder = rf'{directory_path}\{subdirectory}'
    cos_folder = f'{cos_dir}/{subdirectory}'  # 在存储桶内的目标路径
    output_dir = rf"{directory_path}\output"  # 输出文件夹路径

    webp_convert(local_folder, output_dir)
    upload_folder(local_folder, cos_folder)
    print(f"Upload successful to {cos_folder}")
