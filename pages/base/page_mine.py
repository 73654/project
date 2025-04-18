# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:10
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import find_area_image, Template, get_vertical_rect, touch_and_wait
from pages.base.page import BasePage


class PageMine(BasePage):
    """我的"""
    page_name = "我的"

    @classmethod
    def qr_entry(cls):
        with dog.step(f"{cls.page_name}-进入二维码（相册分享）页面"):
            find_area_image(Template("PageMine_qr_entry_1.png"), target_rect=(0.7, 0.2, 1, 0.4), click=True)
            cls.wait_for_enter()

            # 第一次进入会弹框，点取消
            pos = find_area_image(Template(r"tpl1744091568935.png"), target_rect=get_vertical_rect(-0.15))
            if pos:
                touch_and_wait(pos)


    @classmethod
    def clubber(cls):
        with dog.step(f"{cls.page_name}-进入会员(充值)页面"):
            find_area_image(Template(r"tpl1744264284483.png"), target_rect=get_vertical_rect(0.3),click=True)
            cls.wait_for_enter()

    @classmethod
    def page_mine_configure(cls):
        with dog.step(f"{cls.page_name}-设置标识"):
            find_area_image(Template(r"tpl1744963717160.png"), target_rect=get_vertical_rect(0.12), click=True)
            cls.wait_for_enter()

