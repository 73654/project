# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 19:03
# Description:
# -------------------------------------------------------------------------

from common import dog,ui
from common.ui import Template, find_area_image, poco, get_vertical_rect, scroll_and_find_element, touch_and_wait
from pages.base.page import BasePage
from pages.base.page_dynamic_detail import PageDynamicDetail
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import DeviceType

class BasePageShop(BasePage):
    """我的店铺主页"""

    page_name = "店铺主页"

    @classmethod
    def _click_tab(cls, name):
        pass

    @classmethod
    def _click_button(cls, view_id, name):
        pass

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
        with dog.step(f"{cls.page_name}-VIP/SVIP图标暂时是否正常"):
            pass

    @classmethod
    def check_new_number(cls):
        with dog.step(f"{cls.page_name}-上新及数量"):
            pass

    @classmethod
    def check_total_number(cls):
        with dog.step(f"{cls.page_name}-总数及数量"):
            pass

    @classmethod
    def back_to_main_page(cls):
        with dog.step(f"{cls.page_name}-返回到主页"):
            cls.back()

    @classmethod
    def check_all_list(cls):
        pass

    @classmethod
    def check_new_list(cls):
        pass

    @classmethod
    def check_video_list(cls):
        pass

    @classmethod
    def check_picture_grid(cls):
        pass

    @classmethod
    def good_share(cls):
        with dog.step(f"{cls.page_name}-下滑找到分享按钮，并点击分享"):
            pass

    @classmethod
    def shop_table_share(cls):
        with dog.step(f"{cls.page_name}-右上角分享标识"):
            pass

    @classmethod
    def table_share_code(cls):
        with dog.step(f"{cls.page_name}-分享我的主页--二维码"):
            pass


    @classmethod
    def batch_edit_share(cls):
        with dog.step(f"{cls.page_name}-点击批量编辑/分享"):
            pass


    @classmethod
    def table_batch_edit(cls):
        with dog.step(f"{cls.page_name}-批量编辑/分享唤起的弹框--点击批量编辑"):
            pass

    @classmethod
    def batch_forward(cls):
        with dog.step(f"{cls.page_name}-点击好友个人相册--批量转发按钮"):
            pass

    @classmethod
    def share_wx_friend(cls):
        with dog.step(f"{cls.page_name}-分享我的主页--点击微信好友"):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1744599239811.png",threshold=0.6), target_rect=get_vertical_rect(-0.3), click=True)
            cls.wait_for_enter()


    @classmethod
    def shop_table_search(cls):
        with dog.step(f"{cls.page_name}--搜索"):
            pass

    @classmethod
    def find_top_element(cls):
        with dog.step(f"{cls.page_name}--往下滚动查询title为验证商品置顶刷新商品并点击"):
            sleep(ui.step_wait_time)
            if ui.current_device_type == DeviceType.Android:
                scroll_and_find_element(max_scroll_times=3,target_rect=0.4, target_condition={'text': '验证商品置顶刷新'}, click=True)
            else:
                # ios 机型走下面流程

                find_area_image(Template(r"tpl1746685312964.png"), target_rect=(get_vertical_rect(-0.45)),
                                click=True)

            cls.wait_for_enter()

    @classmethod
    def find_refresh_element(cls):
        with dog.step(f"{cls.page_name}--往下滚动查询title为验证商品置顶刷新商品"):
            if ui.current_device_type == DeviceType.Android:
                scroll_and_find_element(max_scroll_times=1, target_rect=-0.3, target_condition={'text': '置顶'})
            else:
                poco.scroll("vertical", 0.3)

            cls.find_top_element()

    @classmethod
    def find_refresh_back(cls):

        with dog.step(f"{cls.page_name}--返回到个人相册页"):
            PageDynamicDetail.back_shop_page()
        with dog.step(f"{cls.page_name}--查看刷新后的商品-验证商品置顶刷新"):
            if ui.current_device_type == DeviceType.Android:
                scroll_and_find_element(max_scroll_times=1, target_rect=-0.3, target_condition={'text': '置顶'})
                scroll_and_find_element(max_scroll_times=3, target_rect=0.4, target_condition={'text': '验证商品置顶刷新'},
                                    click=True)
            else:
                poco.scroll("vertical", 0.3)

            cls.wait_for_enter()

    @classmethod
    def shop_cart_add(cls):
        with dog.step(f"{cls.page_name}-搜索要查询的商品名称"):
            pass

    @classmethod
    def page_add_shop_car(cls):
        with dog.step(f"{cls.page_name}-点击购物车"):
            pass

    @classmethod
    def shop_mine_cart_add(cls):
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            pass

    @classmethod
    def page_shop_forward(cls):
        with dog.step(f"{cls.page_name}-个人相册页--转发"):
            pass

    @classmethod
    def shop_friend_search(cls):
        pass


    @classmethod
    def shop_friend_click(cls):
        with dog.step(f"{cls.page_name}-个人相册页--输入要查询的商品名称"):
            pass

    @classmethod
    def page_friend_contact(cls):
        pass

    @classmethod
    def page_shop_clean_up(cls):
        with dog.step(f"{cls.page_name}-个人相册页--批量删除/图文清理"):
            pass

    @classmethod
    def page_check_photo_permission(cls):
        with dog.step(f"{cls.page_name}-开启所有照片权限弹框"):
            photo_permission=find_area_image(Template(r"tpl1746586958785.png"), target_rect=get_vertical_rect(0.65))
            if photo_permission:
                find_area_image(Template(r"tpl1746586968705.png"), target_rect=get_vertical_rect(-0.2),click=True)
                cls.wait_for_enter()





