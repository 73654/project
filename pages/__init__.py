# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/24 20:13
# Description:
# -------------------------------------------------------------------------
from common.ui import DeviceType, get_device_type

if get_device_type() == DeviceType.Android:
    from pages.android import *
elif get_device_type() == DeviceType.IOS:
    from pages.ios import *

__all__ = ["PageMain"]