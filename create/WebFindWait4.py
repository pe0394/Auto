from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait     #导入显示等待类
from selenium.webdriver.support import expected_conditions as EC    #导入期望场景类
from selenium.webdriver.common.by import By #导入By类
from  typing import List
Vector = List[WebElement]
class WaitUtil:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, method,  value, timeout=30, time_space=0.5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout, time_space)
        try:
            if method == 'id':
                wait.until(EC.visibility_of_element_located((By.ID, value)))#presence_of_element_located省略了message字段必须有两层括号
                element = self.driver.find_element_by_id(value)
            elif method == 'name':
                wait.until(EC.visibility_of_element_located((By.NAME, value)))
                element = self.driver.find_element_by_name(value)
            elif method == 'class':
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, value)))
                element = self.driver.find_element_by_class_name(value)
            elif method == 'linktext':
                wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))
                element = self.driver.find_element_by_partial_link_text(value)
            elif method == 'xpath':
                wait.until(EC.visibility_of_element_located((By.XPATH, value)))
                element = self.driver.find_element_by_xpath(value)
            elif method == 'css':
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                element = self.driver.find_element_by_css_selector(value)
            else:
                print("元素定位错误，语法错误")
        except BaseException as e:
            print(e)
        assert isinstance(element, WebElement)
        return element

    def find_elements(self, method,  value, timeout=30, time_space=0.5) -> Vector:
        wait = WebDriverWait(self.driver, timeout, time_space)
        try:
            if method == 'id':
                wait.until(EC.presence_of_all_elements_located((By.ID, value)))#presence_of_element_located省略了message字段必须有两层括号
                element = self.driver.find_elements_by_id(value)
            elif method == 'name':
                wait.until(EC.presence_of_all_elements_located((By.NAME, value)))
                element = self.driver.find_elements_by_name(value)
            elif method == 'class':
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, value)))
                element = self.driver.find_elements_by_class_name(value)
            elif method == 'linktext':
                wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, value)))
                element = self.driver.find_elements_by_partial_link_text(value)
            elif method == 'xpath':
                wait.until(EC.presence_of_all_elements_located((By.XPATH, value)))
                element = self.driver.find_elements_by_xpath(value)
            elif method == 'css':
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, value)))
                element = self.driver.find_elements_by_css_selector(value)
            else:
                print("元素定位错误，语法错误")
        except BaseException as e:
            print(e)
        assert isinstance(element, list)

        return element