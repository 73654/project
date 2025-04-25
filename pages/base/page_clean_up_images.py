# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_clean_up_images
@ time:    2025/4/23 14:27 
@ desc:
"""


from pages.base.page import BasePage
from common import dog
from common.ui import poco
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true



class PageCleanUpImages(BasePage):
    page_name="清理图文"


    @classmethod
    def page_clean_image(cls):
        with dog.step(f"{cls.page_name}-图文清理"):
            pass

    @classmethod
    def page_click_delete_button(cls):
        with dog.step(f"{cls.page_name}-一键清理弹框关闭按钮"):
            find_area_image(Template(r"tpl1745394566874.png"), target_rect=(get_vertical_rect(0.4)),click=True)




    @classmethod
    def page_cloud_storage_space(cls):
        with dog.step(f"{cls.page_name}-计算云空间大小"):
            pass

    @classmethod
    def page_cloud_to_clean(cls):
        with dog.step(f"{cls.page_name}-去清理"):
            pass

    @classmethod
    def page_cloud_one_cleanup(cls):
        with dog.step(f"{cls.page_name}-一键清理"):
            find_area_image(Template(r"tpl1745401482235.png"), target_rect=(get_vertical_rect(-0.15)), click=True)



    @classmethod
    def page_cloud_ensure_windows(cls):
        with dog.step(f"{cls.page_name}-点击确认清理"):
            pass


    @classmethod
    def page_recycle_bin(cls):
        with dog.step(f"{cls.page_name}-回收站"):
            pass


    @classmethod
    def page_recycle_restore_all(cls):
        with dog.step(f"{cls.page_name}-全部恢复"):
            pass

    @classmethod
    def page_recycle_restore_listed(cls):
        with dog.step(f"{cls.page_name}-恢复到已上架"):
            pass