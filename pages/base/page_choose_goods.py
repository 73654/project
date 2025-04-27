# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_choose_goods
@ time:    2025/4/18 11:16 
@ desc:
"""
from pages.base.page import BasePage
from common import dog, ui
from common.ui import poco
from airtest.core.api import text
from common.ui import Template, find_area_image, get_vertical_rect, swipe_wait_for, get_horizontal_rect
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_exists, assert_is_not_none


class PageChooseGoods(BasePage):
    page_name = "选择商品"

    @classmethod
    def page_choose_goods(cls):
        with dog.step(f"{cls.page_name}-点击选择商品搜索"):
            find_area_image(Template(r"tpl1744945703678.png"), target_rect=(get_vertical_rect(0.2)), click=True)
            sleep(ui.step_wait_time)
            text("标题价格300元")
            sleep(ui.step_wait_time)
        with dog.step(f"{cls.page_name}-点击商品加购标识"):
            find_area_image(Template(r"tpl1744948106844.png"), target_rect=(get_vertical_rect(0.4)), click=True)
            sleep(ui.step_wait_time)

        with dog.step(f"{cls.page_name}-点击商品加购计数器"):
            find_area_image(Template(r"tpl1744948403372.png"), target_rect=(get_horizontal_rect(-0.15)), click=True)
            sleep(ui.step_wait_time)

        with dog.step(f"{cls.page_name}-点击添加"):
            find_area_image(Template(r"tpl1744957101942.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            sleep(ui.step_wait_time)

        with dog.step(f"{cls.page_name}-点击确认"):
            find_area_image(Template(r"tpl1744957352114.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            sleep(ui.step_wait_time)

    @classmethod
    def page_choose_next_step(cls):
        with dog.step(f"{cls.page_name}-点击下一步"):
            pass

    @classmethod
    def page_choose_confirm_order(cls):
        with dog.step(f"{cls.page_name}-点击确认开单"):
            pass

    @classmethod
    def page_choose_payment_status(cls):
        with dog.step(f"{cls.page_name}-选择收款状态"):
            pass

    @classmethod
    def check_order_complete(cls):
        with dog.step(f"{cls.page_name}-开单成功页面检查"):
            assert_is_not_none(
                find_area_image(Template(r"tpl1744958466513.png"), target_rect=(get_vertical_rect(0.5))))
            assert_is_not_none(
                find_area_image(Template(r"tpl1744958500468.png"), target_rect=(get_vertical_rect(0.5))))

    @classmethod
    def page_back_lever(cls):
        with dog.step(f"{cls.page_name}-返回上一层"):
            cls.back()
            sleep(ui.step_wait_time)


