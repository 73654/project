# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_clean_up_images
@ time:    2025/4/23 14:27 
@ desc:
"""


from pages.base.page_clean_up_images import PageCleanUpImages
from common import dog
from common.ui import poco
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true



class IOSPageCleanUpImages(PageCleanUpImages):
    page_name="清理图文"

    @classmethod
    def page_clean_image(cls):
        with dog.step(f"{cls.page_name}-图文清理"):
            cls.wait_for_enter()
            poco("图文清理").click()


    @classmethod
    def page_cloud_storage_space(cls):
        with dog.step(f"{cls.page_name}-计算云空间大小"):
            target_element = poco(textMatches=r'^.*G/500G')
            if target_element.exists():
                text = target_element.get_text()
                values = text.split('/')
                return values[0]


    def page_cloud_to_clean(cls):
        with dog.step(f"{cls.page_name}-去清理"):
            poco("去清理").click()



    @classmethod
    def page_cloud_ensure_windows(cls):
        with dog.step(f"{cls.page_name}-点击确认清理"):
            poco("确认清理").click()


    @classmethod
    def page_recycle_bin(cls):
        with dog.step(f"{cls.page_name}-回收站"):
            poco("回收站").click()

    @classmethod
    def page_recycle_restore_all(cls):
        with dog.step(f"{cls.page_name}-全部恢复"):
            poco("全部恢复").click()

    @classmethod
    def page_recycle_restore_listed(cls):
        with dog.step(f"{cls.page_name}-恢复到已上架"):
            poco("恢复到已上架").click()