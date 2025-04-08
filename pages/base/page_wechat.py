# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 9:53
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import sleep, text, touch

from common import dog, utils
from common.ui import DeviceType, Template, current_device_type, find_area_image, find_loop_area_image, \
    get_vertical_rect, step_wait_time, touch_and_wait
from pages.base.page import BasePage


class PageWechat(BasePage):
    page_name = "微信页面操作"

    @classmethod
    def poster_publish(cls):
        """朋友圈点发布按钮"""
        with dog.step(f"{cls.page_name}-朋友圈点发布按钮"):
            find_area_image(Template(r"PageWechat_poster_publish_1.png", threshold=0.6), target_rect=(0, 0, 1, 0.1),
                            timeout=10,
                            click=True)

    @classmethod
    def enter_mini_program(cls):
        """识别小程序码"""
        with dog.step(f"{cls.page_name}-点击商品图片小程序码"):
            find_loop_area_image(Template("PageWechat_enter_mini_program_1.png", threshold=0.6), area_size=-0.2,
                                 click=True)

        with dog.step(f"{cls.page_name}-长按图片"):
            touch_and_wait((0.5, 0.5), duration=3)
            sleep(step_wait_time)

        with dog.step(f"{cls.page_name}-点击进入小程序"):
            pos = find_area_image(Template(r"PageWechat_enter_mini_program_2.png", threshold=0.6), target_rect=get_vertical_rect(-0.2))
            sleep(step_wait_time)
            touch_and_wait(pos)

    @classmethod
    def keep_weixin(cls):
        with dog.step(f"{cls.page_name}-是否留在微信弹框-点击留在微信"):
            find_area_image(Template(r"tpl1743674795976.png"), target_rect=get_vertical_rect(0.2, middle=True),
                            click=True)

    @classmethod
    def back_album(cls):
        with dog.step(f"{cls.page_name}-是否留在微信弹框-点击返回微商相册"):
            find_area_image(Template(r"tpl1743675572362.png"), target_rect=get_vertical_rect(0.2, middle=True),
                            click=True)

    @classmethod
    def share_search(cls, _text):
        with dog.step(f"{cls.page_name}-查找搜索框，并搜索'{_text}'"):
            find_area_image(Template(r"tpl1744006058838.png"), target_rect=get_vertical_rect(0.2), click=True)
            text(_text)

    @classmethod
    def send_to_file_assistant(cls):
        """发送到文件助手"""
        cls.share_search("文件传输助手")

        with dog.step(f"{cls.page_name}-查找'文件助手'并点击"):
            find_area_image(Template(r"tpl1744006647861.png"), target_rect=get_vertical_rect(0.4),
                            click=True)

        with dog.step(f"{cls.page_name}-点击发送按钮"):
            find_area_image(Template(r"tpl1743673978285.png"), target_rect=get_vertical_rect(-0.3), click=True)

        # 苹果会弹一个框
        if DeviceType.IOS == current_device_type:
            cls.keep_weixin()

        with dog.step(f"{cls.page_name}-等待进入文件传输助手对话框"):
            find_area_image(Template(r"tpl1744010225134.png"), target_rect=get_vertical_rect(0.1))
