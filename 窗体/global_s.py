# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'global_s.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Global(object):
    def setupUi(self, Global):
        Global.setObjectName("Global")
        Global.resize(550, 380)
        font = QtGui.QFont()
        font.setFamily("黑体")
        Global.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Global.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Global)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Global)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Global)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Global)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        self.listView = QtWidgets.QListView(Global)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 1, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_2 = QtWidgets.QLabel(Global)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(Global)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Global)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.listView_2 = QtWidgets.QListView(Global)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_3.addWidget(self.listView_2, 1, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_10 = QtWidgets.QPushButton(Global)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(Global)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.listView_5 = QtWidgets.QListView(Global)
        self.listView_5.setObjectName("listView_5")
        self.gridLayout.addWidget(self.listView_5, 1, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(Global)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Global)
        QtCore.QMetaObject.connectSlotsByName(Global)

    def retranslateUi(self, Global):
        _translate = QtCore.QCoreApplication.translate
        Global.setWindowTitle(_translate("Global", "全局参数"))
        self.label.setText(_translate("Global", "图像文件夹路径："))
        self.pushButton_2.setText(_translate("Global", "删除"))
        self.pushButton.setText(_translate("Global", "选择文件夹"))
        self.label_2.setText(_translate("Global", "工作簿路径："))
        self.pushButton_4.setText(_translate("Global", "删除"))
        self.pushButton_3.setText(_translate("Global", "选择工作簿"))
        self.pushButton_10.setText(_translate("Global", "删除"))
        self.pushButton_9.setText(_translate("Global", "选择文件"))
        self.label_5.setText(_translate("Global", "扩展程序："))
import images_rc
