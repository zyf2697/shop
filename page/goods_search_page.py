from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class GoodsSearchPage(BasePage):
    def __init__(self):
        super().__init__()

        self.goods_item = (By.XPATH, "//div[@class='shop_name2']/a[contains(text(),'{}')]")
        # self.goods_item = (By.XPATH, "//div[@class='shop_name2']/a[contains(text(),'%S')]")

    def find_goods_item(self, kw):
        location = (self.goods_item[0], self.goods_item[1].format(kw))
        # location = (self.goods_item[0], self.goods_item[1] % kw)
        return self.find_element(location)


class GoodsSearchHandle(BaseHandle):
    def __init__(self):
        self.goods_search_page = GoodsSearchPage()

    def click_goods_item(self, kw):
        self.goods_search_page.find_goods_item(kw).click()


class GoodsSearchProxy:
    def __init__(self):
        self.goods_search_handle = GoodsSearchHandle()

    # 点击商品,跳转到商品详情页
    def to_goods_detail_page(self, kw):
        self.goods_search_handle.click_goods_item(kw)

