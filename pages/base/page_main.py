# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 18:01
# Description:
# -------------------------------------------------------------------------

from common import dog,ui
from pages.base.page import BasePage
from common.ui import find_feature_until_end, Template, get_vertical_rect, touch_and_wait
from common.ui import DeviceType
from common.utils import auto_screenshot
from airtest.core.assertions import assert_true
import time

class BasePageMain(BasePage):
    """首页"""
    page_name = "首页"

    @staticmethod
    def _real_click(name):
        pass

    @classmethod
    def _base_click(cls, name):
        with dog.step(f"f{cls.page_name}-点击{name}"):
            cls._real_click(name)
            cls.wait_for_enter()

    @classmethod
    @auto_screenshot("登录页面截图")
    def login(cls):
        """登录"""
        with dog.step(f"{cls.page_name}-找到小手"):
            find_feature_until_end(end_feature_names=["hand"], feature_names=["skip", "duihuakuang1", "duihuakuang2", "new_game"])
        with dog.step(f"{cls.page_name}-进入瞄准"):
            find_feature_until_end(end_feature_names=["miaozhun"], feature_names=["skip", "hand", "duihuakuang1", "duihuakuang2"])
        with dog.step(f"{cls.page_name}-进入搜索"):
            find_feature_until_end(end_feature_names=["search"], feature_names=["skip", "miaozhun", "duihuakuang1", "duihuakuang2", "miaozhun2"])
        with dog.step(f"{cls.page_name}-进入日记"):
            find_feature_until_end(end_feature_names=["riji"], feature_names=["skip", "search", "hand", "duihuakuang1", "duihuakuang2", "id_card"])
        with dog.step(f"{cls.page_name}-进入翻页"):
            find_feature_until_end(end_feature_names=["fanye"], feature_names=["skip", "riji", "hand", "duihuakuang1", "duihuakuang2"])