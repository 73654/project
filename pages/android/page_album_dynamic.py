# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""
from pages.base.page_album_dynamic import BasePageAlbumDynamic
from common.ui import poco,find_area_image
from airtest.core.api import text
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui
from common.ui import Template, poco, find_area_image, get_vertical_rect

class AndroidBasePageAlbumDynamic(BasePageAlbumDynamic):
    """相册动态页"""
    page_name = "相册动态页"

    @classmethod
    def _perform_search(cls, keyword):
        poco("com.truedian.dragon:id/et_search").click()
        sleep(ui.step_wait_time)
        text(keyword)
        sleep(ui.step_wait_time)

    @classmethod
    def text_search(cls):
        with dog.step(f"{cls.page_name}-标题价格300元搜索"):
            cls._perform_search("标题价格300元")

    @classmethod
    def page_team_permission_search(cls):
        with dog.step(f"{cls.page_name}-团队权限商品搜索"):
            cls._perform_search("团队权限商品")

    @classmethod
    def page_add_commodity_img(cls):
        with dog.step(f"{cls.page_name}-通用_0012新增商品搜索"):
            cls._perform_search("通用_0012新增商品")
            cls.wait_for_enter()
            poco(text="通用_0012新增商品使用的图片资源").click()
            cls.wait_for_enter()
            find_area_image(Template(r"tpl1745552659688.png"), target_rect=(get_vertical_rect(-0.2)),click=True)
            for i in range(4):
                sleep(ui.step_wait_time)





    @classmethod
    def page_release(cls):
        with dog.step(f"{cls.page_name}-发布"):
            poco(text="发布").click()
            cls.wait_for_enter()