# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 17:25
# Description:
# -------------------------------------------------------------------------
from common import dog
from pages.base.page import BasePage


class BasePageFriends(BasePage):
    """主页-好友页面"""
    @staticmethod
    def _real_click(name):
        pass

    @classmethod
    def _base_click(cls, name):
        with dog.step(f"点击好友列表-{name}"):
            cls._real_click(name)

    @classmethod
    def fans_and_customers(cls):
        """粉丝与客户"""
        cls._base_click("粉丝与客户")

    @classmethod
    def transfer_agent(cls):
        """转图代理"""
        cls._base_click("转图代理")

    @classmethod
    def seller_agent(cls):
        """帮卖代理"""
        cls._base_click("帮卖代理")

    @classmethod
    def extension_agent(cls):
        """帮卖代理"""
        cls._base_click("推广员")

    @classmethod
    def my_album(cls):
        """帮卖代理"""
        cls._base_click("我的相册")

    @classmethod
    def goto_album(cls, album_name):
        """进入到列表其他相册中去"""
        cls._base_click(name=album_name)
