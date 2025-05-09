# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 17:28
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import home, keyevent, sleep, swipe
from airtest.core.assertions import assert_true

from common import dog, ui
from common.ui import DeviceType


class BasePage(object):
    page_name = ""

    @classmethod
    def wait_for_enter(cls, timeout=15):
        interval = ui.step_wait_time
        for i in range(ui.get_timeout_cycle(timeout)):
            if not ui.is_white_screen():
                return
            else:
                sleep(interval)
        assert_true(False, f"{cls.page_name}-等待{timeout}后，界面依然白屏")

    @classmethod
    def back(cls):
        with dog.step("返回上一页"):
            if ui.current_device_type == DeviceType.Android:
                keyevent("BACK")

            else:
                # swipe((0, 0.5), (0.8, 0.5), duration=1)
                swipe((0, 400), (680, 400), duration=2)

            sleep(ui.step_wait_time)
    @classmethod
    def home(cls):
        with dog.step("按home键返回主页面"):
            home()
