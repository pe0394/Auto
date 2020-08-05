from selenium import webdriver
#加载Chrome驱动
driver = webdriver.Chrome(r'd:\chromedriver.exe')
#打开网址
driver.get('http://www.51job.com')
#等待5秒
#driver.implicitly_wait(5)
#查找输入框
ele = driver.find_element_by_id('kwdselectid')
#输入文字
ele.send_keys('python')
#查找城市按钮
ele = driver.find_element_by_id('work_position_input')\
#点击
ele.click()

#取消选中城市
eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')

for ele in eles:
    ele.click()
#选中城市北京
ele = driver.find_element_by_id('work_position_click_center_right_list_category_000000_010000').click()
#点击保存
driver.find_element_by_id('work_position_click_bottom_save').click()

driver.find_element_by_css_selector('.ush button').click()
'''
#搜索结果分析
job = driver.find_elements_by_css_selector('#resultList div[class=el]')

for job in jobs:
'''
pass