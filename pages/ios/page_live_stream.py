# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_live_stream
@ time:    2025/4/23 19:05 
@ desc:
"""

from common import dog, ui
from pages.base.page_live_stream import PageLiveStream
from common.ui import poco
from common.ui import Template, find_area_image, get_vertical_rect, long_click_custom, swipe_wait_for, touch_and_wait,get_horizontal_rect
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_equal, assert_is_not_none, assert_is_none
from common.ui import DeviceType

class IOSPageLiveStream(PageLiveStream):
    page_name = "直播页面"

    @classmethod
    def page_private_domain_live(cls):
        with dog.step(f"{cls.page_name}-私域直播"):
            poco("私域直播").click()
            cls.wait_for_enter()

    @classmethod
    def page_to_live(cls):
        with dog.step(f"{cls.page_name}-去直播"):
            poco("去直播").click()
            cls.wait_for_enter()





    @classmethod
    def page_live_commodity_list(cls):
        with ((dog.step(f"{cls.page_name}-从全部商品推"))):
            all_commodity = poco("从全部商品推")
            mine_commodity = poco("从我选的推")
            if all_commodity:
                all_commodity.click()
                sleep(ui.step_wait_time)
                if ui.current_device_type == DeviceType.Android:
                    assert_is_not_none(
                        find_area_image(Template(r"tpl1745463461524.png",threshold=0.6), target_rect=(get_vertical_rect(-0.6))))

                else:
                    assert_is_not_none(find_area_image(Template(r"tpl1747043038820.png", threshold=0.6),
                                    target_rect=(get_vertical_rect(-0.6))))


        with ((dog.step(f"{cls.page_name}-从我选的推"))):
            if mine_commodity:
                mine_commodity.click()
                sleep(ui.step_wait_time)
                if ui.current_device_type == DeviceType.Android:
                    assert_is_not_none(
                        find_area_image(Template(r"tpl1745463461524.png",threshold=0.6), target_rect=(get_vertical_rect(-0.6))))
                else:
                    assert_is_not_none(find_area_image(Template(r"tpl1747043038820.png", threshold=0.6),
                                    target_rect=(get_horizontal_rect(-0.3))))

            sleep(ui.step_wait_time)
            #返回上一层
            poco("live back icon").click()

    @classmethod
    def page_live_commodity_function(cls):
        with dog.step(f"{cls.page_name}-直播设置封面/主题商品按钮"):
            poco("商品").click()

    @classmethod
    def page_live_next_step(cls):
        with dog.step(f"{cls.page_name}-下一步"):
            sleep(ui.step_wait_time)
            next_step = poco("下一步")
            if next_step:
                next_step.click()

            cls.wait_for_enter()

    @classmethod
    def page_live_start(cls):
        with dog.step(f"{cls.page_name}-开始直播"):
            poco("开始直播").click()




    @classmethod
    def page_streaming_to_live(cls):
        with dog.step(f"{cls.page_name}-走去直播流程"):
            cls.page_to_live()
            cls.page_live_commodity_function()
            cls.page_live_commodity_list()
            cls.page_live_next_step()
            cls.page_live_start()

    @classmethod
    def page_continue_live_stream(cls):
        with dog.step(f"{cls.page_name}-继续直播"):
            continue_live = poco("继续直播")
            if continue_live:
                continue_live.click()
                continue_live_windows = find_area_image(Template(r"tpl1745458663313.png"),
                                                        target_rect=(get_vertical_rect(0.6)))
                if continue_live_windows:
                    for i in range(4):
                        sleep(ui.step_wait_time)
                    find_area_image(Template(r"tpl1745458689655.png"), target_rect=(get_vertical_rect(-0.6)),
                                    click=True)



    @classmethod
    def page_continue_live_process(cls):
        with dog.step(f"{cls.page_name}-走继续直播流程"):
            cls.page_continue_live_stream()
        with dog.step(f"{cls.page_name}-直播中断,恢复直播"):
            cls.page_live_streaming_interruption()



    @classmethod
    def page_live_streaming_all(cls):
        if poco("去直播"):
            cls.page_streaming_to_live()
        if poco("继续直播"):
            cls.page_continue_live_process()

    @classmethod
    def check_page_live(cls):
        with (dog.step(f"{cls.page_name}-直播间检查")):
            sleep(ui.step_wait_time)
            assert_is_not_none(poco("点击右下角分享，邀请粉丝加入直播"))
            assert_is_not_none(
                find_area_image(Template(r"tpl1745481980853.png",threshold=0.6), target_rect=(get_vertical_rect(-0.16))))


    @classmethod
    def page_live_continue(cls):
        with (dog.step(f"{cls.page_name}-直播间出现继续直播")):

            continue_live = poco("com.truedian.dragon:id/live_pause_btn")
            if continue_live:
                continue_live.click()


    @classmethod
    def page_share_live(cls):
        with (dog.step(f"{cls.page_name}-分享直播间")):
            find_area_image(Template(r"tpl1747049259905.png"), target_rect=(0.4,0.85,0.58,1),click=True)
            sleep(ui.step_wait_time)

    @classmethod
    def page_assistant_live(cls):
        poco("进直播间").click()
        cls.wait_for_enter()