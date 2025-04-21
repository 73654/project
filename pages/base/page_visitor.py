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
from airtest.core.assertions import assert_exists, assert_is_not_none


class PageVisitor(BasePage):
    page_name = "访客足迹页面"

    @classmethod
    def check_page_visitor_title(cls):
        with dog.step(f"{cls.page_name}-访客足迹页面title"):
            assert_is_not_none(find_area_image(Template(r"tpl1745201812953.png"), target_rect=(get_vertical_rect(0.15))))



    @classmethod
    def check_page_visitor(cls):
        with dog.step(f"{cls.page_name}-验证访客足迹页面"):
            assert_is_not_none(find_area_image(Template(r"tpl1745201825564.png"), target_rect=(get_vertical_rect(0.4))))
            assert_is_not_none(find_area_image(Template(r"tpl1745203574539.png"), target_rect=(get_vertical_rect(0.4))))

