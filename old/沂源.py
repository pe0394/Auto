from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('d:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://test.yy.eduzibo.com/')
waittime = 30
mintime = 3



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


driver.find_element_by_css_selector('.jykj-yy').click()
kj = driver.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(driver).move_to_element(kj).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'个人空间')]").click()
time.sleep(mintime)
kj = driver.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(driver).move_to_element(kj).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'教育空间')]").click()

driver.find_element_by_xpath("//span[contains(.,'首页')]").click()

#首页点社区
driver.find_element_by_css_selector('.jysq-yy').click()
time.sleep(mintime)
driver.find_element_by_xpath("//span[contains(.,'首页')]").click()


#首页点教研
driver.find_element_by_css_selector('.wljy-yy').click()
jy = driver.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(driver).move_to_element(jy).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//body/div[3]/ul/li").click()#集体备课
jy = driver.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(driver).move_to_element(jy).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'录播评课')]").click()#录播评课
jy = driver.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(driver).move_to_element(jy).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'主题研讨')]").click()#主题研讨
jy = driver.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(driver).move_to_element(jy).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'优化作业')]").click()#优化作业
jy = driver.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(driver).move_to_element(jy).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'一师一优课')]").click()#一师一优课






driver.close()


