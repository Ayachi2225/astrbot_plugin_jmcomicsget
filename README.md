# jmcomicsget

~~封号模拟器~~ AstrBot 插件

A template plugin for AstrBot 

本插件主要依赖于jmcomic和astrbot
jmcomic包详细使用请查阅：https://github.com/hect0x7/JMComic-Crawler-Python
本插件默认安装jmcomic中转pdf插件和获取浏览器cookies插件，若希望进一步实现其他功能请查阅上述jmcomic源项目
安装：请将clone本插件到"AstrBot\data\plugins"中
(后续更新也在这里)
\```bash
git clone https://github.com/Ayachi2225/astrbot_plugin_jmcomicsget.git
\```

默认下载文件保存到D:\jmcomic_files，如需修改请修改option.yml文件中base_url和plugin项pdf_dir中地址（修改后还要修改main.py中读取pdf文件位置）
ps：目前本插件仅能借助napcat发送文件（lagrange不行），且仅在qq个人号windows napcat上成功运行了。

后续更新：
我猜现在估计只能下载单本本子，多章本子估计报错，后续可能改进
