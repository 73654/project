import os
from enum import Enum
from typing import Any

import toml
from airtest.core.helper import log

# 定义环境类型的枚举类，包含日常、预发、线上三种环境
class Env(str, Enum):
    DAILY = "日常"  # 日常环境
    PRE = "预发"    # 预发布环境
    ONLINE = "线上"  # 线上环境

# 配置管理类，负责管理和读取项目的各种配置信息
class __ConfigManage(object):
    __configs = {}  # 用于缓存已读取的配置文件内容，避免重复读取
    # 获取项目根目录的绝对路径
    __project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    log(f"---------当前项目根目录为：{__project_path}-----------")

    TEST_DIR_NAME = "test"  # 测试目录名称
    FEISHU_USER = "user.toml"  # 飞书用户配置文件名
    TESTER_USERS = "wguser.toml"  # 测试用户配置文件名
    CARD_CONFIG = "card.toml"  # 卡片配置文件名

    # 飞书机器人地址
    FEISHU_BOT = "https://open.feishu.cn/open-apis/bot/v2/hook/9cc0b25a-a2eb-4629-9d47-55c426192434"

    # 运维api地址
    OPERATION_HOST = "http://api-ops.default.devops.szwego.com"

    @classmethod
    def get_project_dir(cls):
        """
        返回项目的根目录，绝对路径
        :return: 项目根目录的绝对路径
        """
        return cls.__project_path

    @classmethod
    def get_tests_dir(cls):
        """
        获取测试用例目录的绝对路径
        :return: 测试目录绝对路径
        """
        return os.path.join(cls.get_project_dir(), cls.TEST_DIR_NAME)

    @classmethod
    def get_images_dir(cls):
        """
        获取测试图片目录的绝对路径
        :return: 测试图片目录绝对路径
        """
        return os.path.join(cls.get_project_dir(), cls.TEST_DIR_NAME, 'images')

    @classmethod
    def get_temp_dir(cls):
        """
        获取临时文件目录的绝对路径（如报告临时文件）
        :return: 临时目录绝对路径
        """
        return os.path.join(cls.get_project_dir(), 'reports', "temp")

    @classmethod
    def get_config_dir(cls):
        """
        获取配置文件目录的绝对路径
        :return: 配置目录绝对路径
        """
        return os.path.join(cls.get_project_dir(), 'config')

    @classmethod
    def read_config(cls, config_name: str) -> dict[str, Any]:
        """
        读取config目录下的配置文件，传入文件名，会自动区分环境
        :param config_name: 配置文件名（如 user.toml）
        :return: 配置内容的字典
        """
        path = os.path.join(cls.get_config_dir(), config_name)
        if not os.path.exists(path):
            log(f"配置文件{path}不存在。")
            return {}
        # 如果配置未被缓存，则读取并缓存
        if config_name not in cls.__configs:
            cls.__configs[config_name] = toml.load(path)
        return cls.__configs[config_name]

# 对外暴露 config 变量，便于直接调用配置管理方法
config = __ConfigManage

if __name__ == '__main__':
    # 测试：打印项目根目录
    print(config.get_project_dir())
