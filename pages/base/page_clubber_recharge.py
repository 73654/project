# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_clubber_recharge
@ time:    2025/4/10 15:52 
@ desc:
"""
from airtest.core.assertions import assert_exists, assert_is_not_none
from pages.base.page import BasePage
from common import dog,ui
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from common.ui import poco
from airtest.core.api import home, keyevent, sleep, swipe

class PageClubberRecharge(BasePage):
    page_name = "会员充值页面操作"

    @classmethod
    def person_version(cls):
        with dog.step(f"{cls.page_name}-个人版续费-288"):
            pass

    @classmethod
    def shop_version(cls):
        with dog.step(f"{cls.page_name}-商城版续费-588"):
            pass

    @classmethod
    def team_version(cls):
        with dog.step(f"{cls.page_name}-团队版续费-1288"):
            pass

    @classmethod
    def downgrade_person_click(cls):
        with dog.step(f"{cls.page_name}-点击 降级续费288/年 "):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1744337129259.png"), target_rect=(0.5, 0.5, 1, 1),
                            click=True)

    @classmethod
    def downgrade_shop_click(cls):
        with dog.step(f"{cls.page_name}-点击 降级续费588/年 "):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1744355649295.png"), target_rect=(get_vertical_rect(-0.3)), click=True)

    @classmethod
    def choose_wechatpay(cls):
        """选择支付方式--微信"""
        pass

    @classmethod
    def choose_alipay(cls):
        """选择支付方式--支付宝"""
        pass

    @classmethod
    def choose_other_pay(cls):
        """选择支付方式--他人代付"""
        pass

    @classmethod
    def activation_confirmation(cls):
        """点击开通确认--同意并立即购买"""
        pass

    @classmethod
    def check_image_existence(cls, template_path, target_msg):
        """
        检查指定模板图片是否存在于各支付页面上
        :param template_path: 模板图片的路径
        :param target_msg: 检查的目标信息，用于日志记录
        """
        with dog.step(f"{cls.page_name}-{target_msg}"):
            cls.wait_for_enter()
            template = Template(template_path, threshold=0.7)
            result = find_area_image(template, target_rect=get_vertical_rect(0.5))
            assert_is_not_none(result, target_msg)

    @classmethod
    def check_wechat_pay(cls):
        """
        检查微信支付页面上的关键标识是否存在
        """
        check_items = [
            ("tpl1744342000194.png", "微信支付页面--存在288.00标识"),
            ("tpl1744342047832.png", "微信支付页面--存在微购科技标识"),
            ("tpl1744342063163.png", "微信支付页面--存在立即支付标识")
        ]

        for template_path, target_msg in check_items:
            cls.check_image_existence(template_path, target_msg)

    @classmethod
    def check_alipay_pay(cls):
        """
        检查支付宝支付页面上的关键标识是否存在
        """
        pass

    @classmethod
    def check_other_pay(cls):
        """检查他人代付页面"""
        with dog.step(f"{cls.page_name}-他人代付页面检查"):
            check_items = [
                ("tpl1744361990740.png", "他人代付页面含有文案标识"),

            ]

            for template_path, target_msg in check_items:
                cls.check_image_existence(template_path, target_msg)
