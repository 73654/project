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
def get_package_name():
    import pytest
    try:
        config = pytest.get_config()
        custom_package = config.getoption("--package-name")
        if custom_package:
            return {DeviceType.Android: custom_package, DeviceType.IOS: custom_package}
    except (RuntimeError, AttributeError):
        pass
    
    # 使用默认包名
    return {
        DeviceType.Android: "com.lmbl.im30.cn",
        DeviceType.IOS: "com.more.lastfortress.appstore"
    }

package_name = get_package_name()

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
    if device_type == DeviceType.Android:
        cmd = "adb devices"
        try:
            data = utils.execute_command(cmd)
        except Exception as e:
            log(f"执行命令失败: {cmd}, 错误: {e}")
            return None
            
        match = re.search(r"List of devices attached\s*(\S+)", data)
        if match:
            unique_device_id = match.group(1)
            log(f"获取{device_type.name}设备id： {unique_device_id}")
            return unique_device_id
    else:  # iOS使用go-ios
        cmd = "ios list --details"
        try:
            data = utils.execute_command(cmd)
        except Exception as e:
            log(f"执行命令失败: {cmd}, 错误: {e}")
            return None
        
        # go-ios返回JSON格式，解析Udid字段
        import json
        try:
            json_data = json.loads(data)
            device_list = json_data.get("deviceList", [])
            if device_list and len(device_list) > 0:
                unique_device_id = device_list[0].get("Udid")
                if unique_device_id:
                    log(f"获取{device_type.name}设备id： {unique_device_id}")
                    return unique_device_id
        except json.JSONDecodeError as e:
            log(f"解析go-ios JSON输出失败: {e}")
            # 尝试旧的正则表达式解析作为备用
            match = re.search(r'"Udid":"([^"]+)"', data)
            if match:
                unique_device_id = match.group(1)
                log(f"获取{device_type.name}设备id（备用方法）： {unique_device_id}")
                return unique_device_id
                
    return None

# 初始化当前设备类型
current_device_type = get_device_type()
# 步骤等待时间，Android 为 1.5 秒，iOS 为 1 秒
step_wait_time = 0.5 if current_device_type == DeviceType.Android else 0.25

# 获取 poco 实例，Android 返回 AndroidUiautomationPoco，iOS 返回 iosPoco
# 用于后续 UI 自动化操作

def get_poco():
    if current_device_type == DeviceType.Android:
        return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False,
                                       action_interval=step_wait_time)
    elif current_device_type == DeviceType.IOS:
        # 使用go-ios连接，格式: ios:///http+usbmux://设备ID
        try:
            connect_device(f"ios:///http+usbmux://{current_device_id}")
            return iosPoco(use_airtest_input=True, screenshot_each_action=False, action_interval=step_wait_time)
        except Exception as e:
            log(f"iOS连接失败: {e}")
            log("请确保WebDriverAgent已通过go-ios正确启动")
            log(f"设备ID: {current_device_id}")
            raise
    return None

# 启动被测 App

def start_wg_app():
    if current_device_type == DeviceType.IOS:
        # iOS使用go-ios启动App
        import subprocess
        try:
            cmd = ['ios', 'launch', package_name[current_device_type], '--udid', current_device_id]
            subprocess.run(cmd, check=True)
            log(f"使用go-ios启动App: {package_name[current_device_type]}")
        except subprocess.CalledProcessError as e:
            log(f"go-ios启动App失败: {e}")
            # 降级到airtest方式
            start_app(package=package_name[current_device_type])
    else:
        start_app(package=package_name[current_device_type])
    sleep(step_wait_time)

# 停止被测 App

def stop_wg_app():
    if current_device_type == DeviceType.IOS:
        # iOS使用go-ios停止App
        import subprocess
        try:
            cmd = ['ios', 'kill', package_name[current_device_type], '--udid', current_device_id]
            subprocess.run(cmd, check=True)
            log(f"使用go-ios停止App: {package_name[current_device_type]}")
        except subprocess.CalledProcessError as e:
            log(f"go-ios停止App失败: {e}")
            # 降级到airtest方式
            stop_app(package=package_name[current_device_type])
    else:
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
# stop_wg_app()

# 获取当前设备对象
device = device()
