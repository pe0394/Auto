from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait     #导入显示等待类
from selenium.webdriver.support import expected_conditions as EC    #导入期望场景类
from selenium.webdriver.common.by import By #导入By类
from typing import List #导入类型标注List类
from create.screenshot import getscreenshot

class WaitUtil:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, method,  value, timeout=30, time_space=0.5) -> WebElement:   #定位一个元素
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
            # 抛出异常信息给上层调用者
            getscreenshot(self.driver)
            raise e
        return element

    def find_elements(self, method,  value, timeout=30, time_space=0.5) -> List[WebElement]:    #定位一组元素
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
            # 抛出异常信息给上层调用者
            getscreenshot(self.driver)
            raise e
        return element

    def frame_to_be_available_and_switch_to_it(self, method, value, timeout, time_space) -> WebElement: #检查frame是否存在，存在则切换进去
        wait = WebDriverWait(self.driver, timeout, time_space)
        try:
            if method == 'id':
                wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, value)))  # presence_of_element_located省略了message字段必须有两层括号
                element = self.driver.find_element_by_id(value)
            elif method == 'css':
                wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, value)))
                element = self.driver.find_element_by_css_selector(value)
            else:
                print("元素定位错误，语法错误")
        except Exception as e:
            # 抛出异常信息给上层调用者
            getscreenshot(self.driver)
            raise e
        return element

    def frame_to_be_available_and_switch_to_it(self, locationType, locatorExpression, *args) -> WebElement:
        """
        检查frame是否存在，存在则切换进去
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            # 抛出异常信息给上层调用者
            raise e

