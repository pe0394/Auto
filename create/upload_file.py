import win32api
import win32con
import time
import pyperclip

def upload_file():
    # 发送 ctrl（17） + V（86）按钮
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    win32api.keybd_event(13, 0, 0, 0)  # (回车)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    time.sleep(3)