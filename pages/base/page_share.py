# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/4/3 16:38
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import touch

from common import dog
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect
from pages.base.page import BasePage


class PageShare(BasePage):
    page_name = "分享面板"

    @classmethod
    def _get_share_area(cls):
        """分享面板那个中间区域"""
        pass

    @classmethod
    def choose_wechat(cls, num=1):
        """分享时的弹框，如果是微信多开的话，会有多个图标"""
        with dog.step(f"{cls.page_name}-分享时，多微信选择"):
            pos = find_all_area_image(Template(r"PageShare_choose_wechat_1.png", threshold=0.6),
                                      target_rect=(0, 0.7, 1, 1))
            if pos and len(pos) >= num:
                touch(pos[num - 1])

    @classmethod
    def enable_mini_code(cls):
        with dog.step(f"{cls.page_name}-商品分享，确认小程序码开启"):
            pass

    @classmethod
    def share_wechat_poster(cls):
        """海报分享"""
        with dog.step(f"{cls.page_name}-商品分享，并点击'海报分享'"):
            find_area_image(Template(r"PageShare_wechat_poster_share_1.png"), target_rect=cls._get_share_area(),
                            click=True)

    @classmethod
    def share_wechat_friends(cls):
        """好友分享"""
        with dog.step(f"{cls.page_name}-商品分享，并点击'好友分享'"):
            find_area_image(Template(r"PageShare_share_wechat_friends_1.png"), target_rect=cls._get_share_area(),
                            click=True)

    @classmethod
    def share_pingtu(cls):
        """拼图分享"""
        with dog.step(f"{cls.page_name}-商品分享，并点击'拼图分享'"):
            find_area_image(Template(r"tpl1743672929276.png"), target_rect=cls._get_share_area(),
                            click=True)

    @classmethod
    def top_right_corner_button(cls):
        """右上角分享按钮"""
        with dog.step(f"{cls.page_name}-拼图/海报分享详情页，并点击'右上角分享按钮'"):
            find_area_image(Template(r"tpl1743672972925.png"), target_rect=get_vertical_rect(0.1),
                            click=True)


class PageShare2(BasePage):
    page_name = "分享面板2"

    @classmethod
    def _get_share_area(cls):
        """分享面板的区域"""
        return get_vertical_rect(-0.5)

    @classmethod
    def share_wechat(cls):
        """好友分享"""
        with dog.step(f"{cls.page_name}-分享，并点击'微信'"):
            find_area_image(Template(r"tpl1743670657392.png"), target_rect=cls._get_share_area(),
                            click=True)
