# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_place_order
@ time:    2025/4/17 17:44 
@ desc:
"""
from pages.base.page import BasePage
from common import dog,ui
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from common.ui import poco
from pages.base.page_place_order import PagePlaceOrder
from airtest.core.api import home, keyevent, sleep, swipe


class AndroidPagePlaceOrder(PagePlaceOrder):
    page_name = "开单"

    @classmethod
    def page_place_customer(cls):
        with dog.step(f"{cls.page_name}-客户"):
            poco(text="客户").click()
            sleep(ui.step_wait_time)



    @classmethod
    def page_place_delivery_mode(cls):
        with dog.step(f"{cls.page_name}-发货方式"):
            poco(text="发货方式").click()


    @classmethod
    def page_place_delivery_choose(cls):
        with dog.step(f"{cls.page_name}-选择发货方式"):
            poco(text="快递").click()



    @classmethod
    def page_place_delivery_information(cls):
        with dog.step(f"{cls.page_name}-选择收货信息"):
            poco(text="收货信息").click()
            cls.wait_for_enter()

    @classmethod
    def page_place_choose_goods(cls):
        with dog.step(f"{cls.page_name}-选择商品"):
            poco(text="选择商品").click()
            cls.wait_for_enter()

