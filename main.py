from cos_upload import upload_folder
from webp_convert import webp_convert
import os
from colorama import Fore, Style, init

init(autoreset=True)

directory_path = r"C:\Users\worker\Pictures\Blog_webp"

subdirectories = [
    d for d in os.listdir(directory_path)
    if os.path.isdir(os.path.join(directory_path, d)) and d != "output"
]

for subdirectory in subdirectories:

    local_folder = rf'{directory_path}\{subdirectory}'
    cos_folder = f'images/blog/{subdirectory}'
    output_dir = rf"{directory_path}\_temp_output"

    webp_convert(local_folder, output_dir)
    upload_folder(local_folder, cos_folder)
    print(
        f"{Fore.GREEN}✓{Style.RESET_ALL} 上传成功到 {Fore.CYAN}{cos_folder}{Style.RESET_ALL}"
    )
