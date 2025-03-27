# -------------------------------------------------------------------------
# Project: dogdog
# Author: songjianfeng
# Date: 2025/1/24 16:29
# Description:
# -------------------------------------------------------------------------
import functools

import allure
from airtest.core.helper import log


class DogAllure:
    __all__ = allure.__all__

    def __getattr__(self, name):
        attr = getattr(allure, name)
        if callable(attr):
            @functools.wraps(attr)
            def wrapper(*args, **kwargs):
                try:
                    _args, _kwargs = self.before(name, *args, **kwargs)
                    return self.after(name, attr(*_args, **_kwargs))
                finally:
                    pass

            return wrapper
        return attr

    @staticmethod
    def before(attr_name, *args, **kwargs):
        if attr_name == 'step':
            log(f"步骤: ==> {args[0]}")
        return args, kwargs

    @staticmethod
    def after(attr_name, result):
        return result


dog_allure = DogAllure()
