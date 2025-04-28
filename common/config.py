import os
from enum import Enum
from typing import Any

import toml
from airtest.core.helper import log


class Env(str, Enum):
    DAILY = "日常"
    PRE = "预发"
    ONLINE = "线上"


class __ConfigManage(object):
    __configs = {}
    __project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    log(f"---------当前项目根目录为：{__project_path}-----------")

    TEST_DIR_NAME = "test"
    FEISHU_USER = "user.toml"
    TESTER_USERS = "wguser.toml"
    CARD_CONFIG = "card.toml"

    # 飞书机器人地址
    FEISHU_BOT = "https://open.feishu.cn/open-apis/bot/v2/hook/{}"

    # 运维api地址
    OPERATION_HOST = "http://api-ops.default.devops.szwego.com"

    @classmethod
    def get_project_dir(cls):
        """
        返回项目的根目录，绝对路径
        :return:
        """
        return cls.__project_path

    @classmethod
    def get_tests_dir(cls):
        return os.path.join(cls.get_project_dir(), cls.TEST_DIR_NAME)

    @classmethod
    def get_images_dir(cls):
        return os.path.join(cls.get_project_dir(), cls.TEST_DIR_NAME, 'images')

    @classmethod
    def get_temp_dir(cls):
        return os.path.join(cls.get_project_dir(), 'reports', "temp")

    @classmethod
    def get_config_dir(cls):
        return os.path.join(cls.get_project_dir(), 'config')

    @classmethod
    def read_config(cls, config_name: str) -> dict[str, Any]:
        """
        读取config目录下的配置文件，传入文件名，会自动区分环境
        :param config_name:
        :return:
        """
        path = os.path.join(cls.get_config_dir(), config_name)
        if not os.path.exists(path):
            log(f"配置文件{path}不存在。")
            return {}
        if config_name not in cls.__configs:
            cls.__configs[config_name] = toml.load(path)
        return cls.__configs[config_name]


config = __ConfigManage

if __name__ == '__main__':
    print(config.get_project_dir())
