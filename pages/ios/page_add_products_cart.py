# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_add_products_cart
@ time:    2025/4/21 16:18 
@ desc:
"""
from pages.base.page import BasePage
from common import dog,ui
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import poco, Template, find_area_image, touch_and_wait
from pages.base.page_add_products_cart import PageAddProductsCart
from airtest.core.api import text
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true

class IOSPageAddProductsCart(PageAddProductsCart):
    page_name = "加购商品页面"

    @classmethod
    def page_products_invoice(cls):
        with dog.step(f"{cls.page_name}-开单"):
            poco("开单").click()

    @classmethod
    def page_clean_invoice(cls):
        with dog.step(f"{cls.page_name}-清理相册动态的原始数据"):
            clean_search=find_area_image(Template(r"tpl1746784587982.png"), target_rect=(0.7, 0.03, 1, 0.14))

            if clean_search:
                touch_and_wait(clean_search)
            sleep(ui.step_wait_time)
            text("通用26这是帮卖过来的商品")



    @classmethod
    def page_products_buy(cls):
        with dog.step(f"{cls.page_name}-购买"):
            sleep(ui.step_wait_time)
            poco("购买").click()
            cls.wait_for_enter()


