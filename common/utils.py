import re
import subprocess
import time
from copy import deepcopy
from datetime import datetime

from dateutil.relativedelta import relativedelta

from common import dog


def deep_merge(dict1, dict2):
    """
    合并两个字典，如果key重复，则建dict2值覆盖dict1的值
    :param dict1:
    :param dict2: 该值会覆盖dict1的值
    :return: 返回一个新的字典，不会修改原字典的值
    """
    d = deepcopy(dict1)

    for key, value in dict2.items():
        if key in d and isinstance(d[key], dict) and isinstance(value, dict):
            d[key] = deep_merge(d[key], value)
        else:
            d[key] = deepcopy(value)
    return d


def execute_command(command: str):
    """
    执行命令，并获取返回值
    :param command: 命令行，比如"python -v"
    :return:
    """
    command = re.split("\\s", command)
    return subprocess.check_output(command).decode("utf-8").strip()


def now_str(_format: str = '%Y-%m-%d %H:%M:%S') -> str:
    """
    获取当前时间字符串格式
    :param _format:
    :return:
    """
    return datetime.now().strftime(_format)


def date_add_str(_format: str = '%Y-%m-%d %H:%M:%S', **kwargs) -> str:
    """
    获取当前时间的相对时间
    :param _format: 时间格式，'%Y-%m-%d'等
    :param kwargs: 相对时间，比如：加1年 years=1，减1天 days=-1 等，可以组合使用
    :return:
    """
    time1 = datetime.now() + relativedelta(**kwargs)
    return time1.strftime(_format)


def wait_for_success(timeout=15, wait=2, exception=True, errmsg=None):
    """
    有些场景是异步的，需要循环等待确认，返回None认为等待超时
    使用 @wait_for_success()
    :param timeout: 总共的等待多久退出（单位秒），默认15秒
    :param wait: 循环等待的间隔时间，每次等待多久（单位秒），默认2秒
    :param exception: 超时后，是否抛异常，默认True
    :param errmsg: 超时后，assert断言信息（exception=True时生效），未设置打印默认错误信息
    :return: 成功返回function函数的返回，校验超时（一直未成功）返回None
    """

    def wrapper(function):
        """
        校验的函数，返回False或者None认为需要循环校验，返回其他认为校验成功
        @param function:
        @return:
        """

        def on_called(*args, **kwargs):
            if timeout % wait == 0:
                cycle = timeout // wait
            else:
                cycle = timeout // wait + 1
            for i in range(cycle):
                time.sleep(wait)
                result = function(*args, **kwargs)
                if result is not None and result is not False:
                    return result
            if exception:
                dog.assert_true(False,
                                errmsg or f"{timeout}秒后，累计循环{cycle}次，[{function.__name__}]依然返回未成功。")
            return None

        return on_called

    return wrapper


if __name__ == '__main__':
    print(date_add_str(days=1))
