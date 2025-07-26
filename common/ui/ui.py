# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/28 14:25
# Description:
# -------------------------------------------------------------------------
import os
import time

import cv2
import numpy as np
from PIL import Image
from airtest.aircv import aircv
from airtest.core.android.touch_methods.base_touch import DownEvent, MotionEvent, MoveEvent, SleepEvent, UpEvent
from airtest.core.api import sleep, swipe, touch
from airtest.core.assertions import assert_true
from airtest.core.cv import Template
from airtest.core.helper import G, log
from poco.proxy import UIObjectProxy

from common import utils
from common.config import config
from common.ui.start import current_device_type, device, poco, step_wait_time, DEBUG_ON
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
    sleep(step_wait_time)


def swipe_down(start=0.5):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((start, 0.4), (start, 0.6))
    sleep(step_wait_time)


def swipe_right(start=0.5):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((0.4, start), (0.6, start))
    sleep(step_wait_time)


def swipe_left(start):
    """
    :param start: 滑动的位置，上下滑动X的位置，或者左右滑动Y的位置
    """
    swipe((0.6, start), (0.4, start))
    sleep(step_wait_time)


def touch_and_wait(pos, wait: float = step_wait_time, times=1, **kwargs):
    sleep(wait * 0.5)
    touch(pos, times=times, **kwargs)
    sleep(wait)

def adb_snapshot():
    return G.DEVICE.snapshot(quality=99)

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
    interval = interval or step_wait_time
    if timeout % interval == 0:
        cycle = timeout // interval
    else:
        cycle = timeout // interval + 1
    return int(cycle)

