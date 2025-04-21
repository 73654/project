# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_visitor
@ time:    2025/4/21 10:10 
@ desc:
"""
from common import dog
from common.ui import find_area_image, Template, get_vertical_rect, touch_and_wait
from pages.base.page import BasePage
from pages.base.page_visitor import PageVisitor


class AndroidPageVisitor(PageVisitor):
    page_name = "访客足迹页面"



