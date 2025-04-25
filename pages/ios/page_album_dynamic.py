# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""

from pages.base.page import BasePage
from common.ui import poco,find_area_image
from pages.base.page_album_dynamic import BasePageAlbumDynamic
from airtest.core.api import text
from common import dog, ui

class IOSBasePageAlbumDynamic(BasePageAlbumDynamic):
    """相册动态页"""
    page_name = "相册动态页"


    @classmethod
    def text_search(cls):
        poco("com.truedian.dragon:id/et_search").click()

    @classmethod
    def page_release(cls):
        with dog.step(f"{cls.page_name}-发布"):
            poco("发布").click()

