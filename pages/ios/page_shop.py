# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 16:46
# Description:
# -------------------------------------------------------------------------
from airtest.core.assertions import assert_equal, assert_false, assert_is_not_none, assert_true

from common import dog, ui
from common.ui import find_area_image, poco, Template, swipe_up
from common.ui.ui import swipe_wait_for
from pages.base.page_shop import BasePageShop


class IOSPageShop(BasePageShop):
    @classmethod
    def __get_info_area(cls):
        """用户信息，上新，svip标识这块区域"""
        return 0, 0, 1, 0.4

    @classmethod
    def __get_tab_area(cls):
        """中间tab bar和搜索框这个区域"""
        return 0, 0.3, 1, 0.5

    @classmethod
    def __get_list_area(cls):
        """列表展示区域"""
        return 0, 0.4, 1, 1

    @classmethod
    def __get_button_area(cls):
        return 0, 0.8, 1, 1

    @classmethod
    def _click_tab(cls, name):
        with dog.step(f"{cls.page_name}-TAB-{name}"):
            find_area_image(Template(r"tpl1743581555996.png"), target_rect=cls.__get_tab_area(), click=True)
            find_area_image(Template(r"tpl1743581563282.png"), target_rect=cls.__get_tab_area(), click=True)
            find_area_image(Template(r"tpl1743581568987.png"), target_rect=cls.__get_tab_area(), click=True)
            find_area_image(Template(r"tpl1743581575121.png"), target_rect=cls.__get_tab_area(), click=True)

    @classmethod
    def _click_button(cls, view_id, name):
        with dog.step(f"{cls.page_name}-底下button-{name}"):
            find_area_image(Template(r"tpl1743583130224.png"), target_rect=cls.__get_button_area(), click=True)
            find_area_image(Template(r"tpl1743583138865.png"), target_rect=cls.__get_button_area(), click=True)
            find_area_image(Template(r"tpl1743583145561.png"), target_rect=cls.__get_button_area(), click=True)

    @classmethod
    def _check_search_bar(cls):
        with dog.step(f"{cls.page_name}-确认搜索框存在"):
            assert_true(find_area_image(Template(r"tpl1743581583819.png"), target_rect=cls.__get_tab_area()))

        with dog.step(f"{cls.page_name}-确认搜索框-图搜图标存在"):
            assert_true(find_area_image(Template(r"tpl1743581590252.png"), target_rect=cls.__get_tab_area()))

    @classmethod
    def check_vip_status(cls):
        with dog.step(f"{cls.page_name}-校验VIP/SVIP图标暂时是否正常"):
            assert_true(find_area_image(Template(r"common_svip.png"), target_rect=cls.__get_info_area()))

    @classmethod
    def check_new_number(cls):
        with dog.step(f"{cls.page_name}-校验上新"):
            assert_true(find_area_image(Template(r"tpl1743582625692.png"), target_rect=cls.__get_info_area()),
                        "未暂展示正确的“上新”文案")
            # 数量不好校验

    @classmethod
    def check_total_number(cls):
        with dog.step(f"{cls.page_name}-校验总数"):
            assert_true(find_area_image(Template(r"tpl1743582630891.png"), target_rect=cls.__get_info_area()),
                        "未暂展示正确的“总数”文案")
            # 数量不好校验

    @classmethod
    def check_all_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-全部列表-发布商品按钮是否存在"):
            assert_true(find_area_image(Template(r"tpl1743581602090.png"), target_rect=cls.__get_list_area()))

        with dog.step(f"{cls.page_name}-全部列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-全部列表-确认分享按钮是否存在"):
            assert_true(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def check_new_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-上新列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-上新列表-确认分享按钮是否存在"):
            assert_true(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def check_video_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-小视频列表-判断界面是否白屏"):
            assert_true(ui.is_white_area(target_rect=cls.__get_list_area()))

        with dog.step(f"{cls.page_name}-小视频列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-小视频列表-判断界面是否白屏"):
            assert_true(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def check_picture_grid(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-图集-判断界面是否白屏"):
            assert_true(ui.is_white_area(target_rect=cls.__get_list_area()))

        with dog.step(f"{cls.page_name}-图集-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-图集-判断界面是否白屏"):
            assert_true(ui.is_white_area(target_rect=cls.__get_list_area()))
