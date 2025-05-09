# import pytest
# import os
# import requests
# import time
# import allure
# import subprocess
# from airtest.core.api import home, keyevent, sleep, swipe
# from common import dog,ui
# from airtest.core.helper import log
# from run import results_dir,reports_dir
# allure_raw_dir=results_dir
#
# def adb_screenshot(screenshot_path):
#     screenshot_dir = os.path.dirname(screenshot_path)
#     # 确保目录存在
#     if not os.path.exists(screenshot_dir):
#         try:
#             os.makedirs(screenshot_dir)
#             print(f"成功创建目录: {screenshot_dir}")
#         except Exception as e:
#             print(f"创建目录 {screenshot_dir} 时出现错误: {e}")
#             return None
#
#     try:
#         # 使用 ADB 命令进行截图
#         adb_screenshot_cmd = f"adb shell screencap -p /sdcard/screenshot.png"
#         subprocess.run(adb_screenshot_cmd, shell=True, check=True)
#
#         # 将截图从设备复制到本地
#         adb_pull_cmd = f"adb pull /sdcard/screenshot.png {screenshot_path}"
#         subprocess.run(adb_pull_cmd, shell=True, check=True)
#
#         print(f"截图已保存到 {screenshot_path}")
#         return screenshot_path
#     except subprocess.CalledProcessError as e:
#         print(f"使用 ADB 截图时出现错误: {e}")
#         return None
#
#
# def capture_error_screenshot(error_msg):
#     allure.attach(error_msg, "错误详情", allure.attachment_type.TEXT)
#     max_retries = 3
#     retry_delay = 2  # 重试间隔时间（秒）
#     for attempt in range(max_retries):
#         for i in range(4):
#             sleep(ui.step_wait_time)
#         try:
#             timestamp = time.strftime("%Y%m%d-%H%M%S")
#             screenshot_filename = f"error_{timestamp}.png"
#             screenshot_path = os.path.join(allure_raw_dir, screenshot_filename)
#
#             actual_screenshot_path = adb_screenshot(screenshot_path)
#
#             if actual_screenshot_path:
#                 max_wait_time = 10  # 最大等待时间（秒）
#                 wait_time = 0
#                 while wait_time < max_wait_time:
#                     if os.path.exists(actual_screenshot_path) and os.path.getsize(actual_screenshot_path) > 0:
#                         try:
#                             # 读取图片的二进制数据
#                             with open(actual_screenshot_path, "rb") as image_file:
#                                 image_data = image_file.read()
#                             # 将图片的二进制数据添加到 Allure 报告中
#                             allure.attach(image_data, "错误页面截图", allure.attachment_type.PNG)
#                             return
#                         except Exception as read_error:
#                             log(f"读取截图文件时出现错误: {read_error}")
#                         break
#                     time.sleep(1)
#                     wait_time += 1
#                 else:
#                     log(f"等待 {max_wait_time} 秒后，截图文件 {actual_screenshot_path} 仍未正确保存")
#             else:
#                 if attempt < max_retries - 1:
#                     allure.attach(f"第 {attempt + 1} 次截图失败，将在 {retry_delay} 秒后重试", "截图重试信息", allure.attachment_type.TEXT)
#                     log(f"第 {attempt + 1} 次截图失败，将在 {retry_delay} 秒后重试")
#                     time.sleep(retry_delay)
#                 else:
#                     allure.attach("多次截图均失败，请检查设备连接和权限", "截图错误信息", allure.attachment_type.TEXT)
#                     log("多次截图均失败，请检查设备连接和权限")
#         except Exception as e:
#             if attempt < max_retries - 1:
#                 allure.attach(f"第 {attempt + 1} 次截图时出现异常: {str(e)}，将在 {retry_delay} 秒后重试", "截图重试信息", allure.attachment_type.TEXT)
#                 log(f"第 {attempt + 1} 次截图时出现异常: {e}，将在 {retry_delay} 秒后重试")
#                 time.sleep(retry_delay)
#             else:
#                 allure.attach(f"多次截图均出现异常: {str(e)}，请检查设备连接和权限", "截图错误信息", allure.attachment_type.TEXT)
#                 log(f"多次截图均出现异常: {e}，请检查设备连接和权限")
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         try:
#             error_msg = f"测试用例 {item.name} 失败"
#             capture_error_screenshot(error_msg)
#         except Exception as e:
#             allure.attach(f"捕获错误截图时出现错误: {str(e)}", "截图错误信息", allure.attachment_type.TEXT)