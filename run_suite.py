import unittest

import time

import config
from script.test_cart import TestCart
from script.test_login import TestLogin
from script.test_order import TestOrder
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

# 关闭自动退出的开关
DriverUtil.set_auto_quit(False)

suite = unittest.TestSuite()
# suite.addTest(TestLogin("test_login"))
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(TestCart("test_add_goods_to_cart"))
suite.addTest(TestOrder("test_order"))
unittest.TextTestRunner().run(suite)

# 测试报告路径
report_file = config.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_file,"wb") as f:
    runner = HTMLTestRunner(f,title="TPshop自动化测试报告",description="firefox.selenium2.48.0")
    runner.run(suite)

# 开启自动退出的开关
DriverUtil.set_auto_quit(True)
DriverUtil.quit_driver()
