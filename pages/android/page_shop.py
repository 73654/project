# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 16:46
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import poco
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
    def tab_picture_collection(cls):
        cls._click_tab("全部")

    @classmethod
    def button_goods(cls):
        cls._click_button("tv_tag_category_container", "商品分类")

    @classmethod
    def button_batch_share(cls):
        cls._click_button("ll_batch_share", "批量编辑和分享")

    @classmethod
    def button_contact(cls):
        cls._click_button("tv_connect_other", "联系Ta")
