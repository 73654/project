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

        with dog.step("检查个人主页"):
            PageShop.check_vip_status()
            PageShop.check_new_number()
            PageShop.check_total_number()

        with dog.step("检查个人主页-全部列表"):
            PageShop.check_all_list()

        with dog.step("检查个人主页-上新列表"):
            PageShop.back_to_main_page()
            PageFriends.my_album()

            PageShop.tab_new()
            PageShop.check_new_list()

        with dog.step("检查个人主页-小视频列表"):
            PageShop.back_to_main_page()
            PageFriends.my_album()

            PageShop.tab_video()
            PageShop.check_video_list()

        with dog.step("检查个人主页-图集列表"):
            PageShop.back_to_main_page()
            PageFriends.my_album()

            PageShop.tab_picture_grid()
            PageShop.check_picture_grid()
