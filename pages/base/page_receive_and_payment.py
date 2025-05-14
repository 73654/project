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
from common.ui import Template,find_area_image, get_vertical_rect,long_click_custom,swipe_wait_for
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import DeviceType

class PageReceiveAndPayment(BasePage):
    page_name = "收付款页面"


    @classmethod
    def page_click_payment_code(cls):
        with dog.step(f"{cls.page_name}-长按点击付款码"):
            if ui.current_device_type == DeviceType.Android:
                payment_code = find_area_image(Template(r"tpl1745217541605.png"), target_rect=(get_vertical_rect(0.6)))
                if payment_code:
                    long_click_custom(payment_code)
                    sleep(ui.step_wait_time)
            else:
                poco("保存").click()
                sleep(ui.step_wait_time)
                poco("立即添加").click()
                sleep(ui.step_wait_time)
                poco("微信").click()




    @classmethod
    def page_send_friend_window(cls):
        with dog.step(f"{cls.page_name}-发送给朋友"):
            pass











