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
from common.ui import Template,scroll_and_find_element
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import DeviceType

class PageConfigure(BasePage):
    page_name="设置页面"

    @classmethod
    def page_switch_account(cls):
        with dog.step(f"{cls.page_name}-点击切换账号"):
            if ui.current_device_type == DeviceType.Android:
                scroll_and_find_element(max_scroll_times=3, target_rect=0.4, target_condition={'text': '切换账号'},
                                    click=True)
            else:
                poco("切换账号").click()
            cls.wait_for_enter()

    @classmethod
    def page_config_click(cls):
        with dog.step(f"{cls.page_name}-点击切换test01账号"):
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template(r"tpl1745199684884.png"), target_rect=(get_vertical_rect(0.5)), click=True)
            else:
                find_area_image(Template(r"tpl1745199684884.png",threshold=0.6), target_rect=(get_vertical_rect(0.5)), click=True)
            cls.wait_for_enter()


    @classmethod
    def page_config_other_click(cls):
        with dog.step(f"{cls.page_name}-点击切换冒泡账号"):
            find_area_image(Template(r"tpl1745202515162.png"), target_rect=(get_vertical_rect(0.5)), click=True)
            cls.wait_for_enter()



