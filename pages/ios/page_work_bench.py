# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_work_bench
@ time:    2025/4/17 16:20 
@ desc:
"""

from pages.base.page import BasePage
from common import dog
from common.ui import poco
from pages.base.page_work_bench import PageWorkBench
class IOSPageWorkBench(PageWorkBench):
    page_name="工作台"

    # @classmethod
    # def page_invoice_write(cls):
    #     with dog.step(f"{cls.page_name}-开单"):
    #         poco(text="开单").click()
    #         cls.wait_for_enter()