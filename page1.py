# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page1.ui'
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
    QLabel, QLineEdit, QMainWindow, QRadioButton,
    QSizePolicy, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 580)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 580))
        MainWindow.setBaseSize(QSize(900, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(47, 47, 47);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 121, 571))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, -10, 121, 531))
        self.groupBox.setStyleSheet(u"border: none;")
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 360, 101, 70))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_9)

        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 440, 101, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_5)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 111, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setStyleSheet(u"color: rgb(147, 163, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"height: 20px;")

        self.gridLayout.addWidget(self.comboBox, 7, 0, 1, 1)

        self.lineEdit.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 20, 51, 16))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 40, 91, 21))
        self.label_11.setStyleSheet(u"color: rgb(85, 170, 127);\n"
"font-weight: bold;\n"
"font-size: 20px;")
        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(80, 0, 31, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(130, 0, 20, 167772))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setMinimumSize(QSize(0, 167772))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(159, 29, 721, 531))
        self.groupBox_2.setStyleSheet(u"border: none;\n"
"")
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 9, 701, 521))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.tableView = QTableView(self.verticalLayoutWidget_3)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8868\u793a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u30c7\u30d5\u30a9\u30eb\u30c8", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8a73\u7d30", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u914d\u9001\u65b9\u6cd5", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"EMS", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"ePacket", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4ed5\u5165\u308c\u5024(\u5186)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u30ab\u30c6\u30b4\u30ea", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8ca9\u58f2\u4fa1\u683c($)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5186", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u91cf(g)", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u672c\u3068\u96d1\u8a8c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\"\u6620\u753b&\u30c6\u30ec\u30d3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u97f3\u697d", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5730\u91d1", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u30ec\u30c7\u30a3\u30fc\u30b9\u30d0\u30c3\u30b0&\u30cf\u30f3\u30c9\u30d0\u30c3\u30b0", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u30b8\u30e5\u30a8\u30ea\u30fc&\u8155\u6642\u8a08", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u8155\u6642\u8a08\u3001\u90e8\u54c1&\u4ed8\u5c5e\u54c1", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u30ae\u30bf\u30fc&\u30d9\u30fc\u30b9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u30b9\u30dd\u30fc\u30c4\u30b7\u30e5\u30fc\u30ba", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\u305d\u306e\u4ed6", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"USDJPY", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_2.setTitle("")
    # retranslateUi

