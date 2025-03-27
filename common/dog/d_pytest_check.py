import copy
import functools
import math

import pytest
import pytest_check
from airtest.core.helper import log
from pytest_check import check

from common import dog


class DogCheck:
    __all__ = copy.copy(pytest_check.check_functions.__all__)
    __all__.extend(["assert_true", "assert_equal"])

    @staticmethod
    def check_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            return True

        return wrapper

    # --非阻塞性断言 start--
    @staticmethod
    def equal(act, expect, title=""):
        with check:
            DogCheck.assert_equal(act, expect, title)

    @staticmethod
    def not_equal(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} 期望值不等于：{expect} 实际值：{act}")
                assert act != expect, f"{title} 检查失败: {act} 等于 {expect}"

    @staticmethod
    def is_(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 是 {expect}")
                assert act is expect, f"{title} 检查失败: {act} 不是 {expect}"

    @staticmethod
    def is_not(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 不是 {expect}")
                assert act is not expect, f"{title} 检查失败: {act} 是 {expect}"

    @staticmethod
    def is_true(x, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {x} 为真")
                assert bool(x), f"{title} 检查失败: {x} 不为真"

    @staticmethod
    def is_false(x, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {x} 为假")
                assert not bool(x), f"{title} 检查失败: {x} 不为假"

    @staticmethod
    def is_none(x, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {x} 为 None")
                assert x is None, f"{title} 检查失败: {x} 不为 None"

    @staticmethod
    def is_not_none(x, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {x} 不为 None")
                assert x is not None, f"{title} 检查失败: {x} 为 None"

    @staticmethod
    def is_nan(a, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {a} 是 NaN")
                assert math.isnan(a), f"{title} 检查失败: {a} 不是 NaN"

    @staticmethod
    def is_not_nan(a, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {a} 不是 NaN")
                assert not math.isnan(a), f"{title} 检查失败: {a} 是 NaN"

    @staticmethod
    def is_in(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 在 {expect} 中")
                assert act in expect, f"{title} 检查失败: {act} 不在 {expect} 中"

    @staticmethod
    def is_not_in(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 不在 {expect} 中")
                assert act not in expect, f"{title} 检查失败: {act} 在 {expect} 中"

    @staticmethod
    def is_instance(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 是 {expect} 的实例")
                assert isinstance(act, expect), f"{title} 检查失败: {act} 不是 {expect} 的实例"

    @staticmethod
    def is_not_instance(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 不是 {expect} 的实例")
                assert not isinstance(act, expect), f"{title} 检查失败: {act} 是 {expect} 的实例"

    @staticmethod
    def almost_equal(act, expect, rel=None, abs=None, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 近似等于 {expect} (rel={rel}, abs={abs})")
                assert act == pytest.approx(expect, rel=rel,
                                            abs=abs), f"{title} 检查失败: {act} 不近似等于 {expect} (rel={rel}, abs={abs})"

    @staticmethod
    def not_almost_equal(act, expect, rel=None, abs=None, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 不近似等于 {expect} (rel={rel}, abs={abs})")
                assert act != pytest.approx(expect, rel=rel,
                                            abs=abs), f"{title} 检查失败: {act} 近似等于 {expect} (rel={rel}, abs={abs})"

    @staticmethod
    def greater(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 大于 {expect}")
                assert act > expect, f"{title} 检查失败: {act} 不大于 {expect}"

    @staticmethod
    def greater_equal(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 大于等于 {expect}")
                assert act >= expect, f"{title} 检查失败: {act} 不大于等于 {expect}"

    @staticmethod
    def less(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 小于 {expect}")
                assert act < expect, f"{title} 检查失败: {act} 不小于 {expect}"

    @staticmethod
    def less_equal(act, expect, title=""):
        with check():
            with dog.step(title):
                log(f"检查: {title} {act} 小于等于 {expect}")
                assert act <= expect, f"{title} 检查失败: {act} 不小于等于 {expect}"

    @staticmethod
    def between(b, a, c, title="", ge=False, le=False):
        with check():
            with dog.step(title):
                if ge and le:
                    log(f"检查: {title} {a} <= {b} <= {c}")
                    assert a <= b <= c, f"{title} 检查失败: {a} <= {b} <= {c} 不成立"
                elif ge:
                    log(f"检查: {title} {a} <= {b} < {c}")
                    assert a <= b < c, f"{title} 检查失败: {a} <= {b} < {c} 不成立"
                elif le:
                    log(f"检查: {title} {a} < {b} <= {c}")
                    assert a < b <= c, f"{title} 检查失败: {a} < {b} <= {c} 不成立"
                else:
                    log(f"检查: {title} {a} < {b} < {c}")
                    assert a < b < c, f"{title} 检查失败: {a} < {b} < {c} 不成立"

    @staticmethod
    def between_equal(b, a, c, title=""):
        return DogCheck.between(b, a, c, title, ge=True, le=True)

    @staticmethod
    def fail(title):
        with check():
            with dog.step(title):
                log(f"强制失败: {title}")
                assert False, title

    # --非阻塞性断言 end--

    # --以下是阻塞性断言方法--
    @staticmethod
    def assert_true(expect_true, title=""):
        with dog.step(title):
            assert expect_true, f"{title}"

    @staticmethod
    def assert_equal(act, expect, title=""):
        DogCheck.assert_true(act == expect, f"{title} 期望值：{expect} 实际值：{act}")


dog_check = DogCheck()
