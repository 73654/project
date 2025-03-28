# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:40
# Description:
# -------------------------------------------------------------------------
import re
from enum import Enum

from airtest.core.api import auto_setup, connect_device, device, sleep, start_app, stop_app
from airtest.core.helper import log
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.ios import iosPoco

from common import utils


class DeviceType(Enum):
    Android = "android"
    IOS = "ios"


package_name = {DeviceType.Android: "com.truedian.dragon", DeviceType.IOS: "com.sd.StoreSystem.12"}

current_device_id = None


def get_device_type() -> DeviceType:
    global current_device_id
    current_device_id = get_device_id(DeviceType.Android)
    if current_device_id:
        return DeviceType.Android

    current_device_id = get_device_id(DeviceType.IOS)
    if current_device_id:
        return DeviceType.IOS

    log(f"获取设备失败，请确认已经连接设备。")
    raise RuntimeError("获取设备失败，请确认已经连接设备。")


def get_device_id(device_type: DeviceType) -> str | None:
    cmd = "adb devices" if device_type == DeviceType.Android else "tidevice info"
    match_str = r"List of devices attached\s*(\S+)" if device_type == DeviceType.Android else r"UniqueDeviceID:\s*(\S+)"
    data = utils.execute_command(cmd)
    match = re.search(match_str, data)
    if match:
        unique_device_id = match.group(1)
        log(f"获取{device_type.name}设备id： {unique_device_id}")
        return unique_device_id


current_device_type = get_device_type()


def get_poco():
    if current_device_type == DeviceType.Android:
        return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, action_interval=1.5)
    elif current_device_type == DeviceType.IOS:
        connect_device(f"ios:////http+usbmux://{current_device_id}")
        return iosPoco(use_airtest_input=True, screenshot_each_action=False, action_interval=1)


def start_wg_app():
    sleep(1)
    start_app(package=package_name[current_device_type])
    sleep(1)


def stop_wg_app():
    sleep(1)
    stop_app(package=package_name[current_device_type])
    sleep(1)


auto_setup(__file__)

poco = get_poco()
stop_wg_app()

device = device()
