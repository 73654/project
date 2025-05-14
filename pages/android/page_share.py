# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 16:38
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import Template, find_area_image, poco,touch_and_wait
from pages.base.page_share import PageShare, PageShare2


class AndroidPageShare(PageShare):
    page_name = "分享面板"

    @classmethod
    def _get_share_area(cls):
        poco(nameMatches=".*id/rv_share_entry", type="androidx.recyclerview.widget.RecyclerView")

    @classmethod
    def enable_mini_code(cls):
        super().enable_mini_code()
        pos = find_area_image(Template(r"tpl1747221535338.png", threshold=1), timeout=3,
                              target_rect=(0,0.38,0.25,0.55))
        if pos:
            touch_and_wait(pos)




class AndroidPageShare2(PageShare2):
    pass