from common import allure,ui
from pages.base.page import BasePage
from common.ui import find_feature_until_end, poco, find_node_until_end
from common.ui import DeviceType
from airtest.core.assertions import assert_true
import time

class BasePageNewGame(BasePage):
    """新手流程"""
    page_name = "新手流程"

    @staticmethod
    def _real_click(name):
        pass

    @classmethod
    def _base_click(cls, name):
        with allure.step(f"f{cls.page_name}-点击{name}"):
            cls._real_click(name)
            cls.wait_for_enter()

    @classmethod
    def zh_new_game(cls):
        """新手流程"""
        with allure.step(f"{cls.page_name}-点击小手"):
            find_feature_until_end(end_feature_names=["hand"], feature_names=["skip", "duihuakuang1", "duihuakuang2", "new_game"])
            cls.take_step_screenshot("点击小手")
        with allure.step(f"{cls.page_name}-点击瞄准"):
            find_feature_until_end(end_feature_names=["miaozhun"], feature_names=["skip", "hand", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击瞄准")
        with allure.step(f"{cls.page_name}-点击搜索"):
            # 国服他们应该是icon配错了，应该是search图标，现在是hand了，所以这里用hand
            find_feature_until_end(end_feature_names=["hand", "search"], feature_names=["skip", "miaozhun", "duihuakuang1", "duihuakuang2", "miaozhun2"])
            cls.take_step_screenshot("点击搜索")
        with allure.step(f"{cls.page_name}-点击日记"):
            find_feature_until_end(end_feature_names=["riji"], feature_names=["skip", "search", "hand", "duihuakuang1", "duihuakuang2", "id_card"])
            cls.take_step_screenshot("点击日记")
        with allure.step(f"{cls.page_name}-点击翻页"):
            find_feature_until_end(end_feature_names=["fanye"], feature_names=["skip", "riji", "hand", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击翻页")
        with allure.step(f"{cls.page_name}-点击任务"):
            find_feature_until_end(end_feature_names=["task"], feature_names=["skip", "fanye", "hand", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击任务")
        with allure.step(f"{cls.page_name}-点击搜索"):
            find_feature_until_end(end_feature_names=["search"], feature_names=["skip", "task", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击搜索")
        with allure.step(f"{cls.page_name}-点击工作"):
            find_feature_until_end(end_feature_names=["work"], feature_names=["skip", "search", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击工作")
        with allure.step(f"{cls.page_name}-点击布雷迪"):
            find_feature_until_end(end_feature_names=["buleidi"], feature_names=["skip", "work", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击布雷迪")
        with allure.step(f"{cls.page_name}-点击返回"):
            find_feature_until_end(end_feature_names=["return"], feature_names=["skip", "buleidi", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击返回")
        with allure.step(f"{cls.page_name}-点击挖掘"):
            find_feature_until_end(end_feature_names=["wajue_zhiyin"], feature_names=["skip", "return", "duihuakuang1", "duihuakuang2", "task"])
            cls.take_step_screenshot("点击挖掘")
        with allure.step(f"{cls.page_name}-点击石头"):
            find_feature_until_end(end_feature_names=["shitou"], feature_names=["skip", "wajue_zhiyin", "duihuakuang1", "duihuakuang2", "task"])
            cls.take_step_screenshot("点击石头")
        with allure.step(f"{cls.page_name}-点击挖掘"):
            find_feature_until_end(end_feature_names=["wajue_zhiyin"], feature_names=["skip", "shitou", "duihuakuang1", "duihuakuang2", "task_done", "goto"])
            cls.take_step_screenshot("点击挖掘")
        with allure.step(f"{cls.page_name}-点击建造"):
            find_feature_until_end(end_feature_names=["build"], feature_names=["skip", "wajue_zhiyin", "duihuakuang1", "duihuakuang2", "task_done", "goto"])
            cls.take_step_screenshot("点击建造")
        with allure.step(f"{cls.page_name}-点击基础"):
            find_feature_until_end(end_feature_names=["base"], feature_names=["skip", "build", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击基础")
        with allure.step(f"{cls.page_name}-点击客厅"):
            find_feature_until_end(end_feature_names=["living_room"], feature_names=["skip", "base", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击客厅")
        with allure.step(f"{cls.page_name}-点击建造完成"):
            find_feature_until_end(end_feature_names=["build_done"], feature_names=["skip", "living_room", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击建造完成")
        with allure.step(f"{cls.page_name}-点击建造完成"):
            find_feature_until_end(end_feature_names=["build_done2"], feature_names=["skip", "build_done", "duihuakuang1", "duihuakuang2"])
            cls.take_step_screenshot("点击建造完成")
        with allure.step(f"{cls.page_name}-点击上楼"):
            find_feature_until_end(end_feature_names=["go_upstairs"], feature_names=["skip", "build_done2", "task_done", "goto"])
            cls.take_step_screenshot("点击上楼")