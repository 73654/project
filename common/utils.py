import os.path
import re
import subprocess
import time

from PIL import Image
from airtest.core.api import snapshot
from airtest.core.helper import log
from pyzbar import pyzbar

from common.config import config
from common.ui import *


def execute_command(command: str):
    """
    执行命令，并获取返回值
    :param command: 命令行，比如"python -v"
    :return:
    """
    command = re.split("\\s", command)
    return subprocess.check_output(command).decode("utf-8").strip()


def save_image(image, prefix):
    path = os.path.join(config.get_temp_dir(), f"{prefix}{time.time()}.png")
    if isinstance(image, Image.Image):
        image.save(path)
    else:
        Image.fromarray(image).save(path)
    log(f"文件保存在：{path}")
    return path


def parse_qr_code():
    """
    识别当前屏幕上的二维码内容

    return: 返回二维码内容 或者 None-未识别到
    """
    filename = os.path.join(config.get_temp_dir(), f"parse_qr_code{time.time()}.png")
    snapshot(filename=filename, quality=99)
    image = Image.open(filename)
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        result = obj.data.decode("utf-8")
        log(f"二维码内容: {result}")
        return result


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


if __name__ == "__main__":
    a = parse_qr_code()
    # a = find_area_image(Template("common_mini_qr.png", threshold=0.6), target_rect=(0.2, 0, 1, 0.8))
    print(a)
