# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 16:46
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import text
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true
from common import dog, ui
from common import dog
from common.ui import Template, find_area_image, poco, swipe_up
from common.ui import swipe_wait_for,scroll_and_find_element,get_vertical_rect,get_horizontal_rect
from pages.base.page_shop import BasePageShop
from airtest.core.api import home, keyevent, sleep, swipe


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
    def batch_edit_share(cls):
        with dog.step(f"{cls.page_name}-点击批量分享/编辑"):
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
    def _check_search_bar(cls):
        with dog.step(f"{cls.page_name}-确认搜索框存在"):
            search_bar = poco(nameMatches=".*id/search_view_home")
            assert_true(search_bar.exists())

        with dog.step(f"{cls.page_name}-确认搜索框-文案为: 搜索"):
            text = search_bar.offspring(nameMatches=".*id/et_search").get_text()
            assert_true(text.__contains__("搜索"), f"搜索框文案不包含搜索：原文案： {text}")

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
            poco.scroll("vertical", 0.38)

            assert_is_not_none(find_area_image(Template(r"tpl1745820651067.png"), target_rect=(get_vertical_rect(-0.6))))
            poco.scroll("vertical", -0.38)

            # assert_true(swipe_wait_for(cls.__share_button()))

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
            poco.scroll("vertical", 0.45)
            assert_is_not_none(find_area_image(Template(r"tpl1745821075739.png"), target_rect=(get_horizontal_rect(0.4))))
            poco.scroll("vertical", -0.45)
            # assert_true(swipe_wait_for(poco(nameMatches=".*id/ll_dynamic_edit").offspring(text="删除")))

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


    @classmethod
    def shop_table_share(cls):
        with dog.step(f"{cls.page_name}-右上角分享标识"):
            poco("com.truedian.dragon:id/iv_date").click()


    @classmethod
    def table_share_code(cls):
        with dog.step(f"{cls.page_name}-分享我的主页--二维码"):
            poco("com.truedian.dragon:id/qr_code").click()


    @classmethod
    def shop_table_search(cls):
        with dog.step(f"{cls.page_name}-个人相册页--搜索"):
            poco("com.truedian.dragon:id/et_search").click()
            cls.wait_for_enter()

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
    def shop_cart_add(cls):
        with dog.step(f"{cls.page_name}-好友相册页--输入要查询的商品名称"):
            cls.shop_table_search()
            text("标题价格499元")

    @classmethod
    def page_add_shop_car(cls):
        with dog.step(f"{cls.page_name}-点击购物车"):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745832710232.png"),
                            target_rect=(get_vertical_rect(0.6)), click=True)
            cls.wait_for_enter()
            find_area_image(Template(r"tpl1745832781441.png"),
                            target_rect=(get_vertical_rect(-0.65)), click=True)

            cls.wait_for_enter()

    @classmethod
    def shop_mine_cart_add(cls):
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            cls.shop_table_search()
            text("标题价格300元")
            sleep(ui.step_wait_time)
            scroll_and_find_element(max_scroll_times=2, target_rect=0.3)
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745893534161.png"),
                            target_rect=(get_vertical_rect(0.5)), click=True)

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
                        target_rect=(get_vertical_rect(-0.45)),click=True)
        cls.wait_for_enter()

    @classmethod
    def shop_friend_click(cls):
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            cls.shop_table_search()
            text("验证转发商品测试数")
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745310773304.png"), target_rect=get_vertical_rect(-0.39), click=True)
            cls.wait_for_enter()


    @classmethod
    def shop_share_poster_click(cls):
        with dog.step(f"{cls.page_name}-搜索--海报分享-勿删商品"):
            cls.shop_table_search()
            text("海报分享-勿删")
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745811562751.png"), target_rect=(0.7,0.6,1,0.85), click=True)
            cls.wait_for_enter()


    @classmethod
    def page_friend_contact(cls):
        with dog.step(f"{cls.page_name}-个人相册页--联系ta"):
            find_area_image(Template(r"tpl1745314413629.png"), target_rect=get_vertical_rect(-0.15), click=True)

    @classmethod
    def page_shop_clean_up(cls):
        with dog.step(f"{cls.page_name}-个人相册页--批量删除/图文清理"):
            poco(text="批量删除/图文清理").click()
