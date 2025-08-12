
from common import allure
from common.ui import *
from pages.base import PageLogin, PageNewGame
import pytest

@allure.parent_suite("sdk测试")
@allure.suite("新手引导功能测试")
@allure.feature("新手引导")
class Test_SDK:

    @staticmethod
    def setup_method():
        start_wg_app()

    @staticmethod
    def teardown_method():
        # stop_wg_app()
        pass


    @allure.title("新手引导")
    @pytest.mark.login
    def test_login_page(self):
        # PageLogin.login()
        PageNewGame.zh_new_game()
        
