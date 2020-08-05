from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time



dr = webdriver.Chrome('H:\\auto\chromedriver.exe')
dr.maximize_window()

dr.get('http://test.271bay.com/')
waittime = 10
mintime = 3
dr.implicitly_wait(waittime)

#教师操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()

#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('271sqa888')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('123456')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

#进入金雕
dr.get('http://test.course2.271bay.com/createlist')
time.sleep(10)
dr.implicitly_wait(waittime)
#创建部分
#新建学程
dr.find_element_by_css_selector('.makeNew').click()
time.sleep(1)

#选择目录
def mulu():
    dr.find_element_by_css_selector('div[title="小学"]').click()
    time.sleep(1)
    dr.find_element_by_css_selector('div[title="数学"]').click()
    time.sleep(1)
    dr.find_element_by_css_selector('div[title="271版（2019）"]').click()
    time.sleep(1)
    dr.find_element_by_css_selector('div[title="一年级上"]').click()
    time.sleep(1)
    dr.find_element_by_css_selector('div[title="271版（2019）"]').click()
    time.sleep(1)
    dr.find_element_by_css_selector('div[title="第一章　有理数　"]').click()
    time.sleep(1)

#调用目录方法
#mulu()
#目录确定
dr.find_element_by_xpath('/html/body/div[2]/div/div[3]/span/div[2]/span[2]').click()
time.sleep(2)

#修改学习设计名称
rename = dr.find_element_by_css_selector('.el-input__inner')
rename.send_keys('生活多姿多彩')
time.sleep(1)


#点击建任务群
dr.find_element_by_xpath('//div[contains(text(),"建任务群")]').click()
time.sleep(1)
dr.find_element_by_css_selector('[class="item-title active-title"]').click()
time.sleep(2)
#任务群名
missionname = dr.find_element_by_css_selector('[class="el-input"] [type="text"][class="el-input__inner"]')
missionname.send_keys('任务群1')
time.sleep(1)


#定义iframe方法
def changeIframe():
    # 内容+传图
    dr.find_element_by_css_selector('div[title="加粗"]').click()  # 粗体字
    # 切换iframe
    iframe = dr.find_element_by_css_selector('.edui-editor-iframeholder > iframe[id]')
    dr.switch_to.frame(iframe)
    dr.find_element_by_css_selector('[contenteditable="true"][spellcheck="false"]').click()  # 输入框
    time.sleep(1)
    dr.find_element_by_css_selector('[contenteditable="true"][spellcheck="false"]').send_keys('输入框作答')
    # 释放iframe，重新回到主页面上
    dr.switch_to.default_content()
    time.sleep(1)
    # 切换到另外一个iframe
    iframe = dr.find_element_by_css_selector('.edui-box > iframe[style]')
    dr.switch_to.frame(iframe)
    upload = dr.find_element_by_css_selector('form > [type="file"][accept="image/*"]')
    upload.send_keys(r'H:\\auto\test.PNG')
    time.sleep(3)
    dr.switch_to.default_content()
#切换iframe
changeIframe()

#保存
# dr.find_element_by_css_selector('.save').click()
# time.sleep(1)
#添加任务
#点击群名+号从隐藏状态显示出来
ActionChains(dr).move_to_element(dr.find_element_by_css_selector('[class="item-title active-title active-click-title"]')).perform()
time.sleep(2)
dr.find_element_by_css_selector('.btn-add').click()
dr.find_element_by_css_selector('[class="sitem-title active-title"]').click()
mission1 = dr.find_element_by_css_selector('[class="el-input"] [class="el-input__inner"]')
mission1.send_keys('任务1')
time.sleep(1)
#手动开启ON
dr.find_elements_by_css_selector('[class="el-switch__core"]')[0].click()
time.sleep(0.5)
#闯关模式ON
dr.find_elements_by_css_selector('[class="el-switch__core"]')[1].click()
time.sleep(0.5)
#保存任务1
dr.find_element_by_xpath('//div[contains(text(),"保存")]').click()
time.sleep(1)
#点击任务1

# dr.find_element_by_css_selector('.unit-task').click()
# time.sleep(1)
ActionChains(dr).move_to_element(dr.find_element_by_css_selector('[class="sitem-title active-title active-click-title"]')).perform()
#进行添加子任务
dr.find_elements_by_css_selector('[class="btn-add"]')[1].click()
time.sleep(2)
dr.find_element_by_css_selector('[class="titem-title active-title"]').click()
sublevelmission = dr.find_element_by_css_selector('[class="input-box"]>[class="el-input"]>[class="el-input__inner"]')
sublevelmission.send_keys('子任务123')
time.sleep(1)
#保存子任务
dr.find_element_by_xpath('//div[contains(text(),"保存")]').click()
time.sleep(1)
#模块部分
#添加标题
dr.find_element_by_xpath('//div[contains(text(),"标题")]').click()
time.sleep(1)
title = dr.find_element_by_css_selector('.task-title .el-input__inner')
title.send_keys('这是标题')
time.sleep(1)

#添加文字
dr.find_element_by_xpath('//div[contains(text(),"文字")]').click()


# 内容+传图
dr.find_element_by_css_selector('div[title="加粗"]').click()  # 粗体字
# 切换iframe
iframe = dr.find_element_by_css_selector('.edui-editor-iframeholder > iframe[id]')
dr.switch_to.frame(iframe)
dr.find_element_by_css_selector('[contenteditable="true"][spellcheck="false"]').click()  # 输入框
time.sleep(1)
dr.find_element_by_css_selector('[contenteditable="true"][spellcheck="false"]').send_keys('输入框作答')
# 释放iframe，重新回到主页面上
dr.switch_to.default_content()
time.sleep(1)

