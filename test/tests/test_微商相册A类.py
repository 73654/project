# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 9:53
# Description:
# -------------------------------------------------------------------------


from common import dog, ui
from common.ui import *
from pages import *
# from pages.base.page_mine import PageMine


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
            # PageShop.good_share()
            PageShop.shop_share_poster_click()

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

    @dog.title("通用_0012:新增商品")
    def test_0012(self):
        with dog.step("新增商品"):
            PageMain.tab_dynamic()
            BasePageAlbumDynamic.page_add_commodity_img()
            BasePageAlbumDynamic.page_add_content()
            BasePageAlbumDynamic.page_release()
            PageMobilePhoneAlbum.page_mobile_phone()
            PageMobilePhoneAlbum.page_mobile_img_enter()
            PageMobilePhoneAlbum.page_enter_title_writing()
            PageMobilePhoneAlbum.page_add_details()
            PageMobilePhoneAlbum.page_select_from_mobile()
            PageMobilePhoneAlbum.page_choose_img_mobile()
            PageMobilePhoneAlbum.page_mobile_img_enter()
            PageMobilePhoneAlbum.page_scroll_little_down()
            PageMobilePhoneAlbum.page_add_details()
            PageMobilePhoneAlbum.page_select_from_mobile()
            PageMobilePhoneAlbum.page_choose_one_img()
            PageMobilePhoneAlbum.page_mobile_img_enter()

            PageMobilePhoneAlbum.page_scroll_little_down()
            PageMobilePhoneAlbum.page_commodity_properties()
            PageMobilePhoneAlbum.page_click_commodity_selling_price()
            PageMobilePhoneAlbum.page_click_commodity_wholesale_price()
            PageMobilePhoneAlbum.page_click_commodity_package_price()
            PageMobilePhoneAlbum.page_click_commodity_drop_shipping_price()
            PageMobilePhoneAlbum.page_commodity_release()

        with dog.step("切换test01账号看新增商品"):
            PageMain.tab_mine()
            PageMine.page_mine_configure()
            PageConfigure.page_switch_account()
            PageConfigure.page_config_click()
            BasePageAlbumDynamic.page_new_commodity_search()
            BasePageAlbumDynamic.page_check_commodity_info()

        with dog.step("切换冒泡账号"):
            PageChooseGoods.page_back_lever()
            PageMain.tab_mine()
            PageMine.page_mine_configure()
            PageConfigure.page_switch_account()
            PageConfigure.page_config_other_click()

    @dog.title("通用_0013:--转存商品分享")
    def test_0013(self):
        PageMain.tab_friends()
        PageFriends.goto_other_album(album_name="test01")
        PageShop.shop_friend_search()
        PageDynamicDetail.page_one_click_forward()
        PageDynamicDetail.page_detail_drag_other()
        PageDynamicDetail.page_detail_delete_material()
        PageDynamicDetail.page_detail_forward_album()
        PageImMessage.page_two_back()
        PageFriends.my_album()
        PageShop.shop_friend_click()
        PageDynamicDetail.check_detail_forward_product()

    @dog.title("通用_0015:店铺分享-卡片分享")
    def test_0015(self):
        PageMain.tab_friends()
        PageFriends.my_album()
        PageShop.shop_table_share()
        PageShop.table_share_code()
        PageShop.share_wx_friend()
        PageShare.choose_wechat()
        PageWechat.send_to_file_assistant()
        PageWechat.enter_wx_code()
        PageWechat.wx_open_immediately()

    @dog.title("通用_0018:商品置顶&刷新")
    def test_0018(self):
        with dog.step("验证商品置顶/取顶功能"):
            PageMain.tab_friends()
            PageFriends.my_album()
            PageShop.shop_search_name()
            PageDynamicDetail.table_commodity_top()
            PageDynamicDetail.back_to_friend_page()
            PageMain.tab_friends()
            PageFriends.my_album()
            PageShop.find_top_element()
            PageDynamicDetail.table_commodity_obtain_top()
            PageDynamicDetail.back_shop_page()

        with dog.step("验证刷新功能"):
            PageShop.find_refresh_element()
            PageDynamicDetail.table_refresh()
            PageShop.find_refresh_back()


    @dog.title("通用_0019:批量转发好友")
    def test_0019(self):
        with dog.step("进入到个人相册页"):
            PageMain.tab_friends()
            PageFriends.my_album()
            PageShop.batch_edit_share()
            PageShop.table_batch_edit()
            PageBatchEdit.check_page_scroll()
            PageFriends.goto_other_album(album_name="test01")
            PageShop.batch_forward()
        with dog.step("进入到好友相册页--批量转发"):
            PageBatchForward.page_batch_filter()
            PageBatchForward.page_batch_end_time()
            PageBatchForward.page_filter_little_video()
            PageBatchForward.page_filter_confirm()
            PageBatchForward.page_batch_search()
            PageBatchForward.click_search_result()
        with dog.step("批量转发页--进行自动加价/选择标签操作"):
            PageBatchForward.page_batch_increase_price()
            PageBatchForward.page_batch_enter_price()
            PageBatchForward.page_batch_label()
        with dog.step("查看批量转发后的商品"):
            PageBatchForward.page_batch_mine_shop()
            PageBatchForward.check_tabel_info()

    @dog.title("通用_0022:开单")
    def test_0022(self):
        with dog.step("开单"):
            PageMain.tab_workbench()
            PageWorkBench.page_invoice_write()
            PageWorkBench.check_invoice_windows()
            PagePlaceOrder.page_place_customer()
            PagePlaceOrder.page_place_choose_customer()
            PagePlaceOrder.page_place_delivery_mode()
            PagePlaceOrder.page_place_delivery_choose()
            PagePlaceOrder.page_place_delivery_information()
            PageSendReceiveMessages.page_receive_historical_address()
            PageSendReceiveMessages.page_receive_search()
            PagePlaceOrder.page_place_choose_goods()
            PageChooseGoods.page_choose_goods()
            PageChooseGoods.page_choose_next_step()
            PageChooseGoods.page_choose_payment_status()
            PageChooseGoods.page_choose_confirm_order()

    @dog.title("通用_0021:访客足迹")
    def test_0021(self):
        with dog.step("A进入B相册主页查看"):
            PageMain.tab_friends()
            PageFriends.goto_other_album(album_name="test01")
            PageChooseGoods.page_back_lever()
            PageMain.tab_mine()
            PageMine.page_mine_configure()
        with dog.step("切换B账号"):
            PageConfigure.page_switch_account()
            PageConfigure.page_config_click()
            PageMain.tab_mine()
            PageMine.page_mine_visitor()
            PageVisitor.check_page_visitor_title()
            PageVisitor.check_page_visitor()
            PageChooseGoods.page_back_lever()
            PageMine.page_mine_configure()
            PageConfigure.page_switch_account()
            PageConfigure.page_config_other_click()

    @dog.title("通用_0023:收款码支付")
    def test_0023(self):
        with dog.step("A进入工作台，保存收款码"):
            PageMain.tab_workbench()
            PageWorkBench.receiving_payment_code()
            PageReceiveAndPayment.page_click_payment_code()
            PageReceiveAndPayment.page_send_friend_window()
            PageShare.choose_wechat()
            PageWechat.send_to_file_assistant()
            PageWechat.click_wx_payment_code()
            PageWechat.page_payment_amount()

    @dog.title("通用_0026:加购自己商品")
    def test_0026(self):
        with dog.step("加购自己的商品--开单"):
            PageMain.tab_dynamic()
            BasePageAlbumDynamic.text_search()
            PageAddProductsCart.page_products_invoice()
            PageAddProductsCart.check_products_invoice()

        with dog.step("加购自己的商品--立即购买"):
            PageAddProductsCart.page_clean_invoice()
            PageAddProductsCart.page_products_buy()
            PageAddProductsCart.check_enter_order()

    # @dog.title("通用_0027_1:采购商品--在未开通在线收款")
    # def test_0027_1(self):
    #     with dog.step("采购未开通在线收款用户的商品"):
    #         PageMain.tab_friends()
    #         PageFriends.goto_other_album(album_name="test01")
    #         PageShop.shop_cart_add()
    #         PageShop.page_add_shop_car()
    #         PageAddProductsCart.page_click_purchase()
    #         PageAddProductsCart.page_click_purchase_order()
    #         PageAddProductsCart.page_phone_remind_window()
    #     with dog.step("确认采购页检查"):
    #         PageAddProductsCart.check_ensure_purchase()
    #
    # @dog.title("通用_0027_2:采购商品--已开通在线收款")
    # def test_0027_2(self):
    #     with dog.step("采购已开通在线收款用户的商品"):
    #         PageMain.tab_friends()
    #         PageFriends.my_album()
    #         PageShop.shop_mine_cart_add()
    #
    #         PageAddProductsCart.page_mine_shop_buy()
    #         PageAddProductsCart.page_commit_order_buy()
    #         PageShare.choose_wechat()
    #         PageAddProductsCart.page_no_pay_windows()
    #         PageAddProductsCart.check_purchase_pay_page()
    #
    #
    #
    # @dog.title("通用_0011:IM消息")
    # def test_0011(self):
    #     with dog.step("冒泡查看给test01发送消息"):
    #         PageMain.tab_friends()
    #         PageFriends.goto_other_album(album_name="test01")
    #         PageShop.page_friend_contact()
    #         PageImMessage.page_online_chat()
    #         PageImMessage.page_message_windows()
    #
    #         PageImMessage.page_send_sticker()
    #         PageImMessage.page_send_sticker_packs()
    #         PageImMessage.page_click_send_enter()
    #
    #         PageImMessage.page_send_message()
    #
    #         PageImMessage.page_click_plus_sign()
    #         PageImMessage.page_choose_photo_album()
    #         PageImMessage.page_two_back()
    #     with dog.step("切换test01账号,并查看对应消息是否正常展示"):
    #         PageMain.tab_mine()
    #         PageMine.page_mine_configure()
    #         PageConfigure.page_switch_account()
    #         PageConfigure.page_config_click()
    #         PageMain.tab_message()
    #         PageImMessage.page_send_message_switch()
    #         PageImMessage.check_im_message()
    #         PageChooseGoods.page_back_lever()
    #     with dog.step("切换冒泡账号"):
    #         PageMain.tab_mine()
    #         PageMine.page_mine_configure()
    #         PageConfigure.page_switch_account()
    #         PageConfigure.page_config_other_click()
    #
    # @dog.title("通用_0029:云盘一键清理")
    # def test_0029(self):
    #     with dog.step("冒泡账号云盘一键清理"):
    #         PageMain.tab_friends()
    #         PageFriends.my_album()
    #         PageShop.batch_edit_share()
    #         PageShop.page_shop_clean_up()
    #         PageCleanUpImages.page_clean_image()
    #         PageCleanUpImages.page_check_cloud_space()
    #         PageImMessage.page_two_back()
    #     with dog.step("个人相册查看一个月前的商品是否删除"):
    #         PageCleanUpImages.check_shop_cloud_commodity()
    #         PageShop.batch_edit_share()
    #         PageShop.page_shop_clean_up()
    #         PageCleanUpImages.page_recycle_bin()
    #         PageCleanUpImages.page_recycle_restore_all()
    #         PageCleanUpImages.page_recycle_restore_listed()
    #
    # @dog.title("通用_0028:开播功能验证")
    # def test_0028(self):
    #     with dog.step("冒泡账号开启直播"):
    #         PageMain.tab_dynamic()
    #         BasePageAlbumDynamic.page_add_content()
    #         PageLiveStream.page_private_domain_live()
    #         PageLiveStream.page_live_streaming_all()
    #         PageLiveStream.check_page_live()
    #         PageLiveStream.page_live_continue()
    #         PageLiveStream.page_share_live()
    #         PageLiveStream.page_share_live_wechat()
    #         PageShare.choose_wechat()
    #         PageWechat.send_to_file_assistant()
    #         PageWechat.page_wechat_live()
    #         PageLiveStream.page_live_start_app()
    #         PageMain.tab_mine()
    #     with dog.step("切换test01账号看直播"):
    #         PageMine.page_mine_configure()
    #         PageConfigure.page_switch_account()
    #         PageConfigure.page_config_click()
    #         PageMain.tab_mine()
    #         PageMine.page_switch_sub_account()
    #         BasePageAlbumDynamic.page_add_content()
    #         PageLiveStream.page_private_domain_live()
    #         PageLiveStream.page_assistant_live()
    #         PageLiveStream.check_page_live()
    #
    # @dog.title("通用_0024:员工账号权限验证")
    # def test_0024(self):
    #     with dog.step("子账号相册动态页搜索"):
    #         BasePageAlbumDynamic.page_team_permission_search()
    #         PageTeamPermissions.check_team_permissions_price()
    #
    # @dog.title("通用_0025:员工账号权限验证")
    # def test_0025(self):
    #     with dog.step("我的钱包"):
    #         PageMain.tab_mine()
    #         PageMine.page_mine_my_wallet()
    #         PageChooseGoods.page_back_lever()
    #         PageMain.tab_workbench()
    #         PageWorkBench.page_work_check_earning()
    #         PageTeamPermissions.check_team_statistical_data()
    #
