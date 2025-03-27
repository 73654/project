# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/24 20:24
# Description:
# -------------------------------------------------------------------------
from common.ui import poco
from pages.base.page_main import BasePageMain


class IOSPageMain(BasePageMain):
    @staticmethod
    def _real_click(name):
        poco(type='TabBar', name='标签页栏').offspring(type="StaticText", name=name).click()
