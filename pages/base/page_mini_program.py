# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 15:27
# Description:
# -------------------------------------------------------------------------
from airtest.core.assertions import assert_is_not_none, assert_true

from common import dog
from common.ui import find_area_image, Template, get_vertical_rect
from pages.base.page import BasePage


class PageMiniProgram(BasePage):
    page_name = "小程序页面的操作"

    @classmethod
    def check_buy_button(cls):
        with dog.step(f"{cls.page_name}-查看商品是否存在'立即购买'按钮"):
            assert_is_not_none(find_area_image(Template(r"tpl1744007002446.png"), target_rect=get_vertical_rect(-0.2)))

    @classmethod
    def check_enter_mini_program(cls):
        with dog.step(f"{cls.page_name}-确认是否进入小程序，并且不是白屏"):
            cls.wait_for_enter()
            assert_is_not_none(find_area_image(Template(r"tpl1744080381046.png"), target_rect=get_vertical_rect(-0.1)))
