# -*- coding=utf-8 -*-
import os
from PIL import Image
import shutil


def webp_convert(input_dir, output_dir):

    # 创建输出根目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 转换函数
    def convert_to_webp(input_path, output_path, quality=20):
        with Image.open(input_path) as img:
            img.convert("RGB").save(output_path, "webp", quality=quality)

    # 计数
    success_count = 0
    total_count = 0

    # 遍历输入目录及所有子文件夹
    for root, _, files in os.walk(input_dir):
        # 创建对应的输出目录
        relative_path = os.path.relpath(root, input_dir)
        target_dir = os.path.join(output_dir, relative_path)
        os.makedirs(target_dir, exist_ok=True)

        for filename in files:
            # 检查文件扩展名
            if filename.lower().endswith(
                ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
                total_count += 1
                input_path = os.path.join(root, filename)
                output_filename = os.path.splitext(filename)[0] + ".webp"
                output_path = os.path.join(target_dir, output_filename)

                try:
                    # 转换图片为 WebP 格式
                    convert_to_webp(input_path, output_path, quality=20)
                    success_count += 1
                    print(f"Converted {input_path} to WebP format.")

                    # 移动 WebP 文件到目标文件夹
                    final_output_path = os.path.join(root, output_filename)
                    shutil.move(output_path, final_output_path)
                    print(f"Moved WebP file to {final_output_path}.")

                    # 删除目标文件夹中的 PNG 文件
                    png_file_path = os.path.join(root, filename)
                    if png_file_path.lower().endswith('.png'):
                        os.remove(png_file_path)
                        print(f"Deleted original PNG file: {png_file_path}")

                except Exception as e:
                    print(f"Failed to convert {input_path}: {e}")

    # 检查是否全部成功转换
    if success_count == total_count:
        print("All images were successfully converted to WebP format.")
    else:
        print("Not all images were converted successfully.")
