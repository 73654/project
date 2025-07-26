# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:53
# Description:
# -------------------------------------------------------------------------


from common import dog
from common.ui import *
from pages.base import PageMain


@dog.parent_suite("自动化测试套件")
@dog.suite("登录功能测试")
@dog.feature("用户认证")
class TestLogin:

    @staticmethod
    def setup_method():
        start_wg_app()

    @staticmethod
    def teardown_method():
        stop_wg_app()


    @dog.title("进入登录页面")
    def test_login_page(self):
        PageMain.login()
