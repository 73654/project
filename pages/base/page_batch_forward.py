# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_batch_forword
@ time:    2025/4/16 16:53 
@ desc:
"""
from airtest.core.assertions import assert_is_not_none

from pages.base.page import BasePage
from common import dog
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, scroll_and_find_element
from common.ui import poco

class PageBatchForward(BasePage):
    page_name="批量转发页面"

    @classmethod
    def page_batch_filter(cls):
        with dog.step(f"{cls.page_name}-筛选"):
            pass

    @classmethod
    def page_batch_end_time(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--结束时间"):
            pass


    @classmethod
    def page_filter_little_video(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--小视频"):
            pass


    @classmethod
    def page_filter_confirm(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--确认按钮"):
            find_area_image(Template(r"tpl1744795603380.png"), target_rect=(get_vertical_rect(-0.2)), click=True)

    @classmethod
    def page_batch_add_tabel(cls):
        with dog.step(f"{cls.page_name}-添加标签"):
            pass


    @classmethod
    def page_batch_search(cls):
        with dog.step(f"{cls.page_name}-搜索"):
            pass


    @classmethod
    def click_search_result(cls):
        with dog.step(f"{cls.page_name}-点击搜索后的结果"):
            find_area_image(Template(r"tpl1744852657237.png"), target_rect=(get_vertical_rect(0.4)), click=True)


    @classmethod
    def page_batch_increase_price(cls):
        with dog.step(f"{cls.page_name}-加价转"):
            pass


    @classmethod
    def page_batch_enter_price(cls):
        with dog.step(f"{cls.page_name}-请填写金额(选填)"):
            pass

    @classmethod
    def page_batch_next_step(cls):
        with dog.step(f"{cls.page_name}-点击下一步"):
            find_area_image(Template(r"tpl1744862202743.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            cls.wait_for_enter()


    @classmethod
    def page_batch_next_button(cls):
        with dog.step(f"{cls.page_name}-确认"):
            find_area_image(Template(r"tpl1744868937101.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_batch_mine_shop(cls):
        with dog.step(f"{cls.page_name}-查看我的相册"):
            pass



    @classmethod
    def page_batch_label(cls):
        with dog.step(f"{cls.page_name}-判断页面是否存在自定义标签,如果不存在则添加"):
            label = find_area_image(Template(r"tpl1744857835595.png"), target_rect=(get_vertical_rect(-0.3)))
            if label:
                pass
            else:
                cls.page_batch_add_tabel()
                cls.wait_for_enter()
                find_area_image(Template(r"tpl1744860208813.png"), target_rect=(get_vertical_rect(0.4)),click=True)
                find_area_image(Template(r"tpl1744861170613.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
                cls.back()


            cls.page_batch_next_step()
            cls.page_batch_next_button()

        with dog.step(f"{cls.page_name}-判断页面是否存在转发成功字样"):
            cls.wait_for_enter()
            assert_is_not_none(find_area_image(Template(r"tpl1744872672373.png"), target_rect=(get_vertical_rect(0.4))))


    @classmethod
    def check_tabel_info(cls):
        with dog.step(f"{cls.page_name}-下滑滚动页面，在页面上查看转发后的商品"):
            check_title='商品标题价310元'
            scroll_and_find_element(max_scroll_times=3,target_rect=0.4,target_condition={'text':check_title},click=True)
            cls.wait_for_enter()
            assert_is_not_none(find_area_image(Template(r"tpl1744874968440.png"), target_rect=(0.2,0.4,0.6,0.6)))
            assert_is_not_none(find_area_image(Template(r"tpl1744873647885.png"), target_rect=(get_vertical_rect(-0.5))))
            cls.back()




