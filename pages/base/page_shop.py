# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 19:03
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import keyevent, touch

from common import dog
from common.ui import Template, find_area_image
from pages.base.page import BasePage


class BasePageShop(BasePage):
    """我的店铺主页"""

    @classmethod
    def tab_all(cls):
        with dog.step(f"店铺主页-全部"):
            touch(Template(r"BasePageShop_tab_all_1.png"))

    @classmethod
    def tab_new(cls):
        with dog.step(f"店铺主页-上新"):
            touch(Template(r"BasePageShop_tab_new_1.png"))

    @classmethod
    def tab_video(cls):
        with dog.step(f"店铺主页-小视频"):
            touch(Template(r"BasePageShop_tab_video_1.png"))

    @classmethod
    def tab_picture_grid(cls):
        with dog.step(f"店铺主页-图集"):
            touch(Template(r"BasePageShop_tab_picture_collection_1.png"))

    @classmethod
    def button_goods(cls):
        with dog.step(f"店铺主页-商品分类按钮"):
            touch(Template(r"BasePageShop_button_goods_1.png"))

    @classmethod
    def button_batch_share(cls):
        with dog.step(f"店铺主页-批量编辑和分享"):
            touch(Template(r"BasePageShop_button_batch_share_1.png"))

    @classmethod
    def button_contact(cls):
        with dog.step(f"店铺主页-联系Ta"):
            touch(Template(r"BasePageShop_button_contact_1.png"))

    @classmethod
    def check_vip_status(cls):
        with dog.step("店铺主页-VIP/SVIP图标暂时是否正常"):
            find_area_image(Template(r"common_svip.png"))

    @classmethod
    def check_new_number(cls):
        with dog.step("店铺主页-上新及数量"):
            pass

    @classmethod
    def check_total_number(cls):
        with dog.step("店铺主页-总数及数量"):
            pass


    @classmethod
    def back_to_main_page(cls):
        with dog.step("店铺主页-返回到主页"):
            keyevent("BACK")