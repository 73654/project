# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""

from pages.base.page import BasePage
from common.ui import poco
from pages.base.page_album_dynamic import BasePageAlbumDynamic
from airtest.core.api import text

class IOSBasePageAlbumDynamic(BasePageAlbumDynamic):
    """相册动态页"""
    page_name = "相册动态页"


    @classmethod
    def text_search(cls):
        poco("com.truedian.dragon:id/et_search").click()

