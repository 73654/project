# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:10
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import find_area_image, Template
from pages.base.page import BasePage


class PageMine(BasePage):
    """我的"""
    page_name = "我的"

    @classmethod
    def qr_entry(cls):
        with dog.step(f"{cls.page_name}-进入二维码（相册分享）页面"):
            find_area_image(Template("PageMine_qr_entry_1.png"), target_rect=(0.7, 0.1, 1, 0.5), click=True)
            cls.wait_for_enter()
