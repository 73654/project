# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:40
# Description:
# -------------------------------------------------------------------------
import re
import shutil
from enum import Enum
from pathlib import Path

from airtest.core.api import auto_setup, connect_device, device, sleep, start_app, stop_app
from airtest.core.helper import log
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.ios import iosPoco

from common import utils
from common.config import config

DEBUG_ON = True


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
    try:
        data = utils.execute_command(cmd)
    except Exception as e:
        return None
    match = re.search(match_str, data)
    if match:
        unique_device_id = match.group(1)
        log(f"获取{device_type.name}设备id： {unique_device_id}")
        return unique_device_id


current_device_type = get_device_type()
step_wait_time = 1.5 if current_device_type == DeviceType.Android else 1


def get_poco():
    if current_device_type == DeviceType.Android:
        return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False,
                                       action_interval=step_wait_time)
    elif current_device_type == DeviceType.IOS:
        connect_device(f"ios:////http+usbmux://{current_device_id}")
        return iosPoco(use_airtest_input=True, screenshot_each_action=False, action_interval=step_wait_time)


def start_wg_app():
    start_app(package=package_name[current_device_type])
    sleep(step_wait_time)


def stop_wg_app():
    stop_app(package=package_name[current_device_type])
    sleep(step_wait_time)


def init_local():
    """一些本地化初始项目"""
    temp_path = Path(config.get_temp_dir())
    shutil.rmtree(config.get_temp_dir(), ignore_errors=True)
    temp_path.mkdir(parents=True, exist_ok=True)


init_local()

auto_setup(__file__)

poco = get_poco()
stop_wg_app()

device = device()
