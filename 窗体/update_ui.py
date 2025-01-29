# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import images_rc

class Ui_Update_UI(object):
    def setupUi(self, Update_UI):
        if not Update_UI.objectName():
            Update_UI.setObjectName(u"Update_UI")
        Update_UI.resize(238, 139)
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        Update_UI.setFont(font)
        icon = QIcon()
        icon.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u66f4\u65b0.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Update_UI.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Update_UI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Update_UI)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u56fe\u6807.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Update_UI)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.progressBar = QProgressBar(Update_UI)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: red; /* \u5c06\u9ec4\u8272\u6539\u4e3a\u7ea2\u8272 */\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Update_UI)

        QMetaObject.connectSlotsByName(Update_UI)
    # setupUi

    def retranslateUi(self, Update_UI):
        Update_UI.setWindowTitle(QCoreApplication.translate("Update_UI", u"\u8f6f\u4ef6\u66f4\u65b0", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Update_UI", u"\u4fe1\u606f", None))
    # retranslateUi

