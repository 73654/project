# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:39
# Description:
# -------------------------------------------------------------------------
from airtest.core.assertions import assert_is_not_none

from common import dog, utils,ui
from common.ui import Template, find_area_image
from pages.base.page import BasePage
from common.ui import poco, Template, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe



class PageQrShare(BasePage):
    """分享我的相册页面（分享二维码）"""
    page_name = "我的-分享相册"

    @classmethod
    def _click_tab(cls, name):
        with dog.step(f"{cls.page_name}-点击{name}"):
            cls._tab_view(name)

    @classmethod
    def _tab_view(cls, name):
        pass

    @classmethod
    def _check_qr_code(cls, name):
        with dog.step(f"{cls.page_name}-解析“{name}”不为空"):
            if name == "小程序码":
                # poco.scroll("vertical", 0.35)
                assert_is_not_none(
                    find_area_image(Template("tpl1745806953109.png", threshold=0.6), target_rect=(0.25, 0.55, 0.8, 1)))
                # assert assert_is_not_none(
                #     find_area_image(Template("common_mini_qr.png", threshold=0.6), target_rect=(0, 0, 1, 0.8)))
            elif name == "二维码":
                assert_is_not_none(utils.parse_qr_code())
            else:
                # 收款码没有适配
                pass

    @classmethod
    def refresh(cls):
        with dog.step(f"{cls.page_name}-刷新二维码/小程序码"):
            find_area_image(Template("PageQrShare_refresh_1.png", threshold=0.6), target_rect=(0.8, 0, 1, 0.2), click=True)
            # poco(text="刷新成功").wait_for_appearance(timeout=5)
            # 是个toast不好捕获

    @classmethod
    def tab_qr(cls):
        cls._click_tab("二维码")

    @classmethod
    def tab_mini_qr(cls):
        cls.wait_for_enter()
        sleep(ui.step_wait_time)
        find_area_image(Template("tpl1745755795184.png"), target_rect=(0.3, 0.15, 0.75, 0.4),click=True)
        # cls._click_tab("小程序码")

    @classmethod
    def tab_payee_qr(cls):
        """收款码"""
        cls._click_tab("收款码")

    @classmethod
    def check_qr(cls):
        cls._check_qr_code("二维码")

    @classmethod
    def check_mini_qr(cls):
        cls._check_qr_code("小程序码")

    @classmethod
    def check_payee_qr(cls):
        """收款码"""
        cls._check_qr_code("收款码")


    @classmethod
    def tab_mini_qr_img(cls):
        with dog.step(f"{cls.page_name}-点击小程序码"):
            find_area_image(Template("tpl1745755795184.png"), target_rect=(0.35, 0.1, 0.7, 0.35), click=True)

