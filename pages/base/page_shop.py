# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 19:03
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import touch

from common import dog
from common.dog import Template

from pages.base.page import BasePage


class BasePageShop(BasePage):
    """我的店铺主页"""

    @classmethod
    def tab_all(cls):
        with dog.step(f"店铺主页-全部"):
            touch(Template(r"tpl1743064141765.png"))

    @classmethod
    def tab_new(cls):
        with dog.step(f"店铺主页-上新"):
            touch(Template(r"tpl1743064145050.png"))

    @classmethod
    def tab_video(cls):
        with dog.step(f"店铺主页-小视频"):
            touch(Template(r"tpl1743064148415.png"))

    @classmethod
    def tab_picture_collection(cls):
        with dog.step(f"店铺主页-图集"):
            touch(Template(r"tpl1743064152096.png"))

    @classmethod
    def button_goods(cls):
        with dog.step(f"店铺主页-商品分类按钮"):
            touch(Template(r"tpl1743064328334.png"))

    @classmethod
    def button_batch_share(cls):
        with dog.step(f"店铺主页-批量编辑和分享"):
            touch(Template(r"tpl1743064342902.png"))

    @classmethod
    def button_contact(cls):
        with dog.step(f"店铺主页-联系Ta"):
            touch(Template(r"tpl1743064181106.png"))
