# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/1 14:10
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import find_area_image, Template, get_vertical_rect, touch_and_wait
from pages.base.page import BasePage


class PageMine(BasePage):
    """我的"""
    page_name = "我的"

    @classmethod
    def qr_entry(cls):
        with dog.step(f"{cls.page_name}-进入二维码（相册分享）页面"):
            find_area_image(Template("PageMine_qr_entry_1.png"), target_rect=(0.7, 0.2, 1, 0.4), click=True)
            cls.wait_for_enter()

            # 第一次进入会弹框，点取消
            pos = find_area_image(Template(r"tpl1744091568935.png"), target_rect=get_vertical_rect(-0.15))
            if pos:
                touch_and_wait(pos)


    @classmethod
    def clubber(cls):
        with dog.step(f"{cls.page_name}-进入会员(充值)页面"):
            find_area_image(Template(r"tpl1744264284483.png"), target_rect=get_vertical_rect(0.3),click=True)
            cls.wait_for_enter()

    @classmethod
    def page_mine_configure(cls):
        with dog.step(f"{cls.page_name}-设置标识"):
            mine_config=find_area_image(Template(r"tpl1744963717160.png"), target_rect=get_vertical_rect(0.12))

            if mine_config:
                touch_and_wait(mine_config)
            else:
                find_area_image(Template(r"tpl1745203758139.png"), target_rect=get_vertical_rect(0.12),click=True)


            cls.wait_for_enter()


    @classmethod
    def page_mine_visitor(cls):
        # 当前迭代根据尾号去控制我的table页的背景颜色，test01为深蓝，冒泡为白色，后面需要再调整
        with dog.step(f"{cls.page_name}-点击访客"):
            find_area_image(Template(r"tpl1745200900426.png"), target_rect=get_vertical_rect(0.25), click=True)
            cls.wait_for_enter()
            visitor_img=find_area_image(Template(r"tpl1745201015761.png"), target_rect=get_vertical_rect(0.5))
            if visitor_img:
                find_area_image(Template(r"tpl1745201161124.png"), target_rect=get_vertical_rect(-0.15), click=True)





