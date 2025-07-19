# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/28 14:25
# Description: UI自动化操作的核心模块，封装了图像识别、滑动、点击等基础操作
# -------------------------------------------------------------------------
import os

import cv2
from PIL import Image
from airtest.aircv import aircv
from airtest.core.android.touch_methods.base_touch import DownEvent, MotionEvent, MoveEvent, SleepEvent, UpEvent
from airtest.core.api import sleep, swipe, touch
from airtest.core.assertions import assert_true
from airtest.core.cv import Template
from airtest.core.helper import G, log
from poco.proxy import UIObjectProxy

from common import ui, utils
from common.config import config
from common.ui import current_device_type, device, poco
from common.utils import save_image


class DogTemplate(Template):
    """
    自定义图片模板类，继承自Airtest的Template
    用于管理不同平台（Android/iOS）的图片资源路径
    """
    def __init__(self, filename, **kwargs):
        # 根据当前设备类型确定图片目录
        base_dir = current_device_type.value
        # 构建完整的图片路径
        self.filename = os.path.join(config.get_images_dir(), base_dir, filename)
        # 调用父类初始化
        super().__init__(self.filename, **kwargs)


def swipe_up(start=0.5):
    """
    向上滑动操作
    :param start: 滑动起始点的X坐标比例（0-1之间），默认0.5表示屏幕中间
    """
    swipe((start, 0.6), (start, 0.4))  # 从屏幕60%位置滑动到40%位置
    sleep(ui.step_wait_time)  # 等待操作完成


def swipe_down(start=0.5):
    """
    向下滑动操作
    :param start: 滑动起始点的X坐标比例（0-1之间），默认0.5表示屏幕中间
    """
    swipe((start, 0.4), (start, 0.6))  # 从屏幕40%位置滑动到60%位置
    sleep(ui.step_wait_time)  # 等待操作完成


def swipe_right(start=0.5):
    """
    向右滑动操作
    :param start: 滑动起始点的Y坐标比例（0-1之间），默认0.5表示屏幕中间
    """
    swipe((0.4, start), (0.6, start))  # 从屏幕40%位置滑动到60%位置
    sleep(ui.step_wait_time)  # 等待操作完成


def swipe_left(start):
    """
    向左滑动操作
    :param start: 滑动起始点的Y坐标比例（0-1之间）
    """
    swipe((0.6, start), (0.4, start))  # 从屏幕60%位置滑动到40%位置
    sleep(ui.step_wait_time)  # 等待操作完成


def touch_and_wait(pos, wait: float = ui.step_wait_time, times=1, **kwargs):
    """
    点击并等待操作
    :param pos: 点击位置坐标
    :param wait: 等待时间，默认使用全局等待时间
    :param times: 点击次数，默认1次
    :param kwargs: 其他点击参数
    """
    sleep(wait * 0.5)  # 点击前等待
    touch(pos, times=times, **kwargs)  # 执行点击
    sleep(wait)  # 点击后等待


def get_vertical_rect(ration, middle=False):
    """
    获取垂直屏幕区域坐标
    :param ration: 区域比例，范围0~±1
                  正数：从上往下的比例区域
                  负数：从下往上的比例区域
    :param middle: 是否从中间展开对称比例
                  例如：ration=0.2，middle=True时，中间区域占比0.6（上下各减0.2）
    :return: 返回区域坐标元组 (x0, y0, x1, y1)，坐标值为相对值（0-1）
    """
    if middle:
        return 0, abs(ration), 1, 1 - abs(ration)  # 中间对称区域

    if ration > 0:
        return 0, 0, 1, ration  # 从上往下的区域
    else:
        return 0, 1 + ration, 1, 1  # 从下往上的区域


def get_horizontal_rect(ration, middle=False):
    """
    获取水平屏幕区域坐标
    :param ration: 区域比例，范围0~±1
                  正数：从左往右的比例区域
                  负数：从右往左的比例区域
    :param middle: 是否从中间展开对称比例
                  例如：ration=0.2，middle=True时，中间区域占比0.6（左右各减0.2）
    :return: 返回区域坐标元组 (x0, y0, x1, y1)，坐标值为相对值（0-1）
    """
    if middle:
        return abs(ration), 0, 1 - abs(ration), 1  # 中间对称区域

    if ration > 0:
        return 0, 0, ration, 1  # 从左往右的区域
    else:
        return 1 + ration, 0, 1, 1  # 从右往左的区域


