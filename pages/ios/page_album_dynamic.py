# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_album_dynamic
@ time:    2025/4/14 15:43 
@ desc:
"""

from pages.base.page import BasePage
from common.ui import poco, find_area_image, touch_and_wait
from pages.base.page_album_dynamic import BasePageAlbumDynamic
from airtest.core.api import text, double_click
from common import dog, ui
from airtest.core.api import home, keyevent, sleep, swipe,assert_is_not_none
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
    def page_team_permission_search(cls):
        with dog.step(f"{cls.page_name}-团队权限商品搜索"):
            cls._perform_search("团队权限商品")



    @classmethod
    def text_search(cls):
        with dog.step(f"{cls.page_name}-标题价格300元搜索"):
            cls._perform_search("标题价格300元")


    @classmethod
    def page_release(cls):
        with dog.step(f"{cls.page_name}-发布"):
            poco("发布").click()
            sleep(ui.step_wait_time)




    @classmethod
    def page_add_commodity_img(cls):
        with dog.step(f"{cls.page_name}-通用_0012新增商品搜索"):
            cls._perform_search("通用_0012新增商品")
            cls.wait_for_enter()
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1747102876896.png"), target_rect=(get_vertical_rect(0.35)), click=True)

            cls.wait_for_enter()

            find_area_image(Template(r"tpl1747106908012.png",threshold=0.6), target_rect=(0.18,0.85,0.4,1), click=True)
            for i in range(3):
                sleep(ui.step_wait_time)

            find_area_image(Template(r"tpl1747103404000.png"), target_rect=(0, 0.02, 0.14, 0.14),click=True)

            for i in range(2):
                sleep(ui.step_wait_time)

            left_img = find_area_image(Template(r"tpl1747102640128.png",threshold=0.6), target_rect=(0.7,0.1,1,0.38))
            sleep(ui.step_wait_time)
            if left_img:
                test_clean_image=poco("image search close")
                if test_clean_image:
                    test_clean_image.click()
                else:
                    find_area_image(Template(r"tpl1747105990802.png"), target_rect=(0.86,0.08,1,0.23),click=True)

            sleep(ui.step_wait_time)

            find_area_image(Template(r"tpl1747103404000.png"), target_rect=(0, 0.02, 0.15, 0.15),click=True)


    @classmethod
    def page_new_commodity_search(cls):
        with dog.step(f"{cls.page_name}-新增商品搜索"):
            sleep(ui.step_wait_time)
            cls._perform_search("安卓自动化测滨海wegoufsafsdfsdfsdf")
            cls.wait_for_enter()

    @classmethod
    def page_check_commodity_info(cls):
        with dog.step(f"{cls.page_name}-检查新增商品价格"):
            sleep(ui.step_wait_time)
            assert_is_not_none(
                find_area_image(Template(r"tpl1747128040250.png"), target_rect=(get_vertical_rect(-0.35))))
            assert_is_not_none(
                find_area_image(Template(r"tpl1747128055587.png"), target_rect=(get_vertical_rect(-0.3))))
