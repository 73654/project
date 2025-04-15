# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_clubber_recharge
@ time:    2025/4/10 16:13 
@ desc:
"""
from airtest.core.assertions import assert_exists
from common.ui import Template, find_area_image, poco, swipe_up,get_vertical_rect

from pages.base.page_clubber_recharge import PageClubberRecharge
from common.ui import poco
from common import dog

class AndroidPageClubberRecharge(PageClubberRecharge):
    page_name = "会员充值页面操作"

    @classmethod
    def person_version(cls):
        poco(text="¥288").click()

    @classmethod
    def shop_version(cls):
        poco(text="¥588").click()


    @classmethod
    def team_version(cls):
        poco(text="¥988").click()

    @classmethod
    def activation_confirmation(cls):
        with dog.step(f"{cls.page_name}-点击开通确认--同意并立即购买"):
            poco(text="同意并立即购买").click()
            cls.wait_for_enter()


    @classmethod
    def choose_wechatpay(cls):
        """选择支付方式--微信"""
        poco(text="微信支付").click()


    @classmethod
    def choose_alipay(cls):
        """选择支付方式--支付宝"""
        poco(text="支付宝").click()


    @classmethod
    def choose_other_pay(cls):
        """选择支付方式--他人代付"""
        poco(text="他人代付").click()


    @classmethod
    def check_alipay_pay(cls):
        """
        检查支付宝支付页面上的关键标识是否存在
        """
        pass




