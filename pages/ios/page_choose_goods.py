# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_choose_goods
@ time:    2025/4/18 11:16 
@ desc:
"""
from pages.base.page import BasePage
from common import dog,ui
from common.ui import poco
from airtest.core.api import text
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, get_horizontal_rect
from airtest.core.api import home, keyevent, sleep, swipe
from pages.base.page_choose_goods import PageChooseGoods

class IOSPageChooseGoods(PageChooseGoods):
    page_name="选择商品"


    @classmethod
    def page_choose_next_step(cls):
        with dog.step(f"{cls.page_name}-点击下一步"):
            poco("下一步").click()


    @classmethod
    def page_choose_confirm_order(cls):
        with dog.step(f"{cls.page_name}-点击确认开单"):
            poco("确认开单").click()



    @classmethod
    def page_choose_payment_status(cls):
        with dog.step(f"{cls.page_name}-选择收款状态"):
            poco("已私下收款").click()