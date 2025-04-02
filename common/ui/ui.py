# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/28 14:25
# Description:
# -------------------------------------------------------------------------
import os
import time

import cv2
from PIL import Image
from airtest.aircv import aircv
from airtest.core.api import sleep, swipe, touch
from airtest.core.assertions import assert_true
from airtest.core.cv import Template
from airtest.core.helper import G, log
from poco.proxy import UIObjectProxy

from common import ui, utils
from common.config import config
from common.ui import current_device_type, poco
from common.utils import save_image


class DogTemplate(Template):
    def __init__(self, filename, **kwargs):
        base_dir = current_device_type.value
        self.filename = os.path.join(config.get_images_dir(), base_dir, filename)
        super().__init__(self.filename, **kwargs)


def swipe_up():
    swipe((0.5, 0.6), (0.5, 0.4))
    sleep(ui.step_wait_time)


def swipe_down():
    swipe((0.5, 0.4), (0.5, 0.6))
    sleep(ui.step_wait_time)


def swipe_left():
    swipe((0.4, 0.5), (0.6, 0.5))
    sleep(ui.step_wait_time)


def swipe_right():
    swipe((0.6, 0.5), (0.4, 0.5))
    sleep(ui.step_wait_time)


def swipe_wait_for(element: UIObjectProxy, direction: int = 1, times: int = 5, click=False) -> bool:
    """
    滑动找到对应的控件
    :param element: 需要查找的控件
    :param direction: 发动的方向，1上，2下，3左，4右
    :param times: 最多滑动几次
    :param click: 找到后是否点击，默认：False
    :return: True 或者 False - 滑动times次数后未找到
    """
    for _ in range(times):
        if element.exists():
            if click:
                element.click()
            return True
        if direction == 1:
            swipe_up()
        elif direction == 2:
            swipe_down()
        elif direction == 3:
            swipe_left()
        elif direction == 4:
            swipe_right()
    return False


def get_area(parent: UIObjectProxy = None, target_rect=None) -> tuple[float, float, float, float]:
    """
    parent:查找控件的范围
    target_rect: 屏幕截图区域(x0,y0, x1,y1) 这个是相对坐标在0~1之间
    return: 返回绝对坐标值[x0,y0, x1,y1]
    """
    rect = []
    w, h = poco.get_screen_size()
    if parent:
        view_w, view_h = parent.get_size()  # 这个是相对值
        x0, y0 = parent.get_position((0, 0))  # 这个也是相对值
        x0, y0 = x0 * w, y0 * h
        x1, y1 = x0 + w * view_w, y0 + h * view_h
        rect = (x0, y0, x1, y1)
    elif target_rect:
        rect = (target_rect[0] * w, target_rect[1] * h, target_rect[2] * w, target_rect[3] * h)
    else:
        rect = (0, 0, w, h)
    log(f"所需查找图片的范围：{rect}")
    return rect


def get_timeout_cycle(timeout, interval=None):
    """
    根据interval 计算循环次数

    :param timeout: 超时时间
    :param interval: sleep的时间，默认用统一的时间
    return: 返回循环次数
    """
    interval = interval or ui.step_wait_time
    if timeout % interval == 0:
        cycle = timeout // interval
    else:
        cycle = timeout // interval + 1
    return int(cycle)


def find_area_image(source: Template, parent: UIObjectProxy = None, target_rect=None, timeout: int = 5, click=False):
    """
    在指定控件内查找图片或者点击图片

    :param source: 需要查找的图片
    :param parent: 在所需控件范围内查找
    :param target_rect: 指定区域(x0,y0, x1,y1) 是相对坐标值
    :param timeout: 查找超时时间，间隔1s查一次
    :param click: 是否需要点击
    :return: 查找到了就返回对应的坐标值，否则返回None
    """
    rect = get_area(parent, target_rect)

    locality_image = None
    for i in range(get_timeout_cycle(timeout)):
        locality_image = aircv.crop_image(G.DEVICE.snapshot(quality=99), rect)
        r = source.match_in(locality_image)
        if r:
            log(f"区域图片里面找到图片{r} {source.filepath}")
            if click:
                touch((r[0] + rect[0], r[1] + rect[1]))
                sleep(ui.step_wait_time)
            return r

        sleep(ui.step_wait_time)

    path = ""
    if ui.DEBUG_ON:
        path = save_image(locality_image, "find_area_image")
    if click:
        assert_true(False, f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
    return None


def is_white_screen(image: Image.Image | Template = None) -> bool:
    """
    判断图片是否为白屏
    :param image: PIL.Image | Template | None-自动截屏
    :return: 是否为白屏
    """
    if image is None:
        image = G.DEVICE.snapshot(quality=99)
    elif isinstance(image, Template):
        image = cv2.imread(image.filepath, cv2.IMREAD_COLOR_RGB)
    image = Image.fromarray(image)
    percentages = utils.calculate_white_percentage_parts(image, 10)

    white = 0
    non_white = 0
    has_white = False

    log(f"白屏情况{percentages}")
    for p in percentages:
        if p >= 0.95:
            has_white = True
            white += 1
        else:
            # 如果开始是白的，中间出现非白色区域，认为不是白屏
            if has_white:
                log("中间区域出现非白屏区域，认定为非白屏.")
                if ui.DEBUG_ON:
                    save_image(image, "is_white_screen")
                return False
            non_white += 1

    # 上面一节不是白色，下面全是白色，按百分比认为是白屏
    if ui.DEBUG_ON:
        save_image(image, "is_white_screen")
    return white / len(percentages) > 0.7


def is_white_area(image: Template = None, view: UIObjectProxy = None, target_rect=None) -> bool:
    """
    判断图片是否为白屏
    :param image: Template | None-自动截屏
    :param view: 控件范围是否白屏
    :param target_rect: 屏幕截图区域(x0,y0, x1,y1) 这个是相对坐标在0~1之间
    :return: 是否为白屏
    """
    if image is None:
        image = G.DEVICE.screenshot(quality=99)
    elif isinstance(image, Template):
        image = cv2.imread(image.filepath, cv2.IMREAD_COLOR_RGB)
    image = Image.fromarray(image)
    rect = get_area(view, target_rect)
    image = image.crop(rect)
    percentage = utils.calculate_white_percentage(image)
    log(f"区域图片白屏占比：{percentage}")
    if ui.DEBUG_ON:
        save_image(image, "is_white_area")
    return percentage > 0.95


if __name__ == "__main__":
    # for p1 in Path(config.get_temp_dir()).iterdir():
    #     print(f"{p1}: {is_white_screen(Template(p1))}")
    print(is_white_area(Template(r"D:\code\python\dogdog-ui\reports\temp\1743510173.4788177.png"),
                        target_rect=(0, 0, 1, 0.1)))
    print(is_white_screen())
