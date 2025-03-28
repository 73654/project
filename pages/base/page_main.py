# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 18:01
# Description:
# -------------------------------------------------------------------------

from common import dog
from pages.base.page import BasePage


class BasePageMain(BasePage):
    """主页"""
    @staticmethod
    def _real_click(name):
        pass

    @classmethod
    def _base_click(cls, name):
        with dog.step(f"点击首页-{name}"):
            cls._real_click(name)

    @classmethod
    def tab_dynamic(cls):
        """动态"""
        cls._base_click("动态")

    @classmethod
    def tab_friends(cls):
        """好友"""
        cls._base_click("好友")

    @classmethod
    def tab_workbench(cls):
        """工作台"""
        cls._base_click("工作台")

    @classmethod
    def tab_message(cls):
        """消息"""
        cls._base_click("消息")

    @classmethod
    def tab_mine(cls):
        """我的"""
        cls._base_click("我的")
