# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 17:25
# Description:
# -------------------------------------------------------------------------
from common.ui import poco
from pages.base.page_friends import BasePageFriends


class AndroidPageFriends(BasePageFriends):

    @staticmethod
    def _real_click(name):
        poco(nameMatches=".*id/wv", type="android.widget.FrameLayout").offspring(type="android.widget.TextView",
                                                                                 name="android.widget.TextView",
                                                                                 text=name).click()
