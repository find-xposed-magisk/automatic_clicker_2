# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QSplitter,
    QTableView, QTableWidget, QTableWidgetItem, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 679)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u56fe\u6807.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        icon1 = QIcon()
        icon1.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u5173\u4e8e.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionabout.setIcon(icon1)
        self.actionj = QAction(MainWindow)
        self.actionj.setObjectName(u"actionj")
        icon2 = QIcon()
        icon2.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u66f4\u65b0.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionj.setIcon(icon2)
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        icon3 = QIcon()
        icon3.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u5e2e\u52a9.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionhelp.setIcon(icon3)
        self.actionb = QAction(MainWindow)
        self.actionb.setObjectName(u"actionb")
        icon4 = QIcon()
        icon4.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u4fdd\u5b58.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionb.setIcon(icon4)
        self.setting = QAction(MainWindow)
        self.setting.setObjectName(u"setting")
        icon5 = QIcon()
        icon5.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u8bbe\u7f6e.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting.setIcon(icon5)
        self.actionf = QAction(MainWindow)
        self.actionf.setObjectName(u"actionf")
        icon6 = QIcon()
        icon6.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u5bfc\u5165\u6307\u4ee4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionf.setIcon(icon6)
        self.actions_2 = QAction(MainWindow)
        self.actions_2.setObjectName(u"actions_2")
        self.actions_2.setIcon(icon5)
        self.actiong = QAction(MainWindow)
        self.actiong.setObjectName(u"actiong")
        self.actiong.setCheckable(True)
        self.actiong.setChecked(False)
        self.actiona = QAction(MainWindow)
        self.actiona.setObjectName(u"actiona")
        self.actiona.setIcon(icon4)
        self.actionk = QAction(MainWindow)
        self.actionk.setObjectName(u"actionk")
        self.actionk.setIcon(icon3)
        self.actionx = QAction(MainWindow)
        self.actionx.setObjectName(u"actionx")
        self.actionx.setIcon(icon4)
        self.actionceui_1 = QAction(MainWindow)
        self.actionceui_1.setObjectName(u"actionceui_1")
        self.actiondh = QAction(MainWindow)
        self.actiondh.setObjectName(u"actiondh")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.lineEdit_22 = QLineEdit(self.centralwidget)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMaximumSize(QSize(220, 16777215))

        self.verticalLayout_43.addWidget(self.lineEdit_22)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem5)
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        self.treeWidget.setMinimumSize(QSize(150, 0))
        self.treeWidget.setMaximumSize(QSize(220, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.treeWidget.setFont(font1)
        self.treeWidget.setStyleSheet(u"")

        self.verticalLayout_43.addWidget(self.treeWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_43)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.tableWidget = QTableWidget(self.splitter)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush2 = QBrush(QColor(0, 0, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(0, 0, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        brush5 = QBrush(QColor(0, 0, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.tableWidget.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.tableWidget.setFont(font3)
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setRowCount(0)
        self.splitter.addWidget(self.tableWidget)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableView = QTableView(self.splitter)
        self.tableView.setObjectName(u"tableView")
        self.splitter.addWidget(self.tableView)

        self.verticalLayout.addWidget(self.splitter)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.layoutWidget1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        palette1 = QPalette()
        brush6 = QBrush(QColor(255, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.groupBox_3.setPalette(palette1)
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setBold(True)
        self.groupBox_3.setFont(font4)
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(True)
        palette2 = QPalette()
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        brush8 = QBrush(QColor(249, 249, 249, 77))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        brush9 = QBrush(QColor(0, 0, 0, 92))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        self.radioButton_2.setPalette(palette2)
        self.radioButton_2.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_2, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush10 = QBrush(QColor(255, 0, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        brush11 = QBrush(QColor(255, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        brush12 = QBrush(QColor(255, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.spinBox.setPalette(palette3)
        font5 = QFont()
        font5.setFamilies([u"SimSun"])
        font5.setBold(True)
        self.spinBox.setFont(font5)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(1000000)
        self.spinBox.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spinBox, 0, 1, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        self.radioButton.setPalette(palette4)

        self.gridLayout_3.addWidget(self.radioButton, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei"])
        font6.setBold(True)
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: red;\n"
"    color: white;\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    font-family: 'Microsoft YaHei'; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u5fae\u8f6f\u96c5\u9ed1 */\n"
"    padding: 3px 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd\uff0c\u4f7f\u6309\u94ae\u770b\u8d77\u6765\u66f4\u7f8e\u89c2 */\n"
"border: 2px solid transparent; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u900f\u660e */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0); /* \u8bbe\u7f6e\u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 127); /* \u8bbe\u7f6e\u6309\u94ae\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font4)

        self.gridLayout_4.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font4)

        self.gridLayout_4.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: red;\n"
"    color: white;\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    font-family: 'Microsoft YaHei'; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u5fae\u8f6f\u96c5\u9ed1 */\n"
"    padding: 3px 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd\uff0c\u4f7f\u6309\u94ae\u770b\u8d77\u6765\u66f4\u7f8e\u89c2 */\n"
"border: 2px solid transparent; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u900f\u660e */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0); /* \u8bbe\u7f6e\u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 127); /* \u8bbe\u7f6e\u6309\u94ae\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_5, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.splitter_2.addWidget(self.layoutWidget1)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u5220\u9664.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.groupBox_2)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        font7 = QFont()
        font7.setFamilies([u"Microsoft YaHei UI"])
        font7.setPointSize(9)
        self.tableWidget_2.setFont(font7)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget_2, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon8 = QIcon()
        icon8.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon8)

        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.tableWidget_3 = QTableWidget(self.groupBox_4)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tableWidget_3, 0, 0, 1, 2)

        self.pushButton_12 = QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon8)

        self.gridLayout_2.addWidget(self.pushButton_12, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon7)

        self.gridLayout_2.addWidget(self.pushButton_13, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.splitter_2.addWidget(self.layoutWidget)

        self.horizontalLayout.addWidget(self.splitter_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1121, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_5 = QMenu(self.menu)
        self.menu_5.setObjectName(u"menu_5")
        self.menuzv = QMenu(self.menu)
        self.menuzv.setObjectName(u"menuzv")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionf)
        self.menu.addAction(self.menuzv.menuAction())
        self.menu_5.addAction(self.actiona)
        self.menu_2.addAction(self.actionabout)
        self.menu_2.addAction(self.actionj)
        self.menu_2.addAction(self.actionhelp)
        self.menu_2.addAction(self.actionk)
        self.menu_4.addAction(self.actions_2)
        self.menu_3.addAction(self.actiong)
        self.toolBar.addAction(self.actionx)
        self.toolBar.addAction(self.actionf)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actions_2)
        self.toolBar.addAction(self.actionhelp)
        self.toolBar.addAction(self.actionj)
        self.toolBar.addAction(self.actionabout)

        self.retranslateUi(MainWindow)
        self.actiong.toggled.connect(self.toolBar.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clicker", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.actionj.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.actionb.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3aDB", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.actionf.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6307\u4ee4", None))
#if QT_CONFIG(shortcut)
        self.actionf.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actions_2.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(shortcut)
        self.actions_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actiong.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u680f", None))
        self.actiona.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u4fdd\u5b58\u4e3aExcel", None))
#if QT_CONFIG(shortcut)
        self.actiona.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionk.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u952e\u8bf4\u660e", None))
        self.actionx.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.actionx.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionceui_1.setText(QCoreApplication.translate("MainWindow", u"ceui_1", None))
        self.actiondh.setText(QCoreApplication.translate("MainWindow", u"dh", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6307\u4ee4...", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\u9009\u62e9", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u952e\u9f20\u6307\u4ee4", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u70b9\u51fb", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u591a\u56fe\u70b9\u51fb", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u5750\u6807\u70b9\u51fb", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u9f20\u6807", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u9f20\u6807\u70b9\u51fb", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u6eda\u8f6e\u6ed1\u52a8", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem1.child(6)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u6309\u4e0b\u952e\u76d8", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem1.child(7)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u6587\u672c\u8f93\u5165", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem1.child(8)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u4e2d\u952e\u6fc0\u6d3b", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem1.child(9)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u9f20\u6807\u62d6\u62fd", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem1.child(10)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u989c\u8272\u5224\u65ad", None));
        ___qtreewidgetitem13 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u7b49\u5f85", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u7b49\u5f85", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem13.child(1)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7b49\u5f85", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem13.child(2)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u5012\u8ba1\u65f6\u7a97\u53e3", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem13.child(3)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u6309\u952e\u7b49\u5f85", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem13.child(4)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u7126\u70b9\u7b49\u5f85", None));
        ___qtreewidgetitem19 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u53d8\u91cf", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u5224\u65ad", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem19.child(1)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u65f6\u95f4", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem19.child(2)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"\u83b7\u53d6Excel", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem19.child(3)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9f20\u6807\u4f4d\u7f6e", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem19.child(4)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u526a\u5207\u677f", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem19.child(5)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5bf9\u8bdd\u6846", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem19.child(6)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u6570\u5b57\u9a8c\u8bc1\u7801", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem19.child(7)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"OCR\u8bc6\u522b", None));
        ___qtreewidgetitem28 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"Excel\u6307\u4ee4", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem28.child(0)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"\u5199\u5165\u5355\u5143\u683c", None));
        ___qtreewidgetitem30 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u6307\u4ee4", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem30.child(0)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u7f51\u5740", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem30.child(1)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"\u5143\u7d20\u63a7\u5236", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem30.child(2)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u5f55\u5165", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem30.child(3)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"\u5207\u6362frame", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem30.child(4)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8868\u683c", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem30.child(5)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"\u62d6\u52a8\u5143\u7d20", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem30.child(6)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"\u5207\u6362\u7a97\u53e3", None));
        ___qtreewidgetitem38 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"\u5fae\u4fe1", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem38.child(0)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6d88\u606f", None));
        ___qtreewidgetitem40 = self.treeWidget.topLevelItem(6)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem40.child(0)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("MainWindow", u"\u8fd0\u884cPython", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem40.child(1)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("MainWindow", u"\u8fd0\u884ccmd", None));
        ___qtreewidgetitem43 = ___qtreewidgetitem40.child(2)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u5916\u90e8\u6587\u4ef6", None));
        ___qtreewidgetitem44 = ___qtreewidgetitem40.child(3)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u63a7\u5236", None));
        ___qtreewidgetitem45 = ___qtreewidgetitem40.child(4)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u5f55\u5165", None));
        ___qtreewidgetitem46 = ___qtreewidgetitem40.child(5)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u622a\u56fe", None));
        ___qtreewidgetitem47 = ___qtreewidgetitem40.child(6)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("MainWindow", u"\u63d0\u793a\u97f3", None));
        ___qtreewidgetitem48 = ___qtreewidgetitem40.child(7)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u901a\u77e5", None));
        ___qtreewidgetitem49 = ___qtreewidgetitem40.child(8)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("MainWindow", u"\u63d0\u793a\u7a97\u53e3", None));
        ___qtreewidgetitem50 = self.treeWidget.topLevelItem(7)
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("MainWindow", u"\u6d41\u7a0b\u63a7\u5236", None));
        ___qtreewidgetitem51 = ___qtreewidgetitem50.child(0)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c\u5206\u652f", None));
        ___qtreewidgetitem52 = ___qtreewidgetitem50.child(1)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u6d41\u7a0b", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\u96c6\u5408", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6d41\u7a0b\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u6d41\u7a0b", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u952e\u9f20\u6307\u4ee4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5206\u652f\u5904\u7406", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\u5907\u6ce8", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u590d", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u590d\u6b21\u6570\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u9650\u5faa\u73af", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8d44\u6e90\u6587\u4ef6\u5939", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c/\u6062\u590d", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u4efb\u52a1\uff08F11\uff09", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u6d41\u7a0b\uff08shift+1\uff09", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8fd0\u884c\uff08F10\uff09", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6d41\u7a0b", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u79fb", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u6d41\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u952e", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u590d\u6b21\u6570", None));
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u79fb", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5168\u5c40\u53d8\u91cf", None))
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u53d8\u91cf", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.menuzv.setTitle(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u6253\u5f00", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

