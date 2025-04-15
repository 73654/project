# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_dynamic_detail
@ time:    2025/4/14 17:50 
@ desc:
"""
from common import dog
from pages.base.page import BasePage
from airtest.core.api import text
from common.ui import poco
from pages.base.page_dynamic_detail import PageDynamicDetail

class AndroidPageDynamicDetail(PageDynamicDetail):
    page_name = "动态相册页"

    @classmethod
    def table_commodity_top(cls):
        with dog.step(f"{cls.page_name}-动态详情页判断商品是否是置顶状态,并置顶该商品"):
            commodity_top = poco(text="置顶")
            commodity_pin = poco(text="取顶")
            if commodity_top:
                commodity_top.click()
                cls.wait_for_enter()
            elif commodity_pin:
                commodity_pin.click()
                cls.wait_for_enter()
                commodity_top.click()
        # with dog.step(f"{cls.page_name}-返回到好友table页"):
        #     for i in range(2):
        #         BasePage.back()

























