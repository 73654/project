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
from airtest.core.assertions import assert_not_equal

class AndroidPageDynamicDetail(PageDynamicDetail):
    page_name = "动态相册页"

    @classmethod
    def _handle_commodity_status(cls, first_text, second_text):
        with dog.step(f"{cls.page_name}-动态详情页处理商品状态"):
            first_button = poco(text=first_text)
            second_button = poco(text=second_text)
            if first_button:
                first_button.click()
                cls.wait_for_enter()
            elif second_button:
                second_button.click()
                cls.wait_for_enter()
                first_button.click()

    @classmethod
    def table_commodity_top(cls):
        cls._handle_commodity_status("置顶", "取顶")

    @classmethod
    def table_commodity_obtain_top(cls):
        cls._handle_commodity_status("取顶", "置顶")


    @classmethod
    def back_shop_page(cls):
        with dog.step(f"{cls.page_name}-返回到个人相册页"):
            cls.back()
            cls.wait_for_enter()

        with dog.step(f"{cls.page_name}-个人相册页置顶区域不存在验证商品置顶刷新"):
            assert_not_equal(poco("com.truedian.dragon:id/title_home_fragment").get_text(), "验证商品置顶刷新",
                             msg="验证置顶区域不存在验证商品置顶刷新")


    @classmethod
    def table_refresh(cls):
        with dog.step(f"{cls.page_name}-动态详情页--点击刷新按钮"):
            poco("com.truedian.dragon:id/refresh_btn").click()


















