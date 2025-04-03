# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 19:03
# Description:
# -------------------------------------------------------------------------

from common import dog
from common.ui import Template, find_area_image
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

