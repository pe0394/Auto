from selenium import webdriver
import time


dates = csv.reader(open("D:\\test.csv", 'r'))
list = []
for date in dates:
    if date == 0:
        pass
    else:
        list.append(date)
print(list)
print(list[0])
print(list[0][0])
print(list[0][1])
driver = webdriver.Chrome('d:\chromedriver.exe')
driver.maximize_window()
driver.get('http:\\paas.forclass.net')
time.sleep(3)
dr.find_element_by_css_selector('.glyphicon-login').click()
time.sleep(3)
driver.find_element_by_id("login").send_keys(list[1][0])
driver.find_element_by_id("pwd").send_keys(list[1][1])
driver.find_element_by_css_selector('.btnlogin').click()

time.sleep(2)
driver.quit()


#读取本地CSV文件
# file = open(r'D:\test.csv')
# data = csv.reader(file)
# print(data)
#
# for www in data:
#     print(www)