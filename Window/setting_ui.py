# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QHeaderView, QKeySequenceEdit, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import images_rc

class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(354, 487)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Setting.setFont(font)
        icon = QIcon()
        icon.addFile(u":/\u6309\u94ae\u56fe\u6807/Window/res/\u56fe\u6807.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Setting.setWindowIcon(icon)
        Setting.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Setting)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(Setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 2)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_5.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 3)

        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.verticalSpacer_2 = QSpacerItem(20, 253, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.keySequenceEdit = QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")

        self.gridLayout_6.addWidget(self.keySequenceEdit, 0, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)

        self.keySequenceEdit_2 = QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit_2.setObjectName(u"keySequenceEdit_2")

        self.gridLayout_6.addWidget(self.keySequenceEdit_2, 1, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_20, 2, 0, 1, 1)

        self.keySequenceEdit_3 = QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit_3.setObjectName(u"keySequenceEdit_3")

        self.gridLayout_6.addWidget(self.keySequenceEdit_3, 2, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_21, 3, 0, 1, 1)

        self.keySequenceEdit_4 = QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit_4.setObjectName(u"keySequenceEdit_4")

        self.gridLayout_6.addWidget(self.keySequenceEdit_4, 3, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)

        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.verticalSpacer_3 = QSpacerItem(20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableWidget = QTableWidget(self.tab_4)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 2)

        self.pushButton_5 = QPushButton(self.tab_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_7.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.tab_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon1 = QIcon()
        icon1.addFile(u":/\u6309\u94ae\u56fe\u6807/Window/res/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon1)

        self.gridLayout_7.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_7.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.tab_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon2 = QIcon()
        icon2.addFile(u":/\u6309\u94ae\u56fe\u6807/Window/res/\u5220\u9664.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon2)

        self.gridLayout_7.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_3 = QCheckBox(Setting)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_3.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.pushButton = QPushButton(Setting)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton, 4, 1, 1, 1)

        self.checkBox_4 = QCheckBox(Setting)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(Setting)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 0, 1, 2)

        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.retranslateUi(Setting)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"\u8bbe\u7f6e", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Setting", u"\u767e\u5ea6OCR\u8bbe\u7f6e", None))
        self.label_16.setText(QCoreApplication.translate("Setting", u"secretKey\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("Setting", u"appId\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("Setting", u"apiKey\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Setting", u"\u524d\u5f80\u7f51\u9875", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Setting", u"\u4e91\u7801\u8bbe\u7f6e", None))
        self.pushButton_4.setText(QCoreApplication.translate("Setting", u"\u524d\u5f80\u7f51\u9875", None))
        self.label_18.setText(QCoreApplication.translate("Setting", u"Token\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Setting", u"\u5176\u4ed6\u8bbe\u7f6e", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Setting", u"\u5168\u5c40\u5feb\u6377\u952e", None))
        self.label_17.setText(QCoreApplication.translate("Setting", u"\u5f00\u59cb\u8fd0\u884c\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("Setting", u"\u7ed3\u675f\u8fd0\u884c\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("Setting", u"\u5206\u652f\u9009\u62e9\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("Setting", u"\u6682\u505c\u548c\u6062\u590d\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Setting", u"\u5feb\u6377\u952e", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Setting", u"\u5206\u652f\u540d\u79f0", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Setting", u"\u5feb\u6377\u952e", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Setting", u"\u91cd\u590d\u6b21\u6570", None))
        self.pushButton_5.setText(QCoreApplication.translate("Setting", u"\u4e0a\u79fb", None))
        self.pushButton_7.setText(QCoreApplication.translate("Setting", u"\u6dfb\u52a0\u5206\u652f", None))
        self.pushButton_6.setText(QCoreApplication.translate("Setting", u"\u4e0b\u79fb", None))
        self.pushButton_8.setText(QCoreApplication.translate("Setting", u"\u5220\u9664\u9009\u4e2d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Setting", u"\u5206\u652f\u7ba1\u7406", None))
        self.checkBox_3.setText(QCoreApplication.translate("Setting", u"\u7cfb\u7edf\u63d0\u793a\u97f3", None))
        self.pushButton.setText(QCoreApplication.translate("Setting", u"\u5e94\u7528", None))
        self.checkBox_4.setText(QCoreApplication.translate("Setting", u"\u4efb\u52a1\u5b8c\u6210\u540e\u663e\u793a\u4e3b\u7a97\u53e3", None))
        self.checkBox_2.setText(QCoreApplication.translate("Setting", u"\u6bcf\u6b21\u9000\u51fa\u63d0\u793a\u6e05\u7a7a\u6307\u4ee4", None))
    # retranslateUi

