# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_live_stream
@ time:    2025/4/23 19:05 
@ desc:
"""

from common import dog, ui
from pages.base.page_live_stream import PageLiveStream
from common.ui import poco
from common.ui import Template, find_area_image, get_vertical_rect, long_click_custom, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_is_none


class IOSPageLiveStream(PageLiveStream):
    page_name = "直播页面"

    @classmethod
    def page_private_domain_live(cls):
        with dog.step(f"{cls.page_name}-私域直播"):
            poco("私域直播").click()
            cls.wait_for_enter()

    @classmethod
    def page_to_live(cls):
        with dog.step(f"{cls.page_name}-去直播"):
            poco("去直播").click()
            cls.wait_for_enter()