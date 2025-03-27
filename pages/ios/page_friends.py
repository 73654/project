# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 17:25
# Description:
# -------------------------------------------------------------------------
from common.ui import poco
from pages.base.page_friends import BasePageFriends


class IOSPageFriends(BasePageFriends):

    @staticmethod
    def _real_click(name):
        poco(type='WebView', name="WebView").offspring(type="Other", name="好友").offspring(type="StaticText",
                                                                                            name=name).click()
