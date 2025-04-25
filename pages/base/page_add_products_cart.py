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
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true


class PageAddProductsCart(BasePage):
    page_name = "加购商品页面"

    @classmethod
    def page_products_invoice(cls):
        with dog.step(f"{cls.page_name}-开单"):
            pass

    @classmethod
    def check_products_invoice(cls):
        with dog.step(f"{cls.page_name}-开单页面"):
            find_area_image(Template(r"tpl1745224676375.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            cls.wait_for_enter()
        with dog.step(f"{cls.page_name}-检查页面元素(存在下一步)"):
            assert_is_not_none(find_area_image(Template(r"tpl1745225145511.png"), target_rect=(get_vertical_rect(0.5))))
            assert_is_not_none(
                find_area_image(Template(r"tpl1745225176070.png"), target_rect=(get_vertical_rect(-0.15))))

        with dog.step(f"{cls.page_name}-返回主页面"):
            cls.back()
            find_area_image(Template(r"tpl1745225558744.png"), target_rect=(get_vertical_rect(-0.5)), click=True)

    @classmethod
    def page_clean_invoice(cls):
        with dog.step(f"{cls.page_name}-清理相册动态的原始数据"):
            pass

    @classmethod
    def page_products_buy(cls):
        with dog.step(f"{cls.page_name}-购买"):
            poco(text="购买").click()

    @classmethod
    def check_enter_order(cls):
        with dog.step(f"{cls.page_name}-购买"):
            assert_is_not_none(
                find_area_image(Template(r"tpl1745228536620.png"), target_rect=(get_vertical_rect(-0.15))))
            assert_is_not_none(
                find_area_image(Template(r"tpl1745228559364.png"), target_rect=(get_vertical_rect(0.15))))

    @classmethod
    def page_click_purchase(cls):
        with dog.step(f"{cls.page_name}-采购"):
            find_area_image(Template(r"tpl1745285497750.png"), target_rect=(get_vertical_rect(-0.15)), click=True)

    @classmethod
    def page_click_purchase_order(cls):
        with dog.step(f"{cls.page_name}-提交采购单"):
            find_area_image(Template(r"tpl1745285684851.png"), target_rect=(get_vertical_rect(-0.15)), click=True)

    @classmethod
    def page_phone_remind_window(cls):
        with dog.step(f"{cls.page_name}-手机号弹框确认提醒"):
            remind_window = find_area_image(Template(r"tpl1745285867680.png"), target_rect=(get_vertical_rect(-0.6)))
            if remind_window:
                find_area_image(Template(r"tpl1745285906008.png"), target_rect=(get_vertical_rect(-0.5)), click=True)
                cls.wait_for_enter()

    @classmethod
    def check_ensure_purchase(cls):
        with dog.step(f"{cls.page_name}-确认采购页"):
            assert_is_not_none(
                find_area_image(Template(r"tpl1745286360785.png"), target_rect=(get_vertical_rect(0.5)), click=True))
            assert_is_not_none(
                find_area_image(Template(r"tpl1745286379167.png"), target_rect=(get_vertical_rect(-0.3)), click=True))

    @classmethod
    def page_mine_shop_buy(cls):
        with dog.step(f"{cls.page_name}-立即购买"):
            find_area_image(Template(r"tpl1745288955520.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_commit_order_buy(cls):
        with dog.step(f"{cls.page_name}-立即购买"):
            find_area_image(Template(r"tpl1745289077466.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_no_pay_windows(cls):
        with dog.step(f"{cls.page_name}-无法支付弹框"):
            sleep(ui.step_wait_time)
            cls.wait_for_enter()
            no_pay = find_area_image(Template(r"tpl1745290337883.png"), target_rect=(get_vertical_rect(0.5)))
            if no_pay:
                find_area_image(Template(r"tpl1745290365367.png"), target_rect=(get_vertical_rect(-0.5)), click=True)

    @classmethod
    def check_purchase_pay_page(cls):
        with dog.step(f"{cls.page_name}-采购单支付页面"):
            assert_is_not_none(
                find_area_image(Template(r"tpl1745290793707.png"), target_rect=(get_vertical_rect(-0.35))))
            assert_is_not_none(
                find_area_image(Template(r"tpl1745290807759.png"), target_rect=(get_vertical_rect(0.5))))
