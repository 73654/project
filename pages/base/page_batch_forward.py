# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_batch_forword
@ time:    2025/4/16 16:53 
@ desc:
"""
from airtest.core.assertions import assert_is_not_none

from pages.base.page import BasePage
from common import dog, ui
from common.ui import Template, find_all_area_image, find_area_image, get_vertical_rect, swipe_wait_for, \
    scroll_and_find_element
from common.ui import poco
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import DeviceType


class PageBatchForward(BasePage):
    page_name = "批量转发页面"

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
            find_area_image(Template(r"tpl1744795603380.png", threshold=0.6), target_rect=(get_vertical_rect(-0.2)),
                            click=True)

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
            search_result = find_area_image(Template(r"tpl1745746833047.png"), target_rect=(get_vertical_rect(-0.6)))
            if search_result:
                find_area_image(Template(r"tpl1745746844347.png"), target_rect=(get_vertical_rect(0.25)), click=True)

            sleep(ui.step_wait_time)
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template(r"tpl1744852657237.png"), target_rect=(get_vertical_rect(0.4)), click=True)
            else:
                find_area_image(Template(r"tpl1746759786894.png"), target_rect=(0.05, 0.22, 0.2, 0.35), click=True)

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
            if ui.current_device_type == DeviceType.Android:
                label = find_area_image(Template(r"tpl1744857835595.png"), target_rect=(get_vertical_rect(-0.35)))
            else:
                label = find_area_image(Template(r"tpl1746774372706.png"), target_rect=(0.04, 0.6, 0.45, 0.75))
            if label:
                pass

            else:
                cls.page_batch_add_tabel()
                cls.wait_for_enter()
                if ui.current_device_type == DeviceType.Android:
                    find_area_image(Template(r"tpl1744860208813.png"), target_rect=(get_vertical_rect(0.4)), click=True)
                else:
                    find_area_image(Template(r"tpl1746772811394.png"), target_rect=(0.02, 0.28, 0.45, 0.45), click=True)
                cls.wait_for_enter()
                sleep(ui.step_wait_time)

                find_area_image(Template(r"tpl1744861170613.png"), target_rect=(get_vertical_rect(-0.15)), click=True)
                sleep(ui.step_wait_time)

            cls.page_batch_next_step()
            cls.page_batch_next_button()

        with dog.step(f"{cls.page_name}-判断页面是否存在转发成功字样"):
            cls.wait_for_enter()
            assert_is_not_none(find_area_image(Template(r"tpl1744872672373.png"), target_rect=(get_vertical_rect(0.4))))

    @classmethod
    def check_tabel_info(cls):
        with dog.step(f"{cls.page_name}-下滑滚动页面，在页面上查看转发后的商品"):
            check_title = '商品标题价310元'
            if ui.current_device_type == DeviceType.Android:
                scroll_and_find_element(max_scroll_times=3, target_rect=0.4, target_condition={'text': check_title},
                                        click=True)
                cls.wait_for_enter()
            else:
                poco.scroll("vertical", 0.3)
                sleep(ui.step_wait_time)
                share_commodity_title = poco("商品标题价310元")
                if share_commodity_title:
                    share_commodity_title.click()
                else:
                    find_area_image(Template(r"tpl1746774993550.png"), target_rect=(0.3, 0.4, 0.75, 0.8),
                                    click=True)

            assert_is_not_none(find_area_image(Template(r"tpl1744874968440.png"), target_rect=(0.2, 0.4, 0.6, 0.6)))
            assert_is_not_none(
                find_area_image(Template(r"tpl1744873647885.png"), target_rect=(get_vertical_rect(-0.5))))
            cls.back()
