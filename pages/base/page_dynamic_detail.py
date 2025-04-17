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


class PageDynamicDetail(BasePage):
    page_name = "动态相册页"

    @classmethod
    def table_commodity_top(cls):
        with dog.step(f"{cls.page_name}-动态详情页判断商品是否是置顶状态,并置顶该商品"):
            pass


    @classmethod
    def back_to_friend_page(cls):
        with dog.step(f"{cls.page_name}-返回到好友页"):
            for i in range(2):
                cls.back()


    @classmethod
    def back_shop_page(cls):
        with dog.step(f"{cls.page_name}-返回到个人相册页"):
            cls.back()

    @classmethod
    def table_refresh(cls):
        with dog.step(f"{cls.page_name}-动态详情页--点击刷新按钮"):
            pass
















