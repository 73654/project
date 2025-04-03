# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 15:27
# Description:
# -------------------------------------------------------------------------
from airtest.core.assertions import assert_is_not_none

from common import dog
from common.ui import find_area_image, Template
from pages.base.page import BasePage


class PageMiniProgram(BasePage):
    page_name = "小程序页面的操作"

    @classmethod
    def check_goods_show(cls):
        with dog.step(f"{cls.page_name}-查看图片商品展示是后正确"):
            assert_is_not_none(find_area_image(Template(r"PageMiniProgram_check_goods_show_1.png"), target_rect=(0, 0.8, 0.5, 1)))