def find_gray_image(source, locality_image, thd=0.9, types=1):
    '''
    灰度找图
    :param source: Template对象，包含模板图片信息
    :param locality_image: 要搜索的图像数组（numpy array）
    :param thd: 相似度阈值
    :param types: 默认1为灰度化找图，其他为彩色找图
    :return: 匹配到的坐标 (x, y) 或 None，格式与 focus_pos 完全一致
    '''
    # 从 Template 对象获取模板图像
    template = cv2.imdecode(np.fromfile(source.filepath, dtype=np.uint8), cv2.IMREAD_COLOR)
    th, tw = template.shape[:2]
    
    # 处理图像格式
    if types == 1:
        locality_image = cv2.cvtColor(locality_image, cv2.COLOR_RGB2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # 模板匹配
    rv = cv2.matchTemplate(locality_image, template, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
    
    if maxVal < thd:
        return None
    else:
        focus_pos = (int(maxLoc[0] + tw / 2), int(maxLoc[1] + th / 2))
        return focus_pos
    

# def find_area_image(source: Template, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
#                     timeout: int = 10, click=False, target: Template = None):
#     """
#     在指定控件内查找图片或者点击图片

#     :param source: 需要查找的图片
#     :param target_rect: 在所需控件范围内查找 或 指定区域(x0,y0, x1,y1) 是相对坐标值
#     :param timeout: 查找超时时间，间隔1s查一次
#     :param click: 是否需要点击
#     :param target: 在指定的图片中找（如果是指定图片，timeout没用），None - 自动截屏
#     :return: 查找到了就返回对应的坐标值，否则返回None
#     """
#     rect = get_area(target_rect)

#     path = ""
#     locality_image = None
#     cycle = 1 if target is not None else get_timeout_cycle(timeout)
#     for i in range(cycle):
#         log(f"->第{i}次查找图片<-")
#         if target:
#             locality = utils.image_toarray(image=target.filepath)
#         else:
#             locality = adb_snapshot()
#         locality_image = aircv.crop_image(locality, rect)
#         r = source.match_in(locality_image)
#         if r:
#             r = (r[0] + rect[0], r[1] + rect[1])
#             log(f"区域图片{path}里面找到图片{r} {source.filepath}")
#             if click:
#                 touch_and_wait(r)
#             return r

#         sleep(ui.step_wait_time)

#     if ui.DEBUG_ON:
#         path = save_image(locality_image, "find_area_image")
#     if click:
#         assert_true(False, f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
#     return None


def find_area_image(source: Template, target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
                    click=False, offset=0, click_times=1, target: Template = None):
    """
    在指定控件/范围内查找图片或者点击图片

    :param source: 需要查找的图片
    :param target_rect: 在所需控件范围内查找 或 指定区域(x0,y0, x1,y1) 是相对坐标值
    :param click: 是否需要点击
    :param target: 在指定的图片中找，None - 自动截屏
    :return: 查找到了就返回对应的坐标值，否则返回None
    """
    rect = get_area(target_rect)

    path = ""
    locality_image = None
    if target:
        locality = utils.image_toarray(image=target.filepath)
    else:
        locality = adb_snapshot()
    locality_image = aircv.crop_image(locality, rect)
    r = source.match_in(locality_image)
    if r:
        r = (r[0] + rect[0], r[1] + rect[1])
        log(f"区域图片{path}里面找到图片{r} {source.filepath}")
        if click:
            log(f"点击坐标{r}")
            touch_and_wait(r,times=click_times)
        return r
    else:
        log(f"在区域：{rect}图片{path}中，未找到对应图片{source.filepath}")
        # sleep(ui.step_wait_time)
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

        sleep(step_wait_time)

    if DEBUG_ON:
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
        if DEBUG_ON:
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
    if DEBUG_ON:
        save_image(image, "is_white_area")
    return percentage > threshold


def scroll_and_find_element(max_scroll_times: int, target_rect: float, target_condition: dict|str|None = None, click=False):
    """
    滚动屏幕查找目标元素
    :param max_scroll_times: 最大滚动次数
    :param target_rect: 滚动的距离 (0.5 代表滚动屏幕高度的50%)
    :param target_condition: 目标元素的查找条件，例如 {'text': '验证商品置顶刷新'}
    :param click: 是否点击找到的目标元素，默认为 False
    """
    scroll_count = 0
    while scroll_count < max_scroll_times:
        # 执行滚动操作
        poco.scroll("vertical", target_rect)
        sleep(step_wait_time)

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
    自定义长按操作函数
    :param target: 目标元素，可以是坐标或者图片模板匹配结果
    :param duration: 长按持续时间，默认为 2 秒
    """
    touch(target, duration=duration)


def drag_to(from_: Template, to: Template | tuple[float, float],
            target_rect: UIObjectProxy | tuple[float, float, float, float] = None,
            long_click_duration=1, steps=5, duration=1):
    """
    将一个图片拖拽到目标位置（只有Android可以用，iOS不支持）

    参数:
        from_: Template类型，起始拖拽的模板图片
        to: Template或tuple类型，拖拽的目标位置
            - 如果是Template：表示拖拽到目标图片位置
            - 如果是tuple：表示拖拽到指定的相对坐标位置(x, y)，坐标值范围0~1
        target_rect: UIObjectProxy或tuple类型，可选，默认为None
            - 如果是UIObjectProxy：在指定控件范围内查找
            - 如果是tuple：指定区域的相对坐标(x0, y0, x1, y1)，坐标值范围0~1
            - 如果是None：在全屏范围内查找
        long_click_duration：拖动长按的时间，默认1秒
        steps：拖动的步数，默认5步完成
        duration: float类型，可选，拖拽动作持续时间，单位秒，默认1秒

    功能:
        在指定区域内查找起始模板图片，并将其拖拽到目标位置。
        目标位置可以是另一个模板图片或指定的坐标位置。
    """
    from common.ui import DeviceType
    if current_device_type == DeviceType.IOS:
        raise RuntimeError("该方法不支持iOS使用。")

    from_pos = find_area_image(from_, target_rect=target_rect, timeout=1, click=False)
    if isinstance(to, Template):
        to_pos = find_area_image(to, target_rect=target_rect, timeout=1, click=False)
    else:
        to_pos = to
    pass

    x_step = (to_pos[0] - from_pos[0]) / steps
    y_step = (to_pos[1] - from_pos[1]) / steps
    duration_step = duration / steps

    events: list[MotionEvent] = [DownEvent(from_pos), SleepEvent(long_click_duration)]

    for step in range(steps - 2):
        step = step + 1
        events.append(MoveEvent((from_pos[0] + x_step * step, from_pos[1] + y_step * step)))
        events.append(SleepEvent(duration_step))
    events.append(MoveEvent(to_pos))

    events.append(SleepEvent(0.01))
    events.append(UpEvent(0))

    device.touch_proxy.perform(events)


def parse_coordinate_string(coord_str):
    """解析坐标字符串 "(0.26, 0.53, 0.7, 0.7)" 为元组"""
    try:
        # 移除括号并分割
        coord_str = coord_str.strip('()')
        coords = [float(x.strip()) for x in coord_str.split(',')]
        if len(coords) != 4:
            raise ValueError(f"坐标应该有4个值，实际有{len(coords)}个")
        return tuple(coords)
    except Exception as e:
        raise ValueError(f"解析坐标字符串失败 '{coord_str}': {e}")





# def clear_feature_cache():
#     """清除特征配置缓存"""
#     global _global_feature_cache, _cache_initialized
#     _global_feature_cache.clear()
#     _cache_initialized = False
#     log("特征配置缓存已清除")


# def get_feature_cache_info():
#     """获取特征配置缓存信息"""
#     global _global_feature_cache, _cache_initialized
    
#     info = {
#         'initialized': _cache_initialized,
#         'files': list(_global_feature_cache.keys()),
#         'total_features': sum(len(features) for features in _global_feature_cache.values())
#     }
    
#     for file_name, features in _global_feature_cache.items():
#         info[f'features_in_{file_name}'] = list(features.keys())
    
#     return info


def find_feature_until_end(end_feature_names: list[str], feature_names: list[str], 
                          timeout: int = 600):
    """
    读取feature.py文件，循环查找指定特征直到找到任意一个结束特征
    :param end_feature_names: 结束特征名称列表（在feature.py中定义，找到任意一个就停止）
    :param feature_names: 循环查找的特征名称列表（在feature.py中定义）
    :param timeout: 超时时间（秒），默认600秒
    :return: True表示找到结束特征，False表示超时失败
    """
    
    # 直接导入feature.py配置
    try:
        from test.黎明堡垒sdk测试.feature import features
        log(f"📋 从feature.py加载特征配置")
    except ImportError as e:
        assert_true(False, f"无法导入特征配置: {e}")
        return False
    
    # 解析结束特征
    end_features = []
    for end_feature_name in end_feature_names:
        if end_feature_name not in features:
            assert_true(False, f"结束特征 '{end_feature_name}' 在配置文件中不存在")
            return False
        
        coord_str, image_file = features[end_feature_name]
        target_rect = parse_coordinate_string(coord_str)
        template = DogTemplate(image_file)
        
        end_features.append({
            'name': end_feature_name,
            'description': f"结束特征-{end_feature_name}",
            'template': template,
            'target_rect': target_rect
        })
        log(f"✓ 加载结束特征: {end_feature_name}")
    
    # 解析循环特征
    cycle_features = []
    for feature_name in feature_names:
        if feature_name not in features:
            assert_true(False, f"循环特征 '{feature_name}' 在配置文件中不存在")
            return False
        
        coord_str, image_file = features[feature_name]
        target_rect = parse_coordinate_string(coord_str)
        template = DogTemplate(image_file)
        
        cycle_features.append({
            'name': feature_name,
            'description': f"循环特征-{feature_name}",
            'template': template,
            'target_rect': target_rect
        })
        log(f"✓ 加载循环特征: {feature_name}")
    
    # 开始循环查找
    start_time = time.time()
    
    log(f"开始循环查找特征，结束特征: {[f['description'] for f in end_features]}")
    log(f"循环特征列表: {[f['description'] for f in cycle_features]}")
    
    cycle_index = 0
    while True:
        cycle_index += 1
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # 检查是否超时
        if elapsed_time >= timeout:
            log(f"查找超时: {elapsed_time:.1f}秒")
            break
            
        log(f"->第{cycle_index}次大循环，已用时: {elapsed_time:.1f}秒<-")
        
        # 首先检查所有结束特征
        for end_feature in end_features:
            if find_area_image(end_feature['template'], target_rect=end_feature['target_rect'], click=False):
                log(f"找到结束特征: {end_feature['description']}")
                return True
        
        # 遍历所有循环特征，找到第一个存在的特征就点击
        found_any_feature = False
        for j, current_feature in enumerate(cycle_features):
            log(f"  查找特征 {j+1}/{len(cycle_features)}: {current_feature['description']}")
            
            # 查找当前特征
            if find_area_image(current_feature['template'], 
                              target_rect=current_feature['target_rect'], 
                              click=True):
                log(f"  ✓ 已点击特征: {current_feature['description']}")
                found_any_feature = True
                break  # 找到一个特征后就跳出内循环
            else:
                log(f"  ✗ 未找到特征: {current_feature['description']}")
        
        if not found_any_feature:
            log(f"  本轮未找到任何循环特征，等待后继续")
            sleep(step_wait_time)
        else:
            # 找到并点击了特征，稍作等待再继续下一轮大循环
            sleep(step_wait_time)
    
    # 超时失败，保存截图并断言失败
    log(f"查找特征超时失败，总用时: {time.time() - start_time:.1f}秒")
    
    if DEBUG_ON:
        # 保存失败时的截图
        locality = adb_snapshot()
        path = save_image(locality, f"find_feature_timeout_{end_feature_names[0]}")
        log(f"超时失败截图已保存: {path}")
    
    assert_true(False, f"在{timeout}秒内未找到任何结束特征{[f['description'] for f in end_features]}，查找的循环特征: {[f['description'] for f in cycle_features]}")
    return False







if __name__ == "__main__":
    # for p1 in Path(config.get_temp_dir()).iterdir():
    #     print(f"{p1}: {is_white_screen(Template(p1))}")
    # find_area_image(DogTemplate(r"tpl1744091478418.png"), target_rect=(0.7, 0.2, 1, 0.4), timeout=1)
    # drag_to(DogTemplate(r"tpl1745390496173.png"), DogTemplate(r"tpl1745390507116.png", target_pos=6),
    #         target_rect=get_vertical_rect(0.5))
    pass
