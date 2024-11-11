# -*- coding=utf-8 -*-
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import sys
import logging

# COS配置
secret_id = ''
secret_key = ''
region = ''
bucket_name = ''
token = None
scheme = 'https'

# 初始化 COS 客户端
config = CosConfig(Region=region,
                   SecretId=secret_id,
                   SecretKey=secret_key,
                   Token=token,
                   Scheme=scheme)
client = CosS3Client(config)


# 检查文件是否已存在于 COS 中
def file_exists_in_cos(cos_folder, file_name):
    response = client.list_objects(Bucket=bucket_name, Prefix=cos_folder)
    for content in response.get('Contents', []):
        if content['Key'] == os.path.join(cos_folder,
                                          file_name).replace("\\", "/"):
            return True
    return False


# 定义上传文件夹函数
def upload_folder(local_folder, cos_folder):
    for root, _, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            cos_path = os.path.join(cos_folder,
                                    os.path.relpath(local_path,
                                                    local_folder)).replace(
                                                        "\\", "/")

            # 检查文件是否已经存在
            if file_exists_in_cos(cos_folder, file_name):
                print(f"文件 {file_name} 已存在，跳过上传。")
                continue

            # 上传文件并自动覆盖
            response = client.upload_file(Bucket=bucket_name,
                                          LocalFilePath=local_path,
                                          Key=cos_path,
                                          PartSize=1,
                                          MAXThread=10,
                                          EnableMD5=False)
            print(f"已上传文件：{cos_path}，ETag: {response['ETag']}")
