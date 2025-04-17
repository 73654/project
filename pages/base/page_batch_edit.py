# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_batch_edit
@ time:    2025/4/16 16:00 
@ desc:
"""

from pages.base.page import BasePage
from common import dog
from common.ui.ui import scroll_and_find_element

class PageBatchEdit(BasePage):
    page_name = "批量编辑页"


    @classmethod
    def check_page_scroll(cls):
        with dog.step(f"{cls.page_name}-上下滚动查看页面是否有白屏"):
            scroll_and_find_element(max_scroll_times=2,target_rect=0.2)
            cls.wait_for_enter()
            scroll_and_find_element(max_scroll_times=2, target_rect=-0.2)
        with dog.step(f"{cls.page_name}-返回到好友table页"):
            for i in range(2):
                cls.back()




