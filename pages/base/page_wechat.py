# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 9:53
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import sleep, text, touch

from common import dog, utils,ui
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

            find_loop_area_image(Template("tpl1745812127310.png"), area_size=-0.2,
                                 click=True)
            # find_loop_area_image(Template("PageWechat_enter_mini_program_1.png", threshold=0.6), area_size=-0.2,
            #                      click=True)

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
            keep_wx=find_area_image(Template(r"tpl1743674795976.png"), target_rect=get_vertical_rect(0.2, middle=True))
            if keep_wx:
                touch_and_wait(keep_wx)

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
        # if DeviceType.IOS == current_device_type:
        cls.keep_weixin()

        with dog.step(f"{cls.page_name}-等待进入文件传输助手对话框"):
            find_area_image(Template(r"tpl1744010225134.png"), target_rect=get_vertical_rect(0.1))



    @classmethod
    def enter_wx_code(cls):
        """识别文件传输助手中的二维码"""
        with dog.step(f"{cls.page_name}-点击文件传输助手的二维码"):
                find_loop_area_image(Template("tpl1744602748379.png", threshold=0.6), area_size=-0.2,
                                 click=True)

        with dog.step(f"{cls.page_name}-长按图片"):
            touch_and_wait((0.5, 0.5), duration=3)
            sleep(step_wait_time)

        with dog.step(f"{cls.page_name}-点击进入二维码"):
            pos = find_area_image(Template(r"tpl1744602885005.png", threshold=0.6), target_rect=get_vertical_rect(-0.2))
            sleep(step_wait_time)
            touch_and_wait(pos)




    @classmethod
    def wx_open_immediately(cls):
        """
        识别二维码--跳转打开app看款
        """
        pass



    @classmethod
    def click_wx_payment_code(cls):
        """识别文件传输助手中的收款码"""
        with dog.step(f"{cls.page_name}-点击文件传输助手的收款码"):
            find_loop_area_image(Template("tpl1745220549589.png", threshold=0.6), area_size=-0.2,
                                 click=True)

            sleep(ui.step_wait_time)
        with dog.step(f"{cls.page_name}-长按图片"):
            touch_and_wait((0.5, 0.5), duration=3)
            sleep(ui.step_wait_time)

        with dog.step(f"{cls.page_name}-点击进入收款码"):
            pos = find_area_image(Template(r"tpl1744602885005.png", threshold=0.6), target_rect=get_vertical_rect(-0.2))
            sleep(step_wait_time)
            touch_and_wait(pos)
            sleep(step_wait_time)


    @classmethod
    def page_payment_amount(cls):
        with dog.step(f"{cls.page_name}-跳转付款金额页面"):
            find_area_image(Template(r"tpl1745221027845.png"), target_rect=get_vertical_rect(-0.15),click=True)
            sleep(step_wait_time)
            find_area_image(Template(r"tpl1745221044224.png"), target_rect=get_vertical_rect(-0.15),click=True)
            sleep(step_wait_time)
            find_area_image(Template(r"tpl1745221027845.png"), target_rect=get_vertical_rect(-0.15),click=True)
            sleep(step_wait_time)
            find_area_image(Template(r"tpl1745221267005.png"), target_rect=get_vertical_rect(-0.4),click=True)
            sleep(step_wait_time)
            find_area_image(Template(r"tpl1745221534520.png"), target_rect=get_vertical_rect(-0.4), click=True)




    @classmethod
    def page_wechat_live(cls):
        with dog.step(f"{cls.page_name}-点击直播分享"):
            find_loop_area_image(Template("tpl1745481323508.png", threshold=0.6), area_size=-0.2,
                                 click=True)
            cls.wait_for_enter()
            find_area_image(Template("tpl1745480451564.png",threshold=0.6), target_rect=get_vertical_rect(-0.15), click=True)
            cls.wait_for_enter()
            find_area_image(Template("tpl1745480675892.png"), target_rect=get_vertical_rect(-0.7),
                            click=True)
            cls.wait_for_enter()
            find_area_image(Template("tpl1745480710998.png"), target_rect=get_vertical_rect(-0.15),
                            click=True)



