import logging.handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def init_log_config():
    ## 初始化日志配置

    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 创建处理器-控制台
    sh = logging.StreamHandler()

    #创建处理器-文件
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/tpshop.log",when="midnight",interval=1,backupCount=3,encoding="utf-8")

    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)