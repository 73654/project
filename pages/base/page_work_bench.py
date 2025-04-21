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
from common.ui import Template, find_all_area_image, find_area_image,get_vertical_rect,touch_and_wait

class PageWorkBench(BasePage):
    page_name="工作台"

    @classmethod
    def page_invoice_write(cls):
        with dog.step(f"{cls.page_name}-开单"):
            find_area_image(Template(r"tpl1744891352613.png"), target_rect=(get_vertical_rect(0.3)),click=True)


    @classmethod
    def check_invoice_windows(cls):
        with dog.step(f"{cls.page_name}-判断是否存在开单提示弹框"):
            invoice_windows=find_area_image(Template(r"tpl1744873647885.png"), target_rect=(get_vertical_rect(-0.15)))
            if invoice_windows:
                touch_and_wait(invoice_windows)


    @classmethod
    def receiving_payment_code(cls):
        with dog.step(f"{cls.page_name}-收款码"):
            find_area_image(Template(r"tpl1745204867043.png"), target_rect=(get_vertical_rect(0.3)), click=True)
            cls.wait_for_enter()