#添加资源

dr.find_element_by_xpath("//div[contains(text(),'资源')]").click()
time.sleep(1)
dr.find_element_by_css_selector('.resource-right > span').click()#资源库选择
time.sleep(1)
dr.find_element_by_css_selector('.cata-btn').click()#目录
time.sleep(1)

#调用目录
mulu()

time.sleep(1)
dr.find_element_by_xpath("/html/body/div[5]/div/div[3]/span/div/span[2]").click()#确定

time.sleep(1)
dr.find_element_by_css_selector('.no-use').click()#选择添加资源
time.sleep(1)
dr.find_element_by_css_selector('a').click()#下载资源
time.sleep(1)
dr.find_element_by_css_selector('.x-btn').click()
time.sleep(1)
#资源本地上传
zy = dr.find_element_by_css_selector('.el-upload__input')
zy.send_keys(r'G:\\test.txt')
time.sleep(2)
#资源标引
dr.find_element_by_xpath("//span[text()='资源标引']").click()
time.sleep(1)


dr.find_element_by_css_selector('.check-box-item .el-checkbox__inner').click()#选中

time.sleep(1)
dr.find_element_by_xpath('//span[text()="标引"]').click()
time.sleep(1)
dr.find_element_by_xpath('//span[text()="培养品质"]').click()
time.sleep(1)
#dr.find_element_by_xpath('//div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/label/span/span').click()#选中
#time.sleep(1)
dr.find_element_by_xpath('//span[text()="添加"]').click()
time.sleep(1)
dr.find_element_by_xpath('//span[text()="使用场景"]').click()
time.sleep(1)
#dr.find_element_by_xpath('//div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/label/span/span').click()#选中
time.sleep(1)
dr.find_element_by_xpath('//span[text()="添加"]').click()
time.sleep(1)
#dr.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]/input').click()#原创是
time.sleep(1)
#dr.find_element_by_xpath('./html/body/div[5]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/span/span').click()#下拉选中框
time.sleep(1)
#dr.find_element_by_xpath('//span[text()="学习设计与指导"]').click()
time.sleep(1)
dr.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/span[2]').click()#确定
time.sleep(1)
dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[3]/span[3]').click()#确定完成
time.sleep(1)
dr.find_element_by_css_selector('.ivu-icon').click()#关闭窗口

#返回
dr.find_element_by_css_selector('.back-img').click()
time.sleep(1)
dr.find_element_by_css_selector('.back-img-over').click()
#点击练习
dr.find_element_by_xpath("//span[contains(.,'练习')]").click()
#点击编辑练习
dr.find_element_by_css_selector('edit-trainer').click()
#点击新建习练
dr.find_element_by_xpath('//span[contains(.,"新建习练")]').click()
#定义iframe方法
def changeIframe1():
    # 切换iframe，找到新的iframe
    iframe2 = dr.find_element_by_css_selector('[id="paper-q-create"]')
    dr.switch_to.frame(iframe2)
    #点击题干输入框
    timutigan = dr.find_element_by_css_selector('[class="form-control cq-tmpl-input cq-tmpl-q-title"]').click()  # 输入框
    time.sleep(1)
    timutigan.send_keys('单选题题干')
    #编辑A选项
    a = dr.find_elements_by_css_selector('[class="form-control cq-option-input"]')[1].click()
    a.send_keys('选项A')
    #编辑B选项
    b = dr.find_element_by_css_selector('[class="form-control cq-option-input"]')[2].click()
    b.send_keys('选项B')
    #编辑C选项
    c = dr.find_element_by_css_selector('[class="form-control cq-option-input"]')[3].click()
    c.send_keys('选项C')
    #编辑D选项
    d = dr.find_element_by_css_selector('[class="form-control cq-option-input"]')[4].click()
    d.send_keys('选项D')
    #新增一个选项E
    dr.find_element_by_css_selector('[class="cq-q-btn cq-op-option-add"]').click()
    #编辑E选项
    e = dr.find_element_by_css_selector('[class="form-control cq-option-input"]')[5].click()
    e.send_keys('选项E')
    #指定一个正确的选项
    dr.find_element_by_xpath('//span[contains(.,"A")]').click()
    # 释放iframe，重新回到主页面上
    dr.switch_to.default_content()
    time.sleep(1)
    # 切换到另外一个iframe
    iframe3 = dr.find_element_by_css_selector('id="paper-q-create"')
    dr.switch_to.frame(iframe3)
    #新建选择题完毕，点击保存按钮
    savebutton = dr.find_element_by_css_selector('[class="btn btn-primary cq-btn-save"]').click()
    time.sleep(3)
    dr.switch_to.default_content()
#切换iframe
changeIframe1()
#点击弹窗返回按钮
dr.find_element_by_css_selector('value="返回"').click()
time.sleep(2)
#关闭新建练习
dr.find_element_by_css_selector('[class="el-icon-close"]').click()
#点击提交按钮
dr.find_element_by_xpath('//div[@class="template-item" ][contains(text(),"提交")]').click()
#添加量表
dr.find_element_by_xpath('//span[@class="edit-trainer"][contains(text(),"添加量表")]').click()


pass




