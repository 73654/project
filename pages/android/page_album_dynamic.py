# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""
from pages.base.page_album_dynamic import BasePageAlbumDynamic
from common.ui import poco
from airtest.core.api import text
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui


class AndroidBasePageAlbumDynamic(BasePageAlbumDynamic):
    """相册动态页"""
    page_name = "相册动态页"

    @classmethod
    def text_search(cls):
        poco("com.truedian.dragon:id/et_search").click()
        sleep(ui.step_wait_time)
        text("标题价格300元")
        sleep(ui.step_wait_time)


