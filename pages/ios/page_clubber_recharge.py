# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_clubber_recharge
@ time:    2025/4/10 16:13 
@ desc:
"""
from common.ui import poco
from pages.base.page_clubber_recharge import PageClubberRecharge
from common import dog, ui
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait


class IOSPageClubberRecharge(PageClubberRecharge):

    @classmethod
    def person_version(cls):
        with dog.step(f"{cls.page_name}-点击云相册版-288"):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1746584621042.png"), target_rect=(0.05, 0.35, 0.25, 0.5), click=True)



    @classmethod
    def shop_version(cls):
        sleep(ui.step_wait_time)
        poco("588").click()

    @classmethod
    def team_version(cls):
        poco("988").click()

    @classmethod
    def activation_confirmation(cls):
        with dog.step(f"{cls.page_name}-点击开通确认--同意并立即购买"):
            find_area_image(Template(r"tpl1746582844319.png"), target_rect=(0.2,0.45,0.8,0.7), click=True)

    @classmethod
    def choose_wechatpay(cls):
        """选择支付方式--微信"""
        poco("微信支付").click()

    @classmethod
    def choose_alipay(cls):
        """选择支付方式--支付宝"""
        poco("支付宝").click()

    @classmethod
    def choose_other_pay(cls):
        """选择支付方式--他人代付"""
        poco("他人代付").click()

    @classmethod
    def check_alipay_pay(cls):
        """
        检查支付宝支付页面上的关键标识是否存在
        """
        with dog.step(f"{cls.page_name}-支付宝付款页面检查"):
            check_items = [
                ("tpl1744356134925.png", "支付宝支付页面--存在588.00标识")
            ]

            for template_path, target_msg in check_items:
                cls.check_image_existence(template_path, target_msg)
