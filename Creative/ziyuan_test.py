from selenium import webdriver
from create.Smart_Waiting import waitutil
from create.Paas_Login import Loginfor
import time
import pyperclip
from create import upload_file
driver = webdriver.Chrome('d:\\chromedriver.exe')
waitutil = waitutil(driver)
Loginfor = Loginfor(driver)

def setup():
    driver.maximize_window()
    driver.get("http://paas.forclass.net")
    driver.implicitly_wait(30)

def test_1():   #资源中心创建教学资源，数字试题，教学应用，互动微课
    Loginfor.login('sqa001', '654321')
    # 进入同步资源
    waitutil.visibility_of_element_located('linktext', '同步资源', 30, 0.3).click()
    time.sleep(1)
    # 创建
    waitutil.element_to_be_clickable('css', '.ivu-icon-compose', 30, 0.3).click()
    #教学资源标签
    #非input标签上传文件
    pyperclip.copy("D:\\test.jpg")  # 复制文件路径到剪切板，pyperclip库需要安装
    waitutil.visibility_of_element_located('css', '.upload-prompt-text', 30, 0.3).click()
    time.sleep(1)  # 等待程序加载 时间 看你电脑的速度 单位(秒)
    upload_file.upload_file()
    waitutil.visibility_of_element_located('xpath', '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/i', 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', "//li[text()='初中']", 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/i', 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', "//li[text()='语文']", 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div/i', 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', "//li[text()='统编版']", 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div/i', 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', "//li[text()='七年级上']", 30, 0.3).click()
    waitutil.visibility_of_element_located('css', '[class="ivu-icon ivu-icon-plus-circled"]', 30, 0.3).click()
    waitutil.visibility_of_element_located('xpath', '//span[text()="2 济南的冬天"]', 30, 0.3).click()
    waitutil.visibility_of_element_located('css', '[class="ivu-btn ivu-btn-primary ivu-btn-large"]', 30, 0.3).click()
    jianjie = waitutil.visibility_of_element_located('css', '[wrap="soft"][autocomplete="off"]', 30, 0.3)
    jianjie.send_keys('等待程序加载 时间 看你电脑的速度 单位')

    waitutil.element_to_be_clickable('xpath', "//span[text()='发布']", 30, 0.3).click()
    time.sleep(1)
    # 创建
    waitutil.element_to_be_clickable('css', '.ivu-icon-compose', 30, 0.3).click()
    # 数字试卷标签
    waitutil.visibility_of_element_located('xpath', "//div[contains(text(),'数字试题')]", 30, 0.3).click()
    # 选择题型
    waitutil.visibility_of_element_located('css', '[title="2 济南的冬天"]', 30, 0.3).click()
    time.sleep(0.5)
    waitutil.element_to_be_clickable('css', '[title="单选题"]', 30, 0.3).click()
    # 编辑试题
    # 切换iframe
    waitutil.frame_to_be_available_and_switch_to_it('id', 'ueditor_0', 30, 0.3)
    # 答题要求
    element = waitutil.visibility_of_element_located('css', '.cq-require-input', 30, 0.3)
    element.send_keys('这是答题要求')
    # 大题干
    element = waitutil.visibility_of_element_located('css', '.cq-tigan1-input', 30, 0.3)
    element.send_keys('这是大题干')
    # 小题干
    element = waitutil.visibility_of_element_located('css', '.cq-tmpl-q-title', 30, 0.3)
    element.send_keys('这是小题干')
    # 选项
    element = waitutil.visibility_of_any_elements_located('css', '[class="form-control cq-option-input"]', 30, 0.3)[0]
    element.send_keys('这是选项A')
    element = waitutil.visibility_of_any_elements_located('css', '[class="form-control cq-option-input"]', 30, 0.3)[1]
    element.send_keys('这是选项B')
    element = waitutil.visibility_of_any_elements_located('css', '[class="form-control cq-option-input"]', 30, 0.3)[2]
    element.send_keys('这是选项C')
    element = waitutil.visibility_of_any_elements_located('css', '[class="form-control cq-option-input"]', 30, 0.3)[3]
    element.send_keys('这是选项D')
    # 正确答案
    waitutil.visibility_of_any_elements_located('css', '.cq-op-checkbox', 30, 0.3)[0].click()
    # 答案解析
    element = waitutil.visibility_of_element_located('css', '.cq-tmpl-textarea', 30, 0.3)
    element.send_keys('这是答案解析')
    # 退出iframe
    driver.switch_to.default_content()
    # 保存
    waitutil.visibility_of_element_located('css', '.cq-btn-save', 30, 0.3).click()
    # 去我的题库
    waitutil.visibility_of_element_located('css', '.dlg-btn-submit', 30, 0.3).click()
    # 首页
    waitutil.visibility_of_element_located('xpath', "//div[text()='首页']", 30, 0.3).click()
