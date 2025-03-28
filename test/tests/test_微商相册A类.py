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

        # PageShop.check_vip_status()
        # PageShop.check_new_number()
        # PageShop.check_total_number()
        #
        # PageShop.check_all_list()
        #
        # PageShop.tab_new()
        # PageShop.check_new_list()

        PageShop.tab_video()
        PageShop.check_video_list()

        PageShop.tab_picture_grid()
        PageShop.check_picture_grid()
