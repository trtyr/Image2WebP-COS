from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import sys
import logging
from colorama import Fore, Style, init
import time

secret_id = ''
secret_key = ''
region = ''
bucket_name = ''
token = None
scheme = 'https'

config = CosConfig(Region=region,
                   SecretId=secret_id,
                   SecretKey=secret_key,
                   Token=token,
                   Scheme=scheme)
client = CosS3Client(config)


def file_exists_in_cos(cos_folder, file_name):
    response = client.list_objects(Bucket=bucket_name, Prefix=cos_folder)
    for content in response.get('Contents', []):
        if content['Key'] == os.path.join(cos_folder,
                                          file_name).replace("\\", "/"):
            return True
    return False


def upload_folder(local_folder, cos_folder):
    start_time = time.time()
    uploaded_count = 0
    skipped_count = 0

    for root, _, files in os.walk(local_folder):
        for file_name in files:

            if not file_name.lower().endswith('.webp'):
                continue
            local_path = os.path.join(root, file_name)
            local_path = os.path.join(root, file_name)
            cos_path = os.path.join(cos_folder,
                                    os.path.relpath(local_path,
                                                    local_folder)).replace(
                                                        "\\", "/")

            if file_exists_in_cos(cos_folder, file_name):
                print(
                    f"{Fore.YELLOW}⚠{Style.RESET_ALL} 文件 {Fore.CYAN}{file_name}{Style.RESET_ALL} 已存在，跳过上传"
                )
                skipped_count += 1
                continue

            try:
                response = client.upload_file(Bucket=bucket_name,
                                              LocalFilePath=local_path,
                                              Key=cos_path,
                                              PartSize=10,
                                              MAXThread=20,
                                              EnableMD5=False)
                print(
                    f"{Fore.GREEN}↑{Style.RESET_ALL} 上传成功 {Fore.CYAN}{cos_path}{Style.RESET_ALL} "
                    f"(ETag: {Fore.MAGENTA}{response['ETag']}{Style.RESET_ALL})"
                )
                uploaded_count += 1
            except Exception as e:
                print(
                    f"{Fore.RED}×{Style.RESET_ALL} 上传失败 {cos_path}: {Fore.RED}{str(e)}{Style.RESET_ALL}"
                )

    total_time = time.time() - start_time
    print(f"\n{Fore.CYAN}≡≡≡ 上传总结 ≡≡≡{Style.RESET_ALL}")
    print(f"{Fore.GREEN}成功上传: {uploaded_count} 文件")
    print(f"{Fore.YELLOW}跳过文件: {skipped_count} 文件")
    print(f"{Fore.BLUE}总耗时: {total_time:.2f} 秒{Style.RESET_ALL}\n")


init(autoreset=True)
