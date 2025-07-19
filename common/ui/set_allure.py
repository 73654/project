import json
import os


class SetAllureW:

    # 设置报告窗口的标题
    def set_windows_title(self, allure_html_path, new_title):
        """
        通过修改allure-html目录下的index.html文件，设置打开的 Allure 报告的浏览器窗口标题文案
        @param allure_html_path: allure生成的html测试报告根目录
        @param new_title:  需要更改的标题文案 【 原文案为：Allure Report 】
        @return:
        """
        report_title_filepath = os.path.join(allure_html_path, "index.html")
        # 定义为只读模型，并定义名称为: f
        with open(report_title_filepath, 'r+', encoding="utf-8") as f:
            # 读取当前文件的所有内容
            all_the_lines = f.readlines()
            f.seek(0)
            f.truncate()
            # 循环遍历每一行的内容，将 "Allure Report" 全部替换为 → new_title(新文案)
            for line in all_the_lines:
                f.write(line.replace("Allure Report", new_title))
            # 关闭文件
            f.close()

    # 修改Allure报告Overview的标题文案
    def set_report_name(self, allure_html_path, new_name):
        """
        通过修改allure-html目录下的widgets/summary.json, 修改Allure报告Overview的标题文案
        @param allure_html_path: allure生成的html测试报告根目录
        @param new_name:  需要更改的标题文案 【 原文案为：ALLURE REPORT 】
        @return:
        """
        title_filepath = os.path.join(allure_html_path, "widgets", "summary.json")
        # 读取summary.json中的json数据，并改写reportName
        with open(title_filepath, 'rb') as f:
            # 加载json文件中的内容给params
            params = json.load(f)
            # 修改内容
            params['reportName'] = new_name
            # 将修改后的内容保存在dict中
            new_params = params
        # 往summary.json中，覆盖写入新的json数据
        with open(title_filepath, 'w', encoding="utf-8") as f:
            json.dump(new_params, f, ensure_ascii=False, indent=4)

    def set_report_env_on_html(self, allure_html_path, env_info: dict):
        """
         在allure-html报告中往widgets/environment.json中写入环境信息,
            格式参考如下：[{"values":["Auto Test Report"],"name":"report_title"},{"values":["autotestreport_"]]
        """
        envs = []
        for k, v in env_info.items():
            envs.append({
                "name": k,
                "values": [v]
            })
        with open(os.path.join(allure_html_path, "widgets", "environment.json"), 'w', encoding="utf-8") as f:
            json.dump(envs, f, ensure_ascii=False, indent=4)