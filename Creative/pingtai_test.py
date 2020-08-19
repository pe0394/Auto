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
