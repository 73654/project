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

DEBUG_ON = True  # 调试开关

# 设备类型枚举，区分 Android 和 iOS
class DeviceType(Enum):
    Android = "android"
    IOS = "ios"

# 各平台包名映射
package_name = {DeviceType.Android: "com.more.lastfortress.gp", DeviceType.IOS: "com.sd.StoreSystem.12"}

current_device_id = None  # 当前设备ID

# 获取当前连接的设备类型（优先Android，其次iOS），并设置 current_device_id
# 若未检测到设备则抛出异常

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

# 根据设备类型获取设备ID，Android 通过 adb，iOS 通过 tidevice
# 返回设备唯一ID，未获取到则返回 None

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
    return None

# 初始化当前设备类型
current_device_type = get_device_type()
# 步骤等待时间，Android 为 1.5 秒，iOS 为 1 秒
step_wait_time = 1.5 if current_device_type == DeviceType.Android else 1

# 获取 poco 实例，Android 返回 AndroidUiautomationPoco，iOS 返回 iosPoco
# 用于后续 UI 自动化操作

def get_poco():
    if current_device_type == DeviceType.Android:
        return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False,
                                       action_interval=step_wait_time)
    elif current_device_type == DeviceType.IOS:
        connect_device(f"ios:////http+usbmux://{current_device_id}")
        return iosPoco(use_airtest_input=True, screenshot_each_action=False, action_interval=step_wait_time)
    return None

# 启动被测 App

def start_wg_app():
    start_app(package=package_name[current_device_type])
    sleep(step_wait_time)

# 停止被测 App

def stop_wg_app():
    stop_app(package=package_name[current_device_type])
    sleep(step_wait_time)

# 初始化本地临时目录，清空并重建 reports/temp 目录

def init_local():
    """一些本地化初始项目"""
    temp_path = Path(config.get_temp_dir())
    shutil.rmtree(config.get_temp_dir(), ignore_errors=True)
    temp_path.mkdir(parents=True, exist_ok=True)

# 初始化本地环境
init_local()

# 自动设置 airtest 环境
auto_setup(__file__)

# 获取 poco 实例
poco = get_poco()
# 停止被测 App，确保初始状态
stop_wg_app()

# 获取当前设备对象
device = device()
