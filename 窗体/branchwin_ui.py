# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'branchwin.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QLabel,
    QListView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_branch(object):
    def setupUi(self, branch):
        if not branch.objectName():
            branch.setObjectName(u"branch")
        branch.resize(240, 276)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        branch.setFont(font)
        self.verticalLayout = QVBoxLayout(branch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(branch)
        self.label.setObjectName(u"label")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 255, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.label.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.listView = QListView(branch)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(0, 100))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.listView.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(11)
        self.listView.setFont(font2)
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.listView.setFlow(QListView.Flow.TopToBottom)
        self.listView.setViewMode(QListView.ViewMode.ListMode)
        self.listView.setSelectionRectVisible(True)

        self.verticalLayout.addWidget(self.listView)

        self.pushButton = QPushButton(branch)
        self.pushButton.setObjectName(u"pushButton")
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setBold(True)
        self.pushButton.setFont(font3)

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(branch)

        QMetaObject.connectSlotsByName(branch)
    # setupUi

    def retranslateUi(self, branch):
        branch.setWindowTitle(QCoreApplication.translate("branch", u"\u5206\u652f\u6267\u884c", None))
        self.label.setText(QCoreApplication.translate("branch", u"\u53cc\u51fb\u5206\u652f\u540d\u79f0\u5f00\u59cb\u6267\u884c", None))
        self.pushButton.setText(QCoreApplication.translate("branch", u"\u663e\u793a\u4e3b\u7a97\u53e3", None))
    # retranslateUi

