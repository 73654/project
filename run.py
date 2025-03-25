#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Project: dogdog
# Author: songjianfeng
# Date: 2025/2/7 14:37
# Description: 运行测试用例
# -------------------------------------------------------------------------
import argparse
import os
import platform
import shutil

import requests

from common import utils
from common.config import config
from test import setting

root_dir = config.get_project_dir()
results_dir = os.path.join(root_dir, 'reports', 'results')
reports_dir = os.path.join(root_dir, 'reports', 'reports')
results_history = os.path.join(results_dir, 'history')
reports_history = os.path.join(reports_dir, 'history')
metric_file = os.path.join(reports_dir, 'prometheusData.txt')
allure_bin = os.path.join(root_dir, 'external', 'allure-2.32.2', 'bin', 'allure')
environment_file = os.path.join(results_dir, 'environment.properties')
pyconfig_file = os.path.join(root_dir, config.TEST_DIR_NAME, 'pytest.ini')
local_run = not platform.system() == 'Linux'
cmd_run = 'PYCHARM_HOSTED' not in os.environ


def run_test(tests: str = '', m='', k=''):
    """
    执行pytest命令
    :param tests: 包，模块，类等 tests/album/test_case/test.py::TestA::test_c
    :param m: 执行指定的marker用例或跳过指定marker用例 a and not b，名称和pytest.ini中定义的一致
    :param k: 指定用例名称、类名的类、marker名称， test_method and not test_class，名称不区分大小写
    :return:
    """
    if m:
        m = f'-m {m}'
    if k:
        k = f'-k {k}'

    # 删除之前的目录
    shutil.rmtree(results_dir, ignore_errors=True)

    os.system(f"pytest {tests} {m} {k} -c {pyconfig_file} -s -q --alluredir={results_dir} --clean-alluredir")


def gen_report():
    # 把历史记录拷过来集成到新的报告中去
    if os.path.exists(reports_history):
        shutil.copytree(reports_history, results_history)

    os.system(f"{allure_bin} generate {results_dir} -o {reports_dir} --clean")


def open_report():
    os.system(f"{allure_bin} open {reports_dir}")


def set_environment():
    envs = {
        "Git.Version": utils.execute_command("git rev-parse HEAD"),
        "Git.Commit.Time": utils.execute_command("git show -s --format=%ci HEAD"),
        "Python.Version": utils.execute_command("python --version").replace("Python ", ""),
    }

    with open(environment_file, mode='w', encoding='utf-8') as f:
        for k, v in envs.items():
            f.write(f"{k}={v}\n")


def send_notification():
    def get_metric_data():
        """
        这个依靠Jenkins插件去生成报告
        :return:
        """
        results = {}
        if os.path.exists(metric_file):
            with open(metric_file, 'r') as file:
                for line in file:
                    launch_name, num = line.strip('\n').split(' ')
                    results[launch_name] = num

        _metric = dict()
        _metric["total"] = results.get("launch_retries_retries", 0)
        _metric["time"] = results.get("launch_time_duration", 0)
        _metric["pass"] = results.get("launch_status_passed", 0)
        _metric["fail"] = results.get("launch_status_failed", 0)
        _metric["error"] = results.get("launch_status_broken", 0) + results.get("launch_status_unknown", 0)
        _metric["skip"] = results.get("launch_status_skipped", 0)
        _metric["ratio"] = _metric["total"] != 0 and f"{_metric["pass"] / _metric["total"]:.0%}" or "100%"

        return _metric

    metric = get_metric_data()
    param = setting.report
    var = param["card"]["data"]["template_variable"]
    var["result"] = metric["ratio"] == "100%" and "<font color='green'>成功</font>" or "<font color='red'>失败</font>"
    var["url"] = "https://cn.bing.com"
    var.update(get_metric_data())
    requests.post(setting.feishu_bot.format("54fa5b01-f4f2-43a6-becb-ec148ca2af66"))


def run(tests='', m='', k=''):
    run_test(tests, m, k)
    set_environment()

    # 在服务器上跑，插件会自动生成测试报告
    if local_run:
        gen_report()

    if not local_run:
        send_notification()


def main(tests='', m='', k=''):
    class Args:
        pass

    if cmd_run:
        parser = argparse.ArgumentParser()
        parser.add_argument('-tests', type=str, default='', help='测试集')
        parser.add_argument('-m', type=str, default='', help='同pytest -m参数')
        parser.add_argument('-k', type=str, default='', help='同pytest -k参数')
        args = parser.parse_args()
    else:
        args = Args()
        args.tests = tests
        args.m = m
        args.k = k

    run(args.tests, args.m, args.k)


if __name__ == '__main__':
    main(tests='test/tests')
