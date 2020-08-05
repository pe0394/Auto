from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()
time.sleep(1)

dr.get('http:\\paas.forclass.net')
waittime = 10
dr.implicitly_wait(waittime)

#学生操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
dr.implicitly_wait(waittime)
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa01s07')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('666666')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
dr.implicitly_wait(waittime)
#作业系统
dr.find_element_by_link_text('作业系统').click()
dr.implicitly_wait(waittime)
#作答
#待完成
dr.find_element_by_css_selector('.el-main-tab:nth-child(2)').click()
time.sleep(1)
act = ActionChains(dr)
act.move_to_element(dr.find_element_by_css_selector('tr:nth-child(1) .icon-write')).perform()
dr.implicitly_wait(waittime)
dr.find_element_by_css_selector('.icon-write:nth-child(2)').click()
dr.implicitly_wait(waittime)

#学生作答区
#切换iframe
dr.switch_to.frame('ueditor_0')
dr.find_element_by_css_selector('.view:nth-child(2)').send_keys('输入框作答')
dr.implicitly_wait(waittime)
#释放iframe，重新回到主页面上
dr.switch_to.default_content()
dr.implicitly_wait(waittime)

#上传素材
dr.find_element_by_id('fileToUpload').send_keys('D:\\test.jpg')
time.sleep(waittime)
#提交
dr.find_element_by_css_selector('.el-dati-attsubmit').click()