from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()
time.sleep(1)

dr.get('http:\\paas.forclass.net')
waittime = 10
dr.implicitly_wait(10)


#教师操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa001')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('666666')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

#作业系统
dr.find_element_by_link_text('作业系统').click()
time.sleep(waittime)

#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(waittime)


#拓展作业
dr.find_element_by_css_selector('.el-main-tab:nth-child(2)').click()
time.sleep(waittime)
dr.find_element_by_css_selector('li:nth-child(1) > .el-tree-level1 > .el-tree-item > .el-tree-leaf').click()
time.sleep(waittime)
dr.find_element_by_css_selector('li:nth-child(1) li:nth-child(2) .el-tree-leaf').click()
time.sleep(waittime)
dr.find_element_by_id('fileToUpload').send_keys('D:\\test.jpg')
time.sleep(waittime)
dr.find_element_by_css_selector('.ass-attach-btnnext').click()
time.sleep(waittime)
dr.find_element_by_css_selector('.ass-class-check:nth-child(1)').click()
time.sleep(waittime)
dr.find_element_by_css_selector('.ass-dlg-awbtn').click()
time.sleep(waittime)

