# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_live_stream
@ time:    2025/4/23 19:05 
@ desc:
"""

from common import dog, ui
from pages.base.page import BasePage
from common.ui import poco
from common.ui import Template, find_area_image, get_vertical_rect, long_click_custom, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_is_none
from common.ui.start import stop_wg_app,start_wg_app

class PageLiveStream(BasePage):
    page_name = "直播页面"

    @classmethod
    def page_private_domain_live(cls):
        with dog.step(f"{cls.page_name}-私域直播"):
            pass

    @classmethod
    def page_to_live(cls):
        with dog.step(f"{cls.page_name}-去开播"):
            pass

    @classmethod
    def camera_microphone_permission(cls):
        with dog.step(f"{cls.page_name}相机和麦克风权限"):
            camera_microphone_windows = find_area_image(Template(r"tpl1745409506393.png"),
                                                        target_rect=(get_vertical_rect(0.65)))
            if camera_microphone_windows:
                find_area_image(Template(r"tpl1745409518797.png"), target_rect=(get_vertical_rect(-0.65)), click=True)
                sleep(ui.step_wait_time)
                find_area_image(Template(r"tpl1745409551849.png"), target_rect=(get_vertical_rect(-0.35)), click=True)

    @classmethod
    def page_live_next_step(cls):
        with dog.step(f"{cls.page_name}-下一步"):
            pass

    @classmethod
    def page_live_start(cls):
        with dog.step(f"{cls.page_name}-开始直播"):
            pass

    @classmethod
    def page_continue_live_stream(cls):
        with dog.step(f"{cls.page_name}-继续直播"):
            pass

    @classmethod
    def page_live_commodity_function(cls):
        with dog.step(f"{cls.page_name}-直播设置封面/主题商品按钮"):
            pass

    @classmethod
    def page_live_streaming_interruption(cls):
        with dog.step(f"{cls.page_name}-直播中断，恢复直播弹框"):
            live_streaming_interruption = find_area_image(Template(r"tpl1745459764858.png"),
                                                          target_rect=(get_vertical_rect(0.6)))
            if live_streaming_interruption:
                find_area_image(Template(r"tpl1745459778935.png"), target_rect=(get_vertical_rect(-0.6)), click=True)
        with dog.step(f"{cls.page_name}-等待4s，完全进入到直播间"):
            for i in range(3):
                sleep(ui.step_wait_time)

    @classmethod
    def page_share_live_wechat(cls):
        with dog.step(f"{cls.page_name}-分享直播给微信好友"):
            share_live_wechat = find_area_image(Template(r"tpl1745466112526.png"),
                                                target_rect=(get_vertical_rect(-0.3)))
            if share_live_wechat:
                touch_and_wait(share_live_wechat)

    @classmethod
    def page_live_start_app(cls):
        with dog.step(f"{cls.page_name}-重启进入到app"):
            stop_wg_app()
            sleep(ui.step_wait_time)
            start_wg_app()

    @classmethod
    def page_live_microphone(cls):
        with dog.step(f"{cls.page_name}-直播后允许访问麦克风弹框"):
            share_live_wechat = find_area_image(Template(r"tpl1747041408500.png",threshold=0.6),
                                                target_rect=(0.3,0.1,0.7,0.8))
            if share_live_wechat:
                find_area_image(Template(r"tpl1747041460109.png",threshold=0.6),
                                target_rect=(0.7,0.3,1,0.6))

