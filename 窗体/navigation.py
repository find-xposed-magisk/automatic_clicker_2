# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'navigation.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_navigation(object):
    def setupUi(self, navigation):
        navigation.setObjectName("navigation")
        navigation.resize(392, 434)
        font = QtGui.QFont()
        font.setFamily("黑体")
        navigation.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        navigation.setWindowIcon(icon)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(navigation)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(navigation)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.tab)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 0, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.tab)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout.addWidget(self.comboBox_8, 0, 1, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setEnabled(False)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab_3)
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_6.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_6.addWidget(self.checkBox, 0, 0, 1, 2)
        self.verticalLayout_5.addLayout(self.gridLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_8.addWidget(self.label_25)
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_6)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_8.addWidget(self.label_26)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_5, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.textEdit = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_8.addWidget(self.textEdit)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_24 = QtWidgets.QLabel(self.tab_7)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.tab_7)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.label_31 = QtWidgets.QLabel(self.tab_7)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_7.addWidget(self.label_31)
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_16.addWidget(self.pushButton_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_30 = QtWidgets.QLabel(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_30.setPalette(palette)
        self.label_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_30.setLineWidth(1)
        self.label_30.setTextFormat(QtCore.Qt.PlainText)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_16.addWidget(self.label_30)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.radioButton = QtWidgets.QRadioButton(self.tab_8)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_13.addWidget(self.radioButton)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.tab_8)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_9.addWidget(self.label_27)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_8)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(999)
        self.spinBox_3.setProperty("value", 10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_9.addWidget(self.spinBox_3)
        self.label_28 = QtWidgets.QLabel(self.tab_8)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_9.addWidget(self.label_28)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_14.setSpacing(20)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_8)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_14.addWidget(self.radioButton_2)
        self.label_29 = QtWidgets.QLabel(self.tab_8)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_14.addWidget(self.label_29)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_9)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_32 = QtWidgets.QLabel(self.tab_9)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_17.addWidget(self.label_32)
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_7)
        self.verticalLayout_17.addLayout(self.horizontalLayout_17)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem7)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tab_10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_37 = QtWidgets.QLabel(self.tab_10)
        self.label_37.setObjectName("label_37")
        self.gridLayout_7.addWidget(self.label_37, 0, 0, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_14.setObjectName("comboBox_14")
        self.gridLayout_7.addWidget(self.comboBox_14, 3, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_7.addWidget(self.checkBox_3, 5, 0, 1, 2)
        self.label_41 = QtWidgets.QLabel(self.tab_10)
        self.label_41.setObjectName("label_41")
        self.gridLayout_7.addWidget(self.label_41, 4, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.tab_10)
        self.label_39.setObjectName("label_39")
        self.gridLayout_7.addWidget(self.label_39, 2, 0, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout_7.addWidget(self.comboBox_12, 0, 1, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_7.addWidget(self.comboBox_13, 1, 1, 1, 1)
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_15.setObjectName("comboBox_15")
        self.gridLayout_7.addWidget(self.comboBox_15, 4, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.tab_10)
        self.label_38.setObjectName("label_38")
        self.gridLayout_7.addWidget(self.label_38, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_7.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab_10)
        self.label_40.setObjectName("label_40")
        self.gridLayout_7.addWidget(self.label_40, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 6, 0, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout_7)
        self.tabWidget.addTab(self.tab_10, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_21 = QtWidgets.QLabel(navigation)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(navigation)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(navigation)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 1, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(navigation)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 1, 2, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(navigation)
        self.comboBox_11.setEnabled(False)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_5.addWidget(self.comboBox_11, 1, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(navigation)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 0, 2, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(navigation)
        self.comboBox_10.setEnabled(False)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_5.addWidget(self.comboBox_10, 1, 1, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(navigation)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_9, 0, 3, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_2 = QtWidgets.QPushButton(navigation)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_14.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(navigation)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_14.addWidget(self.pushButton_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.retranslateUi(navigation)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.pushButton_3.clicked.connect(navigation.close) # type: ignore
        self.checkBox.toggled['bool'].connect(self.lineEdit_2.setDisabled) # type: ignore
        self.checkBox.toggled['bool'].connect(self.dateTimeEdit.setEnabled) # type: ignore
        self.checkBox.toggled['bool'].connect(self.comboBox_6.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(navigation)

    def retranslateUi(self, navigation):
        _translate = QtCore.QCoreApplication.translate
        navigation.setWindowTitle(_translate("navigation", "导航页"))
        self.label.setText(_translate("navigation", "操作说明：将图像统一保存至某文件夹，点击添加文件夹即可。在图像名称中选择对应的图像，再在指令中选择指令。"))
        self.label_2.setText(_translate("navigation", "当前文件夹："))
        self.label_3.setText(_translate("navigation", "暂无"))
        self.label_5.setText(_translate("navigation", "指令名称："))
        self.checkBox_2.setText(_translate("navigation", "匹配不到指定图像时自动略过该指令"))
        self.comboBox_2.setItemText(0, _translate("navigation", "左键单击"))
        self.comboBox_2.setItemText(1, _translate("navigation", "左键双击"))
        self.comboBox_2.setItemText(2, _translate("navigation", "右键单击"))
        self.comboBox_2.setItemText(3, _translate("navigation", "右键双击"))
        self.label_4.setText(_translate("navigation", "图像名称："))
        self.label_36.setText(_translate("navigation", "文件夹名称："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("navigation", "图像识别"))
        self.label_11.setText(_translate("navigation", "指令名称："))
        self.label_6.setText(_translate("navigation", "操作说明：按下获取鼠标位置按钮并拖动鼠标，即可显示鼠标当前的位置。"))
        self.pushButton_4.setText(_translate("navigation", "获取坐标"))
        self.label_7.setText(_translate("navigation", "X："))
        self.label_9.setText(_translate("navigation", "0"))
        self.label_8.setText(_translate("navigation", "Y："))
        self.label_10.setText(_translate("navigation", "0"))
        self.comboBox_3.setItemText(0, _translate("navigation", "左键单击"))
        self.comboBox_3.setItemText(1, _translate("navigation", "左键双击"))
        self.comboBox_3.setItemText(2, _translate("navigation", "右键单击"))
        self.comboBox_3.setItemText(3, _translate("navigation", "右键双击"))
        self.comboBox_3.setItemText(4, _translate("navigation", "左键（自定义次数）"))
        self.label_22.setText(_translate("navigation", "自定义次数："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("navigation", "坐标点击"))
        self.label_12.setText(_translate("navigation", "移动方向："))
        self.comboBox_4.setItemText(0, _translate("navigation", "→"))
        self.comboBox_4.setItemText(1, _translate("navigation", "←"))
        self.comboBox_4.setItemText(2, _translate("navigation", "↑"))
        self.comboBox_4.setItemText(3, _translate("navigation", "↓"))
        self.label_13.setText(_translate("navigation", "移动距离（像素）："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("navigation", "移动鼠标"))
        self.label_23.setText(_translate("navigation", "操作说明：当选择等待时长并输入秒数后，该指定会停止对应的秒数。当选择启用定时后，该指令会停止到指定的时间退出，再继续执行后续的其他指令操作。"))
        self.label_14.setText(_translate("navigation", "等待时长（秒）："))
        self.dateTimeEdit.setDisplayFormat(_translate("navigation", "yyyy/M/d H:mm:ss"))
        self.label_15.setText(_translate("navigation", "等待至指定时间："))
        self.checkBox.setText(_translate("navigation", "启用定时功能"))
        self.label_25.setText(_translate("navigation", "每"))
        self.comboBox_6.setCurrentText(_translate("navigation", "1000"))
        self.comboBox_6.setItemText(0, _translate("navigation", "1000"))
        self.comboBox_6.setItemText(1, _translate("navigation", "500"))
        self.comboBox_6.setItemText(2, _translate("navigation", "200"))
        self.comboBox_6.setItemText(3, _translate("navigation", "100"))
        self.comboBox_6.setItemText(4, _translate("navigation", "50"))
        self.comboBox_6.setItemText(5, _translate("navigation", "10"))
        self.label_26.setText(_translate("navigation", "毫秒检测一次当前时间"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("navigation", "等待"))
        self.label_16.setText(_translate("navigation", "滚动方向："))
        self.comboBox_5.setItemText(0, _translate("navigation", "↑"))
        self.comboBox_5.setItemText(1, _translate("navigation", "↓"))
        self.label_17.setText(_translate("navigation", "滚动距离（像素）："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("navigation", "滚轮"))
        self.label_18.setText(_translate("navigation", "文本内容："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("navigation", "文本输入"))
        self.label_24.setText(_translate("navigation", "操作说明：鼠标点击按钮后再按下对应的按键即可。支持单键或多键组合。鼠标点击后不要再次点击，否则窗口会失去响应。"))
        self.label_19.setText(_translate("navigation", "按下"))
        self.label_31.setText(_translate("navigation", "暂无"))
        self.label_20.setText(_translate("navigation", "按键"))
        self.pushButton_6.setText(_translate("navigation", "点击此处再按下按键"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("navigation", "键盘指令"))
        self.label_30.setText(_translate("navigation", "重要提示：当选择此指令时，请在主界面中打开“无限循环”功能，否则此指令指挥被执行有限次数。"))
        self.radioButton.setText(_translate("navigation", "模拟点击："))
        self.label_27.setText(_translate("navigation", "当鼠标中键按下时，模拟鼠标左键点击"))
        self.label_28.setText(_translate("navigation", "次"))
        self.radioButton_2.setText(_translate("navigation", "自定义："))
        self.label_29.setText(_translate("navigation", "当鼠标中键按下时，自动执行该指令后续的所有指令"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("navigation", "中键激活"))
        self.label_32.setText(_translate("navigation", "鼠标在当前位置执行："))
        self.comboBox_7.setItemText(0, _translate("navigation", "左键单击"))
        self.comboBox_7.setItemText(1, _translate("navigation", "左键双击"))
        self.comboBox_7.setItemText(2, _translate("navigation", "右键单击"))
        self.comboBox_7.setItemText(3, _translate("navigation", "右键双击"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("navigation", "鼠标点击"))
        self.label_37.setText(_translate("navigation", "Excel工作簿名称："))
        self.checkBox_3.setText(_translate("navigation", "单元格行号自动递增"))
        self.label_41.setText(_translate("navigation", "图像名称："))
        self.label_39.setText(_translate("navigation", "单元格："))
        self.label_38.setText(_translate("navigation", "工作表名："))
        self.label_40.setText(_translate("navigation", "图像文件夹路径："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("navigation", "信息录入"))
        self.label_21.setText(_translate("navigation", "重复次数："))
        self.label_34.setText(_translate("navigation", "分支名称："))
        self.label_35.setText(_translate("navigation", "扩展程序："))
        self.label_33.setText(_translate("navigation", "异常处理："))
        self.comboBox_9.setItemText(0, _translate("navigation", "自动跳过"))
        self.comboBox_9.setItemText(1, _translate("navigation", "抛出异常并暂停"))
        self.comboBox_9.setItemText(2, _translate("navigation", "抛出异常并停止"))
        self.pushButton_2.setText(_translate("navigation", "添加指令"))
        self.pushButton_3.setText(_translate("navigation", "取消"))
import images_rc
