# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:40
# Description:
# -------------------------------------------------------------------------
from enum import Enum

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.ios import iosPoco


class DeviceType(Enum):
    Android = 0
    IOS = 1


package_name = {DeviceType.Android: "com.truedian.dragon", DeviceType.IOS: "com.sd.StoreSystem.12"}


def get_device_type() -> DeviceType:
    return DeviceType.Android


def get_poco():
    if get_device_type() == DeviceType.Android:
        return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    elif get_device_type() == DeviceType.IOS:
        return iosPoco(use_airtest_input=True, screenshot_each_action=False)


def start_wg_app():
    start_app(package=package_name[get_device_type()])
    sleep(2)


def stop_wg_app():
    stop_app(package=package_name[get_device_type()])
    sleep(2)


auto_setup(__file__)

poco = get_poco()
device = device()
