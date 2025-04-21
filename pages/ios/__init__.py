# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/24 20:40
# Description:
# -------------------------------------------------------------------------
from .page_main import IOSPageMain as PageMain
from .page_friends import IOSPageFriends as PageFriends
from .page_shop import IOSPageShop as PageShop
from .page_mine import IOSPageMine as PageMine
from .page_qr_share import IOSPageQrShare as PageQrShare
from .page_wechat import IOSPageWechat as PageWechat
from .page_mini_program import IOSPageMiniProgram as PageMiniProgram
from .page_share import IOSPageShare as PageShare, IOSPageShare2 as PageShare2
from .page_clubber_recharge import IOSPageClubberRecharge as PageClubberRecharge
from .page_dynamic_detail import IOSPageDynamicDetail as PageDynamicDetail
from .page_batch_edit import IOSPageBatchEdit as PageBatchEdit
from .page_batch_forward import IOSPageBatchForward as PageBatchForward
from .page_work_bench import IOSPageWorkBench as PageWorkBench
from .page_place_order import IOSPagePlaceOrder as PagePlaceOrder
from .page_send_receive_messages import IOSPageSendReceiveMessages as PageSendReceiveMessages
from .page_choose_goods import IOSPageChooseGoods as PageChooseGoods
from .page_configure import IOSPageConfigure as PageConfigure
from .page_visitor import IOSPageVisitor as PageVisitor
from .page_receive_and_payment import IOSPageReceiveAndPayment as PageReceiveAndPayment
from .page_album_dynamic import IOSBasePageAlbumDynamic as BasePageAlbumDynamic
from .page_add_products_cart import IOSPageAddProductsCart as PageAddProductsCart
__all__ = ["PageMain", "PageFriends", "PageShop", "PageMine", "PageQrShare", "PageWechat", "PageMiniProgram",
           "PageShare", "PageShare2", "PageClubberRecharge", "PageDynamicDetail", "PageBatchEdit", "PageBatchForward",
           "PageWorkBench", "PagePlaceOrder", "PageSendReceiveMessages", "PageChooseGoods", "PageConfigure",
           "PageVisitor", "PageReceiveAndPayment", "BasePageAlbumDynamic","PageAddProductsCart"]
