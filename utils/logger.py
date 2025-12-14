import logging
import os
import time

# 确保logs文件夹存在
log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Logger:
    def __init__(self):
        # 定义日志文件名：logs/2025-xx-xx.log
        self.logname = os.path.join(log_path, f"{time.strftime('%Y-%m-%d')}.log")
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)
        
        # 防止重复打印日志
        if not self.logger.handlers:
            # 1. 写入文件
            fh = logging.FileHandler(self.logname, encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            # 2. 输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            
            # 定义格式
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

# 初始化一个单例供外部使用
log = Logger().get_log()