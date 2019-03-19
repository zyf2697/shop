import json
import logging
import unittest
import time

import config
import utils
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil
from parameterized import parameterized


def build_data():
    # return [("18600000000", "123456", "8888", "我的账户")]
    result=[]
    with open(config.BASE_DIR + "/data/login.json",encoding="utf-8") as f:
        json_data = json.load(f)
        print("json_data=", json_data)
        test_login_list = json_data.get("test_login")
        for test_login in test_login_list:
            # username = test_login.get("username")
            result.append((test_login.get("username"),test_login.get("pwd"),test_login.get("code"),
                           test_login.get("expect"),test_login.get("is_success")))
    return result


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()

        cls.index_proxy = IndexProxy()
        cls.login_proxy = LoginProxy()

    def setUp(self):
        self.driver.get("http://localhost:8088/")
        self.index_proxy.to_login_page()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()


    # 登录成功
    @parameterized.expand(build_data)
    def test_login(self, username, pwd, verify_code, expect, is_success):
        logging.info("username={} pwd={} verify_code={} expect={} is_success={}".format(username, pwd, verify_code, expect,is_success))
        self.login_proxy.login(username, pwd, verify_code)

        # 断言
        if is_success:
            time.sleep(3)
            self.assertIn(expect, self.driver.title)
        else:
            msg = utils.get_tips_msg()
            self.assertIn(expect, msg)


