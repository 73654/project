#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Project: dogdog
# Author: songjianfeng
# Date: 2025/2/7 14:37
# Description: 运行测试用例
# -------------------------------------------------------------------------
import argparse
import math
import os
import platform
import shutil
import signal

import requests
from airtest.core.helper import log
from common.ui.set_allure import SetAllureW
from common import utils
from common.config import Env, config

# 获取项目根目录
root_dir = config.get_project_dir()
# 测试结果目录
results_dir = os.path.join(root_dir, 'reports', 'results')
# 测试报告目录
reports_dir = os.path.join(root_dir, 'reports', 'reports')
# 结果历史目录
results_history = os.path.join(results_dir, 'history')
# 报告历史目录
reports_history = os.path.join(reports_dir, 'history')
# Prometheus数据文件
metric_file = os.path.join(reports_dir, 'export', 'prometheusData.txt')
# allure命令行工具路径
allure_bin = os.path.join(root_dir, 'external', 'allure-2.32.2', 'bin', 'allure')
# 环境信息文件
environment_file = os.path.join(results_dir, 'environment.properties')
# pytest配置文件
pyconfig_file = os.path.join(root_dir, config.TEST_DIR_NAME, 'pytest.ini')
# 判断是否本地运行
local_run = not platform.system() == 'Linux'
# 判断是否命令行运行
cmd_run = 'PYCHARM_HOSTED' not in os.environ


def run_test(tests: str = '', m='', k=''):
    """
    执行pytest命令，生成allure测试结果
    :param tests: 指定测试用例、模块、类等
    :param m: pytest -m参数，指定marker
    :param k: pytest -k参数，指定用例名、类名等
    """
    
    if m:
        m = f'-m "{m}"'
    if k:
        k = f'-k "{k}"'

    # 删除之前的测试结果目录，保证结果干净
    shutil.rmtree(results_dir, ignore_errors=True)

    # 执行pytest命令，生成allure原始结果
    os.system(f"pytest {tests} {m} {k} -c {pyconfig_file} -s -q --alluredir={results_dir} --clean-alluredir")


def gen_report():
    """
    生成allure测试报告，并集成历史数据
    """
    # 如果有历史报告，拷贝到新结果目录
    if os.path.exists(reports_history):
        shutil.copytree(reports_history, results_history)

    # 生成allure报告
    os.system(f"{allure_bin} generate {results_dir} -o {reports_dir} --clean")
    SetAllureW().set_windows_title(reports_dir, 'LF1 Report')  # 设置allure窗口标题
    SetAllureW().set_report_name(reports_dir, 'LF1自动化')  # 设置overview标题文案


def open_report():
    """
    打开allure测试报告，自动释放端口
    """
    # 杀掉之前占用 62010 端口的进程，避免端口冲突
    try:
        with os.popen('netstat -aon|findstr "62010"') as res:
            res = res.read().split('\n')
            pids = []
            for line in res:
                temp = [i for i in line.split(' ') if i != '']
                if len(temp) > 4:
                    pids.append(temp[4])
        for pid in pids:
            os.kill(int(pid), signal.SIGINT)
            print(f"杀死占用端口的进程成功，该进程 pid：{pid}")
    except Exception as msg:
        print(msg)

    # 启动allure报告服务
    os.system(f"{allure_bin} open {reports_dir} -p 62010")


def set_environment():
    """
    生成环境信息文件，供allure报告展示
    """
    envs = {
        "Git.Version": utils.execute_command("git rev-parse HEAD"),
        "Git.Commit.Time": utils.execute_command("git show -s --format=%ci HEAD"),
        "Python.Version": utils.execute_command("python --version").replace("Python ", ""),
    }

    # 写入环境信息到文件
    with open(environment_file, mode='w', encoding='utf-8') as f:
        for k, v in envs.items():
            f.write(f"{k}={v}\n")


def get_executor():
    """
    根据主机IP获取执行人
    """
    env_map = {
        "10.23.3.88": "芝士",
    }
    executor_ip = utils.get_host_ip()
    executor = env_map.get(utils.get_host_ip())
    if executor:
        return executor
    else:
        return executor_ip


def convert_minutes(minutes):
    """
    分钟数转为天、小时、分钟的字符串
    """
    days = minutes // 1440
    hours = minutes // 60 - (days * 24)
    minutes = minutes % 60

    time_str = ""
    if days > 0:
        time_str += f"{days}天"
    if hours > 0:
        time_str += f"{hours}小时"
    if minutes > 0:
        time_str += f"{minutes}分钟"

    return time_str if time_str else "0分钟"


