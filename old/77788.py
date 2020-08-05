from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://paas.forclass.net/'

driver = webdriver.Chrome('d:\chromedriver.exe')
driver.get(url)


# ele = driver.find_elements_by_css_selector('[class="el-menu-item top-nav-item"]')
# print(ele)
# 设置显示等待
el = WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.glyphicon-login')))
el.click()

el1 = WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located((By.ID,'login-name')))
el1.send_keys('sqa005')

el2 = WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located((By.ID,'login-pwd')))
el2.send_keys('654321')

el3 = WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.btnlogin')))
el3.click()

el4 = WebDriverWait(driver, 60, 0.5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,'作业系统')))
el4.click()

pass
