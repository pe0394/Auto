from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class WaitUtil(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator, timeout=30):
        """
        定位单个元素
        :param by: 定位方式 eg:By.ID
        :param locator: 定位表达式
        :param timeout: 显示等待超时时间
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).\
                until(lambda driver: driver.find_element(by, locator))
            assert isinstance(element, WebElement)
        except (NoSuchElementException, TimeoutException) as e:
            raise e
        else:
            return element


    def find_elements(self, by, locator, timeout=30):
        """
        定位一组元素
        :param by: 定位方式 eg:By.ID
        :param locator: 定位表达式
        :param timeout: 显示等待超时时间
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout).\
                until(lambda driver: driver.find_elements(by, locator))
            assert isinstance(elements, WebElement)
        except (NoSuchElementException, TimeoutException) as e:
            raise e
        else:
            return elements


if __name__ == '__main__':
    pass