def send_notification(groups=None):
    if groups:
        groups = groups.split(",")
    else:
        # groups = ["54fa5b01-f4f2-43a6-becb-ec148ca2af66"]
        groups = ["92d9800b-74e3-4abf-ae58-924458c00b26"]

    def get_metric_data():
        """
        读取prometheusData的数据
        :return:
        """
        results = {}
        if os.path.exists(metric_file):
            with open(metric_file, 'r') as file:
                for line in file:
                    launch_name, num = line.strip('\n').split(' ')
                    results[launch_name] = int(num)
        else:
            log(f"未找到测试结果报告：{metric_file}")

        _metric = dict()
        _metric["total"] = results.get("launch_retries_run", 0)
        cost = results.get("launch_time_duration", 0)
        cost = math.ceil(cost / 1000 / 60)
        _metric["time"] = convert_minutes(cost)
        _metric["pass"] = results.get("launch_status_passed", 0)
        _metric["fail"] = results.get("launch_status_failed", 0)
        _metric["error"] = results.get("launch_status_broken", 0) + results.get("launch_status_unknown", 0)
        _metric["skip"] = results.get("launch_status_skipped", 0)
        _metric["ratio"] = _metric["total"] != 0 and f"{_metric["pass"] / _metric["total"]:.0%}" or "100%"

        return _metric

    metric = get_metric_data()

    param = config.read_config(config.CARD_CONFIG).get("report")
    var = param["card"]["data"]["template_variable"]
    var["result"] = metric["ratio"] == "100%" and "<font color='green'>成功</font>" or "<font color='red'>失败</font>"

    user = config.read_config(config.FEISHU_USER)['user']
    var["user"] = user.get(get_executor(), "all")
    var.update(get_metric_data())
    # 发送通知
    for group in groups:
        a = requests.post(config.FEISHU_BOT.format(group), json=param)
        log(a.text)


def add_user_route(sandbox: str):
    """
    预发环境自动把用法id，添加到对应的沙箱环境中
    :param sandbox: 预发沙箱名，对应运维平台接口 pre_uuid字段
    :return: 错误报异常
    """
    operation_user = "songjianfeng"  # 用例执行人，运维平台用

    # 使用嵌套列表推导式获取所有用户ID
    album_user_ids = config.read_config(config.FEISHU_USER)['user'].get('ids')

    if album_user_ids:
        log(f"添加到沙箱环境[{sandbox}]的用户id={album_user_ids}")
        utils.add_user_route(operation_user, sandbox, album_user_ids)
    else:
        raise RuntimeError("未获取到预发环境执行用例的用户ID，无法添加到沙箱中")


def run(tests='', m='', k='', notice=''):
    """
    测试主流程：执行用例、生成环境、生成报告、推送通知、打开报告
    """
    run_test(tests, m, k)
    set_environment()

    gen_report()
    send_notification(notice)
    open_report()


def main(tests='', m='', k='', env='', sandbox='', notice=''):
    """
    命令行参数解析与主控入口
    """
    class Args:
        pass

    if cmd_run:
        parser = argparse.ArgumentParser()
        parser.add_argument('-env', type=str, default=Env.DAILY, help='测试环境')
        parser.add_argument('-sandbox', type=str, default='', help='沙箱环境id')
        parser.add_argument('-tests', type=str, default='', help='测试集')
        parser.add_argument('-m', type=str, default='',
                            help='同pytest -m参数，同一个组用逗号分隔，解析为or，不同组用空格分隔，解析为and。"1,2 3,4"解析为(1 or 2) and (3 or 4)')
        parser.add_argument('-k', type=str, default='', help='同pytest -k参数')
        parser.add_argument('-notice', type=str, default=None, help='飞书通知群id,多个群用逗号分隔')
        args = parser.parse_args()
    else:
        args = Args()
        args.tests = tests
        args.m = m
        args.k = k
        args.env = env if env else Env.DAILY
        args.sandbox = sandbox
        args.notice = notice

    if args.m:
        # Jenkins多个标记是通过逗号分隔传进来的，转化一下
        temp = []
        for s in args.m.strip().split(' '):
            temp.append(f"({' or '.join(s.split(','))})")
        args.m = ' and '.join(temp)

    if args.env == Env.PRE:
        add_user_route(sandbox=args.sandbox)

    log(f"请求参数为：{args.tests} {args.m} {args.k} {args.env} {args.sandbox}")
    run(args.tests, args.m, args.k, args.notice)


if __name__ == '__main__':
    # test/tests/test_微商相册A类.py::TestCompanyA::test_0006 指定跑单个用例
    # 日常环境运行
    main(tests='test/黎明堡垒sdk测试/test_登录.py', env=Env.DAILY)

    # 预发环境运行（sandbox为预发环境的沙箱id，按情况改，会自动把测试帐号加到对应的沙箱环境中去）
    # main(tests='test/tests/test_微商相册A类.py', env=Env.PRE, sandbox='preprod')
