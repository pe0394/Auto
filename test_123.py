from selenium import webdriver
from create.WebFindWait2 import waiting
from create.Paas_Login import Loginfor
import csv
import pytest
from create.screenshot import getscreenshot

waitUtil = None
Loginloc = None
logindata = []  # 初始化容器
def setup(browser):
    global waitUtil
    global Loginloc
    waitUtil = waiting(browser)# 实例化WaitUtil类
    Loginloc = Loginfor(browser)
    # getscreenshot(self.driver)
    browser.maximize_window()
    browser.get("http://paas.forclass.net")
    csvFile = open(r'd:/Auto/test/username1.csv', 'r')  # 读取本地csv，只读模式
    reader = csv.reader(csvFile)
    for row in reader:  # 循环遍历将表内账号密码放入logindata
        logindata.append((row[0], row[1]))

def test_1(browser):
    for item in logindata:
        print('账号：' + item[0] + ' 密码：' + item[1])
        Loginloc.login(item[0], item[1])
        waitUtil.find_element('linktext', '作业系统', 30, 0.3).click()
        waitUtil.find_element('css', '.menulis', 1, 0.3).click()
        waitUtil.find_element('id', 'logout', 30, 0.3).click()