def swipe_wait_for(element: UIObjectProxy | Template, direction: int = 1, start=0.5, times: int = 10,
                   target_rect: UIObjectProxy | tuple[float, float, float, float] = None, click=False) -> bool:
    """
    滑动查找指定元素
    :param element: 要查找的元素，可以是UI控件或图片模板
    :param direction: 滑动方向，1=上，2=下，3=左，4=右
    :param start: 滑动起始位置比例
    :param times: 最大滑动次数
    :param target_rect: 查找区域，可以是控件或坐标元组，None表示全屏查找
    :param click: 找到后是否点击，默认False
    :return: True表示找到，False表示未找到
    """
    for _ in range(times):
        # 检查UI控件是否存在
        if isinstance(element, UIObjectProxy):
            if element.exists():
                if click:
                    element.click()
                return True
        else:
            # 查找图片模板
            pos = find_area_image(element, target_rect=target_rect, timeout=1)
            if pos:
                if click:
                    touch_and_wait(pos)
                return True

        # 根据方向执行滑动
        if direction == 1:
            swipe_up(start)
        elif direction == 2:
            swipe_down(start)
        elif direction == 3:
            swipe_left(start)
        elif direction == 4:
            swipe_right(start)

    # 达到最大次数仍未找到
    if click:
        assert_true(False, f"滑动{direction}，未找到对应图片或控件 {element}")
    return False


def get_area(target_rect: UIObjectProxy | tuple[float, float, float, float] = None) -> tuple[
    float, float, float, float]:
    """
    获取查找区域的绝对坐标
    :param target_rect: 查找区域
                       UIObjectProxy：控件范围
                       tuple：相对坐标区域(x0,y0,x1,y1)，值范围0-1
                       None：全屏
    :return: 返回绝对坐标值(x0,y0,x1,y1)
    """
    w, h = poco.get_screen_size()  # 获取屏幕尺寸
    
    if isinstance(target_rect, UIObjectProxy):
        # 控件区域：获取控件的相对尺寸和位置，转换为绝对坐标
        view_w, view_h = target_rect.get_size()  # 这个是相对值
        x0, y0 = target_rect.get_position((0, 0))  # 这个也是相对值
        x0, y0 = x0 * w, y0 * h  # 转换为绝对坐标
        x1, y1 = x0 + w * view_w, y0 + h * view_h
        rect = (x0, y0, x1, y1)
    elif target_rect:
        # 相对坐标区域：转换为绝对坐标
        rect = (target_rect[0] * w, target_rect[1] * h, target_rect[2] * w, target_rect[3] * h)
    else:
        # 全屏区域
        rect = (0, 0, w, h)
    
    log(f"所需查找图片的范围：{rect}")
    return rect


