# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    receive_and_payment
@ time:    2025/4/21 11:13 
@ desc:
"""

from pages.base.page import BasePage
from common import dog, ui
from common.ui import poco
from airtest.core.api import text
from common.ui import Template,find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait,long_click_custom
from airtest.core.api import home, keyevent, sleep, swipe

from pages.base.page_receive_and_payment import PageReceiveAndPayment

class IOSPageReceiveAndPayment(PageReceiveAndPayment):
    page_name = "收付款页面"

    @classmethod
    def page_send_friend_window(cls):
        with dog.step(f"{cls.page_name}-发送给朋友"):
            poco("发送给朋友").click()
            sleep(ui.step_wait_time)









