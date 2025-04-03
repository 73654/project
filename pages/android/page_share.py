# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 16:38
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import Template, find_area_image, poco
from pages.base.page_share import PageShare


class AndroidPageShare(PageShare):
    page_name = "分享面板"

    @classmethod
    def _get_share_area(cls):
        poco(nameMatches=".*id/rv_share_entry", type="androidx.recyclerview.widget.RecyclerView")

    @classmethod
    def enable_mini_code(cls):
        super().enable_mini_code()
        mini = poco(nameMatches=".*:id/cb_mini_code")
        if not mini.attr("checked"):
            mini.click()
