#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
# author：Lucien
# 基础包: 压力Log日志封装
from locust import events
import os
import time
import logging
from logging.handlers import RotatingFileHandler


class loadLogger():
    def __init__(self, filePath, fileName):
        self.filePath = filePath  # 存放文件的路径
        self.fileName = fileName  # 存放文件的名字
        self.BACK_UP_COUNT = 5000  # 文件分割上限数
        self.MAX_LOG_BYTES = 1024 * 1024 * 1  # 单个文件最大记录数1M
        self.create_handler()  # 初始化创建日志handler
        self.create_logger()  # 初始化创建Logger

    def create_handler(self):  # 建立handler
        self.success_handler = RotatingFileHandler(filename=os.path.join(self.filePath, self.fileName),
                                                   maxBytes=self.MAX_LOG_BYTES * 100, backupCount=self.BACK_UP_COUNT,
                                                   delay=1)  # 分割文件处理按100m分割
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')  # 设定输出格式
        formatter.converter = time.gmtime  # 时间转换
        self.success_handler.setFormatter(formatter)  # 格式加载到handler

    def create_logger(self):  # 建立Logger
        self.success_logger = logging.getLogger('request_success')
        self.success_logger.propagate = False
        self.success_logger.addHandler(self.success_handler)

    def success_request(self, request_type, name, response_time, response_length):  # 成功日志输出格式加载到Logger中
        msg = ' | '.join([str(request_type), name, str(response_time), str(response_length)])
        self.success_logger.info(msg)

    def get_locust_Hook(self):  # 钩子挂载到Locust中
        events.request_success.fire = self.success_request