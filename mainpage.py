# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QSize(900, 600))
        Form.setStyleSheet(u"background-color: rgb(47, 47, 47);")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(140, -40, 20, 167772))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QSize(0, 167772))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 121, 581))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(-10, -20, 121, 531))
        self.groupBox_3.setStyleSheet(u"border: none;")
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 420, 101, 70))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.verticalLayoutWidget_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_23)

        self.radioButton_5 = QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.radioButton_6)

        self.gridLayoutWidget_3 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 100, 170, 251))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy1.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy1)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout_3.addWidget(self.lineEdit_7, 5, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_25, 1, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_3)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_26, 5, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_3)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_27, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout_3.addWidget(self.lineEdit_8, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy1.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy1)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout_3.addWidget(self.lineEdit_9, 3, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_3)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_28, 6, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_3)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_3)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_30, 3, 1, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_3)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_31, 4, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.comboBox_3.setPalette(palette)
        self.comboBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"height: 20px;")
        self.comboBox_3.setMinimumContentsLength(0)

        self.gridLayout_3.addWidget(self.comboBox_3, 7, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 40, 51, 16))
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 60, 91, 21))
        self.label_33.setStyleSheet(u"color: rgb(85, 170, 127);\n"
"font-weight: bold;\n"
"font-size: 20px;")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 380, 75, 24))
        font = QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"border-radius: 4px;\n"
"color: rgb(255, 255, 255);")
        self.koushin = QLabel(self.groupBox_3)
        self.koushin.setObjectName(u"koushin")
        self.koushin.setGeometry(QRect(100, 20, 30, 30))
        sizePolicy1.setHeightForWidth(self.koushin.sizePolicy().hasHeightForWidth())
        self.koushin.setSizePolicy(sizePolicy1)
        self.koushin.setMinimumSize(QSize(30, 30))
        self.koushin.setMaximumSize(QSize(30, 30))
        self.verticalLayoutWidget_7 = QWidget(self.widget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 480, 101, 80))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.verticalLayoutWidget_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_24)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.checkBox_6)

        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 30, 691, 551))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.layoutWidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 18px;")

        self.verticalLayout_8.addWidget(self.label_34)

        self.tableView_2 = QTableView(self.layoutWidget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setFocusPolicy(Qt.NoFocus)
        self.tableView_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.tableView_2.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));")
        self.tableView_2.setFrameShadow(QFrame.Plain)
        self.tableView_2.setAutoScroll(True)
        self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_2.setTabKeyNavigation(False)
        self.tableView_2.setProperty("showDropIndicator", False)
        self.tableView_2.setDragDropOverwriteMode(False)
        self.tableView_2.horizontalHeader().setVisible(True)
        self.tableView_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView_2.horizontalHeader().setHighlightSections(False)
        self.tableView_2.verticalHeader().setVisible(True)
        self.tableView_2.verticalHeader().setHighlightSections(False)

        self.verticalLayout_8.addWidget(self.tableView_2)

        self.label_35 = QLabel(self.layoutWidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 18px;")

        self.verticalLayout_8.addWidget(self.label_35)

        self.tableView_3 = QTableView(self.layoutWidget)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(47, 47, 47);")

        self.verticalLayout_8.addWidget(self.tableView_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_3.setTitle("")
        self.label_23.setText(QCoreApplication.translate("Form", u"\u8868\u793a", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u30c7\u30d5\u30a9\u30eb\u30c8", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"\u8a73\u7d30", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"$", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"g", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"\u4ed5\u5165\u308c\u5024(\u5186)", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u30ab\u30c6\u30b4\u30ea", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u8ca9\u58f2\u4fa1\u683c($)", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"\u5186", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u91cd\u91cf(g)", None))
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u672c\u3068\u96d1\u8a8c", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"\"\u6620\u753b&\u30c6\u30ec\u30d3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"\u97f3\u697d", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Form", u"\u5730\u91d1", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Form", u"\u30ec\u30c7\u30a3\u30fc\u30b9\u30d0\u30c3\u30b0&\u30cf\u30f3\u30c9\u30d0\u30c3\u30b0", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("Form", u"\u30b8\u30e5\u30a8\u30ea\u30fc&\u8155\u6642\u8a08", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("Form", u"\u8155\u6642\u8a08\u3001\u90e8\u54c1&\u4ed8\u5c5e\u54c1", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("Form", u"\u30ae\u30bf\u30fc&\u30d9\u30fc\u30b9", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("Form", u"\u30b9\u30dd\u30fc\u30c4\u30b7\u30e5\u30fc\u30ba", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("Form", u"\u305d\u306e\u4ed6", None))

        self.label_32.setText(QCoreApplication.translate("Form", u"USDJPY", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8a08\u7b97", None))
        self.koushin.setText("")
        self.label_24.setText(QCoreApplication.translate("Form", u"\u914d\u9001\u65b9\u6cd5", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"EMS", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"ePacket", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"EMS", None))
#if QT_CONFIG(tooltip)
        self.tableView_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("Form", u"ePacket", None))
    # retranslateUi

