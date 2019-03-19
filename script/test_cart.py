import unittest

from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from utils import DriverUtil


class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()
        cls.goods_search_proxy = GoodsSearchProxy()
        cls.goods_detail_proxy = GoodsDetailProxy()

    def setUp(self):
        self.driver.get("http://localhost:8088/")
    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 搜索商品并加入购物车
    def test_add_goods_to_cart(self):
        goods_name = "小米10"

        # 搜索指定商品
        self.index_proxy.search_goods(goods_name)

        # 进入商品详情页
        self.goods_search_proxy.to_goods_detail_page(goods_name)

        # 加入购物车
        self.goods_detail_proxy.join_cart()

        # 断言
        is_success = self.goods_detail_proxy.is_join_success("添加成功")
        self.assertTrue(is_success)









