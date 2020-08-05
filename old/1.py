from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from create import Paas_Login
Loginfor = Paas_Login.loginfor(driver)
Loginfor.login()
driver = webdriver.Chrome('d:\chromedriver.exe')
driver.maximize_window()
driver.get('http://test.yy.eduzibo.com/')
waittime = 30
mintime = 3

driver.implicitly_wait(waittime)

#教师操作
#首页登录按钮
driver.find_element_by_css_selector('.login').click()
#输入账号
login = driver.find_element_by_id('login-name')
login.send_keys('sqa006')
#输入密码
pwd = driver.find_element_by_id('login-pwd')
pwd.send_keys('123566')
#登录按钮
driver.find_element_by_css_selector('.loginbtnc').click()

#首页点教育空间
locator = (By.CSS_SELECTOR, ".jykj-yy")
try:
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(locator))
finally:
    driver.find_element_by_css_selector('.jykj-yy').click()

locator = (By.XPATH, "//span[contains(.,'空间')]")
try:
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(locator))
finally:
    kj = driver.find_element_by_xpath("//span[contains(.,'空间')]")
    ActionChains(driver).move_to_element(kj).perform()
    time.sleep(mintime)
    driver.find_element_by_xpath("//li[contains(.,'个人空间')]").click()
# kj = driver.find_element_by_xpath("//span[contains(.,'空间')]")
# ActionChains(driver).move_to_element(kj).perform()
# time.sleep(mintime)
# driver.find_element_by_xpath("//li[contains(.,'个人空间')]").click()
# try:
#     WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(kongjian))
# finally:
#     kj = driver.find_element_by_xpath("//span[contains(.,'空间')]")
#     ActionChains(driver).move_to_element(kj).perform()
#     time.sleep(mintime)
#     driver.find_element_by_xpath("//li[contains(.,'教育空间')]").click()
# try:
#     WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(kongjian))
# finally:
#     driver.find_element_by_xpath("//span[contains(.,'首页')]").click()



# try:
#     login_loc = WebDriverWait(self.driver, 10, 0.3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.glyphicon-login')))   # 等输入框出现在DOM树中
#     login_loc.click   # 首页登录按钮
# except(NoSuchElementException, TimeoutException) as e:  #捕获异常
#     raise e #错误实例抛出
'''
#首页点教研
locator = (By.CSS_SELECTOR, ".wljy-yy")

try:
    WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located(locator))
finally:
    driver.find_element_by_css_selector('.wljy-yy').click()
'''





pass



