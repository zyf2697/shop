from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    def __init__(self):
        super().__init__()

        self.join_cart = (By.ID, "join_cart")
        self.join_result = (By.CSS_SELECTOR, "div.conect-title>span")

    def find_join_cart(self):
        return self.find_element(self.join_cart)

    def find_join_result(self):
        return self.find_element(self.join_result)


class GoodsDetailHandle(BaseHandle):
    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_join_cart(self):
        self.goods_detail_page.find_join_cart().click()

    def get_join_result_text(self):
        return self.goods_detail_page.find_join_result().text


class GoodsDetailProxy:
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.goods_detail_handle = GoodsDetailHandle()

    # 加入购物车
    def join_cart(self):
        self.goods_detail_handle.click_join_cart()

    # 判断是否加入成功
    def is_join_success(self, expect):
        # 切换表单
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        text = self.goods_detail_handle.get_join_result_text()
        return text == expect