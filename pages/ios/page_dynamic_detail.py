# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_dynamic_detail
@ time:    2025/4/14 17:50 
@ desc:
"""

from common import dog, ui
from pages.base.page import BasePage
from airtest.core.api import text
from common.ui import poco, Template
from airtest.core.assertions import assert_not_equal, assert_is_not_none, assert_is_none
from pages.base.page_dynamic_detail import PageDynamicDetail
from pages.base.page_shop import BasePageShop
from common.ui import scroll_and_find_element, get_vertical_rect, find_area_image
from airtest.core.api import home, keyevent, sleep, swipe
from common.ui import DeviceType

class IOSPageDynamicDetail(PageDynamicDetail):
    page_name = "动态详情页"

    @classmethod
    def _handle_commodity_status(cls, first_text, second_text):
        with dog.step(f"{cls.page_name}-动态详情页处理商品状态"):
            first_button = poco(first_text)
            second_button = poco(second_text)
            if first_button:
                first_button.click()
                cls.wait_for_enter()
            elif second_button:
                second_button.click()
                cls.wait_for_enter()
                first_button.click()

    @classmethod
    def table_commodity_top(cls):
        cls._handle_commodity_status("置顶", "取顶")

    @classmethod
    def table_commodity_obtain_top(cls):
        cls._handle_commodity_status("取顶", "置顶")

    @classmethod
    def back_shop_page(cls):
        with dog.step(f"{cls.page_name}-返回到个人相册页"):
            cls.back()
            cls.wait_for_enter()

        with dog.step(f"{cls.page_name}-个人相册页置顶区域不存在验证商品置顶刷新"):
            assert_is_none(find_area_image(Template(r"tpl1746685312964.png"), target_rect=(0.2, 0.5, 0.6, 0.8)))

    @classmethod
    def table_refresh(cls):
        with dog.step(f"{cls.page_name}-动态详情页--点击刷新按钮"):

            cls.wait_for_enter()
            sleep(ui.step_wait_time)

            poco("刷新").click()

        with dog.step(f"{cls.page_name}-动态详情页--断言出现刷新成功字样"):
            if ui.current_device_type == DeviceType.Android:
                find_area_image(Template(r"tpl1744785314244.png", threshold=0.6), target_rect=(get_vertical_rect(-0.4)))

    @classmethod
    def page_one_click_forward(cls):
        with dog.step(f"{cls.page_name}-动态详情页--一键转发"):
            cls.wait_for_enter()
            find_area_image(Template(r"tpl1746617853940.png"), target_rect=(get_vertical_rect(-0.2)), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_detail_drag_other(cls):
        with dog.step(f"{cls.page_name}-动态详情页--移动主素材的位置"):
            photo_a = poco("Cell")[0].child("matter edit item delete icon")[1]
            photo_b = poco("Cell")[0].child("matter edit item delete icon")[3]
            photo_a.drag_to(photo_b)

            sleep(ui.step_wait_time)

    @classmethod
    def page_detail_delete_material(cls):
        with dog.step(f"{cls.page_name}-删除子素材"):
            poco.scroll("vertical", 0.38)
            # scroll_and_find_element(max_scroll_times=2, target_rect=0.3, target_condition={'text': '谁可以看'})
            if poco("matter edit delete icon"):
                poco("matter edit delete icon").click()
                sleep(ui.step_wait_time)
                poco("删除").click()
