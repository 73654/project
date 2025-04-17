# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_batch_forword
@ time:    2025/4/16 16:53 
@ desc:
"""
from airtest.core.api import text
from pages.base.page_batch_forward import PageBatchForward
from common import dog
from common.ui import poco


class IOSPageBatchForward(PageBatchForward):
    page_name = "批量转发页面"

    @classmethod
    def page_batch_filter(cls):
        with dog.step(f"{cls.page_name}-筛选"):
            poco(text="筛选").click()
            cls.wait_for_enter()

    @classmethod
    def page_batch_end_time(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--结束时间"):
            poco(text="结束时间").click()


    @classmethod
    def page_filter_little_video(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--小视频"):
            poco(text="小视频").click()

    @classmethod
    def page_batch_search(cls):
        with dog.step(f"{cls.page_name}-搜索"):
            poco("android.widget.EditText").click()
            text("商品标题价300元")
            cls.wait_for_enter()


    @classmethod
    def page_batch_increase_price(cls):
        with dog.step(f"{cls.page_name}-加价转"):
            poco(text="加价转").click()


    @classmethod
    def page_batch_enter_price(cls):
        with dog.step(f"{cls.page_name}-请填写金额(选填)"):
            poco("android.widget.EditText").click()
            text("10")

    @classmethod
    def page_batch_mine_shop(cls):
        with dog.step(f"{cls.page_name}-查看我的相册"):
            poco("查看我的相册").click()
            cls.wait_for_enter()