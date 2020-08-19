from selenium import webdriver
from create.Smart_Waiting import waitutil
from create.Paas_Login import Loginfor
import csv
from create.screenshot import getscreenshot


def find_zuo_yeInfo():
    element = waitUtil.visibility_of_element_located('lintext', '学科核心素质评价07')
    if (element == None):
        waitUtil.visibility_of_element_located('xpath', '//li[contains(text(),"下一页")]').click()
        find_zuo_yeInfo()
    else:
        element.click()

logindata = []  # 初始化容器
driver = webdriver.Chrome('d:\\chromedriver.exe')
waitUtil = waitutil(driver)
Loginfor = Loginfor(driver)
def setup():
    driver.maximize_window()
    driver.get("http://paas.forclass.net")
    csvFile = open(r'D:/Auto/test/test1.csv', 'r')  # 读取本地csv，只读模式
    reader = csv.reader(csvFile)
    for row in reader:  # 循环遍历将表内账号密码放入logindata
        logindata.append((row[0], row[1]))

def test_1():
    for item in logindata:
        print('账号：' + item[0] + ' 密码：' + item[1])
        Loginfor.login(item[0], item[1])
        waitUtil.visibility_of_element_located('linktext', '作业系统', 30, 0.3).click()
        try:
            # 作答待完成
            waitUtil.visibility_of_element_located('css', 'div[showname="待完成"]').click()
            find_zuo_yeInfo()
            waitUtil.visibility_of_element_located('xpath', "//div[@id='q1189143']/div[2]/div[2]/div/div/div[2]/span").click()
            waitUtil.visibility_of_element_located('xpath', "//div[@id='q1189144']/div[2]/div[2]/div/div/div[2]/span/span").click()
            waitUtil.visibility_of_element_located('xpath', "//div[@id='q1189158']/div[2]/div[2]/div/div/div[2]/span").click()
            waitUtil.visibility_of_element_located('xpath', "//div[@id='q1189158']/div[2]/div[2]/div/div[2]/div[2]/span").click()
            waitUtil.visibility_of_element_located('xpath', "//div[@id='q1189164']/div[2]/div[2]/div/div/div[2]/span/span").click()
            waitUtil.visibility_of_element_located('xpath', "//div[@id='q1189164']/div[2]/div[2]/div/div[2]/div[2]/span/span").click()
            waitUtil.visibility_of_element_located('css', '.el-dati-btn-submit > span').click()
            waitUtil.visibility_of_element_located('xpath', "//input[@value='确 认']").click()
            #账号退出
            waitUtil.visibility_of_element_located('css', '.menulist', 30, 0.3).click()
            waitUtil.visibility_of_element_located('id', 'logout', 30, 0.3).click()
        except Exception:
            getscreenshot(driver)

