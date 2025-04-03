# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 16:46
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import touch
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true

from common import dog
from common.ui import Template, find_area_image, poco, swipe_up
from common.ui.ui import swipe_wait_for
from pages.base.page_shop import BasePageShop


class AndroidPageShop(BasePageShop):

    @classmethod
    def __share_button(cls):
        return poco(nameMatches=".*id/share_home_fragment", text="分享")

    @classmethod
    def _click_tab(cls, name):
        with dog.step(f"{cls.page_name}-TAB-{name}"):
            poco(nameMatches=".*id/tabs", type="android.widget.HorizontalScrollView").offspring(
                type="android.widget.LinearLayout", name=name).click()

    @classmethod
    def _click_button(cls, view_id, name):
        with dog.step(f"{cls.page_name}-底下button-{name}"):
            poco(nameMatches=f".*id/{view_id}", type="android.widget.LinearLayout").click()

    @classmethod
    def _check_search_bar(cls):
        with dog.step(f"{cls.page_name}-确认搜索框存在"):
            search_bar = poco(nameMatches=".*id/search_view_home")
            assert_true(search_bar.exists())

        with dog.step(f"{cls.page_name}-确认搜索框-文案为: 搜索"):
            assert_equal("搜索", search_bar.offspring(nameMatches=".*id/et_search").get_text())

        with dog.step(f"{cls.page_name}-确认搜索框-图搜图标存在"):
            assert_is_not_none(find_area_image(Template("common_image_search.png"), search_bar))

    @classmethod
    def check_vip_status(cls):
        with dog.step(f"{cls.page_name}-校验VIP/SVIP图标暂时是否正常"):
            find_area_image(Template(r"common_svip.png"), poco(nameMatches=".*id/ll_name"))

    @classmethod
    def check_new_number(cls):
        with dog.step(f"{cls.page_name}-校验上新及数量"):
            view = poco(nameMatches=".*id/fl_new")
            assert_equal("上新", view.offspring(nameMatches=".*id/tag_new_goods").get_text(),
                         "未暂展示正确的“上新”文案")
            assert_true(int(view.offspring(nameMatches=".*id/num_new_goods").get_text()) >= 0,
                        "未暂展示正确的上新数量")

    @classmethod
    def check_total_number(cls):
        with dog.step(f"{cls.page_name}-校验总数及数量"):
            view = poco(nameMatches=".*id/fl_all")
            assert_equal("总数", view.offspring(nameMatches=".*id/tag_total_goods").get_text(),
                         "未暂展示正确的“总数”文案")
            assert_true(int(view.offspring(nameMatches=".*id/num_total_goods").get_text()) >= 0,
                        "未暂展示正确的总数数量")

    @classmethod
    def check_all_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-全部列表-发布商品按钮是否存在"):
            assert_true(poco(nameMatches=".*id/iv_take_photo").exists())

        with dog.step(f"{cls.page_name}-全部列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-全部列表-确认分享按钮是否存在"):
            assert_true(swipe_wait_for(cls.__share_button()))

    @classmethod
    def check_new_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-上新列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-上新列表-确认分享按钮是否存在"):
            assert_true(swipe_wait_for(cls.__share_button()))

    @classmethod
    def check_video_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-小视频列表-判断视频播放按钮是否存在"):
            assert_true(poco(nameMatches=".*id/dynamic_video_play").exists())

        with dog.step(f"{cls.page_name}-小视频列表-上滑、确认删除按钮是否存在"):
            assert_true(swipe_wait_for(poco(nameMatches=".*id/ll_dynamic_edit").offspring(text="删除")))

    @classmethod
    def check_picture_grid(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-图集列表-判断商品是否存在"):
            assert_true(poco(nameMatches=".*id/iv_grid_video").exists())

        with dog.step(f"{cls.page_name}-图集列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-图集列表-判断商品是否存在"):
            assert_true(poco(nameMatches=".*id/iv_grid_video").exists())

    @classmethod
    def good_share(cls):
        super().good_share()
        swipe_wait_for(cls.__share_button(), times=10)
        swipe_up()
        cls.__share_button().click()
