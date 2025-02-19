# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QKeySequenceEdit, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)
import images_rc

class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(354, 491)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Setting.setFont(font)
        icon = QIcon()
        icon.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u56fe\u6807.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Setting.setWindowIcon(icon)
        Setting.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Setting)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(Setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font1)
        self.radioButton.setChecked(True)

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(255, 0, 0, 128))
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
        brush3 = QBrush(QColor(249, 249, 249, 77))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush4 = QBrush(QColor(0, 0, 0, 92))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.radioButton_2.setPalette(palette)
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setChecked(False)

        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 4)

        self.horizontalSlider_2 = QSlider(self.groupBox_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(1000)
        self.horizontalSlider_2.setSingleStep(100)
        self.horizontalSlider_2.setPageStep(100)
        self.horizontalSlider_2.setValue(200)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_2, 0, 1, 1, 2)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(1000000)

        self.gridLayout_2.addWidget(self.spinBox, 4, 1, 1, 2)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 4)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.horizontalSlider_3 = QSlider(self.groupBox_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setMaximum(1000)
        self.horizontalSlider_3.setSingleStep(100)
        self.horizontalSlider_3.setPageStep(100)
        self.horizontalSlider_3.setValue(200)
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_3, 2, 1, 1, 2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 4, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 4)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab, "")
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

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)

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
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton, 4, 1, 1, 1)

        self.checkBox_4 = QCheckBox(Setting)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(Setting)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox = QCheckBox(Setting)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(Setting)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.checkBox_5 = QCheckBox(Setting)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_3.addWidget(self.checkBox_5, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.retranslateUi(Setting)
        self.horizontalSlider_2.valueChanged.connect(self.label_6.setNum)
        self.horizontalSlider_3.valueChanged.connect(self.label_8.setNum)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Setting", u"\u6a21\u5f0f", None))
        self.radioButton.setText(QCoreApplication.translate("Setting", u"\u666e\u901a\u6a21\u5f0f", None))
        self.label.setText(QCoreApplication.translate("Setting", u"\u8be5\u6a21\u5f0f\u8f83\u4e3a\u7a33\u5b9a\uff0c\u53c2\u6570\u9002\u4e2d\uff0c\u9002\u5408\u65e5\u5e38\u4f7f\u7528", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"\u8be5\u6a21\u5f0f\u8fdb\u4e00\u6b65\u63d0\u9ad8\u64cd\u4f5c\u901f\u5ea6\uff0c\u53d6\u6d88\u6240\u6709\u64cd\u4f5c\u65f6\u95f4\u95f4\u9694", None))
        self.radioButton_2.setText(QCoreApplication.translate("Setting", u"\u6781\u901f\u6a21\u5f0f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Setting", u"\u6307\u4ee4\u8bbe\u7f6e", None))
        self.label_11.setText(QCoreApplication.translate("Setting", u"\u6307\u9f20\u6807\u53cc\u51fb\u7684\u65f6\u95f4\u95f4\u9694", None))
        self.label_12.setText(QCoreApplication.translate("Setting", u"\u6307\u6bcf\u5b8c\u6210\u4e00\u6b21\u6307\u4ee4\u81f3\u4e0b\u4e00\u6b21\u6307\u4ee4\u5f00\u59cb\u7684\u65f6\u95f4\u95f4\u9694", None))
        self.label_9.setText(QCoreApplication.translate("Setting", u"\u6682\u505c\u65f6\u95f4\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Setting", u"\u6beb\u79d2", None))
        self.label_6.setText(QCoreApplication.translate("Setting", u"\u6beb\u79d2", None))
        self.label_10.setText(QCoreApplication.translate("Setting", u"\u6beb\u79d2", None))
        self.label_5.setText(QCoreApplication.translate("Setting", u"\u65f6\u95f4\u95f4\u9694\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("Setting", u"\u6307\u6267\u884c\u6307\u4ee4\u5982\u9f20\u6807\u70b9\u51fb\u7684\u6301\u7eed\u65f6\u95f4", None))
        self.label_7.setText(QCoreApplication.translate("Setting", u"\u6301\u7eed\u65f6\u95f4\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Setting", u"\u57fa\u7840\u8bbe\u7f6e", None))
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
        self.checkBox_3.setText(QCoreApplication.translate("Setting", u"\u7cfb\u7edf\u63d0\u793a\u97f3", None))
        self.pushButton.setText(QCoreApplication.translate("Setting", u"\u5e94\u7528", None))
        self.checkBox_4.setText(QCoreApplication.translate("Setting", u"\u4efb\u52a1\u5b8c\u6210\u540e\u663e\u793a\u4e3b\u7a97\u53e3", None))
        self.checkBox_2.setText(QCoreApplication.translate("Setting", u"\u6bcf\u6b21\u9000\u51fa\u63d0\u793a\u6e05\u7a7a\u6307\u4ee4", None))
        self.checkBox.setText(QCoreApplication.translate("Setting", u"\u6bcf\u6b21\u542f\u52a8\u68c0\u67e5\u66f4\u65b0", None))
        self.pushButton_3.setText(QCoreApplication.translate("Setting", u"\u6062\u590d\u81f3\u9ed8\u8ba4", None))
        self.checkBox_5.setText(QCoreApplication.translate("Setting", u"\u9ad8\u5206\u8fa8\u7387\u5c4f\u5e55\u81ea\u9002\u5e94", None))
    # retranslateUi

