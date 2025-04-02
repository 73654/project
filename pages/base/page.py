# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/26 17:28
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import keyevent, sleep, swipe
from airtest.core.assertions import assert_true

from common import ui
from common.ui import DeviceType


class BasePage(object):
    page_name = ""

    @classmethod
    def wait_for_enter(cls, timeout=5):
        interval = ui.step_wait_time
        for i in range(ui.get_timeout_cycle(timeout)):
            if not ui.is_white_screen():
                return
            else:
                sleep(interval)
        assert_true(False, f"{cls.page_name}-等待{timeout}后，界面依然白屏")

    @classmethod
    def back(cls):
        if ui.DeviceType == DeviceType.Android:
            keyevent("BACK")
        else:
            swipe((0, 0.5), (0.8, 0.5), duration=1)
