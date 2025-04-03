# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 9:53
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import touch

from common import dog
from common.ui import Template, find_area_image
from pages.base.page import BasePage


class PageWechat(BasePage):
    page_name = "微信页面操作"

    @classmethod
    def poster_publish(cls):
        """朋友圈点发布按钮"""
        with dog.step(f"{cls.page_name}-朋友圈点发布按钮"):
            find_area_image(Template(r"PageWechat_poster_publish_1.png", threshold=0.6), target_rect=(0, 0, 1, 0.1), timeout=10,
                            click=True)

    @classmethod
    def enter_mini_program(cls):
        """识别小程序码"""
        with dog.step(f"{cls.page_name}-点击商品图片小程序码"):
            find_area_image(Template("PageWechat_enter_mini_program_1.png", threshold=0.6), target_rect=(0, 0.2, 1, 0.8), click=True)

        with dog.step(f"{cls.page_name}-长安图片"):
            touch((0.5, 0.5), duration=3)

        with dog.step(f"{cls.page_name}-点击进入小程序"):
            find_area_image(Template(r"PageWechat_enter_mini_program_2.png"), target_rect=(0, 0.8, 1, 1), click=True)
