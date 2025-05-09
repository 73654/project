# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""

from pages.base.page import BasePage
from common.ui import poco,find_area_image
from pages.base.page_album_dynamic import BasePageAlbumDynamic
from airtest.core.api import text
from common import dog, ui
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import Template, poco, find_area_image, get_vertical_rect

class IOSBasePageAlbumDynamic(BasePageAlbumDynamic):
    """相册动态页"""
    page_name = "相册动态页"


    @classmethod
    def _perform_search(cls, keyword):
        find_area_image(Template(r"tpl1746606233200.png"), target_rect=(0.02, 0.18, 0.5, 0.32), click=True)
        sleep(ui.step_wait_time)
        text(keyword)
        sleep(ui.step_wait_time)

    @classmethod
    def text_search(cls):
        with dog.step(f"{cls.page_name}-标题价格300元搜索"):
            cls._perform_search("标题价格300元")


    @classmethod
    def page_release(cls):
        with dog.step(f"{cls.page_name}-发布"):
            poco("发布").click()

    @classmethod
    def _perform_search(cls, keyword):
        find_area_image(Template(r"tpl1746606233200.png"), target_rect=(0.02,0.18,0.5,0.32), click=True)

        sleep(ui.step_wait_time)
        text(keyword)
        sleep(ui.step_wait_time)


    @classmethod
    def page_add_commodity_img(cls):
        with dog.step(f"{cls.page_name}-通用_0012新增商品搜索"):
            cls._perform_search("通用_0012新增商品")
            cls.wait_for_enter()
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745724878443.png"), target_rect=(get_vertical_rect(0.35)), click=True)

            cls.wait_for_enter()
            find_area_image(Template(r"tpl1745552659688.png"), target_rect=(get_vertical_rect(-0.2)), click=True)
            for i in range(3):
                sleep(ui.step_wait_time)

            cls.back()
            for i in range(2):
                sleep(ui.step_wait_time)
            left_img = find_area_image(Template(r"tpl1746607401544.png"), target_rect=(0.7,0.15,1,0.35))
            find_area_image(Template(r"tpl1746608484832.png",threshold=0.6), target_rect=(0.85, 0.08, 1, 0.25), click=True)
            sleep(ui.step_wait_time)
            cls.back()