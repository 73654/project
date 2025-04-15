# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 9:53
# Description:
# -------------------------------------------------------------------------

from pages.base.page_wechat import PageWechat
from common import dog, utils
from common.ui import Template, find_area_image,poco,get_vertical_rect


class AndroidPageWechat(PageWechat):
    page_name="微信--文件传输助手"

    @classmethod
    def wx_open_immediately(cls):
        """
        识别二维码--跳转打开app看款
        """
        with dog.step(f"{cls.page_name}-跳转关注成功,打开APP看款弹框就,点击立即打开"):
            cls.wait_for_enter()
            find_area_image(Template(r"tpl1744613095607.png"), target_rect=(0.4,0.4,0.9,0.7), click=True)
            cls.wait_for_enter()

        with dog.step(f"{cls.page_name}-跳转即将离开微信,打开'微商相册'"):
            find_area_image(Template(r"tpl1744613131416.png"), target_rect=(0.4, 0.4, 0.9, 0.7), click=True)



