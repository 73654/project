# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_team_permissons
@ time:    2025/4/24 16:48 
@ desc:
"""
from common import dog
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from pages.base.page_team_permissons import PageTeamPermissions


class AndroidPageTeamPermissions(PageTeamPermissions):
    page_name = "团队权限"


