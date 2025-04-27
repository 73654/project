# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_mobile_phone_album
@ time:    2025/4/25 13:47 
@ desc:
"""
from airtest.core.assertions import assert_is_not_none, assert_true

from common import dog, ui
from common.ui import find_area_image, Template, get_vertical_rect, touch_and_wait, scroll_and_find_element
from pages.base.page import BasePage
from common.ui import poco
from pages.base.page_mobile_phone_album import PageMobilePhoneAlbum
from airtest.core.api import home, keyevent, sleep, swipe


class AndroidPageMobilePhoneAlbum(PageMobilePhoneAlbum):
    page_name = "手机相册"

    @classmethod
    def page_mobile_phone(cls):
        with dog.step(f"{cls.page_name}-选择相册中的第一张图片"):
            sleep(ui.step_wait_time)
            first_img = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
                "android:id/content").offspring("com.truedian.dragon:id/recyclerView").child(
                "android.widget.RelativeLayout")[0].offspring("com.truedian.dragon:id/check")
            if first_img:
                first_img.click()

            else:
                first_picture = find_area_image(Template(r"tpl1745565194144.png"),
                                                target_rect=(get_vertical_rect(0.25)))
                touch_and_wait(first_picture, times=2)
            sleep(ui.step_wait_time)
            scroll_and_find_element(max_scroll_times=1, target_rect=0.7)

            sleep(ui.step_wait_time)
            end_picture = find_area_image(Template(r"tpl1745562128076.png"),
                                          target_rect=(get_vertical_rect(0.65)))
            if end_picture:
                touch_and_wait(end_picture, times=2)
            sleep(ui.step_wait_time)

    @classmethod
    def page_mobile_img_enter(cls):
        with dog.step(f"{cls.page_name}-确认"):
            poco("com.truedian.dragon:id/tv_ok").click()
            cls.wait_for_enter()
