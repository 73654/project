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
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, touch_and_wait,scroll_and_find_element
from airtest.core.api import home, keyevent, sleep, swipe
from common import dog, ui
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true
from airtest.core.helper import log


class AndroidPageCleanUpImages(PageCleanUpImages):
    page_name = "清理图文"

    @classmethod
    def page_clean_image(cls):
        with dog.step(f"{cls.page_name}-图文清理"):
            poco(text="图文清理").click()
            cls.wait_for_enter()

    @classmethod
    def page_cloud_storage_space(cls):
        with dog.step(f"{cls.page_name}-计算云空间大小"):
            target_element = poco(textMatches=r'^.*G/500G')
            if target_element.exists():
                text = target_element.get_text()
                values = text.split('/')
                return values[0]

    @classmethod
    def page_cloud_to_clean(cls):
        with dog.step(f"{cls.page_name}-去清理"):
            find_area_image(Template(r"tpl1745496233499.png"), target_rect=(get_vertical_rect(0.45)), click=True)
            # poco(text="去清理").click()
            cls.wait_for_enter()

    @classmethod
    def page_cloud_ensure_windows(cls):
        with dog.step(f"{cls.page_name}-点击确认清理"):
            poco(text="确认清理").click()
            cls.wait_for_enter()
            for i in range(3):
                sleep(ui.step_wait_time)

    @classmethod
    def page_check_cloud_space(cls):
        with dog.step(f"{cls.page_name}-对比云空间数据清理前后的数据"):
            cls.page_click_delete_button()
            sleep(ui.step_wait_time)
            clean_first = cls.page_cloud_storage_space()
            cls.page_cloud_to_clean()
            cls.page_cloud_one_cleanup()
            cls.page_cloud_ensure_windows()
            cls.back()
            cls.page_clean_image()
            cls.page_click_delete_button()
            sleep(ui.step_wait_time)
            clean_after = cls.page_cloud_storage_space()
            print(clean_first, clean_after)
            assert clean_after < clean_first, "清理后云空间减少"

    @classmethod
    def page_recycle_bin(cls):
        with dog.step(f"{cls.page_name}-回收站"):
            poco(text="回收站").click()
            cls.wait_for_enter()


    @classmethod
    def check_shop_cloud_commodity(cls):
        with dog.step(f"{cls.page_name}-个人相册主页查看安卓复制商品是否在置顶位置"):
            # 往下滚动商品,判断个人相册页置顶区域有商品存在
            scroll_and_find_element(max_scroll_times=2,target_rect=0.3,target_condition={'text':'置顶'})
            sleep(ui.step_wait_time)
            scroll_and_find_element(max_scroll_times=3, target_rect=0.5, target_condition={'text': '亲，已经到底啦～'})
            sleep(ui.step_wait_time)

    @classmethod
    def page_recycle_restore_all(cls):
        with dog.step(f"{cls.page_name}-全部恢复"):
            poco(text="全部恢复").click()

    @classmethod
    def page_recycle_restore_listed(cls):
        with dog.step(f"{cls.page_name}-恢复到已上架"):
            poco(text="恢复到已上架").click()
