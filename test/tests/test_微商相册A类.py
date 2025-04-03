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

    @dog.title("通用_0007:我的tab-二维码、小程序码展示&刷新")
    def test_0007(self):
        PageMain.tab_mine()
        PageMine.qr_entry()

        with dog.step("检查相册分享-二维码"):
            PageQrShare.check_qr()

            PageQrShare.refresh()
            PageQrShare.check_qr()

        with dog.step("检查相册分享-小程序码"):
            PageQrShare.tab_mini_qr()
            PageQrShare.check_mini_qr()

            PageQrShare.refresh()
            PageQrShare.check_mini_qr()

    @dog.title("通用_0014:普通商品-海报分享")
    def test_0014(self):
        PageMain.tab_friends()
        PageFriends.my_album()

        PageShop.good_share()
        PageShare.enable_mini_code()
        PageShare.share_wechat_poster()

        PageShare.choose_wechat()

        PageWechat.poster_publish()
        PageWechat.enter_mini_program()

        PageMiniProgram.check_goods_show()
