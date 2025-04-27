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
from common.ui import poco,Template,find_area_image,get_vertical_rect,scroll_and_find_element
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_true

class PageDynamicDetail(BasePage):
    page_name = "动态相册页"

    @classmethod
    def table_commodity_top(cls):
        with dog.step(f"{cls.page_name}-动态详情页判断商品是否是置顶状态,并置顶该商品"):
            pass

    @classmethod
    def back_to_friend_page(cls):
        with dog.step(f"{cls.page_name}-返回到好友页"):
            for i in range(2):
                cls.back()

    @classmethod
    def back_shop_page(cls):
        with dog.step(f"{cls.page_name}-返回上一层"):
            cls.back()

    @classmethod
    def table_refresh(cls):
        with dog.step(f"{cls.page_name}-动态详情页--点击刷新按钮"):
            pass

    @classmethod
    def page_one_click_forward(cls):
        with dog.step(f"{cls.page_name}-动态详情页--一键转发"):
            pass

    @classmethod
    def page_detail_drag_other(cls):
        with dog.step(f"{cls.page_name}-动态详情页--移动主素材的位置"):
            pass

    @classmethod
    def page_detail_delete_material(cls):
        with dog.step(f"{cls.page_name}-删除子素材"):
            scroll_and_find_element(max_scroll_times=2,target_rect=0.3,target_condition={'text':'谁可以看'})
            if poco("com.truedian.dragon:id/iv_delete"):
                poco("com.truedian.dragon:id/iv_delete").click()
                poco(text="删除").click()
            sleep(ui.step_wait_time)


    @classmethod
    def page_detail_forward_album(cls):
        with dog.step(f"{cls.page_name}-转发至我的主页"):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745305822894.png"), target_rect=(get_vertical_rect(-0.25)), click=True)
            sleep(ui.step_wait_time)
            detail_forward_windows=find_area_image(Template(r"tpl1745745267672.png"), target_rect=(get_vertical_rect(-0.65)))
            if detail_forward_windows:
                find_area_image(Template(r"tpl1745745283867.png"), target_rect=(get_vertical_rect(-0.5)),click=True)
            sleep(ui.step_wait_time)
            cls.wait_for_enter()


    @classmethod
    def check_detail_forward_product(cls):
        with dog.step(f"{cls.page_name}-转发后的商品详情验证"):
            assert_is_not_none(find_area_image(Template(r"tpl1745309909398.png"), target_rect=(get_vertical_rect(-0.3))))
            assert_is_not_none(find_area_image(Template(r"tpl1745309934352.png"), target_rect=(get_vertical_rect(-0.45))))


