import sys
import os
import platform

from UI.ui_main import *
from Services.dataset_service import DatasetService
from Services.train_test_service import TrainTestService


WINDOW_SIZE = 0
MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(0, 170, 255, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.datasetService = DatasetService()
        self.trainTestService = TrainTestService()

        self.initialize()

        self.show()

    def initialize(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.btnClose.clicked.connect(lambda: self.closeWindow())
        self.ui.btnMin.clicked.connect(lambda: self.showMinimized())
        self.ui.btnMinMax.clicked.connect(lambda: self.minmaxWindowSize())
        self.ui.windowBar.mouseMoveEvent = self.moveWindow
        self.ui.btnHide.clicked.connect(lambda: self.toogleMenu(250, True))
        self.ui.btnMenuLoadCSV.clicked.connect(lambda: self.buttonClick())
        self.ui.btnMenuTrain.clicked.connect(lambda: self.buttonClick())
        self.ui.btnMenuPredict.clicked.connect(lambda: self.buttonClick())
        self.ui.btnMenuDisplay.clicked.connect(lambda: self.buttonClick())
        self.ui.btnTable.clicked.connect(lambda: self.buttonClick())
        self.ui.btnChart.clicked.connect(lambda: self.buttonClick())

        self.ui.btnOpenCSV.clicked.connect(lambda: self.openCSVFile())
        self.ui.btnOpenFolder.clicked.connect(lambda: self.openCSVFolder())

        self.ui.btnGoTrain.clicked.connect(lambda: self.trainModel())
        cmb_items = self.datasetService.getDatesFromDatabase()
        cmb_items.insert(0, "Chose date...")
        self.ui.cmb1DateTrain.addItems(cmb_items)
        self.ui.cmb2DateTrain.addItems(cmb_items)

        self.ui.cmb1DatePredict.addItems(cmb_items)
        cmb_items = ["1", "2", "3", "4", "5", "6", "7"]
        self.ui.cmb2DatePredict.addItems(cmb_items)
        self.ui.btnGoPredict.clicked.connect(lambda: self.predictLoad())

    def closeWindow(self):
        self.datasetService.closeRepository()
        self.close()

    def minmaxWindowSize(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE
        if win_status == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
            self.ui.btnMinMax.setIcon(QtGui.QIcon(':/icons/icons/minimize.svg'))
        else:
            WINDOW_SIZE = 0
            self.showNormal()
            self.ui.btnMinMax.setIcon(QtGui.QIcon(':/icons/icons/maximize.svg'))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        global WINDOW_SIZE
        if event.buttons() == Qt.LeftButton:
            if WINDOW_SIZE == 1:
                self.minmaxWindowSize()
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def toogleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.leftMenu.width()
            maxEx = maxWidth
            standard = 65

            if width == 65:
                widthEx = maxEx
            else:
                widthEx = standard

            self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthEx)
            self.animation.start()

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btnMenuLoadCSV":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))
        elif btnName == "btnMenuTrain":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))
        elif btnName == "btnMenuPredict":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))
        elif btnName == "btnMenuDisplay":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))
        elif btnName == "btnTable":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.display_page1)
        elif btnName == "btnChart":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.display_page2)


    def resetStyle(self, widget):
        for w in self.ui.leftMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))

    def selectMenu(self, style):
        select = style + MENU_SELECTED_STYLESHEET
        return select

    def deselectMenu(self, style):
        deselect = style.replace(MENU_SELECTED_STYLESHEET, "")
        return deselect

    def openCSVFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', 'E:\milijevic\Desktop\isis\projekat')
        print(file[0])

    def openCSVFolder(self):
        folder = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'E:\milijevic\Desktop\isis\projekat', QFileDialog.ShowDirsOnly)
        self.datasetService.loadCSVFolder(folder)

    def trainModel(self):
        testPredict, testY = self.trainTestService.TrainModel(self.ui.cmb1DateTrain.currentText(), self.ui.cmb2DateTrain.currentText())
        frame = self.trainTestService.GetDatetime(self.ui.cmb1DateTrain.currentText(), self.ui.cmb2DateTrain.currentText())

        frame = frame.tail(len(testY))
        list = []
        for j in testY:
            list.append(j)
        list2 = []
        for j in testPredict:
            list2.append(j)
        frame["testY"] = list
        frame["testPredict"] = list2

        self.ui.tableDisplay.setRowCount(len(testY))
        row2 = 0
        # for i in range(testY):
        for i, row in frame.iterrows():
            self.ui.tableDisplay.setItem(row2, 0, QtWidgets.QTableWidgetItem(row["datetime"].strftime("%m/%d/%Y, %H:%M:%S")))
            self.ui.tableDisplay.setItem(row2, 1, QtWidgets.QTableWidgetItem(str(0)))
            self.ui.tableDisplay.setItem(row2, 2, QtWidgets.QTableWidgetItem(str(row["testY"])))
            self.ui.tableDisplay.setItem(row2, 3, QtWidgets.QTableWidgetItem(str(row["testPredict"])))
            row2 += 1

    def predictLoad(self):
        self.trainTestService.predictLoad(self.ui.cmb1DatePredict.currentText(), self.ui.cmb2DatePredict.currentText())
