# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 16:38
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import touch

from common import dog
from common.ui import Template, find_area_image
from pages.base.page_share import PageShare


class IOSPageShare(PageShare):
    page_name = "分享面板"

    @classmethod
    def _get_share_area(cls):
        return 0, 0.4, 1, 1

    @classmethod
    def enable_mini_code(cls):
        super().enable_mini_code()
        pos = find_area_image(Template(r"IOSPageShare_enable_mini_code_1.png", threshold=0.9), timeout=3,
                              target_rect=cls._get_share_area())
        if pos:
            touch(pos)
