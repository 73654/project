# -------------------------------------------------------------------------
# Project: dogdog
# Author: songjianfeng
# Date: 2025/1/24 16:13
# Description: 封装一些写测试用例的插件进来
# 1、pytest_check
# 2、allure
# -------------------------------------------------------------------------
import sys

from common.dog.d_allure import dog_allure
from common.dog.d_cv import DogTemplate as Template
from common.dog.d_pytest_check import dog_check

for attr_name in dog_allure.__all__:
    setattr(sys.modules[__name__], attr_name, getattr(dog_allure, attr_name))

for attr_name in dog_check.__all__:
    setattr(sys.modules[__name__], attr_name, getattr(dog_check, attr_name))

__all__ = [
    # 非阻塞性断言
    "equal",
    "not_equal",
    "is_",
    "is_not",
    "is_true",
    "is_false",
    "is_none",
    "is_not_none",
    "is_nan",
    "is_not_nan",
    "is_in",
    "is_not_in",
    "is_instance",
    "is_not_instance",
    "almost_equal",
    "not_almost_equal",
    "greater",
    "greater_equal",
    "less",
    "less_equal",
    "between",
    "between_equal",
    "check_func",
    "fail",
    # 阻塞性断言
    "assert_true",
    "assert_equal",

    # allure
    'title',
    'description',
    'description_html',
    'label',
    'severity',
    'suite',
    'parent_suite',
    'sub_suite',
    'tag',
    'id',
    'epic',
    'feature',
    'story',
    'link',
    'issue',
    'testcase',
    'manual',
    'step',
    'dynamic',
    'severity_level',
    'attach',
    'attachment_type',
    'parameter_mode',

    # airtest Template
    "Template"
]
