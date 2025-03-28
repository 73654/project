# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/27 17:50
# Description:
# -------------------------------------------------------------------------
import os
from pathlib import Path

import cv2
from skimage.metrics import structural_similarity as ssim


def rename_images_and_update_code(file_path, image_dir):
    class_name = None
    method_name = None
    count = 0
    new_lines = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        # 提取类名
        if class_name is None and line.strip().startswith("class "):
            class_name = line.split()[1].split("(")[0]
            new_lines.append(line)
            continue

        # 匹配方法定义
        if line.strip().startswith("def "):
            method_name = line.split()[1].split("(")[0]
            count = 0
            new_lines.append(line)
            continue

        # 查找下一行中的 Template 参数
        if line.strip().startswith("touch(Template"):
            count += 1
            # 提取旧文件名
            old_path = line.split('"')[1]
            old_name = os.path.splitext(os.path.basename(old_path))[0]

            # 生成新文件名
            new_name = f"{class_name}_{method_name}_{count}"
            new_path = old_path.replace(old_name, new_name)

            # 重命名图片文件
            old_file = image_dir / f"{old_name}.png"
            new_file = image_dir / f"{new_name}.png"
            if old_file.exists():
                # 更新代码中的路径
                line = line.replace(old_path, new_path)
                print(f"Method Renamed: {line}")
                old_file.rename(new_file)
                print(f"PNG Renamed: {old_file} -> {new_file}")
            else:
                print(f"File Not Exist: {line}")

        new_lines.append(line)

    # 将更新后的内容写回文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def calculate_similarity(image1, image2):
    """计算两张图片的结构相似度 (SSIM)"""
    img1 = cv2.imread(str(image1), cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(str(image2), cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (100, 100))  # 统一尺寸
    img2 = cv2.resize(img2, (100, 100))
    return ssim(img1, img2)


def find_similar_images(ios_dir, android_dir):
    """查找 ios 目录下相似的图片，并重命名 android 目录下的对应图片"""
    for android_image in android_dir.glob("tpl*.png"):
        for ios_image in ios_dir.glob("*.png"):
            similarity = calculate_similarity(ios_image, android_image)
            if similarity > 0.9:  # 相似度阈值
                new_name = ios_image.name
                new_path = android_dir / new_name
                android_image.rename(new_path)
                print(f"Renamed: {android_image} -> {new_path}")
                continue


if __name__ == "__main__":
    # 定义 images 文件夹路径
    IMAGES_DIR = Path("d:/code/python/dogdog-ui/test/images")
    _android_dir = IMAGES_DIR / "android"
    _ios_dir = IMAGES_DIR / "ios"
    _file_path = "d:/code/python/dogdog-ui/pages/base/page_shop.py"
    # rename_images_and_update_code(_file_path, _ios_dir)
    find_similar_images(_ios_dir, _android_dir)
