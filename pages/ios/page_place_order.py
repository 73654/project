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


    @classmethod
    def page_place_delivery_mode(cls):
        with dog.step(f"{cls.page_name}-发货方式"):
            poco("发货方式").click()
            cls.wait_for_enter()

    @classmethod
    def page_place_delivery_choose(cls):
        with dog.step(f"{cls.page_name}-选择发货方式"):
            poco("快递").click()


    @classmethod
    def page_place_delivery_information(cls):
        with dog.step(f"{cls.page_name}-选择收货信息"):
            poco("收货信息").click()

    @classmethod
    def page_place_choose_goods(cls):
        with dog.step(f"{cls.page_name}-选择商品"):
            poco("选择商品").click()
            cls.wait_for_enter()