# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(426, 604)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Setting.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Setting.setWindowIcon(icon)
        Setting.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Setting)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Setting)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.radioButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 4)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_2.setMaximum(1000)
        self.horizontalSlider_2.setSingleStep(100)
        self.horizontalSlider_2.setPageStep(100)
        self.horizontalSlider_2.setProperty("value", 200)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 0, 1, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(1000000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 4, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_3.setMaximum(1000)
        self.horizontalSlider_3.setSingleStep(100)
        self.horizontalSlider_3.setPageStep(100)
        self.horizontalSlider_3.setProperty("value", 200)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_2.addWidget(self.horizontalSlider_3, 2, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 3)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 253, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.gridLayout_6.addWidget(self.keySequenceEdit, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)
        self.keySequenceEdit_2 = QtWidgets.QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit_2.setObjectName("keySequenceEdit_2")
        self.gridLayout_6.addWidget(self.keySequenceEdit_2, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 2, 0, 1, 1)
        self.keySequenceEdit_3 = QtWidgets.QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit_3.setObjectName("keySequenceEdit_3")
        self.gridLayout_6.addWidget(self.keySequenceEdit_3, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 3, 0, 1, 1)
        self.keySequenceEdit_4 = QtWidgets.QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit_4.setObjectName("keySequenceEdit_4")
        self.gridLayout_6.addWidget(self.keySequenceEdit_4, 3, 1, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 239, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_7.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_7.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_7.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_7.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(Setting)
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(Setting)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Setting)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Setting)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setStyleSheet("")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(Setting)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(Setting)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.retranslateUi(Setting)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_6.setNum) # type: ignore
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_8.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "设置"))
        self.groupBox.setTitle(_translate("Setting", "模式"))
        self.radioButton.setText(_translate("Setting", "普通模式"))
        self.label.setText(_translate("Setting", "该模式较为稳定，参数适中，适合日常使用"))
        self.label_2.setText(_translate("Setting", "该模式进一步提高操作速度，取消所有操作时间间隔"))
        self.radioButton_2.setText(_translate("Setting", "极速模式"))
        self.groupBox_2.setTitle(_translate("Setting", "指令设置"))
        self.label_11.setText(_translate("Setting", "指鼠标双击的时间间隔"))
        self.label_12.setText(_translate("Setting", "指每完成一次指令至下一次指令开始的时间间隔"))
        self.label_9.setText(_translate("Setting", "暂停时间："))
        self.label_8.setText(_translate("Setting", "毫秒"))
        self.label_6.setText(_translate("Setting", "毫秒"))
        self.label_10.setText(_translate("Setting", "毫秒"))
        self.label_5.setText(_translate("Setting", "时间间隔："))
        self.label_13.setText(_translate("Setting", "指执行指令如鼠标点击的持续时间"))
        self.label_7.setText(_translate("Setting", "持续时间："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Setting", "基础设置"))
        self.groupBox_3.setTitle(_translate("Setting", "百度OCR设置"))
        self.label_16.setText(_translate("Setting", "secretKey："))
        self.label_14.setText(_translate("Setting", "appId："))
        self.label_15.setText(_translate("Setting", "apiKey："))
        self.pushButton_2.setText(_translate("Setting", "前往网页"))
        self.groupBox_4.setTitle(_translate("Setting", "云码设置"))
        self.pushButton_4.setText(_translate("Setting", "前往网页"))
        self.label_18.setText(_translate("Setting", "Token："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Setting", "其他设置"))
        self.groupBox_5.setTitle(_translate("Setting", "全局快捷键"))
        self.label_17.setText(_translate("Setting", "开始运行："))
        self.label_19.setText(_translate("Setting", "结束运行："))
        self.label_20.setText(_translate("Setting", "分支选择："))
        self.label_21.setText(_translate("Setting", "暂停和恢复："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Setting", "快捷键"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Setting", "分支名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Setting", "快捷键"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Setting", "重复次数"))
        self.pushButton_5.setText(_translate("Setting", "上移"))
        self.pushButton_7.setText(_translate("Setting", "添加分支"))
        self.pushButton_6.setText(_translate("Setting", "下移"))
        self.pushButton_8.setText(_translate("Setting", "删除选中"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Setting", "分支管理"))
        self.checkBox_2.setText(_translate("Setting", "每次退出提示清空指令"))
        self.pushButton_3.setText(_translate("Setting", "恢复至默认"))
        self.pushButton.setText(_translate("Setting", "应用"))
        self.checkBox.setText(_translate("Setting", "每次启动检查更新"))
        self.checkBox_3.setText(_translate("Setting", "系统提示音"))
        self.checkBox_4.setText(_translate("Setting", "任务完成后显示主窗口"))
import images_rc
