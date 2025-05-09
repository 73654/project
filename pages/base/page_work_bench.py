# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_work_bench
@ time:    2025/4/17 16:20 
@ desc:
"""


from pages.base.page import BasePage
from common import dog,ui
from common.ui import poco
from common.ui import Template, find_all_area_image, find_area_image,get_vertical_rect,touch_and_wait
from common.ui import DeviceType

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
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template(r"tpl1745204867043.png"), target_rect=(get_vertical_rect(0.3)), click=True)
            else:
                find_area_image(Template(r"tpl1745204867043.png",threshold=0.6), target_rect=(0.75,0.1,1,0.32), click=True)
            cls.wait_for_enter()


    @classmethod
    def page_work_check_earning(cls):
        with dog.step(f"{cls.page_name}-查看收益"):
            find_area_image(Template(r"tpl1745493384205.png"), target_rect=(get_vertical_rect(-0.6)), click=True)
            cls.wait_for_enter()






