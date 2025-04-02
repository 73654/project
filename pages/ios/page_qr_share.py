# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:39
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import poco
from pages.base.page_qr_share import PageQrShare


class IOSPageQrShare(PageQrShare):

    @classmethod
    def _tab_view(cls, name):
        with dog.title(f"我的-分享相册-点击{name}"):
            poco(type="WebView", name="WebView").offspring(type="Other", name="分享相册").offspring(
                type="StaticText", name=name).click()
