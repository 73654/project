from pathlib import Path

import pytest

from common import dog, log
from common.config import config


def get_model_names(item):
    """
    根据一级目录名，二级目录名，文件名返回对应的配置
    :param item:
    :return:
    """
    case_path = item.module.__file__.replace(config.get_project_dir(), '')
    case_path = Path(case_path).parts
    # /tests/album/test_case/goods/批量编辑和转发/test_批量修改.py
    model1, model2 = case_path[2], case_path[4]  # album, goods
    model3 = case_path[5] if case_path.__len__() > 6 else ""  # 批量编辑和转发
    file_name = item.fspath.purebasename.replace("test_", "")  # 批量修改
    return model1, model2, model3, file_name
