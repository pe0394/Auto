from selenium import webdriver
from create import WebFindWait
from create import Paas_Login
import csv
from create import py_jietu

class Testd():

    def setup(self):
        self.driver = webdriver.Chrome('d:\\chromedriver.exe')
        self.waitUtil = WebFindWait.WaitUtil(self.driver)# 实例化WaitUtil类
        self.Loginfor = Paas_Login.Loginfor(self.driver)
        self.driver.maximize_window()
        self.driver.get("http://paas.forclass.net")
        self.logindata = []  # 初始化容器
        csvFile = open(r'D:\Auto\\test\\username1.csv', 'r')  # 读取本地csv，只读模式
        reader = csv.reader(csvFile)
        for row in reader:  # 循环遍历将表内账号密码放入logindata
            self.logindata.append((row[0], row[1]))

    def test_1(self):
        for item in self.logindata:
            print('账号：' + item[0] + ' 密码：' + item[1])
            self.Loginfor.login(item[0], item[1])
            self.waitUtil.find_element('linktext', '作业系统', 30, 0.3).click()
            self.waitUtil.find_element('css', '.menulist', 30, 0.3).click()
            self.waitUtil.find_element('id', 'logout', 30, 0.3).click()
    def teardown(self):
        pass