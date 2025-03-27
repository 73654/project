# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:53
# Description:
# -------------------------------------------------------------------------
from common import dog
from common.ui import *
from pages import *


class TestCompanyA:

    @staticmethod
    def setup_method():
        start_wg_app()

    @staticmethod
    def teardown_method():
        stop_wg_app()

    @dog.title("通用_0006:店铺主页加载")
    def test_0006(self):
        PageMain.tab_friends()
        PageFriends.my_album()
        PageShop.tab_new()
        PageShop.tab_video()
        PageShop.tab_picture_collection()
