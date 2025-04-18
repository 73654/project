# encoding: utf-8
"""
@ author:  wuyouyuan
@ file:    page_send_receive_messages
@ time:    2025/4/18 10:18 
@ desc:
"""


from pages.base.page_send_receive_messages import PageSendReceiveMessages
from common import dog
from common.ui import poco


class IOSPageSendReceiveMessages(PageSendReceiveMessages):

    @classmethod
    def page_receive_historical_address(cls):
        with dog.step(f"{cls.page_name}-点击历史地址"):
            poco("历史地址").click()


