import os
from datetime import datetime
def getscreenshot(driver, filename="页面截图"):
    """带有时间戳的截图"""
    screenshot_dir = 'D:\\screenshot'  # 当前目录下的screenshot文件夹；或设置其他目录
    if not os.path.exists(screenshot_dir):  # 不存在则创建该目录
        os.mkdir(screenshot_dir)

    nowdate = datetime.now().strftime('%Y%m%d')  # 当日日期
    screenshot_today_dir = os.path.join(screenshot_dir, nowdate)  # 当前日期文件夹
    if not os.path.exists(screenshot_today_dir):
        os.mkdir(screenshot_today_dir)  # 不存在则创建

    nowtime = datetime.now().strftime('%H%M%S%f')  # 时间戳
    filename = nowtime + filename + ".png"  # 拼接文件名 时间戳+文件名+.png
    filepath = os.path.join(screenshot_today_dir, filename)
    driver.get_screenshot_as_file(filepath)  # 截图，文件名=filename+时间戳