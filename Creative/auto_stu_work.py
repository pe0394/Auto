from selenium import webdriver
import csv
import time

driver = webdriver.Chrome('d:\chromedriver.exe')
driver.maximize_window()
waittime = 20
driver.implicitly_wait(waittime)


# 定义函数为 作业链接，如果作业链接找不到，点击下一页查找，直到找到链接
def find_element_by_link_text(key):
    try:
        ele = driver.find_element_by_link_text(key)  # 根据key值获取元素
        return ele  # 如果dr.find_element_by_link_text不出现异常，就会执行这句话，并返回element元素。如果报异常，这句话不执行，直接到异常处理
    except Exception as e:
        print(e)  # 如果dr.find_element_by_link_text报异常，会到这里，然后执行打印
        return None  # 然后执行返回

def find_element_by_css_selector(key):
    try:
        ele = driver.find_element_by_css_selector(key)  # 根据key值获取元素
        return ele
    except Exception as e:
        print(e)
        return None  # 然后执行返回

def find_element_by_xpath(key):
    try:
        ele = driver.find_element_by_xpath(key)  # 根据key值获取元素
        return ele
    except Exception as e:
        print(e)
        return None  # 然后执行返回

def find_element_by_id(key):
    try:
        ele = driver.find_element_by_id(key)  # 根据key值获取元素
        return ele
    except Exception as e:
        print(e)
        return None  # 然后执行返回


#查找作业名字

def find_zuo_yeInfo():
    element = find_element_by_link_text('学科核心素质评价07')  # 对函数find_element_by_link传入'学科核心素质评价04'这个参数,会获取一个返回值，要么是NONE，要么是找到的元素el
    if (element == None):  # 对接受的值做判断，如果find_element_by_link返回的是NONE，执行下一页，再调用当前函数，寻找'学科核心素质评价04'元素
        driver.find_element_by_xpath('//li[contains(text(),"下一页")]').click()
        time.sleep(1)
        find_zuo_yeInfo()  # 递归操作，继续调用当前函数
    else:
        element.click()  # 对接受的值做判断，如果find_element_by_link返回的元素有值，那么直接执行click操作


# 点确定提交作业后，返回首页点击账号信息退出

def find_log_outinfo():
    element = find_element_by_css_selector('.menulist')
    if (element == None):
        driver.find_element_by_css_selector('.menulist').click()
        time.sleep(1)
        find_log_outinfo()  # 递归操作，继续调用当前函数
    else:
        element.click()

def find_log_out():
    element = find_element_by_id('logout')
    if (element == None):
        driver.find_element_by_id('logout').click()
        time.sleep(1)
        find_log_out()  # 递归操作，继续调用当前函数
    else:
        element.click()

# 学生进入作业点待完成

def find_no_complete():
    element = find_element_by_css_selector('div[showname="待完成"]')
    if (element == None):
        driver.find_element_by_css_selector('div[showname="待完成"]').click()
        time.sleep(1)
        find_no_complete()  # 递归操作，继续调用当前函数
    else:
        element.click()


# 学生进入作业详情开始作答后，第一个选项进行点击操作

def find_A_start():
    element = find_element_by_xpath("//div[@id='q1189143']/div[2]/div[2]/div/div/div[2]/span")
    if (element == None):
        driver.find_element_by_xpath("//div[@id='q1189143']/div[2]/div[2]/div/div/div[2]/span").click()
        time.sleep(1)
        find_A_start()  # 递归操作，继续调用当前函数
    else:
        element.click()


# 首页账号登录按钮捕获

def find_log_in():
    element = find_element_by_css_selector('.glyphicon-login')
    if (element == None):
        driver.find_element_by_css_selector('.glyphicon-login').click()
        time.sleep(1)
        find_log_in()  # 递归操作，继续调用当前函数
    else:
        element.click()


logindata = []  #初始化容器
csvFile = open(r'D:\Auto\\test\\test_fu.csv', 'r')   #读取本地csv，只读模式
reader = csv.reader(csvFile)
for row in reader:      #循环遍历将表内账号密码放入logindata
    logindata.append((row[0], row[1]))

driver.get('http:\\test.forclass.net')
driver.implicitly_wait(waittime)
for item in logindata:
    print('账号：' + item[0] + ' 密码：' + item[1])
    # 首页登录按钮
    find_log_in()
    time.sleep(1)
    # 输入账号
    login = driver.find_element_by_id('login-name')
    login.send_keys(item[0])
    # 输入密码
    pwd = driver.find_element_by_id('login-pwd')
    pwd.send_keys(item[1])
    # 登录按钮
    driver.find_element_by_css_selector('.btnlogin').click()
    # 作业系统
    driver.find_element_by_link_text('作业系统').click()
    time.sleep(1)
    # 作答
    # 待完成
    # find_no_complete()
    # time.sleep(1)
    # find_zuo_yeInfo()
    # time.sleep(0.5)
    # find_A_start()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@id='q1189144']/div[2]/div[2]/div/div/div[2]/span/span").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@id='q1189158']/div[2]/div[2]/div/div/div[2]/span").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@id='q1189158']/div[2]/div[2]/div/div[2]/div[2]/span").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@id='q1189164']/div[2]/div[2]/div/div/div[2]/span/span").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@id='q1189164']/div[2]/div[2]/div/div[2]/div[2]/span/span").click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('.el-dati-btn-submit > span').click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//input[@value='确 认']").click()
    # time.sleep(1)

    # 账号退出
    find_log_outinfo()
    time.sleep(0.5)
    find_log_out()


# driver.find_element_by_css_selector('.menulist').click()
#time.sleep(1)
#driver.find_element_by_id('logout').click()
    driver.implicitly_wait(waittime)

driver.close()