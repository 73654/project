# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_mobile_phone_album
@ time:    2025/4/25 13:47 
@ desc:
"""
from airtest.core.assertions import assert_is_not_none, assert_true
from airtest.core.api import text
from common import dog, ui
from common.ui import poco,find_area_image, Template, get_vertical_rect, touch_and_wait,scroll_and_find_element
from pages.base.page import BasePage
from airtest.core.api import home, keyevent, sleep, swipe


class PageMobilePhoneAlbum(BasePage):
    page_name = "手机相册"

    @classmethod
    def page_mobile_phone(cls):
        with dog.step(f"{cls.page_name}-选择图片"):
            pass

    @classmethod
    def page_mobile_img_enter(cls):
        with dog.step(f"{cls.page_name}-确认"):
            pass

    @classmethod
    def page_add_details(cls):
        with dog.step(f"{cls.page_name}-加详情"):
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745562354186.png"), target_rect=(get_vertical_rect(0.7)), click=True)
            sleep(ui.step_wait_time)

    @classmethod
    def page_select_from_mobile(cls):
        with dog.step(f"{cls.page_name}-从手机相册选择"):
            find_area_image(Template(r"tpl1745562742200.png"), target_rect=(get_vertical_rect(-0.4)), click=True)
            sleep(ui.step_wait_time)

    @classmethod
    def page_choose_img_mobile(cls):
        with dog.step(f"{cls.page_name}-从手机相册选择一个视频"):
            first_video = find_area_image(Template(r"tpl1745562871684.png",threshold=0.6), target_rect=(get_vertical_rect(0.3)))
            if first_video:
                touch_and_wait(first_video, times=2)
            sleep(ui.step_wait_time)

    @classmethod
    def page_enter_title_writing(cls):
        with dog.step(f"{cls.page_name}-输入商品标题文案"):
            first_video = find_area_image(Template(r"tpl1745563350183.png"), target_rect=(get_vertical_rect(0.25)))
            if first_video:
                touch_and_wait(first_video)
                text(
                    "安卓自动化测滨海wegoufsafsdfsdfsdfsdfsdfsadfsdfsdfsdfsadfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdffdsssdsfsdfsdfsdfsdfsdfsdfsdfsdfdfdfdfddsfdfdfsdfsdfdsfddfsfdsdsfdffdsafdsaaaaaaaaa")

    @classmethod
    def page_scroll_down(cls):
        with dog.step(f"{cls.page_name}-往下滑动"):
            cls.wait_for_enter()
            sleep(ui.step_wait_time)
            poco.scroll("vertical", 0.6)

    @classmethod
    def page_scroll_little_down(cls):
        with dog.step(f"{cls.page_name}-往下滑动"):
            cls.wait_for_enter()
            sleep(ui.step_wait_time)
            poco.scroll("vertical", 0.3)


    @classmethod
    def page_choose_one_img(cls):
        with dog.step(f"{cls.page_name}-选择一张图片"):
            first_video = find_area_image(Template(r"tpl1745565194144.png"), target_rect=(get_vertical_rect(0.25)))
            if first_video:
                touch_and_wait(first_video)


    @classmethod
    def page_commodity_properties(cls):
        with dog.step(f"{cls.page_name}-商品属性展开"):
            first_video = find_area_image(Template(r"tpl1745566403052.png",threshold=0.8), target_rect=(get_vertical_rect(-0.4)))
            if first_video:
                touch_and_wait(first_video)
                poco.scroll("vertical", 0.4)
            else:
                poco.scroll("vertical", 0.4)


    @classmethod
    def page_click_commodity_selling_price(cls):
        with dog.step(f"{cls.page_name}-商品售价"):
            sleep(ui.step_wait_time)
            # 图片识别这里还需要调整
            # touch_and_wait(find_area_image(Template(r"tpl1745574948246.png", record_pos=6), target_rect=(get_vertical_rect(-0.6))),times=2)
            # text("19.9")
            poco("com.truedian.dragon:id/price_container")[0].offspring("com.truedian.dragon:id/me_price").click()
            text("19.9")
            sleep(ui.step_wait_time)


    @classmethod
    def page_click_commodity_wholesale_price(cls):
        with dog.step(f"{cls.page_name}-商品批发价"):
            trade_price = find_area_image(Template(r"tpl1745571995172.png", record_pos=6),
                                          target_rect=(get_vertical_rect(-0.5)))
            sleep(ui.step_wait_time)

            if trade_price:
                touch_and_wait(trade_price)
                text("5")
                sleep(ui.step_wait_time)
                #图片识别未点击
                # find_area_image(Template(r"tpl1745717392440.png",record_pos=6), target_rect=(get_vertical_rect(-0.4)),click=True)
                poco("com.truedian.dragon:id/price_container")[1].offspring(
                    "com.truedian.dragon:id/tv_price_private").click()
                cls.wait_for_enter()
                find_area_image(Template(r"tpl1745718596084.png"), target_rect=(get_vertical_rect(0.6)), click=True)
                poco.scroll("vertical", 0.2)
                find_area_image(Template(r"tpl1745718749560.png"), target_rect=(get_vertical_rect(-0.5)), click=True)
                sleep(ui.step_wait_time)
                find_area_image(Template(r"tpl1745718921802.png"), target_rect=(get_vertical_rect(-0.2)), click=True)

            poco.scroll("vertical", 0.3)


    @classmethod
    def page_click_commodity_package_price(cls):
        with dog.step(f"{cls.page_name}-商品打包价"):
            # 图片未输入金额
            # find_area_image(Template(r"tpl1745719863394.png"),
            #                               target_rect=(get_vertical_rect(-0.5)),click=True)
            poco("com.truedian.dragon:id/price_container")[2].offspring("com.truedian.dragon:id/me_price").click()
            text("10")
            sleep(ui.step_wait_time)
            poco("com.truedian.dragon:id/price_container")[2].offspring("com.truedian.dragon:id/tv_price_private").click()
            cls.wait_for_enter()
            find_area_image(Template(r"tpl1745720117364.png"),
                            target_rect=(get_vertical_rect(-0.65)), click=True)

            poco.scroll("vertical", 0.2)
            find_area_image(Template(r"tpl1745718749560.png"), target_rect=(get_vertical_rect(-0.4)), click=True)
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745718921802.png"), target_rect=(get_vertical_rect(-0.2)), click=True)

    @classmethod
    def page_click_commodity_drop_shipping_price(cls):
        with dog.step(f"{cls.page_name}-商品代发价"):
            poco("com.truedian.dragon:id/price_container")[3].offspring("com.truedian.dragon:id/me_price").click()
            text("15")
            sleep(ui.step_wait_time)
            poco("com.truedian.dragon:id/price_container")[3].offspring(
                "com.truedian.dragon:id/tv_price_private").click()
            cls.wait_for_enter()
            find_area_image(Template(r"tpl1745733796477.png"), target_rect=(get_vertical_rect(0.4)), click=True)
            sleep(ui.step_wait_time)
            find_area_image(Template(r"tpl1745718921802.png"), target_rect=(get_vertical_rect(-0.2)), click=True)
            cls.wait_for_enter()

    @classmethod
    def page_commodity_release(cls):
        with dog.step(f"{cls.page_name}-发布"):
            find_area_image(Template(r"tpl1745722799252.png"), target_rect=(get_vertical_rect(-0.2)), click=True)
            cls.wait_for_enter()













