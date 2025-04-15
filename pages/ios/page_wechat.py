# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 9:53
# Description:
# -------------------------------------------------------------------------


from pages.base.page_wechat import PageWechat
from common import dog, utils
from common.ui import Template, find_area_image,poco,get_vertical_rect

class IOSPageWechat(PageWechat):


    @classmethod
    def wx_open_immediately(cls):
        """
        识别二维码--跳转打开app看款
        """
        with dog.step(f"{cls.page_name}-ios-无法跳转，到这一步中止"):

            pass