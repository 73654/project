# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 9:53
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import touch

from common import dog
from common.ui import Template, find_area_image
from common.ui.ui import get_vertical_rect, swipe_wait_for
from pages.base.page import BasePage


class PageWechat(BasePage):
    page_name = "微信页面操作"

    @classmethod
    def poster_publish(cls):
        """朋友圈点发布按钮"""
        with dog.step(f"{cls.page_name}-朋友圈点发布按钮"):
            find_area_image(Template(r"PageWechat_poster_publish_1.png", threshold=0.6), target_rect=(0, 0, 1, 0.1),
                            timeout=10,
                            click=True)

    @classmethod
    def enter_mini_program(cls):
        """识别小程序码"""
        with dog.step(f"{cls.page_name}-点击商品图片小程序码"):
            find_area_image(Template("PageWechat_enter_mini_program_1.png", threshold=0.6),
                            target_rect=(0, 0.2, 1, 0.8), click=True)

        with dog.step(f"{cls.page_name}-长安图片"):
            touch((0.5, 0.5), duration=3)

        with dog.step(f"{cls.page_name}-点击进入小程序"):
            find_area_image(Template(r"PageWechat_enter_mini_program_2.png"), target_rect=(0, 0.8, 1, 1), click=True)

    @classmethod
    def keep_weixin(cls):
        with dog.step(f"{cls.page_name}-是否留在微信弹框-点击留在微信"):
            find_area_image(Template(r"tpl1743674795976.png"), target_rect=get_vertical_rect(0.2, middle=True),
                            click=True)

    @classmethod
    def back_album(cls):
        with dog.step(f"{cls.page_name}-是否留在微信弹框-点击返回微商相册"):
            find_area_image(Template(r"tpl1743675572362.png"), target_rect=get_vertical_rect(0.2, middle=True),
                            click=True)

    @classmethod
    def send_to_file_assistant(cls):
        """发送到文件助手"""
        with dog.step(f"{cls.page_name}-查找'文件助手'并点击"):
            swipe_wait_for(Template(r"tpl1743670657392.png"), click=True)

        with dog.step(f"{cls.page_name}-点击发送按钮"):
            find_area_image(Template(r"tpl1743673978285.png"), target_rect=get_vertical_rect(-0.2), click=True)
