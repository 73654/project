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
import re



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
            storage_start = poco("Window").child("Other").child("Other").child("Other").child("Other").child(
                "Other").child("Other").child("Other").child("Other").child("Other").child("WebView").child(
                "WebView").child("WebView").child("Other").child("Other").child("Other").child("云空间清理").offspring(
                "500G").parent().children().attr("value")
            storage_extract = re.findall(r'\d+\.\d+', storage_start)
            storage = float(storage_extract[0])
            print("返回的数据storage",storage)
            return storage




    @classmethod
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
            assert clean_after <= clean_first, "清理后云空间减少"


    @classmethod
    def check_shop_cloud_commodity(cls):
        with dog.step(f"{cls.page_name}-个人相册主页查看安卓复制商品是否在置顶位置"):
            # 往下滚动商品,判断个人相册页置顶区域有商品存在

            sleep(ui.step_wait_time)
            last_page_tips = find_area_image(Template(r"tpl1747019937577.png", threshold=0.35), target_rect=(get_vertical_rect(-0.3)))
            while not last_page_tips:
                swipe((600, 1100), (600, 400))
            #
            # find_area_image(Template(r"tpl1747019937577.png", threshold=0.6), target_rect=(get_vertical_rect(-0.3)),
            #                 click=True)
            # scroll_and_find_element(max_scroll_times=3, target_rect=0.5, target_condition='亲，已经到底啦～')
            # sleep(ui.step_wait_time)