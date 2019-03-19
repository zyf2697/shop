import unittest
import time

import utils
from page.cart_page import CartProxy
from page.index_page import IndexProxy
from page.order_page import OrderProxy
from utils import DriverUtil


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()

        cls.index_proxy = IndexProxy()
        cls.cart_proxy = CartProxy()
        cls.order_proxy = OrderProxy()

    def setUp(self):
        self.index_proxy.to_index_page()
        self.index_proxy.to_my_cart_page()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 下订单
    def test_order(self):
        # 去结算
        self.cart_proxy.go_balance()

        # 等待加载收货人信息
        time.sleep(3)

        # 提交订单
        self.order_proxy.submit_order()

        # 断言
        is_exist = utils.exist_text("订单提交成功，请您尽快付款")
        self.assertTrue(is_exist)

