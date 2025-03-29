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
        jmcomic.download_album(s, option)
        file = [Comp.File(file=f"file:///D:\\jmcomic_files\\{s}.pdf",name=f"{s}.pdf")]  # 从本地文件目录发送pdf
        # file = [Comp.Image.fromFileSystem(f"D:\\jmcomic_files\\{event.message_str[3:]}.pdf")]  # 从本地文件目录发送pdf
        yield event.chain_result(file)
    # async def uploda_file(self, event: AstrMessageEvent):
    #       chain = [
    #           Comp.At(qq=event.get_sender_id()), # At 消息发送者
    #           Comp.Plain("你要的本子来了喵"),
    #       ]
    #       file = Comp.Image.fromFileSystem(f"D:\jmcomic_files\{event.message_str}.pdf") # 从本地文件目录发送pdf
    #       yield event.chain_result(chain)
    #       yield event.chain_result(file)




