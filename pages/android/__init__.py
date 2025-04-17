# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/24 20:40
# Description:
# -------------------------------------------------------------------------
from .page_main import AndroidPageMain as PageMain
from .page_friends import AndroidPageFriends as PageFriends
from .page_shop import AndroidPageShop as PageShop
from .page_mine import AndroidPageMine as PageMine
from .page_qr_share import AndroidPageQrShare as PageQrShare
from .page_wechat import AndroidPageWechat as PageWechat
from .page_mini_program import AndroidPageMiniProgram as PageMiniProgram
from .page_share import AndroidPageShare as PageShare, AndroidPageShare2 as PageShare2
from .page_clubber_recharge import AndroidPageClubberRecharge as PageClubberRecharge
from .page_dynamic_detail import AndroidPageDynamicDetail as PageDynamicDetail
from .page_batch_edit import AndroidPageBatchEdit as PageBatchEdit
from .page_batch_forward import AndroidPageBatchForward as PageBatchForward
from .page_work_bench import AndroidPageWorkBench as PageWorkBench
from .page_place_order import AndroidPagePlaceOrder as PagePlaceOrder

__all__ = ["PageMain", "PageFriends", "PageShop", "PageMine", "PageQrShare", "PageWechat", "PageMiniProgram",
           "PageShare", "PageShare2", "PageClubberRecharge", "PageDynamicDetail", "PageBatchEdit", "PageBatchForward",
           "PageWorkBench", "PagePlaceOrder"]
