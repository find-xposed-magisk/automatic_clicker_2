# coding: utf-8
import datetime
import hashlib
import os
import sys

import ntplib
from PySide6.QtWidgets import QApplication, QInputDialog, QLineEdit, QMessageBox

from functions import get_current_folder
from 数据库操作 import DatabaseOperation

ACTIVATION_MONTH_KEY = "激活月份"
ACTIVATION_STATUS_KEY = "激活状态"
ACTIVATION_CHECK_DATE_KEY = "激活校验日期"
DEFAULT_ACTIVATION_SETTINGS = {
    ACTIVATION_MONTH_KEY: "",
    ACTIVATION_STATUS_KEY: "False",
    ACTIVATION_CHECK_DATE_KEY: "",
}


def get_webserver_time() -> datetime.date | None:
    """获取网络时间，如果网络异常则返回None"""
    ntp_servers = [
        "ntp.aliyun.com",
        "time.windows.com",
        "pool.ntp.org",
        "time.nist.gov",
    ]
    for server in ntp_servers:
        for retry in range(3):
            try:
                client = ntplib.NTPClient()
                response = client.request(server, version=3, timeout=3)
                ntp_time = datetime.datetime.fromtimestamp(response.tx_time)
                print(f"成功从 {server} 获取NTP时间: {ntp_time.date()}")
                return ntp_time.date()
            except Exception as exc:
                print(f"第{retry + 1}次从 {server} 获取NTP时间失败: {exc}")
                if retry == 2:
                    print(f"从 {server} 获取时间的所有重试都失败")
    print("所有NTP服务器都无法获取时间")
    return None


def get_month_start_str(web_date: datetime.date) -> str:
    """返回当前月份第一天的标准字符串。"""
    return web_date.replace(day=1).strftime("%Y-%m-%d")


def generate_activation_code(secret_key: str, web_date: datetime.date) -> str:
    """根据网络时间生成当月激活码。"""
    month_start = get_month_start_str(web_date)
    raw = f"{month_start}|{secret_key}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()[:16]


def get_activation_secret() -> str:
    """从本地DNM文件读取激活密匙。"""
    secret_path = os.path.join(get_current_folder(), "DNM")
    with open(secret_path, "r", encoding="utf-8") as file:
        secret = file.read().strip()
    if not secret:
        raise ValueError("DNM文件为空")
    return secret


def load_activation_state() -> dict:
    """从设置表加载激活状态。"""
    db = DatabaseOperation()
    result = DEFAULT_ACTIVATION_SETTINGS.copy()
    try:
        result.update(db.ensure_setting_values(DEFAULT_ACTIVATION_SETTINGS))
    except Exception as exc:
        print(f"读取激活状态失败: {exc}")
    return result


def save_activation_state(month_str: str, check_date: datetime.date) -> bool:
    """保存激活状态到设置表。"""
    db = DatabaseOperation()
    try:
        db.set_setting_values(
            {
                ACTIVATION_MONTH_KEY: month_str,
                ACTIVATION_STATUS_KEY: "True",
                ACTIVATION_CHECK_DATE_KEY: check_date.strftime("%Y-%m-%d"),
            }
        )
        return True
    except Exception as exc:
        print(f"保存激活状态失败: {exc}")
        return False


def is_activation_valid(web_date: datetime.date) -> bool:
    """检查当前月份是否已激活。"""
    activation_state = load_activation_state()
    current_month = web_date.strftime("%Y-%m")
    return (
        activation_state.get(ACTIVATION_MONTH_KEY) == current_month
        and activation_state.get(ACTIVATION_STATUS_KEY) == "True"
    )


def prompt_activation_code(parent=None) -> tuple[str, bool]:
    """弹出激活码输入框。"""
    app = QApplication.instance()
    if app is None:
        raise RuntimeError("QApplication未初始化")
    dialog = QInputDialog(parent)
    dialog.setWindowTitle("激活验证")
    dialog.setLabelText("请输入本月激活码：")
    dialog.setInputMode(QInputDialog.InputMode.TextInput)
    dialog.setTextEchoMode(QLineEdit.EchoMode.Normal)
    dialog.resize(460, dialog.sizeHint().height())
    dialog.setMinimumWidth(460)
    if parent is not None and parent.styleSheet():
        dialog.setStyleSheet(parent.styleSheet())
    ok = dialog.exec()
    return dialog.textValue(), bool(ok)


def show_error_and_exit(message: str, parent=None) -> None:
    """弹出错误提示并退出程序。"""
    app = QApplication.instance()
    if app is None:
        raise RuntimeError("QApplication未初始化")
    QMessageBox.critical(parent, "提示", message)
    sys.exit(1)


def check_activation_or_exit(parent=None) -> None:
    """检查激活状态，失败时弹窗后退出。"""
    web_date = get_webserver_time()
    if web_date is None:
        show_error_and_exit("无法获取网络时间，请检查网络连接后重试。", parent)

    if is_activation_valid(web_date):
        return

    try:
        expected_code = generate_activation_code(get_activation_secret(), web_date)
    except Exception as exc:
        print(f"读取激活密匙失败: {exc}")
        show_error_and_exit("激活配置文件丢失。", parent)
    while True:
        activation_code, ok = prompt_activation_code(parent)
        if not ok:
            show_error_and_exit("未完成激活验证，程序即将退出。", parent)
        if activation_code.strip().upper() == expected_code:
            current_month = web_date.strftime("%Y-%m")
            if save_activation_state(current_month, web_date):
                return
            print("激活信息写入失败，按校验失败处理。")
            show_error_and_exit("激活信息保存失败，请检查程序目录权限。", parent)
        QMessageBox.warning(parent, "提示", "激活码错误，请重新输入！")
