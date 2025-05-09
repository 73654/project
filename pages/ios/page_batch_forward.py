# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_batch_forword
@ time:    2025/4/16 16:53 
@ desc:
"""
from airtest.core.api import text
from pages.base.page_batch_forward import PageBatchForward
from common import dog,ui
from common.ui import poco,Template,find_area_image,get_vertical_rect,touch_and_wait
from airtest.core.api import home, keyevent, sleep, swipe


class IOSPageBatchForward(PageBatchForward):
    page_name = "批量转发页面"

    @classmethod
    def page_batch_filter(cls):
        with dog.step(f"{cls.page_name}-筛选"):
            poco("筛选").click()
            cls.wait_for_enter()

    @classmethod
    def page_batch_end_time(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--结束时间"):
            sleep(ui.step_wait_time)
            end_time=poco("结束时间")
            if end_time:
                end_time.click()
            else:
                find_area_image(Template(r"tpl1745832225654.png"), target_rect=(get_vertical_rect(0.4)),click=True)
            sleep(ui.step_wait_time)

            find_area_image(Template(r"tpl1746757321394.png"), target_rect=(0.65, 0.6, 0.95, 0.75),click=True)

        sleep(ui.step_wait_time)


    @classmethod
    def page_filter_little_video(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--小视频"):
            poco("小视频").click()

    @classmethod
    def page_batch_search(cls):
        with dog.step(f"{cls.page_name}-搜索"):
            find_area_image(Template(r"tpl1746758585322.png"), target_rect=(0.35,0.15,0.65,0.35), click=True)

            text("商品标题价300元")
            cls.wait_for_enter()


    @classmethod
    def page_batch_increase_price(cls):
        with dog.step(f"{cls.page_name}-加价转"):
            poco("加价转").click()


    @classmethod
    def page_batch_enter_price(cls):
        with dog.step(f"{cls.page_name}-请填写金额(选填)"):
            sleep(ui.step_wait_time)
            enter_price=find_area_image(Template(r"tpl1746770198447.png",threshold=0.65), target_rect=(0.03, 0.36, 0.5, 0.55))
            enter_price_exist = find_area_image(Template(r"tpl1746770108002.png"), target_rect=(0.03, 0.36, 0.5, 0.55))
            if enter_price:
                touch_and_wait(enter_price)
                sleep(ui.step_wait_time)
                text("10")
            if enter_price_exist:
                pass


    @classmethod
    def page_batch_mine_shop(cls):
        with dog.step(f"{cls.page_name}-查看我的相册"):
            poco("查看我的相册").click()
            cls.wait_for_enter()

    @classmethod
    def page_batch_add_tabel(cls):
        with dog.step(f"{cls.page_name}-添加标签"):
            find_area_image(Template(r"tpl1746771944629.png", threshold=0.6), target_rect=(0.7, 0.6, 1, 0.8),
                            click=True)