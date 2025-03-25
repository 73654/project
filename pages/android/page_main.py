# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/24 20:24
# Description:
# -------------------------------------------------------------------------
from common.ui import poco


class PageMain:

    @staticmethod
    def tab_dynamic():
        poco("动态").click()

    @staticmethod
    def tab_friends():
        poco("好友").click()

    @staticmethod
    def tab_workbench():
        poco("工作台").click()

    @staticmethod
    def tab_message():
        poco("消息").click()

    @staticmethod
    def tab_mine():
        poco("我的").click()