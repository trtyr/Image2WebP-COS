import os
from PIL import Image
import shutil
from colorama import Fore, Style, init
import time

init(autoreset=True)


def webp_convert(input_dir, output_dir):

    shutil.rmtree(output_dir)
    print(f"{Fore.YELLOW}♻ 已清理临时目录{Style.RESET_ALL}")
    start_time = time.time()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def convert_to_webp(input_path, output_path, quality=20):
        with Image.open(input_path) as img:
            img.convert("RGB").save(output_path, "webp", quality=quality)

    success_count = 0
    total_count = 0

    for root, _, files in os.walk(input_dir):

        relative_path = os.path.relpath(root, input_dir)
        target_dir = os.path.join(output_dir, relative_path)
        os.makedirs(target_dir, exist_ok=True)

        for filename in files:

            if filename.lower().endswith(
                ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
                total_count += 1
                input_path = os.path.join(root, filename)
                output_filename = os.path.splitext(filename)[0] + ".webp"
                output_path = os.path.join(target_dir, output_filename)

                try:

                    convert_to_webp(input_path, output_path, quality=20)
                    success_count += 1
                    progress = f"[{success_count}/{total_count}]" if total_count > 0 else ""
                    print(
                        f"{Fore.CYAN}🖼 {progress} 转换成功 {Fore.RESET}{os.path.basename(input_path)} → {Fore.GREEN}{output_filename}"
                    )

                    final_output_path = os.path.join(root, output_filename)
                    shutil.move(output_path, final_output_path)
                    print(
                        f"{Fore.BLUE}⇢ 移动文件到 {Fore.RESET}{final_output_path}")

                    png_file_path = os.path.join(root, filename)
                    if png_file_path.lower().endswith('.png'):

                        original_path = os.path.join(root, filename)
                        if original_path.lower().endswith(
                            ('.png', '.jpg', '.jpeg', '.bmp', '.tiff',
                             '.gif')):
                            os.remove(original_path)
                            print(
                                f"{Fore.YELLOW}🗑 删除原始文件 {Fore.RESET}{os.path.basename(original_path)}"
                            )
                        os.remove(png_file_path)
                        print(
                            f"{Fore.YELLOW}🗑 删除原始PNG文件 {Fore.RESET}{os.path.basename(png_file_path)}"
                        )

                except Exception as e:
                    print(
                        f"{Fore.RED}× 转换失败 {os.path.basename(input_path)}: {Fore.RED}{str(e)}"
                    )

    total_time = time.time() - start_time
    print(f"\n{Fore.CYAN}≡≡≡ 转换总结 ≡≡≡{Style.RESET_ALL}")
    if success_count == total_count:
        print(f"{Fore.GREEN}✅ 全部转换成功! ({success_count} 文件)")
    else:
        print(f"{Fore.RED}⚠ 部分转换失败 {success_count}/{total_count}")
    print(f"{Fore.BLUE}⏱ 总耗时: {total_time:.2f} 秒{Style.RESET_ALL}\n")
