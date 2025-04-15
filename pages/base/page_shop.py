# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 19:03
# Description:
# -------------------------------------------------------------------------

from common import dog
from common.ui import Template, find_area_image,poco,get_vertical_rect,scroll_and_find_element
from pages.base.page import BasePage


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
    def share_wx_friend(cls):
        with dog.step(f"{cls.page_name}-分享我的主页--点击微信好友"):
            find_area_image(Template(r"tpl1744599239811.png"),target_rect=get_vertical_rect(-0.3),click=True)
            cls.wait_for_enter()



    @classmethod
    def shop_table_search(cls):
        with dog.step(f"{cls.page_name}--搜索"):
            pass

    @classmethod
    def find_top_element(cls):
        with dog.step(f"{cls.page_name}--往下滚动查询商品"):
            scroll_and_find_element(max_scroll_times=3,target_condition={'text':'验证商品置顶刷新'},click=True)
