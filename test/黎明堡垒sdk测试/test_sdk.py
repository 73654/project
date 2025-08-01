# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:53
# Description:
# -------------------------------------------------------------------------


from common import dog
from common.ui import *
from pages.base import PageLogin, PageNewGame


@dog.parent_suite("sdk测试")
@dog.suite("新手引导功能测试")
@dog.feature("新手引导")
class TestNewGame:

    @staticmethod
    def setup_method():
        start_wg_app()

    @staticmethod
    def teardown_method():
        # stop_wg_app()
        pass


    @dog.title("新手引导")
    def test_login_page(self):
        PageLogin.login()
        PageNewGame.zh_new_game()
        
