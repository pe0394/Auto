from selenium import webdriver
#from webbase import Base
from selenium.webdriver.common.by import By #导入By类
from WebFindWait1 import Basee
import csv
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException #导入捕获异常类
from selenium.webdriver.support.ui import WebDriverWait #导入显示等待类
from selenium.webdriver.support import expected_conditions as EC    #导入期望场景类


class Testdenglu:
    def __init__(self):
        self.base = Basee()

    def setup(self):
        self.driver = webdriver.Chrome('d:\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http:\\paas.forclass.net')
        self.driver.implicitly_wait(20)

    def login(self, username, password):
        # self.base.set_netBase("http:\\paas.forclass.net")
        self.base.find_element(By.CSS_SELECTOR, '.glyphicon-login').click()
        self.base.find_element(By.ID, 'login-name').send_keys(username)
        self.base.find_element(By.ID, 'login-pwd').send_keys(password)

    def test_123(self):

        Testdenglu().login()

        # try:
        #     login_loc = WebDriverWait(self.driver, 10, 0.3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.glyphicon-login')))   # 等输入框出现在DOM树中
        #     login_loc.click   # 首页登录按钮
        # except(NoSuchElementException, TimeoutException) as e:  #捕获异常
        #     raise e #错误实例抛出

    def teardown(self):
        pass
        #self.driver.quit()

# if __name__ == "__main__":
#     bastTest = Testdenglu()
#     bastTest.login(username='sqa006',password='123566')