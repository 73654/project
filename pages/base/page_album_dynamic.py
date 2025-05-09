# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""
from airtest.core.api import text
from airtest.core.assertions import assert_exists, assert_is_not_none
from pages.base.page import BasePage
from common import dog, ui
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from common.ui import poco
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import DeviceType


class BasePageAlbumDynamic(BasePage):
    """相册动态页"""
    page_name = "相册动态页"

    @classmethod
    def text_search(cls):
        pass

    @classmethod
    def page_add_content(cls):
        cls.wait_for_enter()
        sleep(ui.step_wait_time)
        if ui.current_device_type == DeviceType.Android:
            find_area_image(Template(r"tpl1745402221872.png"), target_rect=(get_vertical_rect(0.2)), click=True)
        else:
            find_area_image(Template(r"tpl1746610655519.png"), target_rect=(get_vertical_rect(0.2)), click=True)

    @classmethod
    def page_release(cls):
        with dog.step(f"{cls.page_name}-发布"):
            pass
