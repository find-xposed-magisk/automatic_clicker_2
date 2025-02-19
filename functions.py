import datetime
import os
import re
import typing

import win32con
import win32gui
from PySide6.QtWidgets import QMessageBox
from system_hotkey import SystemHotkey, user32


def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time

        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print("%s cost time: %.3f s" % (func.__name__, time_spend))
        return result

    return func_wrapper


def get_str_now_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_current_folder() -> str:
    """获取当前文件夹"""
    return os.path.dirname(os.path.abspath(__file__))


def line_number_increment(old_value, number=1):
    """行号递增
    :param old_value: 旧的单元格号
    :param number: 递增的数量"""
    # 提取字母部分和数字部分
    column_letters = re.findall(r"[a-zA-Z]+", old_value)[0]
    line_number = int(re.findall(r"\d+\.?\d*", old_value)[0])
    # 计算新的行号
    new_line_number = line_number + number
    # 组合字母部分和新的行号
    new_cell_position = (column_letters + str(new_line_number)).upper()
    new_cell_position = new_cell_position
    return new_cell_position


def is_hotkey_valid(hkobj: SystemHotkey, hk: typing.List[str]):
    """判断快捷键是否有效"""
    hk = hkobj.order_hotkey(hk)
    try:
        keycode, masks = hkobj.parse_hotkeylist(hk)
        reg_hk_res = user32.RegisterHotKey(None, 1, masks, keycode)
        if reg_hk_res:
            user32.UnregisterHotKey(None, reg_hk_res)
            return True
    except Exception as e:
        print("获取快捷键注册信息失败！", e)
    return False


def show_window(title):
    """将指定标题的窗口正常显示，主要用于主窗口显示"""

    def get_window_titles(hwnd, titles):
        titles[hwnd] = win32gui.GetWindowText(hwnd)

    try:
        hwnd_title = {}
        win32gui.EnumWindows(get_window_titles, hwnd_title)
        for h, t in hwnd_title.items():
            if t == title:
                win32gui.ShowWindow(h, win32con.SW_SHOWNORMAL)  # 正常显示窗口
                win32gui.SetForegroundWindow(h)
                break
    except Exception as e:
        print(f"显示窗口出现错误: {e}")


def critical_window(QWidget, title, message):
    """弹出错误窗口"""
    QMessageBox.critical(
        QWidget,
        title,
        message,
        QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.NoButton,
    )


def warning_window(QWidget, title, message):
    """弹出警告窗口"""
    QMessageBox.warning(
        QWidget,
        title,
        message,
        QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.NoButton,
    )
