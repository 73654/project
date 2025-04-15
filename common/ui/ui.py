# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/28 14:25
# Description:
# -------------------------------------------------------------------------
import os

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


def swipe_up(start=0.5):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((start, 0.6), (start, 0.4))
    sleep(ui.step_wait_time)


def swipe_down(start=0.5):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((start, 0.4), (start, 0.6))
    sleep(ui.step_wait_time)


def swipe_right(start=0.5):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((0.4, start), (0.6, start))
    sleep(ui.step_wait_time)


def swipe_left(start):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((0.6, start), (0.4, start))
    sleep(ui.step_wait_time)



def touch_and_wait(pos, wait: float = ui.step_wait_time, times=1, **kwargs):
    sleep(wait * 0.5)
    touch(pos, times=times, **kwargs)
    sleep(wait)


def get_vertical_rect(ration, middle=False):
    """
    获取垂直屏幕区域
    :param ration: 范围 0 ~ +-1，正数从上往下的比例区域，负数从下往上的比例区域
    :param middle: 从中间展开对称的比例, 比如ration=0.2，那就是中间区域占比0.6（上下各减0.2）
    :return:
    """
    if middle:
        return 0, abs(ration), 1, 1 - abs(ration)

    if ration > 0:
        return 0, 0, 1, ration
    else:
        return 0, 1 + ration, 1, 1


def get_horizontal_rect(ration, middle=False):
    """
    获取水平屏幕区域
    :param ration: 范围 0 ~ +-1，正数从左往右的比例区域，负数从右往左的比例区域
    :param middle: 从中间展开对称的比例, 比如ration=0.2，那就是中间区域占比0.6（左右各减0.2）
    :return:
    """
    if middle:
        return abs(ration), 0, 1 - abs(ration), 1

    if ration > 0:
        return 0, 0, ration, 1
    else:
        return 1 + ration, 0, 1, 1


def swipe_wait_for(element: UIObjectProxy | Template, direction: int = 1, start=0.5, times: int = 10,
                   target_rect: UIObjectProxy | tuple[float, float, float, float] = None, click=False) -> bool:
    """
    滑动找到对应的控件
    :param element: 需要查找的控件
    :param direction: 滑动的方向，1上，2下，3左，4右
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    :param times: 最多滑动几次
    :param target_rect: 在所需控件范围内查找 或 指定区域(x0,y0, x1,y1) 是相对坐标值，None - 截屏查找
    :param click: 找到后是否点击，默认：False
    :return: True 或者 False - 滑动times次数后未找到
    """
    for _ in range(times):
        if isinstance(element, UIObjectProxy):
            if element.exists():
                if click:
                    element.click()
                return True
        else:
            pos = find_area_image(element, target_rect=target_rect, timeout=1)
            if pos:
                if click:
                    touch_and_wait(pos)
                return True

        if direction == 1:
            swipe_up(start)
        elif direction == 2:
            swipe_down(start)
        elif direction == 3:
            swipe_left(start)
        elif direction == 4:
            swipe_right(start)

    if click:
        assert_true(False, f"滑动{direction}，未找到对应图片或控件 {element}")
    return False


def get_area(target_rect: UIObjectProxy | tuple[float, float, float, float] = None) -> tuple[
    float, float, float, float]:
    """
    parent:查找控件的范围
    target_rect: 屏幕截图区域(x0,y0, x1,y1) 这个是相对坐标在0~1之间
    return: 返回绝对坐标值[x0,y0, x1,y1]
    """

    w, h = poco.get_screen_size()
    if isinstance(target_rect, UIObjectProxy):
        view_w, view_h = target_rect.get_size()  # 这个是相对值
        x0, y0 = target_rect.get_position((0, 0))  # 这个也是相对值
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


