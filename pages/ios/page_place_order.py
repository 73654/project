# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_place_order
@ time:    2025/4/17 17:44 
@ desc:
"""
from pages.base.page_place_order import PagePlaceOrder
from pages.base.page import BasePage
from common import dog
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from common.ui import poco





class IOSPagePlaceOrder(PagePlaceOrder):
    page_name = "开单"

    @classmethod
    def page_place_customer(cls):
        with dog.step(f"{cls.page_name}-点击客户"):
            poco("客户").click()