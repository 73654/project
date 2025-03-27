import re
import subprocess
from datetime import datetime

from dateutil.relativedelta import relativedelta


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


if __name__ == '__main__':
    print(date_add_str(days=1))
