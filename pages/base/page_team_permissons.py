# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_team_permissons
@ time:    2025/4/24 16:48 
@ desc:
"""
from common import dog
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from pages.base.page import BasePage


class PageTeamPermissions(BasePage):
    page_name = "团队权限"

    @classmethod
    def check_team_permissions_price(cls):
        with dog.step(f"{cls.page_name}-检查团队权限商品价格"):
            find_area_image(Template(r"tpl1745487293604.png"), target_rect=(get_vertical_rect(0.5)))
            find_area_image(Template(r"tpl1745487303549.png"), target_rect=(get_vertical_rect(0.6)))
            find_area_image(Template(r"tpl1745485385524.png"), target_rect=(get_vertical_rect(0.45)))

    @classmethod
    def check_team_statistical_data(cls):
        with dog.step(f"{cls.page_name}-断言数据统计权限"):
            find_area_image(Template(r"tpl1745494060451.png"), target_rect=(get_vertical_rect(0.5)))
            find_area_image(Template(r"tpl1745494051249.png"), target_rect=(get_vertical_rect(-0.6)))

