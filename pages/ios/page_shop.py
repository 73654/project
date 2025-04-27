# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 16:46
# Description:
# -------------------------------------------------------------------------

from airtest.core.assertions import assert_false, assert_true
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui
from common.ui import Template, find_area_image, swipe_up,poco
from common.ui import swipe_wait_for,scroll_and_find_element,get_vertical_rect
from pages.base.page_shop import BasePageShop
from airtest.core.api import text
from common.ui import poco


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

    tab_index = {"全部": 1, "上新": 2, "小视频": 3, "图集": 4}

    @classmethod
    def _click_tab(cls, name):
        with dog.step(f"{cls.page_name}-TAB-{name}"):
            find_area_image(Template(f"IOSPageShop__click_tab_{cls.tab_index[name]}.png"),
                            target_rect=cls.__get_tab_area(), click=True)

    button_index = {"商品分类": 1, "联系Ta": 2, "批量分享/编辑": 3}

    @classmethod
    def _click_button(cls, view_id, name):
        with dog.step(f"{cls.page_name}-底下button-{name}"):
            find_area_image(Template(fr"IOSPageShop__click_button_{cls.button_index[name]}.png"),
                            target_rect=cls.__get_button_area(), click=True)

    @classmethod
    def _check_search_bar(cls):
        with dog.step(f"{cls.page_name}-确认搜索框存在"):
            assert_true(
                find_area_image(Template(r"IOSPageShop__check_search_bar_1.png"), target_rect=cls.__get_tab_area()))

        with dog.step(f"{cls.page_name}-确认搜索框-图搜图标存在"):
            assert_true(
                find_area_image(Template(r"IOSPageShop__check_search_bar_2.png"), target_rect=cls.__get_tab_area()))

    @classmethod
    def batch_edit_share(cls):
        with dog.step(f"{cls.page_name}-点击批量编辑/分享"):
            poco("com.truedian.dragon:id/tv_batch_share").click()

    @classmethod
    def table_batch_edit(cls):
        with dog.step(f"{cls.page_name}-批量编辑/分享唤起的弹框--点击批量编辑"):
            poco(text="批量编辑").click()

    @classmethod
    def batch_forward(cls):
        with dog.step(f"{cls.page_name}-点击好友个人相册--批量转发按钮"):
            poco("com.truedian.dragon:id/tv_batch_share").click()


    @classmethod
    def check_vip_status(cls):
        with dog.step(f"{cls.page_name}-校验VIP/SVIP图标暂时是否正常"):
            assert_true(find_area_image(Template(r"common_svip.png"), target_rect=cls.__get_info_area()))

    @classmethod
    def check_new_number(cls):
        with dog.step(f"{cls.page_name}-校验上新"):
            assert_true(
                find_area_image(Template(r"IOSPageShop_check_new_number_1.png"), target_rect=cls.__get_info_area()),
                "未暂展示正确的“上新”文案")
            # 数量不好校验

    @classmethod
    def check_total_number(cls):
        with dog.step(f"{cls.page_name}-校验总数"):
            assert_true(
                find_area_image(Template(r"IOSPageShop_check_total_number_1.png"), target_rect=cls.__get_info_area()),
                "未暂展示正确的“总数”文案")
            # 数量不好校验

    @classmethod
    def check_all_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-全部列表-发布商品按钮是否存在"):
            assert_true(
                find_area_image(Template(r"IOSPageShop_check_all_list_1.png"), target_rect=cls.__get_list_area()))

        with dog.step(f"{cls.page_name}-全部列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-全部列表-判断界面是否白屏"):
            assert_false(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def check_new_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-上新列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-上新列表-判断界面是否白屏"):
            assert_false(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def check_video_list(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-小视频列表-判断界面是否白屏"):
            assert_false(ui.is_white_area(target_rect=cls.__get_list_area()))

        with dog.step(f"{cls.page_name}-小视频列表-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-小视频列表-判断界面是否白屏"):
            assert_false(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def check_picture_grid(cls):
        cls._check_search_bar()

        with dog.step(f"{cls.page_name}-图集-判断界面是否白屏"):
            assert_false(ui.is_white_area(target_rect=cls.__get_list_area()))

        with dog.step(f"{cls.page_name}-图集-上滑"):
            swipe_up()

        with dog.step(f"{cls.page_name}-图集-判断界面是否白屏"):
            assert_false(ui.is_white_area(target_rect=cls.__get_list_area()))

    @classmethod
    def good_share(cls):
        super().good_share()
        swipe_wait_for(Template(r"IOSPageShop_good_share_1.png", threshold=0.9), click=True)

    @classmethod
    def shop_table_share(cls):
        with dog.step(f"{cls.page_name}-右上角分享标识"):
            poco("nav share icon").click()

    @classmethod
    def table_share_code(cls):
        with dog.step(f"{cls.page_name}-分享我的主页--二维码"):
            poco("com.truedian.dragon:id/qr_code").click()

    @classmethod
    def shop_search_first_value(cls):
        with dog.step(f"{cls.page_name}-个人相册页--点击搜索出来的第一个商品标题"):
            poco("com.truedian.dragon:id/title_home_fragment").click()


    @classmethod
    def shop_search_name(cls):
        cls.shop_table_search()
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            text("验证商品置顶刷新")
            cls.wait_for_enter()
        cls.shop_search_first_value()

    @classmethod
    def page_add_shop_car(cls):
        with dog.step(f"{cls.page_name}-点击购物车"):
            poco("com.truedian.dragon:id/gouwuche").click()
            cls.wait_for_enter()


    @classmethod
    def shop_mine_cart_add(cls):
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            cls.shop_table_search()
            text("标题价格300元")

    @classmethod
    def page_shop_forward(cls):
        with dog.step(f"{cls.page_name}-个人相册页--转发"):
            poco("com.truedian.dragon:id/share_home_fragment").click()

    @classmethod
    def shop_friend_search(cls):
        cls.shop_table_search()
        text("验证转发商品测试数")
        sleep(ui.step_wait_time)

        find_area_image(Template(r"tpl1745743211519.png"),
                                        target_rect=(get_vertical_rect(0.45)),click=True)
        cls.wait_for_enter()

    @classmethod
    def shop_friend_click(cls):
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            cls.shop_table_search()
            text("验证转发商品测试数")
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745743211519.png"), target_rect=get_vertical_rect(-0.45), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_friend_contact(cls):
        find_area_image(Template(r"tpl1745314413629.png"), target_rect=get_vertical_rect(-0.15), click=True)
        sleep(ui.step_wait_time)

    @classmethod
    def page_shop_clean_up(cls):
        with dog.step(f"{cls.page_name}-个人相册页--批量删除/图文清理"):
            poco("批量删除/图文清理").click()