def find_area_image(source: Template, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
                    timeout: int = 10, click=False, target: Template = None):
    """
    在指定控件内查找图片或者点击图片

    :param source: 需要查找的图片
    :param target_rect: 在所需控件范围内查找 或 指定区域(x0,y0, x1,y1) 是相对坐标值
    :param timeout: 查找超时时间，间隔1s查一次
    :param click: 是否需要点击
    :param target: 在指定的图片中找（如果是指定图片，timeout没用），None - 自动截屏
    :return: 查找到了就返回对应的坐标值，否则返回None
    """
    rect = get_area(target_rect)

    path = ""
    locality_image = None
    cycle = 1 if target is not None else get_timeout_cycle(timeout)
    for i in range(cycle):
        log(f"->第{i}次查找图片<-")
        if target:
            locality = utils.image_toarray(image=target.filepath)
        else:
            locality = G.DEVICE.snapshot(quality=99)
        locality_image = aircv.crop_image(locality, rect)
        r = source.match_in(locality_image)
        if r:
            r = (r[0] + rect[0], r[1] + rect[1])
            log(f"区域图片{path}里面找到图片{r} {source.filepath}")
            if click:
                touch_and_wait(r)
            return r

        sleep(ui.step_wait_time)

    if ui.DEBUG_ON:
        path = save_image(locality_image, "find_area_image")
    if click:
        assert_true(False, f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
    return None


def find_loop_area_image(source: Template, area_size: float, click=False, target: Template = None):
    """
    在指定控件内查找图片或者点击图片

    :param source: 需要查找的图片
    :param area_size: 查找区域大小(0~1)，大于0从上往下查找，小于0从下往上查找，比如：0.2，查找区域为(0,0,1,0.2),(0,0.1,1,0.3)...，步长默认0.1
    :param click: 是否需要点击
    :param target: 在指定的图片中找（如果是指定图片，timeout没用），None - 自动截屏
    :return: 查找到了就返回对应的坐标值，否则返回None
    """
    step = 0.1

    for i in range(10):
        if area_size > 0:
            h1 = i * step
            h2 = h1 + area_size
        else:
            h2 = 1 - i * step
            h1 = h2 + area_size

        if h1 < 0 or h2 > 1:
            break

        r = find_area_image(source, target_rect=(0, h1, 1, h2), click=False, target=target, timeout=1)
        if r:
            log(f"循环查找图片：找到对应图片{r}")
            if click:
                touch_and_wait(r)
            return r
    if click:
        assert_true(False, f"循环查找图片：未找到对应图片{source.filepath}")
    return None


def find_all_area_image(source: Template, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
                        timeout: int = 10, click=0, target: Template = None):
    """
    在指定控件内查找所有图片或者点击图片

    :param source: 需要查找的图片
    :param target_rect: 在所需控件范围内查找 或 指定区域(x0,y0, x1,y1) 是相对坐标值
    :param timeout: 查找超时时间，间隔1s查一次
    :param click: 是否需要点击，点击第几个图片(顺序从1开始）
    :param target: 在指定的图片中找（如果是指定图片，timeout没用），None - 自动截屏
    :return: 查找到了就返回对应的坐标值，否则返回None
    """
    rect = get_area(target_rect)

    path = ""
    locality_image = None
    cycle = 1 if target is not None else get_timeout_cycle(timeout)
    for i in range(cycle):
        log(f"->区域第{i}次查找所有图片<-")
        if target:
            locality = utils.image_toarray(image=target.filepath)
        else:
            locality = G.DEVICE.snapshot(quality=99)
        locality_image = aircv.crop_image(locality, rect)
        r = source.match_all_in(locality_image)
        if r:
            r = [x['result'] for x in r]
            log(f"区域图片{path}里面找到图片{r} {source.filepath}")
            if 0 < click <= len(r):
                r = r[click - 1]
                touch_and_wait((r[0] + rect[0], r[1] + rect[1]))
            r = [(x[0] + rect[0], x[1] + rect[1]) for x in r]
            return r

        sleep(ui.step_wait_time)

    if ui.DEBUG_ON:
        path = save_image(locality_image, "find_all_area_image")
    if click >= 1:
        assert_true(False, f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
    return None


def is_white_screen(image: Image.Image | Template = None, threshold=0.98) -> bool:
    """
    判断图片是否为白屏
    :param image: PIL.Image | Template | None-自动截屏
    :param threshold: 白屏占比认定为是白屏
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

    log(f"全屏白屏情况{percentages}")
    for p in percentages:
        if p >= threshold:
            white += 1
        else:
            non_white += 1

    # 上面一节不是白色，下面全是白色，按百分比认为是白屏
    percentage = white / len(percentages) >= 0.7
    log(f"全屏白屏情况比例：{percentage}")
    if percentage:
        if ui.DEBUG_ON:
            save_image(image, "is_white_screen")
        return True
    else:
        return False


def is_white_area(image: Template = None, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
                  threshold=0.98) -> bool:
    """
    判断图片是否为白屏
    :param image: Template | None-自动截屏
    :param target_rect:  控件范围是否白屏 或者 屏幕截图区域(x0,y0, x1,y1) 这个是相对坐标在0~1之间
    :param threshold: 白屏占比认定为是白屏
    :return: 是否为白屏
    """
    if image is None:
        image = G.DEVICE.snapshot(quality=99)
    elif isinstance(image, Template):
        image = cv2.imread(image.filepath, cv2.IMREAD_COLOR_RGB)
    image = Image.fromarray(image)
    rect = get_area(target_rect)
    image = image.crop(rect)
    percentage = utils.calculate_white_percentage(image)
    log(f"区域图片白屏占比：{percentage}")
    if ui.DEBUG_ON:
        save_image(image, "is_white_area")
    return percentage > threshold



def scroll_and_find_element(max_scroll_times: int, target_condition: dict, click=False):
    """
    滚动屏幕查找目标元素
    :param max_scroll_times: 最大滚动次数
    :param target_condition: 目标元素的查找条件，例如 {'text': '验证商品置顶刷新'}
    :param click: 是否点击找到的目标元素，默认为 False
    """
    scroll_count = 0
    while scroll_count < max_scroll_times:
        # 查找目标元素
        poco.scroll("vertical", 0.5)
        sleep(ui.step_wait_time)
        target_element = poco(**target_condition)
        if target_element.exists():
            if click:
                # 若目标元素存在且 click 为 True，点击该元素
                target_element.click()
                assert not target_element.exists(), "点击目标元素后，元素仍存在"
            else:
                assert target_element.exists(), "找到目标元素，但检查时元素不存在"
            break
        else:
            # 若目标元素不存在，继续向下滚动
            poco.scroll("vertical", 0.2)
            scroll_count += 1

    # 如果滚动指定次数后仍未找到目标元素
    if scroll_count == max_scroll_times:
        assert not poco(**target_condition).exists(), "滚动指定次数后，找到了目标元素"














if __name__ == "__main__":
    # for p1 in Path(config.get_temp_dir()).iterdir():
    #     print(f"{p1}: {is_white_screen(Template(p1))}")
    find_area_image(DogTemplate(r"tpl1744091478418.png"), target_rect=(0.7, 0.2, 1, 0.4),timeout=1)
