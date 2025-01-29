# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolBar, QToolButton, QVBoxLayout,
    QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 521)
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
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(255, 0, 0, 128))
        brush1.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush2 = QBrush(QColor(255, 0, 0, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(255, 0, 0, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.tabWidget.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: #131313;\n"
"    color: #00ff00;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.textEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.toolButton_8 = QToolButton(self.tab)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setIcon(icon6)

        self.verticalLayout.addWidget(self.toolButton_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.toolButton_7 = QToolButton(self.tab)
        self.toolButton_7.setObjectName(u"toolButton_7")
        icon7 = QIcon()
        icon7.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u6e05\u9664.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_7.setIcon(icon7)

        self.verticalLayout.addWidget(self.toolButton_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.tab_2)
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
        palette1 = QPalette()
        brush5 = QBrush(QColor(0, 0, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(240, 240, 240, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        brush7 = QBrush(QColor(0, 0, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        brush8 = QBrush(QColor(0, 0, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        brush9 = QBrush(QColor(0, 0, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.tableWidget.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.tableWidget.setFont(font2)
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    alternate-background-color: #f0f0f0; /* \u8bbe\u7f6e\u4ea4\u66ff\u884c\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"")
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        palette2 = QPalette()
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label.setPalette(palette2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.toolButton_2 = QToolButton(self.tab_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon8 = QIcon()
        icon8.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_2.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.toolButton_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolButton = QToolButton(self.tab_2)
        self.toolButton.setObjectName(u"toolButton")
        icon9 = QIcon()
        icon9.addFile(u":/\u6309\u94ae\u56fe\u6807/\u7a97\u4f53/res/\u5220\u9664.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.toolButton)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setBold(True)
        self.pushButton_3.setFont(font3)
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

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(255, 255, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        brush12 = QBrush(QColor(255, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush13 = QBrush(QColor(255, 0, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        brush14 = QBrush(QColor(249, 249, 249, 77))
        brush14.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush15 = QBrush(QColor(0, 0, 0, 92))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush16 = QBrush(QColor(255, 0, 0, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.pushButton.setPalette(palette3)
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setIconSize(QSize(40, 20))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.groupBox_3.setPalette(palette4)
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setBold(True)
        self.groupBox_3.setFont(font5)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(True)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        self.radioButton_2.setPalette(palette5)
        self.radioButton_2.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        self.radioButton.setPalette(palette6)

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        brush17 = QBrush(QColor(255, 0, 0, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush18 = QBrush(QColor(255, 0, 0, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush19 = QBrush(QColor(255, 0, 0, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.spinBox.setPalette(palette7)
        font6 = QFont()
        font6.setFamilies([u"SimSun"])
        font6.setBold(True)
        self.spinBox.setFont(font6)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(1000000)
        self.spinBox.setDisplayIntegerBase(10)

        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        self.checkBox_2.setPalette(palette8)

        self.gridLayout_2.addWidget(self.checkBox_2, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.groupBox_4.setPalette(palette9)
        self.groupBox_4.setFont(font5)
        self.groupBox_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(9, 0, 9, 2)
        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font3)
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

        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 2)

        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font5)

        self.gridLayout_3.addWidget(self.pushButton_6, 3, 0, 1, 2)

        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font5)

        self.gridLayout_3.addWidget(self.pushButton_7, 2, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 430, 33))
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
        self.toolButton_7.clicked.connect(self.textEdit.clear)

        self.tabWidget.setCurrentIndex(0)


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
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528......", None))
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5904\u7406\u72b6\u6001", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u5206\u652f\uff1a", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5206\u652f", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5206\u652f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8d44\u6e90\u6587\u4ef6\u5939", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6307\u4ee4\uff08Ctrl+Enter\uff09", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\u96c6\u5408", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u590d\u6b21\u6570\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u9650\u5faa\u73af", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65f6\u9690\u85cf\u7a97\u53e3", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8fd0\u884c\uff08F10\uff09", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u4efb\u52a1\uff08F11\uff09", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c/\u6062\u590d", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5206\u652f\u8fd0\u884c\uff08shift+1\uff09", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.menuzv.setTitle(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u6253\u5f00", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

