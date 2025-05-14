# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:10
# Description:
# -------------------------------------------------------------------------
from common import dog,ui
from common.ui import find_area_image, Template, get_vertical_rect, touch_and_wait
from pages.base.page import BasePage
from airtest.core.assertions import assert_exists, assert_is_not_none
from airtest.core.api import home, keyevent, sleep, swipe,touch
from common.ui import DeviceType

class PageMine(BasePage):
    """我的"""
    page_name = "我的"

    @classmethod
    def qr_entry(cls):
        with dog.step(f"{cls.page_name}-进入二维码（相册分享）页面"):
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template("tpl1747203595700.png"), target_rect=(0.7, 0.2, 1, 0.4), click=True)

            else:
                find_area_image(Template("tpl1747134648048.png"), target_rect=(0.7, 0.2, 1, 0.4), click=True)

            cls.wait_for_enter()

            # 第一次进入会弹框，点取消
            pos = find_area_image(Template(r"tpl1744091568935.png"), target_rect=get_vertical_rect(-0.15))
            if pos:
                touch_and_wait(pos)

    @classmethod
    def clubber(cls):
        with dog.step(f"{cls.page_name}-进入会员(充值)页面"):
            # find_area_image(Template(r"tpl1744264284483.png"), target_rect=get_vertical_rect(0.3),click=True)
            find_area_image(Template(r"tpl1745821867141.png"), target_rect=get_vertical_rect(0.3), click=True)
            cls.wait_for_enter()
            sleep(ui.step_wait_time)

    @classmethod
    def page_mine_configure(cls):
        with dog.step(f"{cls.page_name}-设置标识"):
            cls.wait_for_enter()
            sleep(ui.step_wait_time)
            mine_config = find_area_image(Template(r"tpl1747031952894.png"), target_rect=get_vertical_rect(0.18))

            if mine_config:
                touch(mine_config)
            else:
                if ui.current_device_type == DeviceType.Android:
                    test_mine_configure_android=find_area_image(Template(r"tpl1745203758139.png",threshold=0.6), target_rect=(0.45,0.02,0.9,0.15))
                    if test_mine_configure_android:
                        touch(test_mine_configure_android)
                    else:
                        find_area_image(Template(r"tpl1745203758139.png",threshold=0.6), target_rect=(0.45,0.02,0.9,0.15), click=True)
                else:

                    test_mine_configure=find_area_image(Template(r"tpl1747035504605.png", threshold=0.6),target_rect=(0.45,0.02,0.9,0.15))
                    if test_mine_configure:
                        touch(test_mine_configure)
                    else:
                        touch(find_area_image(Template(r"tpl1747031526888.png",threshold=0.6), target_rect=(0.45,0.02,0.9,0.15)))




            cls.wait_for_enter()
            sleep(ui.step_wait_time)

    @classmethod
    def page_mine_visitor(cls):
        # 当前迭代根据尾号去控制我的table页的背景颜色，test01为深蓝，冒泡为白色，后面需要再调整
        with dog.step(f"{cls.page_name}-点击访客"):
            find_area_image(Template(r"tpl1745200900426.png"), target_rect=get_vertical_rect(0.25), click=True)
            cls.wait_for_enter()
            visitor_img = find_area_image(Template(r"tpl1745201015761.png"), target_rect=get_vertical_rect(0.5))
            if visitor_img:
                find_area_image(Template(r"tpl1745201161124.png"), target_rect=get_vertical_rect(-0.15), click=True)

    @classmethod
    def page_switch_sub_account(cls):
        with dog.step(f"{cls.page_name}-切换test01子账号"):
            switch_sub_test01 = find_area_image(Template(r"tpl1745478099289.png"), target_rect=get_vertical_rect(0.2))
            if switch_sub_test01:
                touch_and_wait(switch_sub_test01)
                cls.wait_for_enter()
                find_area_image(Template(r"tpl1745479758305.png"), target_rect=get_vertical_rect(0.35), click=True)
                cls.wait_for_enter()

    @classmethod
    def page_mine_my_wallet(cls):
        with dog.step(f"{cls.page_name}-我的钱包"):
            mine_waller = find_area_image(Template(r"tpl1747204285504.png"), target_rect=get_vertical_rect(0.3))
            if ui.current_device_type == DeviceType.Android:
                if mine_waller:
                    touch_and_wait(mine_waller)
            else:
                find_area_image(Template(r"tpl1747040358315.png"), target_rect=(0.72,0.15,0.96,0.3),click=True)
            cls.wait_for_enter()
            # if ui.current_device_type == DeviceType.Android:
            assert_is_not_none(find_area_image(Template(r"tpl1745488484046.png",threshold=0.45), target_rect=get_vertical_rect(0.3)))
            assert_is_not_none(find_area_image(Template(r"tpl1745488632368.png",threshold=0.45), target_rect=get_vertical_rect(0.3)))


