from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


# 对象库层：封装定位元素的方法
class CartPage(BasePage):
    def __init__(self):
        super().__init__()

        self.check_all = (By.CLASS_NAME, "checkCartAll")
        self.go_balance = (By.LINK_TEXT, "去结算")

    def find_check_all(self):
        return self.find_element(self.check_all)

    def find_go_balance(self):
        return self.find_element(self.go_balance)


# 操作层：封装元素操作的方法
class CartHandle(BaseHandle):
    def __init__(self):
        self.cart_page = CartPage()

    # 全选
    def click_all_goods(self):
        if not self.cart_page.find_check_all().is_selected():
            self.cart_page.find_check_all().click()

    # 去结算
    def click_go_balance(self):
        self.cart_page.find_go_balance().click()


# 业务层:将一个或者多个操作组合成一个业务功能
class CartProxy:
    def __init__(self):
        self.cart_handle = CartHandle()

    # 去结算
    def go_balance(self):
        self.cart_handle.click_all_goods()
        self.cart_handle.click_go_balance()