def get_timeout_cycle(timeout, interval=None):
    """
    根据超时时间和间隔计算循环次数
    :param timeout: 超时时间（秒）
    :param interval: 每次循环的间隔时间，默认使用全局等待时间
    :return: 返回循环次数
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
    在指定区域内查找图片
    :param source: 要查找的图片模板
    :param target_rect: 查找区域，可以是控件或坐标元组，None表示全屏
    :param timeout: 查找超时时间（秒）
    :param click: 找到后是否点击
    :param target: 在指定图片中查找，None表示在当前屏幕截图中查找
    :return: 找到返回坐标元组，未找到返回None
    """
    
    rect = get_area(target_rect)  # 获取查找区域的绝对坐标

    path = ""
    locality_image = None
    cycle = 1 if target is not None else get_timeout_cycle(timeout)  # 计算循环次数
    
    for i in range(cycle):
        log(f"->第{i}次查找图片<-")
        
        # 获取查找的图片源
        if target:
            locality = utils.image_toarray(image=target.filepath)  # 从指定图片中查找
        else:
            locality = G.DEVICE.snapshot(quality=99)  # 从当前屏幕截图中查找
            
        # 裁剪到指定区域
        locality_image = aircv.crop_image(locality, rect)
        
        # 在裁剪区域中查找目标图片
        r = source.match_in(locality_image)
        if r:
            # 将相对坐标转换为绝对坐标
            r = (r[0] + rect[0], r[1] + rect[1])
            log(f"区域图片{path}里面找到图片{r} {source.filepath}")
            
            if click:
                touch_and_wait(r)  # 点击找到的位置
            return r

        sleep(ui.step_wait_time)  # 等待后继续查找

    # 未找到时的处理
    if ui.DEBUG_ON:
        path = save_image(locality_image, "find_area_image")  # 保存调试图片
    if click:
        assert_true(False, f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
    return None


def find_loop_area_image(source: Template, area_size: float, click=False, target: Template = None):
    """
    循环查找图片（分段查找）
    :param source: 要查找的图片模板
    :param area_size: 每次查找的区域大小(0~1)
                     正数：从上往下分段查找
                     负数：从下往上分段查找
    :param click: 找到后是否点击
    :param target: 在指定图片中查找，None表示在当前屏幕截图中查找
    :return: 找到返回坐标元组，未找到返回None
    """
    step = 0.1  # 每次移动的步长

    for i in range(10):  # 最多查找10次
        # 计算当前查找区域
        if area_size > 0:
            h1 = i * step  # 从上往下的起始位置
            h2 = h1 + area_size  # 从上往下的结束位置
        else:
            h2 = 1 - i * step  # 从下往上的结束位置
            h1 = h2 + area_size  # 从下往上的起始位置

        # 检查区域是否有效
        if h1 < 0 or h2 > 1:
            break

        # 在当前区域中查找
        r = find_area_image(source, target_rect=(0, h1, 1, h2), click=False, target=target, timeout=1)
        if r:
            log(f"循环查找图片：找到对应图片{r}")
            if click:
                touch_and_wait(r)
            return r
            
    # 未找到时的处理
    if click:
        assert_true(False, f"循环查找图片：未找到对应图片{source.filepath}")
    return None


def find_all_area_image(source: Template, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
                        timeout: int = 10, click=0, target: Template = None):
    """
    在指定区域内查找所有匹配的图片
    :param source: 要查找的图片模板
    :param target_rect: 查找区域，可以是控件或坐标元组，None表示全屏
    :param timeout: 查找超时时间（秒）
    :param click: 点击第几个找到的图片（从1开始），0表示不点击
    :param target: 在指定图片中查找，None表示在当前屏幕截图中查找
    :return: 找到返回坐标列表，未找到返回None
    """
    rect = get_area(target_rect)  # 获取查找区域的绝对坐标

    path = ""
    locality_image = None
    cycle = 1 if target is not None else get_timeout_cycle(timeout)  # 计算循环次数
    
    for i in range(cycle):
        log(f"->区域第{i}次查找所有图片<-")
        
        # 获取查找的图片源
        if target:
            locality = utils.image_toarray(image=target.filepath)
        else:
            locality = G.DEVICE.snapshot(quality=99)
            
        # 裁剪到指定区域
        locality_image = aircv.crop_image(locality, rect)
        
        # 查找所有匹配的图片
        r = source.match_all_in(locality_image)
        if r:
            r = [x['result'] for x in r]  # 提取坐标信息
            log(f"区域图片{path}里面找到图片{r} {source.filepath}")
            
            # 如果需要点击指定位置的图片
            if 0 < click <= len(r):
                r_click = r[click - 1]
                touch_and_wait((r_click[0] + rect[0], r_click[1] + rect[1]))
                
            # 转换为绝对坐标
            r = [(x[0] + rect[0], x[1] + rect[1]) for x in r]
            return r

        sleep(ui.step_wait_time)

    # 未找到时的处理
    if ui.DEBUG_ON:
        path = save_image(locality_image, "find_all_area_image")
    if click >= 1:
        assert_true(False, f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
    return None


def is_white_screen(image: Image.Image | Template = None, threshold=0.98) -> bool:
    """
    判断图片是否为白屏
    :param image: 要检查的图片
                 PIL.Image：PIL图片对象
                 Template：图片模板
                 None：自动截取当前屏幕
    :param threshold: 白屏判定阈值，默认0.98（98%白色像素）
    :return: True表示是白屏，False表示不是白屏
    """
    # 获取要检查的图片
    if image is None:
        image = G.DEVICE.snapshot(quality=99)  # 自动截屏
    elif isinstance(image, Template):
        image = cv2.imread(image.filepath, cv2.IMREAD_COLOR_RGB)  # 读取模板图片
        
    image = Image.fromarray(image)
    # 将图片分为10个区域，计算每个区域的白屏比例
    percentages = utils.calculate_white_percentage_parts(image, 10)

    white = 0      # 白屏区域计数
    non_white = 0  # 非白屏区域计数

    log(f"全屏白屏情况{percentages}")
    for p in percentages:
        if p >= threshold:
            white += 1
        else:
            non_white += 1

    # 判断是否为白屏：70%以上的区域是白屏就认为是白屏
    percentage = white / len(percentages) >= 0.7
    log(f"全屏白屏情况比例：{percentage}")
    
    if percentage:
        if ui.DEBUG_ON:
            save_image(image, "is_white_screen")  # 保存调试图片
        return True
    else:
        return False


def is_white_area(image: Template = None, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
                  threshold=0.98) -> bool:
    """
    判断指定区域是否为白屏
    :param image: 要检查的图片，None表示自动截屏
    :param target_rect: 检查区域，可以是控件或坐标元组，None表示全屏
    :param threshold: 白屏判定阈值，默认0.98
    :return: True表示区域是白屏，False表示不是白屏
    """
    # 获取要检查的图片
    if image is None:
        image = G.DEVICE.snapshot(quality=99)
    elif isinstance(image, Template):
        image = cv2.imread(image.filepath, cv2.IMREAD_COLOR_RGB)
        
    image = Image.fromarray(image)
    rect = get_area(target_rect)  # 获取检查区域的绝对坐标
    image = image.crop(rect)  # 裁剪到指定区域
    
    # 计算白屏比例
    percentage = utils.calculate_white_percentage(image)
    log(f"区域图片白屏占比：{percentage}")
    
    if ui.DEBUG_ON:
        save_image(image, "is_white_area")  # 保存调试图片
        
    return percentage > threshold


def scroll_and_find_element(max_scroll_times: int, target_rect: float, target_condition: dict|str|None = None, click=False):
    """
    滚动屏幕查找目标元素
    :param max_scroll_times: 最大滚动次数
    :param target_rect: 每次滚动的距离比例（0.5表示滚动屏幕高度的50%）
    :param target_condition: 目标元素的查找条件
                           dict：元素属性字典，如{'text': '按钮文本'}
                           str：元素名称
                           None：仅执行滚动，不查找元素
    :param click: 找到目标元素后是否点击，默认False
    :return: True表示找到并操作成功，False表示未找到
    """
    scroll_count = 0
    while scroll_count < max_scroll_times:
        # 执行滚动操作
        poco.scroll("vertical", target_rect)
        sleep(ui.step_wait_time)

        # 如果未指定目标条件，则仅执行滚动
        if target_condition is None:
            pass
        else:
            # 统一处理dict和str类型的查找条件
            target_element = poco(**target_condition) if isinstance(target_condition, dict) else poco(target_condition)
            if target_element.exists():
                if click:
                    target_element.click()
                return True

        scroll_count += 1

    # 如果滚动指定次数后仍未找到目标元素（或仅进行滚动操作）
    return False




def long_click_custom(target, duration=2):
    """
    自定义长按操作
    :param target: 目标元素，可以是坐标或者图片模板匹配结果
    :param duration: 长按持续时间，默认为2秒
    """
    touch(target, duration=duration)


def drag_to(from_: Template, to: Template | tuple[float, float],
            target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
            long_click_duration=1, steps=5, duration=1):
    """
    将一个图片拖拽到目标位置（仅Android支持，iOS不支持）
    :param from_: 起始拖拽的模板图片
    :param to: 拖拽的目标位置
              Template：拖拽到目标图片位置
              tuple：拖拽到指定的相对坐标位置(x, y)，坐标值范围0~1
    :param target_rect: 查找区域，可选，默认为None
                       UIObjectProxy：在指定控件范围内查找
                       tuple：指定区域的相对坐标(x0, y0, x1, y1)，坐标值范围0~1
                       None：在全屏范围内查找
    :param long_click_duration：拖动长按的时间，默认1秒
    :param steps：拖动的步数，默认5步完成
    :param duration: 拖拽动作持续时间，单位秒，默认1秒
    """
    from common.ui import DeviceType
    if current_device_type == DeviceType.IOS:
        raise RuntimeError("该方法不支持iOS使用。")

    # 查找起始位置
    from_pos = find_area_image(from_, target_rect=target_rect, timeout=1, click=False)
    
    # 确定目标位置
    if isinstance(to, Template):
        to_pos = find_area_image(to, target_rect=target_rect, timeout=1, click=False)
    else:
        to_pos = to

    # 计算每步的移动距离
    x_step = (to_pos[0] - from_pos[0]) / steps
    y_step = (to_pos[1] - from_pos[1]) / steps
    duration_step = duration / steps

    # 构建拖拽事件序列
    events: list[MotionEvent] = [DownEvent(from_pos), SleepEvent(long_click_duration)]

    # 添加中间移动事件
    for step in range(steps - 2):
        step = step + 1
        events.append(MoveEvent((from_pos[0] + x_step * step, from_pos[1] + y_step * step)))
        events.append(SleepEvent(duration_step))
        
    # 添加最终移动事件
    events.append(MoveEvent(to_pos))
    events.append(SleepEvent(0.01))
    events.append(UpEvent(0))

    # 执行拖拽操作
    device.touch_proxy.perform(events)






if __name__ == "__main__":
    """
    测试代码示例
    """
    # 白屏检测测试示例
    # for p1 in Path(config.get_temp_dir()).iterdir():
    #     print(f"{p1}: {is_white_screen(Template(p1))}")
    
    # 区域图片查找测试示例
    # find_area_image(DogTemplate(r"tpl1744091478418.png"), target_rect=(0.7, 0.2, 1, 0.4), timeout=1)
    
    # 拖拽操作测试示例
    drag_to(DogTemplate(r"tpl1745390496173.png"), DogTemplate(r"tpl1745390507116.png", target_pos=6),
            target_rect=get_vertical_rect(0.5))
