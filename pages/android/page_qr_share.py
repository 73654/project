# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:39
# Description:
# -------------------------------------------------------------------------
from airtest.core.helper import log

from common.ui import poco
from pages.base.page_qr_share import PageQrShare


class AndroidPageQrShare(PageQrShare):

    @classmethod
    def _tab_view(cls, name):
        poco(nameMatches=".*id/wv", type="android.widget.FrameLayout").offspring(type="android.widget.TextView",
                                                                                 text=name).click()
