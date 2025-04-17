# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_place_order
@ time:    2025/4/17 17:44 
@ desc:
"""
from pages.base.page import BasePage
from common import dog
from common.ui import Template, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from common.ui import poco


class PagePlaceOrder(BasePage):
    page_name = "开单"

    @classmethod
    def page_place_customer(cls):
        with dog.step(f"{cls.page_name}-点击客户"):
            pass

    @classmethod
    def page_place_choose_customer(cls):
        with dog.step(f"{cls.page_name}-点击选择客户"):
            find_area_image(Template(r"tpl1744883934215.png"), target_rect=get_vertical_rect(0.3), click=True)
            cls.wait_for_enter()