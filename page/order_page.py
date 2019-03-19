import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


# 对象库层：封装定位元素的方法
class OrderPage(BasePage):
    def __init__(self):
        super().__init__()

        self.submit_order = (By.LINK_TEXT, "提交订单")

    def find_submit_order(self):
        return self.find_element(self.submit_order)


# 操作层：封装元素操作的方法
class OrderHandle(BaseHandle):
    def __init__(self):
        self.order_page = OrderPage()

    # 点击提交订单
    def click_submit_order(self):
        self.order_page.find_submit_order().click()


# 业务层:将一个或者多个操作组合成一个业务功能
class OrderProxy:
    def __init__(self):
        self.order_handle = OrderHandle()

    # 提交订单
    def submit_order(self):
        time.sleep(2)
        self.order_handle.click_submit_order()










