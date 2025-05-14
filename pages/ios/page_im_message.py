# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_im_message
@ time:    2025/4/22 17:37 
@ desc:
"""
from common import dog,ui
from pages.base.page import BasePage
from common.ui import poco, touch_and_wait
from common.ui import Template,find_area_image, get_vertical_rect,long_click_custom,swipe_wait_for
from pages.base.page_im_message import PageImMessage
from airtest.core.api import text
from airtest.core.api import home, keyevent, sleep, swipe


class IOSPageImMessage(PageImMessage):
    page_name="im_消息"


    @classmethod
    def page_send_message_bar(cls):
        with dog.step(f"{cls.page_name}-点击消息栏"):
            poco("TextView").click()



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
            # 选择一张图片
            photo_album=find_area_image(Template(r"tpl1747030461206.png"),
                            target_rect=(get_vertical_rect(0.3)))
            if photo_album:
                touch_and_wait(photo_album)
                sleep(ui.step_wait_time)
                find_area_image(Template(r"tpl1747030236240.png"),
                                target_rect=(get_vertical_rect(-0.2)), click=True)
            else:
                find_area_image(Template(r"tpl1747030706265.png"),
                                target_rect=(get_vertical_rect(0.16)), click=True)




    @classmethod
    def page_send_sticker_packs(cls):
        with dog.step(f"{cls.page_name}-选择表情"):
            poco("🙏").click()
            sleep(ui.step_wait_time)
            poco("👌").click()