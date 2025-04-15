# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""

from airtest.core.assertions import assert_exists, assert_is_not_none
from pages.base.page import BasePage
from common import dog
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from common.ui import poco

class BasePageAlbumDynamic(BasePage):
    """相册动态页"""
    page_name = "相册动态页"


    @classmethod
    def text_search(cls):
        pass




