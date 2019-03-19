from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


# 对象库层：封装定位元素的方法
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

        self.username = (By.ID, "username")
        self.pwd = (By.ID, "password")
        self.verify_code = (By.ID, "verify_code")
        self.login_btn = (By.NAME, "sbtbutton")

    def find_username(self):
        return self.find_element(self.username)

    def find_pwd(self):
        return self.find_element(self.pwd)

    def find_verify_code(self):
        return self.find_element(self.verify_code)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


# 操作层：封装元素操作的方法
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_pwd(self, pwd):
        self.input_text(self.login_page.find_pwd(), pwd)

    def input_verify_code(self, code):
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层:将一个或者多个操作组合成一个业务功能
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login(self, username, pwd, code):
        self.login_handle.input_username(username)
        self.login_handle.input_pwd(pwd)
        self.login_handle.input_verify_code(code)
        self.login_handle.click_login_btn()
