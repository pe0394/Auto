# 用于实现智能等待页面元素的出现
# encoding = utf-8
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By     #导入By类
from selenium.webdriver.support.ui import WebDriverWait      #导入显示等待类
from selenium.webdriver.support import expected_conditions as EC    #导入期望场景类
import difflib  #导入文本差异


class waitutil:

    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "linktext": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def presence_of_element_located(self, location_type, locator_expression, *args) -> WebElement:
        """
        显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            if location_type.lower() in self.locationTypeDict:
                # if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(
                    EC.presence_of_element_located((
                        self.locationTypeDict[location_type.lower()], locator_expression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def frame_to_be_available_and_switch_to_it(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[location_type.lower()], locator_expression)))
        except Exception as e:
            # 抛出异常信息给上层调用者
            raise e

    def visibility_of_element_located(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element
        except Exception as e:
            raise e

    def wait_title_is(self, string, location_type, locator_expression, *args) -> WebElement:
        """
        当页面标题是string时对页面元素进行定位，并返回页面元素对象
        :param string:
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            if self.driver.title == string:
                element = self.wait.until(
                    EC.visibility_of_element_located((self.locationTypeDict[location_type.lower()], locator_expression)))
                return element
        except Exception as e:
            raise e

    def wait_title_contain(self, string, location_type, locator_expression, *args) -> WebElement:
        """
         当页面标题与string进行比较相似度大于0.8时对页面元素进行定位，并返回页面元素对象
        :param string:
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        page_tile = driver.title
        similarity = difflib.SequenceMatcher(None, page_tile, string).quick_ratio()
        try:
            if similarity >= 0.8:
                element = self.wait.until(
                    EC.visibility_of_element_located((self.locationTypeDict[location_type.lower()], locator_expression)))
                return element
        except Exception as e:
            raise e

    def visibility_of_element(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断元素是否可见，如果可见就返回这个元素
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.visibility_of((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element
        except Exception as e:
            raise e

    def presence_of_all_elements_located(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断是否至少有1个元素存在于dom树中，如果定位到就返回列表
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element_list = self.wait.until(
                EC.presence_of_all_elements_located((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element_list
        except Exception as e:
            raise e

    def visibility_of_any_elements_located(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断是否至少有一个元素在页面中可见，如果定位到就返回列表
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element_list = self.wait.until(
                EC.visibility_of_any_elements_located((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element_list
        except Exception as e:
            raise e

    def text_to_be_present_in_element(self, string, location_type, locator_expression, *args) -> WebElement:
        """
        判断指定的元素中是否包含了预期的字符串，返回布尔值
        :param string:
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((self.locationTypeDict[location_type.lower()], locator_expression), string))
        except Exception as e:
            raise e

    def text_to_be_present_in_element_value(self, string, location_type, locator_expression, *args) -> WebElement:
        """
        判断指定元素的属性值中是否包含了预期的字符串，返回布尔值
        :param string:
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            self.wait.until(
                EC.text_to_be_present_in_element_value((self.locationTypeDict[location_type.lower()], locator_expression), string))
        except Exception as e:
            raise e

    def invisibility_of_element_located(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.invisibility_of_element_located((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element
        except Exception as e:
            raise e

    def element_to_be_clickable(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断某个元素中是否可见并且是enable的，代表可点击
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element
        except Exception as e:
            raise e

    def element_to_be_selected(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断某个元素是否被选中了,一般用在下拉列表
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.element_to_be_selected((self.locationTypeDict[location_type.lower()], locator_expression)))
            return element
        except Exception as e:
            raise e

    def element_selection_state_to_be(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断某个元素的选中状态是否符合预期
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.element_selection_state_to_be((self.locationTypeDict[location_type.lower()], locator_expression), True))
            return element
        except Exception as e:
            raise e

    def element_located_selection_state_to_be(self, location_type, locator_expression, *args) -> WebElement:
        """
        判断某个元素的定位状态是否符合预期
        :param location_type:
        :param locator_expression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.element_located_selection_state_to_be((self.locationTypeDict[location_type.lower()], locator_expression), True))
            return element
        except Exception as e:
            raise e

    def alert_is_present(self) -> WebElement:
        """
        判断页面上是否存在alert,如果有就切换到alert并返回alert的内容
        """
        try:
            alert_instance = self.wait.until(EC.alert_is_present())
            print(alert_instance.text)
            alert_instance.accept()
        except Exception as e:
            raise e


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("paas.forclass.net")
    # 实例化WaitUtil类
    waitutil = waitutil(driver)
    # 判断如果id = x-URS-iframe的iframe存在则切换进去
    wf = waitutil.frame_to_be_available_and_switch_to_it("id", "x-URS-iframe")
    # 等待页面元素xpath = //input[@name='email']的出现
    wv = waitutil.visibility_element_located("xpath", "//input[@name='email']")
    # 显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
    wp = waitutil.presence_of_element_located("xpath", "//input[@name='email']")
    driver.quit()





