# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_mobile_phone_album
@ time:    2025/4/25 13:47 
@ desc:
"""
from airtest.core.assertions import assert_is_not_none, assert_true

from common import dog, ui
from common.ui import poco, find_area_image, Template, get_vertical_rect, touch_and_wait, scroll_and_find_element
from pages.base.page import BasePage
from pages.base.page_mobile_phone_album import PageMobilePhoneAlbum
from airtest.core.api import home, keyevent, sleep, swipe,double_click


class IOSPageMobilePhoneAlbum(PageMobilePhoneAlbum):
    page_name = "手机相册"

    @classmethod
    def page_mobile_phone(cls):
        with dog.step(f"{cls.page_name}-选择相册中的第一张图片"):

            sleep(ui.step_wait_time)
            test_mobile_phone=poco("Window").child("Other")[1].child("Other").offspring("CollectionView").child("Cell")[-1].child(
                "Other").child("Image")[0]
            if test_mobile_phone:
                test_mobile_phone.click()
            else:
                find_area_image(Template(r"tpl1747118474530.png", threshold=0.6),target_rect=(0.1,0.4,1,0.84),click=True)

            sleep(ui.step_wait_time)
            poco.scroll("vertical", -0.6)
            sleep(ui.step_wait_time)
            test_picture=find_area_image(Template(r"tpl1747099980742.png"), target_rect=(0.05,0.3,1,0.8))
            if test_picture:
                double_click(test_picture)

            sleep(ui.step_wait_time)

    @classmethod
    def page_mobile_img_enter(cls):
        with dog.step(f"{cls.page_name}-确认"):
            test_img_enter=find_area_image(Template(r"tpl1747107585030.png"), target_rect=(0.7, 0.87, 1, 1))
            if test_img_enter:
                touch_and_wait(test_img_enter)
            cls.wait_for_enter()
