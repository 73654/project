# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/28 14:25
# Description:
# -------------------------------------------------------------------------
import os

from airtest.aircv import aircv
from airtest.core.api import sleep, snapshot, swipe
from airtest.core.cv import Template
from airtest.core.helper import G, log
from poco.proxy import UIObjectProxy

from common.config import config
from common.ui.start import current_device_type, poco


class DogTemplate(Template):
    def __init__(self, filename, **kwargs):
        base_dir = current_device_type.value
        self.filename = os.path.join(config.get_images_dir(), base_dir, filename)
        super().__init__(self.filename, **kwargs)


def get_area(parent: UIObjectProxy = None, target_rect=None):
    """
    parent:查找控件的范围
    target_rect: 屏幕截图区域(x0,y0, x1,y1)
    """
    rect = []
    w, h = poco.get_screen_size()
    if parent:
        view_w, view_h = parent.get_size()  # 这个是相对值
        x0, y0 = parent.get_position((0, 0))  # 这个也是相对值
        x0, y0 = x0 * w, y0 * h
        x1, y1 = x0 + w * view_w, y0 + h * view_h
        rect = [x0, y0, x1, y1]
    elif target_rect:
        rect = [target_rect[0] * w, target_rect[1] * h, target_rect[2] * w, target_rect[3] * h]
    log(f"所需查找图片的范围：{rect}")
    return rect


def find_area_image(source: Template, parent: UIObjectProxy = None, target_rect=None, timeout: int = 10, click=False):
    """
    在指定控件内查找图片或者点击图片

    :param source: 需要查找的图片
    :param parent: 在所需控件范围内查找
    :param target_rect: 指定区域(x0,y0, x1,y1) 是相对坐标值
    :param timeout: 查找超时时间，间隔1s查一次
    :param click: 是否需要点击
    :return: 查找到了就返回对应的坐标值，否则返回None
    """
    interval = 1
    if timeout % interval == 0:
        cycle = timeout // interval
    else:
        cycle = timeout // interval + 1

    rect = get_area(parent, target_rect)

    for i in range(cycle):
        locality_image = aircv.crop_image(G.DEVICE.snapshot(quality=99), rect)
        r = source.match_in(locality_image)
        if r:
            log(f"区域图片里面找到图片{r} {source.filepath}")
            if click:
                poco.click(r)
            return r
        sleep(interval)
    return None


def swipe_up():
    swipe((0.5, 0.6), (0.5, 0.4))


def swipe_down():
    swipe((0.5, 0.4), (0.5, 0.6))


def swipe_left():
    swipe((0.4, 0.5), (0.6, 0.5))


def swipe_right():
    swipe((0.6, 0.5), (0.4, 0.5))
