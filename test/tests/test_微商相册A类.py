# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:53
# Description:
# -------------------------------------------------------------------------
from airtest.core.api import keyevent

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

        with dog.step("点击分享按钮，进行分享"):
            PageShop.good_share()

            PageShare.enable_mini_code()
            PageShare.share_haibao()
            PageShare.top_right_corner_button()

        with dog.step("分享至微信文件传输助手，并识别二维码进入小程序"):
            PageShare2.share_wechat()
            PageShare.choose_wechat()

            PageWechat.send_to_file_assistant()
            PageWechat.enter_mini_program()

            PageMiniProgram.check_enter_mini_program()

    @dog.title("通用_0008:会员支付-支付跳转微信")
    def test_0008(self):
        PageMain.tab_mine()
        PageMine.clubber()
        with dog.step("点击个体会员，288"):
            PageClubberRecharge.person_version()
            PageClubberRecharge.downgrade_person_click()
            PageClubberRecharge.activation_confirmation()
        with dog.step("跳转至微信支付页面"):
            PageShare.choose_wechat()
            PageClubberRecharge.check_wechat_pay()

    @dog.title("通用_0009:会员支付-支付跳转支付宝")
    def test_0009(self):
        PageMain.tab_mine()
        PageMine.clubber()
        with dog.step("点击商城版，588"):
            PageClubberRecharge.shop_version()
            PageClubberRecharge.choose_wechatpay()
            PageClubberRecharge.choose_alipay()
            PageClubberRecharge.downgrade_shop_click()
            PageClubberRecharge.activation_confirmation()
        with dog.step("跳转至支付宝支付页面"):
            PageShare.choose_wechat()
            PageClubberRecharge.check_alipay_pay()

    @dog.title("通用_0010:会员支付-支付跳转他人代付")
    def test_0010(self):
        PageMain.tab_mine()
        PageMine.clubber()
        with dog.step("点击商城版，588"):
            PageClubberRecharge.shop_version()
            PageClubberRecharge.choose_wechatpay()
            PageClubberRecharge.choose_other_pay()
            PageClubberRecharge.downgrade_shop_click()
            PageClubberRecharge.activation_confirmation()
        with dog.step("跳转至他人代付支付页面"):
            PageClubberRecharge.check_other_pay()

    @dog.title("通用_0015:店铺分享-卡片分享")
    def test_0015(self):
        PageMain.tab_friends()
        PageFriends.my_album()
        PageShop.shop_table_share()
        PageShop.share_wx_friend()
        PageShare.choose_wechat()
        PageWechat.send_to_file_assistant()
        PageWechat.enter_wx_code()
        PageWechat.wx_open_immediately()


    @dog.title("通用_0016:搜索-文搜")
    def test_0016(self):
        pass


    @dog.title("通用_0018:商品置顶&刷新")
    def test_0018(self):
        PageMain.tab_friends()
        PageFriends.my_album()
        PageShop.shop_search_name()
        PageDynamicDetail.table_commodity_top()
        PageDynamicDetail.back_to_friend_page()
        PageMain.tab_friends()
        PageFriends.my_album()
        PageShop.find_top_element()




























