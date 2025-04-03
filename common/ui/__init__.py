# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/28 14:25
# Description:
# -------------------------------------------------------------------------
from .start import DeviceType, DEBUG_ON, current_device_id, current_device_type, poco, device, start_wg_app, stop_wg_app
from .start import step_wait_time
from .ui import DogTemplate as Template
from .ui import find_area_image, swipe_up, swipe_down, swipe_right, swipe_left, is_white_area, is_white_screen, \
    get_timeout_cycle, find_all_area_image,get_vertical_rect,get_horizontal_rect

# 控制导出的对象
__all__ = [
    "DeviceType", "DEBUG_ON", "current_device_id", "current_device_type", "poco", "device", "start_wg_app",
    "stop_wg_app",
    "step_wait_time", "Template", "find_area_image", "swipe_up", "swipe_down", "swipe_right", "swipe_left",
    "is_white_area", "is_white_screen", "get_timeout_cycle", "find_all_area_image","get_vertical_rect","get_horizontal_rect"
]
