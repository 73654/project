# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_im_message
@ time:    2025/4/22 17:37 
@ desc:
"""

from common import dog, ui
from pages.base.page import BasePage
from common.ui import poco
from common.ui import Template, find_area_image, get_vertical_rect, long_click_custom, swipe_wait_for, touch_and_wait,get_horizontal_rect
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_is_none
from common.ui import DeviceType


class PageImMessage(BasePage):
    page_name = "im_消息"

    @classmethod
    def page_online_chat(cls):
        with dog.step(f"{cls.page_name}-在线聊天"):
            find_area_image(Template(r"tpl1745314604935.png"), target_rect=(get_vertical_rect(-0.25)), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_message_windows(cls):
        with dog.step(f"{cls.page_name}-关闭消息收发弹框，判断是否开启"):
            message_windows = find_area_image(Template(r"tpl1745315360450.png"), target_rect=(get_vertical_rect(0.6)))
            if message_windows:
                find_area_image(Template(r"tpl1745315545690.png"), target_rect=(get_vertical_rect(0.6)), click=True)

            cls.wait_for_enter()

    @classmethod
    def page_send_message_bar(cls):
        with dog.step(f"{cls.page_name}-点击消息栏"):
            pass

    @classmethod
    def page_send_sticker(cls):
        with dog.step(f"{cls.page_name}-发送表情按钮"):
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template(r"tpl1745321643190.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            else:
                find_area_image(Template(r"tpl1747021686580.png"), target_rect=(get_vertical_rect(-0.15)), click=True)

    @classmethod
    def page_send_sticker_packs(cls):
        with dog.step(f"{cls.page_name}-选择表情"):
            pass

    @classmethod
    def page_click_send_enter(cls):
        with dog.step(f"{cls.page_name}-点击发送"):
            find_area_image(Template(r"tpl1745322283830.png"), target_rect=(get_vertical_rect(-0.2)), click=True)
            sleep(ui.step_wait_time)

    @classmethod
    def page_click_plus_sign(cls):
        with dog.step(f"{cls.page_name}-点击加号标符"):
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template(r"tpl1745371799478.png"), target_rect=(get_vertical_rect(-0.5)), click=True)
            else:
                find_area_image(Template(r"tpl1747029794689.png"), target_rect=(0.83, 0.55, 1, 0.9), click=True)
            sleep(ui.step_wait_time)

            find_area_image(Template(r"tpl1745372124370.png"), target_rect=(get_vertical_rect(-0.5)), click=True)
            message_table = find_area_image(Template(r"tpl1745375814254.png"), target_rect=(get_vertical_rect(-0.5)))
            if message_table:
                assert_is_none(message_table)

    @classmethod
    def page_send_message_switch(cls):
        with dog.step(f"{cls.page_name}-聊天消息接收开关"):
            cls.wait_for_enter()
            sleep(ui.step_wait_time)
            message_switch_img = find_area_image(Template(r"tpl1745832075982.png"),
                                                 target_rect=(get_vertical_rect(0.45)))
            if ui.current_device_type == DeviceType.Android:
                if not message_switch_img:
                    send_message_switch = find_area_image(Template(r"tpl1745753089954.png"),
                                                          target_rect=(0.7, 0.58, 1, 0.75))
                    if send_message_switch:
                        touch_and_wait(send_message_switch)
                        sleep(ui.step_wait_time)
                        find_area_image(Template(r"tpl1745373415038.png"),
                                        target_rect=(get_vertical_rect(-0.5)), click=True)
                        sleep(ui.step_wait_time)
                        find_area_image(Template(r"tpl1745832075982.png"), target_rect=(get_vertical_rect(0.45)),
                                        click=True)
                else:
                    find_area_image(Template(r"tpl1745832075982.png"), target_rect=(get_vertical_rect(0.45)),
                                    click=True)
                    sleep(ui.step_wait_time)
            else:
                message_switch_img = find_area_image(Template(r"tpl1745832075982.png"),
                                                     target_rect=(get_vertical_rect(0.45)))
                if not message_switch_img:
                    find_area_image(Template(r"tpl1747033536919.png", threshold=0.6),
                                    target_rect=(0.78, 0.5, 1, 0.7), click=True)

                    sleep(ui.step_wait_time)
                    find_area_image(Template(r"tpl1745373415038.png"),
                                    target_rect=(get_vertical_rect(-0.5)), click=True)
                    sleep(ui.step_wait_time)
                    find_area_image(Template(r"tpl1745832075982.png"), target_rect=(get_vertical_rect(0.45)),
                                    click=True)
                else:
                    find_area_image(Template(r"tpl1745832075982.png"), target_rect=(get_vertical_rect(0.45)),
                                    click=True)
                    sleep(ui.step_wait_time)


    @classmethod
    def page_two_back(cls):
        with dog.step(f"{cls.page_name}-返回两次上一个页面"):
            for i in range(2):
                cls.back()

    @classmethod
    def check_im_message(cls):
        with dog.step(f"{cls.page_name}-断言接收消息方获取消息内容"):
            sleep(ui.step_wait_time)
            if ui.current_device_type == DeviceType.Android:
                assert_is_not_none(
                    find_area_image(Template(r"tpl1745377090220.png",threshold=0.5), target_rect=(get_horizontal_rect(0.5))))
            else:
                assert_is_not_none(find_area_image(Template(r"tpl1747037650164.png", threshold=0.5),
                                                   target_rect=(0.1, 0.1, 0.5, 0.85)))

            assert_is_not_none(find_area_image(Template(r"tpl1745377107704.png",threshold=0.35), target_rect=(0.1, 0.1, 0.5, 0.85)))

    @classmethod
    def page_choose_photo_album(cls):
        with dog.step(f"{cls.page_name}-选择相册中的第一张图片"):
            pass
