import logging

from utils import DriverUtil

# 对象库层基类


class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        logging.debug("location={}".format(location))
        return self.driver.find_element(location[0], location[1])

# 操作层基类


class BaseHandle:
    # 输入操作
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)