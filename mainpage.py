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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

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
        self.widget.setGeometry(QRect(10, 20, 121, 571))
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
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 360, 101, 70))
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

        self.verticalLayoutWidget_7 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 440, 101, 80))
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

        self.gridLayoutWidget_3 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 90, 170, 251))
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
        self.lineEdit_8.setCursor(QCursor(Qt.ArrowCursor))
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
        self.comboBox_3.setStyleSheet(u"color: rgb(147, 163, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout_3.addWidget(self.comboBox_3, 7, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 20, 51, 16))
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 40, 91, 21))
        self.label_33.setStyleSheet(u"color: rgb(85, 170, 127);\n"
"font-weight: bold;\n"
"font-size: 20px;")
        self.graphicsView_3 = QGraphicsView(self.groupBox_3)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(80, 0, 31, 31))
        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(180, 30, 691, 551))
        self.verticalLayout_8 = QVBoxLayout(self.widget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.widget1)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 18px;")

        self.verticalLayout_8.addWidget(self.label_34)

        self.tableView_2 = QTableView(self.widget1)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.tableView_2)

        self.label_35 = QLabel(self.widget1)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 18px;")

        self.verticalLayout_8.addWidget(self.label_35)

        self.tableView_3 = QTableView(self.widget1)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setStyleSheet(u"color: rgb(255, 255, 255);")

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
        self.label_24.setText(QCoreApplication.translate("Form", u"\u914d\u9001\u65b9\u6cd5", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"EMS", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"ePacket", None))
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
        self.label_33.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"EMS", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"ePacket", None))
    # retranslateUi

