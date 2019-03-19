from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


# 对象库层
from utils import DriverUtil


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()

        self.login_link = (By.LINK_TEXT, "登录")
        self.search = (By.ID, "q")
        self.search_btn = (By.CSS_SELECTOR, "[type='submit']")
        self.my_cart = (By.ID, "hd-my-cart")

    def find_login_link(self):
        return self.find_element(self.login_link)

    def find_search(self):
        return self.find_element(self.search)

    def find_search_btn(self):
        return self.find_element(self.search_btn)

    def find_my_cart(self):
        return self.find_element(self.my_cart)


# 操作层
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()

    def click_login_link(self):
        self.index_page.find_login_link().click()

    def input_search_kw(self, kw):
        self.input_text(self.index_page.find_search(), kw)

    def click_search_btn(self):
        self.index_page.find_search_btn().click()

    def click_my_cart(self):
        self.index_page.find_my_cart().click()

# 业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 跳转到首页
    def to_index_page(self):
        DriverUtil.get_driver().get("http://localhost:8088/")

    # 跳转到登录页面
    def to_login_page(self):
        self.index_handle.click_login_link()

    # 搜索商品
    def search_goods(self, kw):
        self.index_handle.input_search_kw(kw)
        self.index_handle.click_search_btn()

    # 进入购物车
    def to_my_cart_page(self):
        self.index_handle.click_my_cart()