## 背景介绍

个人在写博客的时候，喜欢在本地 Obsidian 上先写笔记，然后才会上传到博客网站上。为了保证小站的运行速度，个人习惯于将笔记中的 PNG 图片转换为 Webp 格式然后再上传到腾讯对象存储上。但是时间一长就觉得麻烦了，所以有了这个脚本。该脚本主要实现的是将目标文件夹进行处理，将其中的图片转换为 Webp，然后根据当前的文件结构上传到 COS 上。

## 程序介绍

程序主要有三个文件。

- `main.py`: 主程序
- `ebp_convert.py`: Webp 转换
- `cos_upload.py`: COS 上传

请在`cos_upload.py`中填写你的 COS 信息

在`main.py`中填写本地中存放将要转换为 webp 格式的文件夹路径到`directory_path`变量中，程序支持的文件夹结构如下。

- 主文件夹（本地）
  - 子文件夹 1
  - 子文件夹 2
  - 子文件夹 3
  - ...

在主文件下需要存在子文件，设置成这样是因为个人习惯为每个文章单独配置一个图片素材文件夹。对于这个结构来说，`directory_path`变量所代表的就是`主文件夹（本地）`的绝对路径。程序会将下`主文件夹（本地）`的所有图片转换为 Webp 格式，然后将子文件夹上传到目标 COS 上。

> 注意！！！图片转换后只会保留 Webp 格式的图片，原有的图片会被删除！！！

除了本地路径外，还请填写 COS 中的路径到`cos_dir`变量中，最终上传到 COS 的文件夹结构如下

- 主文件夹（COS 上）
  - 子文件夹 1
  - 子文件夹 2
  - 子文件夹 3
  - ...

`cos_dir`所代表的为`主文件夹（COS 上）`的路径，程序会在该目录下上传`主文件夹（本地）`下的子文件夹。

最终用 python 直接运行`main.py`即可
