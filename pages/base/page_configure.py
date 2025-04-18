# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_configure
@ time:    2025/4/18 17:29 
@ desc:
"""
from pages.base.page import BasePage
from common import dog, ui
from common.ui import poco
from common.ui.ui import Template,scroll_and_find_element


class PageConfigure(BasePage):
    page_name="设置页面"

    @classmethod
    def page_switch_account(cls):
        with dog.step(f"{cls.page_name}-点击切换账号"):
            scroll_and_find_element(max_scroll_times=3, target_rect=0.4, target_condition={'text': '切换账号'},
                                    click=True)
            cls.wait_for_enter()