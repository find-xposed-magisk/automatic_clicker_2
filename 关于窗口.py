from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog

from ini控制 import IniControl
from 窗体.about_ui import Ui_About
from 软件信息 import *


class About(QDialog, Ui_About):
    """关于窗体"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化窗体
        self._parent = parent
        self.setupUi(self)
        self.ini = IniControl()
        self.ini.set_window_size(self)  # 获取上次退出时的窗口大小
        self.label_2.setText(f"版本：{CURRENT_VERSION}")  # 设置版本号
        self.label_7.setText(
            '<a href="{}"><font color="red">{}</font></a>'.format(QQ_GROUP, QQ)
        )
        # 绑定事件
        self.gitee.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(MAIN_WEBSITE)))
        self.gitee_2.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(Github_WEBSITE))
        )
        self.pushButton.clicked.connect(
            lambda: self._parent.check_update_software(True)
        )
        self.pushButton_2.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(ISSUE_WEBSITE))
        )
        self.pushButton_3.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(DONATE_WEBSITE))
        )

    def closeEvent(self, event):
        # 保存窗体大小
        self.ini.save_window_size(self.width(), self.height(), self.windowTitle())
