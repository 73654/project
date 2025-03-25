import json
import logging
import os
import time
import uuid
from datetime import datetime
from typing import Any


class RequestIdFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.request_id = self.gen_request_id()

    def filter(self, record):
        record.request_id = self.request_id or '-'
        return True

    def gen_request_id(self):
        self.request_id = uuid.uuid4().__str__().replace('-', '')
        return self.request_id

    def get_request_id(self):
        return self.request_id

    def clear_request_id(self):
        self.request_id = None


def get_logger(name):
    def init_log_file():
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        log_path = os.path.join(project_path, "logs")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        return os.path.join(log_path, f"log-{datetime.now().strftime('%Y%m%d-%H')}.txt")

    _logger = logging.getLogger(name)
    _logger.setLevel(level=logging.INFO)
    _logger.addFilter(RequestIdFilter())

    handler = logging.FileHandler(init_log_file(), encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(request_id)s] %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    _logger.addHandler(handler)
    _logger.addHandler(console)

    return _logger


logger = get_logger("log")


def get_logger_filter() -> RequestIdFilter:
    for f in logger.filters:
        if isinstance(f, RequestIdFilter):
            return f


def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    logger.exception(msg, *args, **kwargs)


def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def json_format(v: Any):
    if not v:
        return v
    if isinstance(v, dict) or isinstance(v, list):
        return json.dumps(v, ensure_ascii=False, default=json_serializer)
    return v


def request_log(function, throw_exception=True):
    """
    为http请求封装的日志装饰器
    @param function:
    @param throw_exception:  是否catch异常，默认不catch
    @return:

    """

    def on_log(*args, **kwargs):
        first_arg = ""
        if len(args) >= 2:
            first_arg = args[1]

        info(f"-->请求{first_arg} request ={json_format(kwargs)}")
        start_time = time.time()
        try:
            result = function(*args, **kwargs)
            info(f"<--返回{first_arg} response={json_format(result)}，耗时：{round((time.time() - start_time) * 1000)}ms")
            return result
        except Exception as e:
            exception(e)
            if throw_exception:
                raise e
            info(f"<--请求{first_arg} 异常！！！，耗时：{round((time.time() - start_time) * 1000)}ms")
        return None

    return on_log
