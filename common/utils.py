import os.path
import re
import socket
import subprocess
import time
from functools import reduce

import numpy as np
import requests
from PIL import Image
from airtest.core.api import snapshot
from airtest.core.cv import Template
from airtest.core.helper import G, log
from pyzbar import pyzbar

from common.config import config




def get_host_ip() -> str:
    """获取本机IP地址

    Returns:
        str: 本机IP地址
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            return ip
    except Exception as e:
        log(f"获取IP地址失败: {str(e)}")
        return ''

def auto_screenshot(name=None):
    """
    装饰器：自动截图并附加到Allure报告
    :param name: 截图名称，如果不提供则使用函数名
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # 执行完函数后截图
            try:
                import allure
                screenshot_name = name or f"{func.__name__}执行后截图"
                screenshot_path = save_image(prefix=f"{func.__name__}_")
                
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=screenshot_name,
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                try:
                    import allure
                    allure.attach(f"自动截图失败: {str(e)}", "截图错误", allure.attachment_type.TEXT)
                except:
                    pass
                    
            return result
        return wrapper
    return decorator


def step_screenshot(step_name=None):
    """
    装饰器：在函数执行完成后自动截图
    :param step_name: 步骤名称，如果不提供则使用函数名
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 获取步骤名称
            if step_name:
                screenshot_name = step_name
            else:
                # 尝试从类中获取page_name
                if args and hasattr(args[0], 'page_name'):
                    screenshot_name = f"{args[0].page_name}-{func.__name__}"
                else:
                    screenshot_name = func.__name__
            
            # 执行原函数
            result = func(*args, **kwargs)
            
            # 函数执行完成后截图
            try:
                import allure
                screenshot_path = save_image(prefix=f"{screenshot_name}_")
                
                # 将截图添加到Allure报告
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=screenshot_name,
                        attachment_type=allure.attachment_type.PNG
                    )
                log(f"📸 步骤截图已添加到Allure报告: {screenshot_name}")
            except Exception as e:
                log(f"❌ 截图失败: {e}")
            
            return result
        return wrapper
    return decorator


def execute_command(command: str):
    """
    执行命令，并获取返回值
    :param command: 命令行，比如"python -v"
    :return:
    """
    command = re.split("\\s", command)
    return subprocess.check_output(command).decode("utf-8").strip()


def save_image(image: Image.Image | np.ndarray = None, prefix="") -> str:
    """
    保存图片
    :param image:需要保存的图片 不传自动截图
    :param  prefix: 保存截图的前缀
    :return: 返回保存图片的地址
    """
    path = os.path.join(config.get_temp_dir(), f"{prefix}{time.time()}.png")
    if image is None:
        snapshot(filename=path, quality=99)
    elif isinstance(image, Image.Image):
        image.save(path)
    elif isinstance(image, np.ndarray):
        Image.fromarray(image).save(path)
    log(f"文件保存在：{path}")
    return path


def image_toarray(image: Image.Image | Template | str = None, prefix=""):
    """将图片转为图片数组
        image 需要转的图片，不传自动截图
        prefix 自动截图的前缀名称.
        
    """
    if isinstance(image, Image.Image):
        return np.array(image)
    elif isinstance(image, Template):
        return np.array(Image.open(image.filepath))
    elif isinstance(image, str):
        return np.array(Image.open(image))
    else:
        return np.array(Image.open(save_image(prefix=prefix)))


def parse_qr_code():
    """
    识别当前屏幕上的二维码内容

    return: 返回二维码内容 或者 None-未识别到
    """
    filename = save_image(prefix="parse_qr_code")
    image = Image.open(filename)
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        result = obj.data.decode("utf-8")
        log(f"二维码内容: {result}")
        return result
    return None


def create_white_image(width: int, height: int, save_path: str = None) -> Image:
    """
    生成一张指定宽高的白底图片
    :param width: 图片宽度
    :param height: 图片高度
    :param save_path: 图片保存路径(可选)
    """
    white_image = Image.new("RGB", (width, height), (255, 255, 255))
    if save_path:
        white_image.save(save_path)
    return white_image


def calculate_white_percentage(image: Image, white_threshold: int = 230) -> float:
    """
    计算图片中白色像素的百分比
    :param image: PIL.Image 对象
    :param white_threshold: 白色像素的阈值（RGB 值均大于该值才认为是白色）
    :return: 白色像素的百分比（0.0 到 1.0 之间）
    """
    # 将图片转换为 RGB 模式
    image = image.convert("RGB")
    pixels = image.getdata()

    # 计算白色像素的数量
    white_pixels = sum(1 for pixel in pixels if all(channel >= white_threshold for channel in pixel))

    # 计算白色百分比
    total_pixels = image.width * image.height
    return white_pixels / total_pixels


def calculate_white_percentage_parts(image: Image, parts: int, white_threshold: int = 230) -> list[float]:
    """
    将图片分为指定等份，并计算每部分的白色百分比
    :param image: PIL.Image 对象
    :param parts: 等份数量
    :param white_threshold: 白色像素的阈值（RGB 值均大于该值才认为是白色）
    :return: 每部分的白色百分比列表（0.0 到 1.0 之间）
    """
    height = image.height
    part_height = height // parts
    percentages = []

    for i in range(parts):
        top = i * part_height
        bottom = (i + 1) * part_height if i < parts - 1 else height
        part = image.crop((0, top, image.width, bottom))
        percentages.append(calculate_white_percentage(part, white_threshold))

    return percentages


def load_toml_config(file_path: str) -> dict:
    """
    通用的toml配置文件读取方法
    
    Args:
        file_path: toml文件路径（必需参数）
        
    Returns:
        dict: 配置内容字典
        
    Examples:
        # 指定toml文件路径
        features = load_toml_config("path/to/config.toml")
    """
    import toml
    
    try:
        # 确保文件存在
        if not os.path.exists(file_path):
            log(f"❌ 配置文件不存在: {file_path}")
            return {}
        
        # 读取toml文件
        config_data = toml.load(file_path)
        return config_data
        
    except Exception as e:
        log(f"❌ 读取配置文件失败: {file_path}, 错误: {str(e)}")
        return {}


if __name__ == "__main__":
    from common.ui import DEBUG_ON

    a = save_image(prefix="test")
    # a = find_area_image(Template("common_mini_qr.png", threshold=0.6), target_rect=(0.2, 0, 1, 0.8))
    print(a)
