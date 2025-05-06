# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_batch_forword
@ time:    2025/4/16 16:53 
@ desc:
"""
from pages.base.page_batch_forward import PageBatchForward
from common import dog
from common.ui import Template, poco, find_area_image, get_vertical_rect
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.api import text
from common import ui


class AndroidPageBatchForward(PageBatchForward):
    page_name = "批量转发页面"

    @classmethod
    def page_batch_filter(cls):
        with dog.step(f"{cls.page_name}-筛选"):
            poco(text="筛选").click()

    @classmethod
    def page_batch_end_time(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--结束时间"):
            sleep(ui.step_wait_time)
            end_time = poco(text="结束时间")
            if end_time:
                end_time.click()
            else:
                find_area_image(Template(r"tpl1745832225654.png"), target_rect=(get_vertical_rect(0.4)), click=True)
            sleep(ui.step_wait_time)
            text_img = poco("android:id/button1")
            if text_img:
                text_img.click()
            else:
                find_area_image(Template(r"tpl1745896494350.png"), target_rect=(0.5, 0.6, 0.9, 0.85), click=True)

        sleep(ui.step_wait_time)


    @classmethod
    def page_filter_little_video(cls):
        with dog.step(f"{cls.page_name}-筛选弹框--小视频"):
            little_video=poco(text="小视频")
            if little_video:
                little_video.click()
            else:
                find_area_image(Template(r"tpl1745892278150.png"), target_rect=(get_vertical_rect(0.4)), click=True)


    @classmethod
    def page_batch_search(cls):
        with dog.step(f"{cls.page_name}-搜索"):
            poco("android.widget.EditText").click()
            text("商品标题价300元")
            cls.wait_for_enter()

    @classmethod
    def page_batch_enter_price(cls):
        with dog.step(f"{cls.page_name}-请填写金额(选填)"):
            poco("android.widget.EditText").click()
            sleep(ui.step_wait_time)
            for i in range(3):
                keyevent("KEYCODE_DEL")
            sleep(ui.step_wait_time)
            text("10")


    @classmethod
    def page_batch_add_tabel(cls):
        with dog.step(f"{cls.page_name}-添加标签"):
            poco(text="添加").click()

    @classmethod
    def page_batch_mine_shop(cls):
        with dog.step(f"{cls.page_name}-查看我的相册"):
            look_album=poco(text="查看我的相册")
            if look_album:
                look_album.click()
            else:
                find_area_image(Template(r"tpl1746510861352.png"), target_rect=(get_vertical_rect(-0.4)), click=True)
            cls.wait_for_enter()




    @classmethod
    def page_batch_increase_price(cls):
        with dog.step(f"{cls.page_name}-加价转"):
            poco(text="加价转").click()
            cls.wait_for_enter()


