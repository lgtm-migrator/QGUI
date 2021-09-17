# Author: Acer Zhang
# Datetime: 2021/9/17 
# Copyright belongs to the author.
# Please indicate the source for reprinting.
import os

from qgui import CreateQGUI
from qgui.bar_tools import BaseBarTool, GitHub
from qgui.notebook_tools import ChooseFileTextButton, RunButton
from qgui import MessageBox

import paddlehub as hub
import cv2

human_seg = hub.Module(name="deeplabv3p_xception65_humanseg")


def infer(info):
    img_path = info["img_path"]
    out_path = info["out_path"]

    # 简单做个判断，保证输入是正确的
    if not os.path.exists(img_path):
        MessageBox.info("请选择要分割的图片")
        # 不选择就不做预测了，气！
        return 1
    if not os.path.exists(out_path):
        MessageBox.info("请选择图片保存目录")
        return 2

    result = human_seg.segmentation(images=[cv2.imread(img_path)],
                                    visualization=True,
                                    output_dir=out_path)


# 创建主界面
main_gui = CreateQGUI(title="一个新应用")

# 在界面最上方添加一个按钮，链接到GitHub主页
main_gui.add_banner_tool(GitHub("https://github.com/QPT-Family/QGUI"))
# 在主界面部分添加一个文件选择工具，绑定刚刚创建的函数吧~
main_gui.add_notebook_tool(ChooseFileTextButton())
# 要不要再添加一个运行按钮？
main_gui.add_notebook_tool(RunButton(infer))
# 简单加个简介
main_gui.set_navigation_about(author="GT",
                              version="0.0.1",
                              github_url="https://github.com/QPT-Family/QGUI",
                              other_info=["欢迎加入QPT！"])
# 跑起来~
main_gui.run()
