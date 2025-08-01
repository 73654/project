from common import dog,ui

from pages.base.page import BasePage
from common.ui import find_feature_until_end, poco, find_node_until_end
from common.ui import DeviceType
from airtest.core.assertions import assert_true
import time

class BasePageLogin(BasePage):
    """国服SDK登录页面"""
    page_name = "国服SDK登录页面"

    @staticmethod
    def _real_click(name):
        pass

    @classmethod
    def _base_click(cls, name):
        with dog.step(f"f{cls.page_name}-点击{name}"):
            cls._real_click(name)
            cls.wait_for_enter()

    @classmethod
    def login(cls):
        """登录"""
        with dog.step(f"{cls.page_name}-接受用户条款"):
            find_node_until_end(["jieshou"])
            poco(text = "接受").click()
            cls.take_step_screenshot("接受用户条款")

        with dog.step(f"{cls.page_name}-同意用户协议"):
            find_node_until_end(["tongyi"])
            poco(resourceId="com.lmbl.im30.cn:id/mr_it_account_login_entry_dialog_cb").click()
            cls.take_step_screenshot("同意用户协议")

        with dog.step(f"{cls.page_name}-切换邮箱登录"):
            find_node_until_end(["email"])
            poco(desc="IM30邮箱").click()
            cls.take_step_screenshot("切换邮箱登录")
            
        with dog.step(f"{cls.page_name}-填写邮箱账号"):
            email_input = poco(resourceId="com.lmbl.im30.cn:id/mr_it_account_email_login_dialog_email_et")
            email_input.set_text("zhishi@corp.im30.net")
            cls.take_step_screenshot("填写邮箱账号")
            
        with dog.step(f"{cls.page_name}-填写邮箱密码"):
            password_input = poco(resourceId="com.lmbl.im30.cn:id/mr_it_account_email_login_dialog_password_et")
            password_input.set_text("Qq65742472")
            cls.take_step_screenshot("填写邮箱密码")
            
        with dog.step(f"{cls.page_name}-点击登录"):
            poco(resourceId="com.lmbl.im30.cn:id/mr_it_account_email_login_dialog_login_btn").click()
            cls.take_step_screenshot("点击登录")