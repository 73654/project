# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_add_products_cart
@ time:    2025/4/21 16:18 
@ desc:
"""
from pages.base.page import BasePage
from common import dog
from common.ui import poco
from pages.base.page_add_products_cart import PageAddProductsCart
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true
from airtest.core.api import text


class AndroidPageAddProductsCart(PageAddProductsCart):
    page_name = "加购商品页面"

    @classmethod
    def page_products_invoice(cls):
        with dog.step(f"{cls.page_name}-开单"):
            poco(text="开单").click()

    @classmethod
    def page_clean_invoice(cls):
        with dog.step(f"{cls.page_name}-清理相册动态的原始数据"):
            pass
            clean_search = poco("com.truedian.dragon:id/iv_search_clear")
            if clean_search:
                clean_search.click()
            text("通用26这是帮卖过来的商品")


    @classmethod
    def page_products_buy(cls):
        with dog.step(f"{cls.page_name}-购买"):
            poco(text="购买").click()
            cls.wait_for_enter()


