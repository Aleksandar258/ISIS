# -*- coding: utf-8 -*-

# Form implementation generated from reading UI file 'gui.UI'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QColor
from UI.resource_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 766)
        MainWindow.setStyleSheet("margin: 0;\n"
"padding 0;\n"
"border: none;\n"
"font: 8pt \"Segoe UI\";;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.bgApp = QtWidgets.QFrame(self.centralwidget)
        self.bgApp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bgApp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgApp.setObjectName("bgApp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bgApp)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QFrame(self.bgApp)
        self.windowBar.setMinimumSize(QtCore.QSize(0, 0))
        self.windowBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.windowBar.setStyleSheet("background-color: rgb(41, 41, 61);\n"
"color: rgb(255, 255, 255);")
        self.windowBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.windowBar)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(13, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(14)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setMaximumSize(QtCore.QSize(40, 16777215))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/images/lightning2.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.logoTitle = QtWidgets.QLabel(self.frame)
        self.logoTitle.setStyleSheet("font: 9pt;")
        self.logoTitle.setObjectName("logoTitle")
        self.horizontalLayout_3.addWidget(self.logoTitle)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.windowBar)
        self.frame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(10, 7, 7, 7)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMin = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMin.sizePolicy().hasHeightForWidth())
        self.btnMin.setSizePolicy(sizePolicy)
        self.btnMin.setStyleSheet("QPushButton:hover {\n"
"           background-color:rgb(61, 61, 92);\n"
"        }")
        self.btnMin.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMin.setIcon(icon)
        self.btnMin.setObjectName("btnMin")
        self.horizontalLayout_2.addWidget(self.btnMin)
        self.btnMinMax = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMinMax.sizePolicy().hasHeightForWidth())
        self.btnMinMax.setSizePolicy(sizePolicy)
        self.btnMinMax.setStyleSheet("QPushButton:hover {\n"
"           background-color:rgb(61, 61, 92);\n"
"        }")
        self.btnMinMax.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinMax.setIcon(icon1)
        self.btnMinMax.setObjectName("btnMinMax")
        self.horizontalLayout_2.addWidget(self.btnMinMax)
        self.btnClose = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setToolTip("")
        self.btnClose.setToolTipDuration(-1)
        self.btnClose.setStyleSheet("QPushButton:hover {\n"
"            background-color: red;\n"
"        }")
        self.btnClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.windowBar)
        self.mainContent = QtWidgets.QFrame(self.bgApp)
        self.mainContent.setStyleSheet("QFrame {\n"
"    background-color: rgb(71, 71, 107);\n"
"    background-color: rgb(82, 82, 122);\n"
"}")
        self.mainContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainContent.setObjectName("mainContent")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainContent)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leftMenu = QtWidgets.QFrame(self.mainContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        self.leftMenu.setMinimumSize(QtCore.QSize(65, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.leftMenu.setStyleSheet("#leftMenu {\n"
"    background-color: rgb(25, 50, 77);\n"
"    background-color: rgb(51, 51, 77);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"    background-color: rgb(25, 50, 77);\n"
"    background-color: rgb(51, 51, 77);\n"
"    color: rgb(255, 255, 255);\n"
"    background-repeat:none;\n"
"    background-position:center left;\n"
"    border-left: 20px solid transparent;\n"
"    text-align: left;\n"
"    padding-left: 47px;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:hover {\n"
"    background-color: rgb(31, 63, 96);\n"
"}\n"
"\n"
"#leftMenu .QPushButton:pressed {    \n"
"    background-color: rgb(62, 128, 193);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.leftMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnHide = QtWidgets.QPushButton(self.leftMenu)
        self.btnHide.setMinimumSize(QtCore.QSize(0, 50))
        self.btnHide.setStyleSheet("background-image: url(:/icons/icons/align-justify.svg);\n"
"")
        self.btnHide.setObjectName("btnHide")
        self.verticalLayout_2.addWidget(self.btnHide)
        self.btnMenuLoadCSV = QtWidgets.QPushButton(self.leftMenu)
        self.btnMenuLoadCSV.setMinimumSize(QtCore.QSize(0, 50))
        self.btnMenuLoadCSV.setStyleSheet("background-image: url(:/icons/icons/database.svg);")
        self.btnMenuLoadCSV.setObjectName("btnMenuLoadCSV")
        self.verticalLayout_2.addWidget(self.btnMenuLoadCSV)
        self.btnMenuTrain = QtWidgets.QPushButton(self.leftMenu)
        self.btnMenuTrain.setMinimumSize(QtCore.QSize(0, 50))
        self.btnMenuTrain.setStyleSheet("background-image: url(:/icons/icons/dribbble.svg);")
        self.btnMenuTrain.setObjectName("btnMenuTrain")
        self.verticalLayout_2.addWidget(self.btnMenuTrain)
        self.btnMenuPredict = QtWidgets.QPushButton(self.leftMenu)
        self.btnMenuPredict.setMinimumSize(QtCore.QSize(0, 50))
        self.btnMenuPredict.setStyleSheet("background-image: url(:/icons/icons/eye.svg);")
        self.btnMenuPredict.setObjectName("btnMenuPredict")
        self.verticalLayout_2.addWidget(self.btnMenuPredict)
        self.btnMenuDisplay = QtWidgets.QPushButton(self.leftMenu)
        self.btnMenuDisplay.setMinimumSize(QtCore.QSize(0, 50))
        self.btnMenuDisplay.setStyleSheet("background-image: url(:/icons/icons/bar-chart-2.svg);")
        self.btnMenuDisplay.setObjectName("btnMenuDisplay")
        self.verticalLayout_2.addWidget(self.btnMenuDisplay)
        self.pushButton_13 = QtWidgets.QPushButton(self.leftMenu)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_13.setStyleSheet("background-image: url(:/icons/icons/tool.svg);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.leftMenu)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_14.setStyleSheet("background-image: url(:/icons/icons/monitor.svg);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.leftMenu)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_15.setStyleSheet("background-image: url(:/icons/icons/pie-chart.svg);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_2.addWidget(self.pushButton_15)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.leftMenu)
        self.frame_4 = QtWidgets.QFrame(self.mainContent)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("background-image: url(:/images/images/lightning2.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_3.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(51, 51, 65);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: center;\n"
"    \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 61, 75);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(62, 128, 193);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(50, 20, 50, -1)
        self.horizontalLayout_6.setSpacing(60)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnOpenCSV = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenCSV.sizePolicy().hasHeightForWidth())
        self.btnOpenCSV.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenCSV.setIcon(icon3)
        self.btnOpenCSV.setObjectName("btnOpenCSV")
        self.horizontalLayout_6.addWidget(self.btnOpenCSV)
        self.btnOpenFolder = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenFolder.sizePolicy().hasHeightForWidth())
        self.btnOpenFolder.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenFolder.setIcon(icon4)
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.horizontalLayout_6.addWidget(self.btnOpenFolder)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.page_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 450))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 450))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.circularProgressBarBaseCSV = QtWidgets.QFrame(self.frame_5)
        self.circularProgressBarBaseCSV.setMinimumSize(QtCore.QSize(0, 320))
        self.circularProgressBarBaseCSV.setMaximumSize(QtCore.QSize(0, 320))
        self.circularProgressBarBaseCSV.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBaseCSV.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBaseCSV.setObjectName("circularProgressBarBaseCSV")
        self.circularProgressCSV = QtWidgets.QFrame(self.circularProgressBarBaseCSV)
        self.circularProgressCSV.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgressCSV.setStyleSheet("QFrame {\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 170, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgressCSV.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressCSV.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressCSV.setObjectName("circularProgressCSV")
        self.circularBgCSV = QtWidgets.QFrame(self.circularProgressBarBaseCSV)
        self.circularBgCSV.setGeometry(QtCore.QRect(20, 20, 280, 280))
        self.circularBgCSV.setStyleSheet("QFrame {\n"
"    border-radius: 140px;\n"
"    background-color: rgb(50, 50, 80);\n"
"}")
        self.circularBgCSV.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBgCSV.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgCSV.setObjectName("circularBgCSV")
        self.layoutWidget = QtWidgets.QWidget(self.circularBgCSV)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 50, 171, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTopMessageCSV = QtWidgets.QLabel(self.layoutWidget)
        self.labelTopMessageCSV.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 14pt \"Perpetua Titling MT\";")
        self.labelTopMessageCSV.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTopMessageCSV.setObjectName("labelTopMessageCSV")
        self.gridLayout.addWidget(self.labelTopMessageCSV, 0, 0, 1, 1)
        self.labelPercentagesCSV = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.labelPercentagesCSV.setFont(font)
        self.labelPercentagesCSV.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Arial Narrow\";")
        self.labelPercentagesCSV.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentagesCSV.setObjectName("labelPercentagesCSV")
        self.gridLayout.addWidget(self.labelPercentagesCSV, 1, 0, 1, 1)
        self.labelBottomMessageCSV = QtWidgets.QLabel(self.layoutWidget)
        self.labelBottomMessageCSV.setStyleSheet("QLabel {\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(60, 60, 97);\n"
"    margin-left: 20px;\n"
"    margin-right: 20px;\n"
"}")
        self.labelBottomMessageCSV.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBottomMessageCSV.setObjectName("labelBottomMessageCSV")
        self.gridLayout.addWidget(self.labelBottomMessageCSV, 2, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.circularProgressBarBaseCSV)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelOpenCSVMessage = QtWidgets.QLabel(self.frame_6)
        self.labelOpenCSVMessage.setMaximumSize(QtCore.QSize(0, 16777215))
        self.labelOpenCSVMessage.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.labelOpenCSVMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOpenCSVMessage.setObjectName("labelOpenCSVMessage")
        self.horizontalLayout_8.addWidget(self.labelOpenCSVMessage, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.page_3)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_9.setStyleSheet("QLabel {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 170, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(61, 61, 75);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/icons/chevron-down.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_2.setContentsMargins(150, -1, 150, -1)
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.cmb2DateTrain = QtWidgets.QComboBox(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb2DateTrain.sizePolicy().hasHeightForWidth())
        self.cmb2DateTrain.setSizePolicy(sizePolicy)
        self.cmb2DateTrain.setObjectName("cmb2DateTrain")
        self.verticalLayout_5.addWidget(self.cmb2DateTrain)
        self.gridLayout_2.addWidget(self.frame_11, 0, 1, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.cmb1DateTrain = QtWidgets.QComboBox(self.frame_10)
        self.cmb1DateTrain.setObjectName("cmb1DateTrain")
        self.verticalLayout_6.addWidget(self.cmb1DateTrain)
        self.gridLayout_2.addWidget(self.frame_10, 0, 0, 1, 1)
        self.btnGoTrain = QtWidgets.QPushButton(self.frame_9)
        self.btnGoTrain.setMinimumSize(QtCore.QSize(70, 40))
        self.btnGoTrain.setMaximumSize(QtCore.QSize(70, 40))
        self.btnGoTrain.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGoTrain.setIcon(icon5)
        self.btnGoTrain.setObjectName("btnGoTrain")
        self.gridLayout_2.addWidget(self.btnGoTrain, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 450))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 450))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.circularProgressBarBaseTrain = QtWidgets.QFrame(self.frame_8)
        self.circularProgressBarBaseTrain.setMinimumSize(QtCore.QSize(0, 320))
        self.circularProgressBarBaseTrain.setMaximumSize(QtCore.QSize(0, 320))
        self.circularProgressBarBaseTrain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBaseTrain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBaseTrain.setObjectName("circularProgressBarBaseTrain")
        self.circularProgressTrain = QtWidgets.QFrame(self.circularProgressBarBaseTrain)
        self.circularProgressTrain.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgressTrain.setStyleSheet("QFrame {\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 170, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgressTrain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressTrain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressTrain.setObjectName("circularProgressTrain")
        self.circularBgTrain = QtWidgets.QFrame(self.circularProgressBarBaseTrain)
        self.circularBgTrain.setGeometry(QtCore.QRect(20, 20, 280, 280))
        self.circularBgTrain.setStyleSheet("QFrame {\n"
"    border-radius: 140px;\n"
"    background-color: rgb(50, 50, 80);\n"
"}")
        self.circularBgTrain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBgTrain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgTrain.setObjectName("circularBgTrain")
        self.layoutWidget1 = QtWidgets.QWidget(self.circularBgTrain)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 50, 171, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelTopMessageTrain = QtWidgets.QLabel(self.layoutWidget1)
        self.labelTopMessageTrain.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 14pt \"Perpetua Titling MT\";")
        self.labelTopMessageTrain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTopMessageTrain.setObjectName("labelTopMessageTrain")
        self.gridLayout_3.addWidget(self.labelTopMessageTrain, 0, 0, 1, 1)
        self.labelPercentagesTrain = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.labelPercentagesTrain.setFont(font)
        self.labelPercentagesTrain.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Arial Narrow\";")
        self.labelPercentagesTrain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentagesTrain.setObjectName("labelPercentagesTrain")
        self.gridLayout_3.addWidget(self.labelPercentagesTrain, 1, 0, 1, 1)
        self.labelBottomMessageTrain = QtWidgets.QLabel(self.layoutWidget1)
        self.labelBottomMessageTrain.setStyleSheet("QLabel {\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(60, 60, 97);\n"
"    margin-left: 20px;\n"
"    margin-right: 20px;\n"
"}")
        self.labelBottomMessageTrain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBottomMessageTrain.setObjectName("labelBottomMessageTrain")
        self.gridLayout_3.addWidget(self.labelBottomMessageTrain, 2, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.circularProgressBarBaseTrain)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.page_3)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelTrainMessage = QtWidgets.QLabel(self.frame_7)
        self.labelTrainMessage.setMinimumSize(QtCore.QSize(0, 0))
        self.labelTrainMessage.setMaximumSize(QtCore.QSize(0, 16777215))
        self.labelTrainMessage.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.labelTrainMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTrainMessage.setObjectName("labelTrainMessage")
        self.horizontalLayout_10.addWidget(self.labelTrainMessage, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_12 = QtWidgets.QFrame(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_12.setStyleSheet("QLabel {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 170, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(61, 61, 75);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/icons/chevron-down.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_4.setContentsMargins(150, -1, 150, -1)
        self.gridLayout_4.setHorizontalSpacing(100)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnGoPredict = QtWidgets.QPushButton(self.frame_12)
        self.btnGoPredict.setMinimumSize(QtCore.QSize(70, 40))
        self.btnGoPredict.setMaximumSize(QtCore.QSize(70, 40))
        self.btnGoPredict.setText("")
        self.btnGoPredict.setIcon(icon5)
        self.btnGoPredict.setObjectName("btnGoPredict")
        self.gridLayout_4.addWidget(self.btnGoPredict, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setStyleSheet("")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.frame_14)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.cmb1DatePredict = QtWidgets.QComboBox(self.frame_14)
        self.cmb1DatePredict.setObjectName("cmb1DatePredict")
        self.verticalLayout_8.addWidget(self.cmb1DatePredict)
        self.gridLayout_4.addWidget(self.frame_14, 0, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.cmb2DatePredict = QtWidgets.QComboBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb2DatePredict.sizePolicy().hasHeightForWidth())
        self.cmb2DatePredict.setSizePolicy(sizePolicy)
        self.cmb2DatePredict.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cmb2DatePredict.setObjectName("cmb2DatePredict")
        self.verticalLayout_7.addWidget(self.cmb2DatePredict)
        self.gridLayout_4.addWidget(self.frame_13, 0, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_12)
        self.frame_15 = QtWidgets.QFrame(self.page_4)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 450))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 450))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.circularProgressBarBasePredict = QtWidgets.QFrame(self.frame_15)
        self.circularProgressBarBasePredict.setMinimumSize(QtCore.QSize(0, 320))
        self.circularProgressBarBasePredict.setMaximumSize(QtCore.QSize(0, 320))
        self.circularProgressBarBasePredict.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBasePredict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBasePredict.setObjectName("circularProgressBarBasePredict")
        self.circularProgressPredict = QtWidgets.QFrame(self.circularProgressBarBasePredict)
        self.circularProgressPredict.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgressPredict.setStyleSheet("QFrame {\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 170, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgressPredict.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressPredict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressPredict.setObjectName("circularProgressPredict")
        self.circularBgPredict = QtWidgets.QFrame(self.circularProgressBarBasePredict)
        self.circularBgPredict.setGeometry(QtCore.QRect(20, 20, 280, 280))
        self.circularBgPredict.setStyleSheet("QFrame {\n"
"    border-radius: 140px;\n"
"    background-color: rgb(50, 50, 80);\n"
"}")
        self.circularBgPredict.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBgPredict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgPredict.setObjectName("circularBgPredict")
        self.layoutWidget_2 = QtWidgets.QWidget(self.circularBgPredict)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 50, 171, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelTopMessagePredict = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelTopMessagePredict.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 14pt \"Perpetua Titling MT\";")
        self.labelTopMessagePredict.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTopMessagePredict.setObjectName("labelTopMessagePredict")
        self.gridLayout_5.addWidget(self.labelTopMessagePredict, 0, 0, 1, 1)
        self.labelPercentagesPredict = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.labelPercentagesPredict.setFont(font)
        self.labelPercentagesPredict.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Arial Narrow\";")
        self.labelPercentagesPredict.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentagesPredict.setObjectName("labelPercentagesPredict")
        self.gridLayout_5.addWidget(self.labelPercentagesPredict, 1, 0, 1, 1)
        self.labelBottomMessagePredict = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelBottomMessagePredict.setStyleSheet("QLabel {\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(60, 60, 97);\n"
"    margin-left: 20px;\n"
"    margin-right: 20px;\n"
"}")
        self.labelBottomMessagePredict.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBottomMessagePredict.setObjectName("labelBottomMessagePredict")
        self.gridLayout_5.addWidget(self.labelBottomMessagePredict, 2, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.circularProgressBarBasePredict)
        self.verticalLayout_9.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.page_4)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelPredictMessage = QtWidgets.QLabel(self.frame_16)
        self.labelPredictMessage.setMinimumSize(QtCore.QSize(0, 0))
        self.labelPredictMessage.setMaximumSize(QtCore.QSize(0, 16777215))
        self.labelPredictMessage.setStyleSheet("color: rgb(85, 170, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.labelPredictMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPredictMessage.setObjectName("labelPredictMessage")
        self.horizontalLayout_12.addWidget(self.labelPredictMessage, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_9.addWidget(self.frame_16)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_17 = QtWidgets.QFrame(self.page_5)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_17.setStyleSheet("QFrame {\n"
"    Border-radius: 15px;\n"
"    background-color: rgb(71, 71, 107);\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.circularProgressBarBaseAccuracy = QtWidgets.QFrame(self.frame_19)
        self.circularProgressBarBaseAccuracy.setMaximumSize(QtCore.QSize(205, 102))
        self.circularProgressBarBaseAccuracy.setStyleSheet("")
        self.circularProgressBarBaseAccuracy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressBarBaseAccuracy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBaseAccuracy.setObjectName("circularProgressBarBaseAccuracy")
        self.circularProgressAccuracy = QtWidgets.QFrame(self.circularProgressBarBaseAccuracy)
        self.circularProgressAccuracy.setGeometry(QtCore.QRect(10, 10, 185, 185))
        self.circularProgressAccuracy.setStyleSheet("QFrame {\n"
"    border-radius: 92px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180, stop:0.749 rgba(255, 85, 255, 0), stop:0.75 rgba(85, 255, 127, 255));\n"
"}")
        self.circularProgressAccuracy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressAccuracy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressAccuracy.setObjectName("circularProgressAccuracy")
        self.circularBgAccuracy = QtWidgets.QFrame(self.circularProgressBarBaseAccuracy)
        self.circularBgAccuracy.setGeometry(QtCore.QRect(15, 15, 175, 175))
        self.circularBgAccuracy.setStyleSheet("QFrame {\n"
"    border-radius: 87px;\n"
"    \n"
"    background-color: rgb(85, 85, 127);\n"
"}")
        self.circularBgAccuracy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBgAccuracy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgAccuracy.setObjectName("circularBgAccuracy")
        self.labPercentAccuracy = QtWidgets.QLabel(self.circularBgAccuracy)
        self.labPercentAccuracy.setGeometry(QtCore.QRect(44, 20, 91, 41))
        self.labPercentAccuracy.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial Narrow\";")
        self.labPercentAccuracy.setAlignment(QtCore.Qt.AlignCenter)
        self.labPercentAccuracy.setObjectName("labPercentAccuracy")
        self.label_18 = QtWidgets.QLabel(self.circularBgAccuracy)
        self.label_18.setGeometry(QtCore.QRect(20, 59, 131, 21))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_14.addWidget(self.circularProgressBarBaseAccuracy)
        self.horizontalLayout_13.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_17)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.circularProgressBarBaseAccuracy_2 = QtWidgets.QFrame(self.frame_20)
        self.circularProgressBarBaseAccuracy_2.setMaximumSize(QtCore.QSize(205, 102))
        self.circularProgressBarBaseAccuracy_2.setStyleSheet("")
        self.circularProgressBarBaseAccuracy_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressBarBaseAccuracy_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBaseAccuracy_2.setObjectName("circularProgressBarBaseAccuracy_2")
        self.circularProgressAccuracy_2 = QtWidgets.QFrame(self.circularProgressBarBaseAccuracy_2)
        self.circularProgressAccuracy_2.setGeometry(QtCore.QRect(10, 10, 185, 185))
        self.circularProgressAccuracy_2.setStyleSheet("QFrame {\n"
"    border-radius: 92px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180, stop:0.749 rgba(255, 170, 255, 0), stop:0.750 rgba(255, 85, 127, 255));\n"
"}")
        self.circularProgressAccuracy_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressAccuracy_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressAccuracy_2.setObjectName("circularProgressAccuracy_2")
        self.circularBgAccuracy_2 = QtWidgets.QFrame(self.circularProgressBarBaseAccuracy_2)
        self.circularBgAccuracy_2.setGeometry(QtCore.QRect(15, 15, 175, 175))
        self.circularBgAccuracy_2.setStyleSheet("QFrame {\n"
"    border-radius: 87px;\n"
"    \n"
"    background-color: rgb(85, 85, 127);\n"
"}")
        self.circularBgAccuracy_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBgAccuracy_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgAccuracy_2.setObjectName("circularBgAccuracy_2")
        self.label_19 = QtWidgets.QLabel(self.circularBgAccuracy_2)
        self.label_19.setGeometry(QtCore.QRect(44, 20, 91, 41))
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial Narrow\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.circularBgAccuracy_2)
        self.label_20.setGeometry(QtCore.QRect(20, 59, 131, 21))
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_15.addWidget(self.circularProgressBarBaseAccuracy_2)
        self.horizontalLayout_13.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_17)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.circularProgressBarBaseAccuracy_3 = QtWidgets.QFrame(self.frame_21)
        self.circularProgressBarBaseAccuracy_3.setMaximumSize(QtCore.QSize(205, 102))
        self.circularProgressBarBaseAccuracy_3.setStyleSheet("")
        self.circularProgressBarBaseAccuracy_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressBarBaseAccuracy_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBaseAccuracy_3.setObjectName("circularProgressBarBaseAccuracy_3")
        self.circularProgressAccuracy_3 = QtWidgets.QFrame(self.circularProgressBarBaseAccuracy_3)
        self.circularProgressAccuracy_3.setGeometry(QtCore.QRect(10, 10, 185, 185))
        self.circularProgressAccuracy_3.setStyleSheet("QFrame {\n"
"    border-radius: 92px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180, stop:0.749 rgba(255, 170, 0, 0), stop:0.75 rgba(255, 255, 127, 255));\n"
"}")
        self.circularProgressAccuracy_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressAccuracy_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressAccuracy_3.setObjectName("circularProgressAccuracy_3")
        self.circularBgAccuracy_3 = QtWidgets.QFrame(self.circularProgressBarBaseAccuracy_3)
        self.circularBgAccuracy_3.setGeometry(QtCore.QRect(15, 15, 175, 175))
        self.circularBgAccuracy_3.setStyleSheet("QFrame {\n"
"    border-radius: 87px;\n"
"    \n"
"    background-color: rgb(85, 85, 127);\n"
"}")
        self.circularBgAccuracy_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBgAccuracy_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgAccuracy_3.setObjectName("circularBgAccuracy_3")
        self.label_21 = QtWidgets.QLabel(self.circularBgAccuracy_3)
        self.label_21.setGeometry(QtCore.QRect(44, 20, 91, 41))
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial Narrow\";")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.circularBgAccuracy_3)
        self.label_22.setGeometry(QtCore.QRect(20, 59, 131, 21))
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_16.addWidget(self.circularProgressBarBaseAccuracy_3)
        self.horizontalLayout_13.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_17)
        self.frame_22.setStyleSheet("QComboBox{\n"
"    background-color: rgb(61, 61, 75);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/icons/chevron-down.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.cmb1DateDisplay = QtWidgets.QComboBox(self.frame_22)
        self.cmb1DateDisplay.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cmb1DateDisplay.setStyleSheet("color: rgb(255, 255, 255);")
        self.cmb1DateDisplay.setEditable(True)
        self.cmb1DateDisplay.setObjectName("cmb1DateDisplay")
        self.verticalLayout_11.addWidget(self.cmb1DateDisplay)
        self.cmb2DateDisplay = QtWidgets.QComboBox(self.frame_22)
        self.cmb2DateDisplay.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cmb2DateDisplay.setStyleSheet("color: rgb(255, 255, 255);")
        self.cmb2DateDisplay.setEditable(True)
        self.cmb2DateDisplay.setObjectName("cmb2DateDisplay")
        self.verticalLayout_11.addWidget(self.cmb2DateDisplay)
        self.btnGoDisplay = QtWidgets.QPushButton(self.frame_22)
        self.btnGoDisplay.setMinimumSize(QtCore.QSize(0, 30))
        self.btnGoDisplay.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btnGoDisplay.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius: 10px;")
        self.btnGoDisplay.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/filter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGoDisplay.setIcon(icon6)
        self.btnGoDisplay.setObjectName("btnGoDisplay")
        self.verticalLayout_11.addWidget(self.btnGoDisplay)
        self.horizontalLayout_13.addWidget(self.frame_22)
        self.verticalLayout_10.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.page_5)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_23 = QtWidgets.QFrame(self.frame_18)
        self.frame_23.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_23.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(51, 51, 65);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.btnTable = QtWidgets.QPushButton(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTable.sizePolicy().hasHeightForWidth())
        self.btnTable.setSizePolicy(sizePolicy)
        self.btnTable.setMinimumSize(QtCore.QSize(50, 0))
        self.btnTable.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnTable.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/table.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTable.setIcon(icon7)
        self.btnTable.setObjectName("btnTable")
        self.horizontalLayout_17.addWidget(self.btnTable)
        self.btnChart = QtWidgets.QPushButton(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChart.sizePolicy().hasHeightForWidth())
        self.btnChart.setSizePolicy(sizePolicy)
        self.btnChart.setMinimumSize(QtCore.QSize(50, 0))
        self.btnChart.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnChart.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/bar-chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnChart.setIcon(icon8)
        self.btnChart.setObjectName("btnChart")
        self.horizontalLayout_17.addWidget(self.btnChart)
        self.verticalLayout_12.addWidget(self.frame_23, 0, QtCore.Qt.AlignRight)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_18)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.display_page1 = QtWidgets.QWidget()
        self.display_page1.setObjectName("display_page1")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.display_page1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tableDisplay = QtWidgets.QTableWidget(self.display_page1)
        self.tableDisplay.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.tableDisplay.setStyleSheet("QTableWidget {    \n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(71, 71, 107);\n"
"    border-bottom: 1px solid rgb(71, 71, 107);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);     \n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color:  rgb(170, 255, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(72, 72, 107)\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"    background-color: rgb(33, 37, 43);\n"
"    background-color: rgb(63, 71, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    padding: 10px\n"
"}\n"
"\n"
"\n"
"/*ScrollBar vertical ---------------------------------------------- */\n"
"\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(71, 71, 107);\n"
"    width: 10px;\n"
"    margin:  10px 0 10px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"       background: rgb(61, 61, 75);\n"
"    height: 10px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(61, 61, 75);\n"
"    height: 10px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/*ScrollBar horizontal ---------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(71, 71, 107);;\n"
"    height: 10px;\n"
"    margin:  0px 10px 0px 10;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(61, 61, 75);\n"
"    width: 10px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background:  rgb(61, 61, 75);\n"
"    width: 10px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"")
        self.tableDisplay.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableDisplay.setRowCount(0)
        self.tableDisplay.setObjectName("tableDisplay")
        self.tableDisplay.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableDisplay.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDisplay.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDisplay.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDisplay.setHorizontalHeaderItem(3, item)
        self.tableDisplay.horizontalHeader().setDefaultSectionSize(250)
        self.tableDisplay.horizontalHeader().setMinimumSectionSize(150)
        self.tableDisplay.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_18.addWidget(self.tableDisplay)
        self.stackedWidget_2.addWidget(self.display_page1)
        self.display_page2 = QtWidgets.QWidget()
        self.display_page2.setObjectName("display_page2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.display_page2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frameChart = QtWidgets.QFrame(self.display_page2)
        self.frameChart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameChart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameChart.setObjectName("frameChart")
        self.horizontalLayout_19.addWidget(self.frameChart)
        self.stackedWidget_2.addWidget(self.display_page2)
        self.verticalLayout_12.addWidget(self.stackedWidget_2)
        self.verticalLayout_10.addWidget(self.frame_18)
        self.stackedWidget.addWidget(self.page_5)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.mainContent)
        self.statusBar = QtWidgets.QFrame(self.bgApp)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 40))
        self.statusBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.statusBar.setStyleSheet("background-color: rgb(61, 61, 92);")
        self.statusBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusBar.setObjectName("statusBar")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.statusBar)
        self.horizontalLayout_20.setContentsMargins(17, 2, 0, 2)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.errorIconLabel = QtWidgets.QLabel(self.statusBar)
        self.errorIconLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.errorIconLabel.setStyleSheet("background-color: red;\n"
"border-radius: 15px;")
        self.errorIconLabel.setInputMethodHints(QtCore.Qt.ImhNone)
        self.errorIconLabel.setText("")
        self.errorIconLabel.setPixmap(QtGui.QPixmap(":/icons/icons/x-circle.svg"))
        self.errorIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorIconLabel.setObjectName("errorIconLabel")
        self.horizontalLayout_20.addWidget(self.errorIconLabel)
        self.errorMessageLabel = QtWidgets.QLabel(self.statusBar)
        self.errorMessageLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.errorMessageLabel.setText("")
        self.errorMessageLabel.setObjectName("errorMessageLabel")
        self.horizontalLayout_20.addWidget(self.errorMessageLabel)
        self.verticalLayout.addWidget(self.statusBar)
        self.horizontalLayout_21.addWidget(self.bgApp)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logoTitle.setText(_translate("MainWindow", "ISIS - NIS"))
        self.btnHide.setText(_translate("MainWindow", "Hide"))
        self.btnMenuLoadCSV.setText(_translate("MainWindow", "Load CSV files"))
        self.btnMenuTrain.setText(_translate("MainWindow", "Train the model"))
        self.btnMenuPredict.setText(_translate("MainWindow", "Predict load"))
        self.btnMenuDisplay.setText(_translate("MainWindow", "Display of forecasted data"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.btnOpenCSV.setText(_translate("MainWindow", "  Open CSV file"))
        self.btnOpenFolder.setText(_translate("MainWindow", "   Open folder with CSV files"))
        self.labelTopMessageCSV.setText(_translate("MainWindow", "Please wait..."))
        self.labelPercentagesCSV.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:38pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelBottomMessageCSV.setText(_translate("MainWindow", "loading..."))
        self.labelOpenCSVMessage.setText(_translate("MainWindow", "Successfully executed"))
        self.label_6.setText(_translate("MainWindow", "Select the second date:"))
        self.label_5.setText(_translate("MainWindow", "Select the first date:"))
        self.labelTopMessageTrain.setText(_translate("MainWindow", "Please wait..."))
        self.labelPercentagesTrain.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:38pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelBottomMessageTrain.setText(_translate("MainWindow", "loading..."))
        self.labelTrainMessage.setText(_translate("MainWindow", "Training successfully completed"))
        self.label_12.setText(_translate("MainWindow", "Choose a date:"))
        self.label_11.setText(_translate("MainWindow", "Select the number of days:"))
        self.labelTopMessagePredict.setText(_translate("MainWindow", "Please wait..."))
        self.labelPercentagesPredict.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:38pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelBottomMessagePredict.setText(_translate("MainWindow", "loading..."))
        self.labelPredictMessage.setText(_translate("MainWindow", "Predicted values can be viewed in Display of forecasted data"))
        self.labPercentAccuracy.setText(_translate("MainWindow", "0%"))
        self.label_18.setText(_translate("MainWindow", "Accuracy"))
        self.label_19.setText(_translate("MainWindow", "0%"))
        self.label_20.setText(_translate("MainWindow", "Accuracy"))
        self.label_21.setText(_translate("MainWindow", "0%"))
        self.label_22.setText(_translate("MainWindow", "Accuracy"))
        self.cmb1DateDisplay.setCurrentText(_translate("MainWindow", "Select the first date..."))
        self.cmb2DateDisplay.setCurrentText(_translate("MainWindow", "Select the second date..."))
        self.tableDisplay.setSortingEnabled(False)
        item = self.tableDisplay.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableDisplay.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hour"))
        item = self.tableDisplay.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Predicted values"))
        item = self.tableDisplay.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Actual values"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

