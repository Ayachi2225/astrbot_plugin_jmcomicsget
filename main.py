from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import jmcomic
import astrbot.api.message_components as Comp
import os,re

@register("jmcomicsget", "ayachi", "下载禁漫本子", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    @filter.command("jm")
    async def get_file(self,event):
        chain = [
            Comp.At(qq=event.get_sender_id()),  # At 消息发送者
            Comp.Plain("你要的本子在来的路上了嗷（大约还需要等待30s）"),
        ]
        yield event.chain_result(chain)
        message = event.message_str
        s=''.join(re.findall(r'\d+', message))
        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        target_file = os.path.join(current_dir, 'option.yml')
        option = jmcomic.JmOption.from_file(target_file)

        pdf_dir = os.path.join(current_dir, 'pdfs')
        os.makedirs(pdf_dir, exist_ok=True)
        for plugin_entry in option.plugins.after_photo:
            if plugin_entry.plugin == 'img2pdf':
                plugin_entry.kwargs.pdf_dir = pdf_dir
                break

        # 动态设置 base_dir 为当前目录下的 pdfs 文件夹（绝对路径）
        base_dir = os.path.join(current_dir, 'pdfs')
        os.makedirs(base_dir, exist_ok=True)
        option.dir_rule.base_dir = base_dir

        jmcomic.download_album(s, option)
        file = [Comp.File(file=f"file:///{pdf_dir}\\{s}.pdf",name=f"{s}.pdf")]  # 从本地文件目录发送pdf

        # file = [Comp.Image.fromFileSystem(f"D:\jmcomic_files\{event.message_str[3:]}.pdf")]  # 从本地文件目录发送pdf
        yield event.chain_result(file)





