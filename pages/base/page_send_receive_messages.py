# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_send_receive_messages
@ time:    2025/4/18 10:18 
@ desc:
"""

from pages.base.page import BasePage
from common import dog,ui
from common.ui import poco
from airtest.core.api import text
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe


class PageSendReceiveMessages(BasePage):
    page_name = "收发信息"

    @classmethod
    def page_receive_historical_address(cls):
        with dog.step(f"{cls.page_name}-点击历史地址"):
            pass


    @classmethod
    def page_receive_search(cls):
        with dog.step(f"{cls.page_name}-点击历史地址搜索"):
            find_area_image(Template(r"tpl1744944380314.png"), target_rect = (get_vertical_rect(0.4)), click = True)
            sleep(ui.step_wait_time)
            text("15827416521")

        with dog.step(f"{cls.page_name}-确认历史地址"):
            find_area_image(Template(r"tpl1744944948533.png"), target_rect=(get_vertical_rect(0.6)), click=True)
            cls.wait_for_enter()











