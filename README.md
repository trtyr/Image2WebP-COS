# 博客图片自动化处理工具

## 📖 项目简介

本工具为博客图片处理自动化解决方案，提供WebP格式转换、腾讯云COS存储上传功能，包含以下核心模块：
- cos_upload.py: 图片格式转换与清理
- cos_upload.py: 腾讯云COS文件上传
- main.py: 主流程控制

## 🚀 核心功能

1. **智能格式转换**  
   - 支持PNG/JPG等格式转WebP（质量压缩20%）
   - 自动清理原始图片文件
   - 保留目录结构转换

2. **云端同步**  
   - 自动跳过已存在文件
   - 实时上传进度反馈
   - 支持多线程分块上传

3. **可视化交互**  
   - 彩色终端输出状态
   - 实时统计报表
   - 异常错误提示

## ⚡ 快速开始

```bash
# 安装依赖
pip install pillow cos-python-sdk-v5 colorama

# 配置密钥（编辑cos_upload.py）
编辑 cos_upload.py

# 运行主程序
python main.py
```

## ⚙ 配置说明

1. **腾讯云密钥配置**  

   修改 cos_upload.py
   ```python
   secret_id = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxx'  # 替换实际SecretID
   secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx' # 替换实际SecretKey
   ```

2. **目录路径设置**  

   修改 main.py
   ```python
   directory_path = r"C:\Users\worker\Pictures\Blog_webp"  # 本地图片根目录
   ```

## 📂 目录结构

```
博客图片上传/
├── cos_upload.py    # COS上传核心逻辑
├── main.py          # 主控制流程
└── webp_convert.py  # 图片转换模块

本地图片目录/
└── Blog_webp/
    ├── 文章1/       # 自动同步为COS的images/blog/文章1
    ├── 文章2/
    └── _temp_output # 临时转换目录（自动清理）
```