# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_clubber_recharge
@ time:    2025/4/10 16:13 
@ desc:
"""
from common.ui import poco
from pages.base.page_clubber_recharge import PageClubberRecharge
from common import dog,ui
from airtest.core.api import home, keyevent, sleep, swipe

class IOSPageClubberRecharge(PageClubberRecharge):

    @classmethod
    def person_version(cls):
        poco("288").click()

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
            poco("同意并立即购买").click()
            cls.wait_for_enter()


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
                ("tpl1744356134925.png", "微信支付页面--存在588.00标识")
            ]

            for template_path, target_msg in check_items:
                cls.check_image_existence(template_path, target_msg)