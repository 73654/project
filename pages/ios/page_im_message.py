# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_im_message
@ time:    2025/4/22 17:37 
@ desc:
"""
from common import dog,ui
from pages.base.page import BasePage
from common.ui import poco
from common.ui import Template,find_area_image, get_vertical_rect,long_click_custom,swipe_wait_for
from pages.base.page_im_message import PageImMessage
from airtest.core.api import text
from airtest.core.api import home, keyevent, sleep, swipe


class IOSPageImMessage(PageImMessage):
    page_name="im_消息"


    @classmethod
    def page_send_message_bar(cls):
        with dog.step(f"{cls.page_name}-点击消息栏"):
            poco("android.widget.EditText").click()


    @classmethod
    def page_send_message(cls):
        with dog.step(f"{cls.page_name}-点击消息栏"):
            cls.page_send_message_bar()
            text("验证会话内容")
            sleep(ui.step_wait_time)

    @classmethod
    def page_choose_photo_album(cls):
        with dog.step(f"{cls.page_name}-选择相册中的第一张图片"):
            sleep(ui.step_wait_time)
            poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
                "com.truedian.dragon:id/recyclerView").child("android.widget.RelativeLayout")[1].offspring(
                "com.truedian.dragon:id/check").click()
            sleep(ui.step_wait_time)
            poco("com.truedian.dragon:id/tv_ok").click()



