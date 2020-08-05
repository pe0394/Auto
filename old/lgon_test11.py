from selenium import webdriver
# from webbase import Base
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.remote.webelement import WebElement

from WebFindWait import Basee
import pytest
import csv
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException #导入捕获异常类
from selenium.webdriver.support.ui import WebDriverWait #导入显示等待类
from selenium.webdriver.support import expected_conditions as EC    #导入期望场景类


class Testdeng():


    def setup(self):
        self.driver = webdriver.Chrome('d:\\chromedriver.exe')
        self.base = Basee(self.driver)
        self.driver.maximize_window()
        self.driver.get('http:\\paas.forclass.net')
        self.driver.implicitly_wait(20)


    def login(self, username, password):
        self.base.find_element(By.ID, 'login-name').send_keys(username)
        self.base.find_element(By.ID, 'login-pwd').send_keys(password)

    def test_1(self):
        self.base.find_element(By.CSS_SELECTOR, '.glyphicon-login').click()

        self.login(username='sqa006', password='123456')


    def teardown(self):
        pass
        #self.driver.quit()

if __name__ == "__main__":
    bastTest = Testdeng()
    bastTest.login(username='sqa006',password='123566')