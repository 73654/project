# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_mobile_phone_album
@ time:    2025/4/25 13:47 
@ desc:
"""
from airtest.core.assertions import assert_is_not_none, assert_true

from common import dog
from common.ui import find_area_image, Template, get_vertical_rect
from pages.base.page import BasePage
from pages.base.page_mobile_phone_album import PageMobilePhoneAlbum

class IOSPageMobilePhoneAlbum(PageMobilePhoneAlbum):
    page_name="手机相册"

    @classmethod
    def page_mobile_phone(cls):
        with dog.step(f"{cls.page_name}-选择图片"):
            pass

