from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()

dr.get('http:\\paas.forclass.net')
waittime = 10
mintime = 3
dr.implicitly_wait(waittime)


#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
time.sleep(waittime)
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa01s01')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('666666')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)
#作业系统
dr.find_element_by_link_text('作业系统').click()
time.sleep(5)

#作答
dr.find_element_by_css_selector('.el-main-tab:nth-child(2)').click()
time.sleep(1)
act = ActionChains(dr)
act.move_to_element(dr.find_element_by_css_selector('tr:nth-child(1) .icon-write')).perform()
time.sleep(waittime)
dr.find_element_by_css_selector('.icon-write:nth-child(2)').click()
time.sleep(waittime)
# 手写答题一(画布)
dr.find_element_by_css_selector('.question_body:nth-child(3) > .ques_funcs_img_item').click()
time.sleep(waittime)

dr.find_element_by_id('cnvs_temp').click()

huabu = dr.find_element_by_id('cnvs_temp')
act = ActionChains(dr)
act.move_to_element(huabu).click_and_hold().perform()
act.move_to_element(huabu).perform()
act.move_by_offset(200, 100).click().perform()
act.move_to_element(huabu).release().perform()
dr.find_element_by_id('cnvs_temp').click()
dr.find_element_by_css_selector('.cnvs_opt_ok').click()

# 选择作答二
dr.find_element_by_css_selector('.qoption:nth-child(1) font').click()
time.sleep(waittime)

# 横线作答三
dr.find_element_by_css_selector('span:nth-child(3) > .qoption > textarea').send_keys('担心')
dr.find_element_by_css_selector('.qoption:nth-child(2) > textarea').send_keys('扁担')
time.sleep(waittime)

# 图片上传四
dr.find_element_by_css_selector('#q256853 .ques_funcs_img')
dr.find_element_by_id('q_file256853').send_keys('D:\\test.jpg')
time.sleep(waittime)

# 手写作答五
dr.find_element_by_css_selector('#q256857 .ques_funcs_img_item').click()
time.sleep(waittime)

dr.find_element_by_id('cnvs_temp').click()
huabu = dr.find_element_by_id('cnvs_temp')
act = ActionChains(dr)
act.move_to_element(huabu).click_and_hold().perform()
act.move_to_element(huabu).perform()
act.move_by_offset(200, 100).click().perform()
act.move_to_element(huabu).release().perform()
dr.find_element_by_id('cnvs_temp').click()
dr.find_element_by_css_selector('.cnvs_opt_ok').click()
time.sleep(waittime)
dr.find_element_by_css_selector('.el-dati-btn-submit > span').click()
time.sleep(waittime)
dr.find_element_by_css_selector('.dlg-btn-submit').click()
time.sleep(waittime)
# 账号退出
dr.find_element_by_css_selector('.menulist').click()
time.sleep(waittime)
dr.find_element_by_id('logout').click()
dr.implicitly_wait(waittime)

dr.close()