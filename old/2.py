from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

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

try:
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.jykj-yy')))
    driver.find_element_by_css_selector('.jykj-yy').click()
except Exception as message:
    print('元素定位报错')
finally:
    pass


WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(.,'个人空间')]")))

kj = driver.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(driver).move_to_element(kj).perform()
time.sleep(mintime)
driver.find_element_by_xpath("//li[contains(.,'个人空间')]").click()




driver.close()


