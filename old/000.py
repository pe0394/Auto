from time import sleep
from selenium import webdriver
# 驱动文件路径
driver = webdriver.Chrome('d:\\chromedriver.exe')
# 打开百度首页
driver.get('https://www.baidu.com/')
driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").click()
# 等待3秒，待全部加载完搜索结果
sleep(3)
# 获取搜索结果
results = driver.find_elements_by_css_selector("h3.t>a")
# 搜索结果以列表形式返回
print("results",results)
for r in results:
    print(r.text)
# 退出
driver.quit()