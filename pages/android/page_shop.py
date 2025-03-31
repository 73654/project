# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 16:46
# Description:
# -------------------------------------------------------------------------
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true

from common import dog
from common.ui import Template, find_area_image, poco, swipe_up
from common.ui.ui import swipe_wait_for
from pages.base.page_shop import BasePageShop


class AndroidPageShop(BasePageShop):
    @classmethod
    def _click_tab(cls, name):
        with dog.step(f"店铺主页-TAB-{name}"):
            poco(nameMatches=".*id/tabs", type="android.widget.HorizontalScrollView").offspring(
                type="android.widget.LinearLayout", name=name).click()

    @classmethod
    def _click_button(cls, view_id, name):
        with dog.step(f"店铺主页-底下button-{name}"):
            poco(nameMatches=f".*id/{view_id}", type="android.widget.LinearLayout").click()

    @classmethod
    def tab_all(cls):
        cls._click_tab("全部")

    @classmethod
    def tab_new(cls):
        cls._click_tab("上新")

    @classmethod
    def tab_video(cls):
        cls._click_tab("小视频")

    @classmethod
    def tab_picture_grid(cls):
        cls._click_tab("图集")

    @classmethod
    def button_goods(cls):
        cls._click_button("tv_tag_category_container", "商品分类")

    @classmethod
    def button_batch_share(cls):
        cls._click_button("ll_batch_share", "批量编辑和分享")

    @classmethod
    def button_contact(cls):
        cls._click_button("tv_connect_other", "联系Ta")

    @classmethod
    def check_vip_status(cls):
        with dog.step("店铺主页-校验VIP/SVIP图标暂时是否正常"):
            find_area_image(Template(r"common_svip.png"), poco(nameMatches=".*id/ll_name"))

    @classmethod
    def check_new_number(cls):
        with dog.step("店铺主页-校验上新及数量"):
            view = poco(nameMatches=".*id/fl_new")
            assert_equal("上新", view.offspring(nameMatches=".*id/tag_new_goods").get_text(),
                         "未暂展示正确的“上新”文案")
            assert_true(int(view.offspring(nameMatches=".*id/num_new_goods").get_text()) >= 0,
                        "未暂展示正确的上新数量")

    @classmethod
    def check_total_number(cls):
        with dog.step("店铺主页-校验总数及数量"):
            view = poco(nameMatches=".*id/fl_all")
            assert_equal("总数", view.offspring(nameMatches=".*id/tag_total_goods").get_text(),
                         "未暂展示正确的“总数”文案")
            assert_true(int(view.offspring(nameMatches=".*id/num_total_goods").get_text()) >= 0,
                        "未暂展示正确的总数数量")

    @classmethod
    def _check_search_bar(cls):
        with dog.step("店铺主页-确认搜索框存在"):
            search_bar = poco(nameMatches=".*id/search_view_home")
            assert_true(search_bar.exists())

        with dog.step("店铺主页-确认搜索框-文案为: 标题/简称/搜索码/货号"):
            assert_equal("标题/简称/搜索码/货号", search_bar.offspring(nameMatches=".*id/et_search").get_text())

        with dog.step("店铺主页-确认搜索框-图搜图标存在"):
            assert_is_not_none(find_area_image(Template("common_image_search.png"), search_bar))

    @classmethod
    def check_all_list(cls):
        cls._check_search_bar()

        with dog.step("店铺主页-全部列表-发布商品按钮是否存在"):
            assert_true(poco(nameMatches=".*id/iv_take_photo").exists())

        with dog.step("店铺主页-全部列表-上滑"):
            swipe_up()

        with dog.step("店铺主页-全部列表-确认分享按钮是否存在"):
            assert_true(poco(nameMatches=".*id/share_home_fragment", text="分享").exists())

    @classmethod
    def check_new_list(cls):
        cls._check_search_bar()

        with dog.step("店铺主页-上新列表-上滑"):
            swipe_up()

        with dog.step("店铺主页-上新列表-确认分享按钮是否存在"):
            assert_true(poco(nameMatches=".*id/share_home_fragment", text="分享").exists())

    @classmethod
    def check_video_list(cls):
        cls._check_search_bar()

        with dog.step("店铺主页-小视频列表-判断视频播放按钮是否存在"):
            assert_true(poco(nameMatches=".*id/dynamic_video_play").exists())

        with dog.step("店铺主页-小视频列表-上滑、确认删除按钮是否存在"):
            assert_true(swipe_wait_for(poco(nameMatches=".*id/ll_dynamic_edit").offspring(text="删除")))

    @classmethod
    def check_picture_grid(cls):
        cls._check_search_bar()

        with dog.step("店铺主页-图集列表-判断商品是否存在"):
            assert_true(poco(nameMatches=".*id/iv_grid_video").exists())

        with dog.step("店铺主页-图集列表-上滑"):
            swipe_up()

        with dog.step("店铺主页-图集列表-判断商品是否存在"):
            assert_true(poco(nameMatches=".*id/iv_grid_video").exists())
