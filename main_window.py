import sys

import txt_to_csv_first as DTC
import txt_to_csv_second as CD
import txt_to_csv_third as CDR
import iterapor as it

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("backgroud-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-80, -50, 931, 671))
        self.frame.setStyleSheet("background-color: #fb5b5d ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dataset_path_input = QtWidgets.QLineEdit(self.frame)
        self.dataset_path_input.setGeometry(QtCore.QRect(210, 50, 561, 51))
        self.dataset_path_input.setObjectName("dataset_path_input")
        self.dataset_path = QtWidgets.QTextEdit(self.frame)
        self.dataset_path.setGeometry(QtCore.QRect(90, 50, 111, 31))
        self.dataset_path.setObjectName("dataset_path")
        self.dataset_path_apply = QtWidgets.QPushButton(self.frame)
        self.dataset_path_apply.setGeometry(QtCore.QRect(780, 50, 89, 25))
        self.dataset_path_apply.setObjectName("dataset_path_apply")
        self.Mark1text = QtWidgets.QTextEdit(self.frame)
        self.Mark1text.setGeometry(QtCore.QRect(90, 120, 111, 31))
        self.Mark1text.setObjectName("Mark1text")
        self.NM1 = QtWidgets.QPushButton(self.frame)
        self.NM1.setGeometry(QtCore.QRect(780, 120, 89, 25))
        self.NM1.setObjectName("NM1")
        self.Mark2text = QtWidgets.QTextEdit(self.frame)
        self.Mark2text.setGeometry(QtCore.QRect(90, 190, 111, 31))
        self.Mark2text.setObjectName("Mark2text")
        self.NM2 = QtWidgets.QPushButton(self.frame)
        self.NM2.setGeometry(QtCore.QRect(780, 190, 89, 25))
        self.NM2.setObjectName("NM2")
        self.Mark3text = QtWidgets.QTextEdit(self.frame)
        self.Mark3text.setGeometry(QtCore.QRect(90, 260, 111, 31))
        self.Mark3text.setObjectName("Mark3text")
        self.NM3 = QtWidgets.QPushButton(self.frame)
        self.NM3.setGeometry(QtCore.QRect(780, 260, 89, 25))
        self.NM3.setObjectName("NM3")
        self.Mark4text = QtWidgets.QTextEdit(self.frame)
        self.Mark4text.setGeometry(QtCore.QRect(90, 330, 111, 31))
        self.Mark4text.setObjectName("Mark4text")
        self.NM4 = QtWidgets.QPushButton(self.frame)
        self.NM4.setGeometry(QtCore.QRect(780, 330, 89, 25))
        self.NM4.setObjectName("NM4")
        self.Mark5text = QtWidgets.QTextEdit(self.frame)
        self.Mark5text.setGeometry(QtCore.QRect(90, 400, 111, 31))
        self.Mark5text.setObjectName("Mark5text")
        self.NM5 = QtWidgets.QPushButton(self.frame)
        self.NM5.setGeometry(QtCore.QRect(780, 400, 89, 25))
        self.NM5.setObjectName("NM5")
        self.DTC = QtWidgets.QPushButton(self.frame)
        self.DTC.setGeometry(QtCore.QRect(120, 570, 191, 25))
        self.DTC.setObjectName("DTC")
        self.CD = QtWidgets.QPushButton(self.frame)
        self.CD.setGeometry(QtCore.QRect(400, 570, 191, 25))
        self.CD.setObjectName("CD")
        self.DWRN = QtWidgets.QPushButton(self.frame)
        self.DWRN.setGeometry(QtCore.QRect(650, 570, 191, 25))
        self.DWRN.setObjectName("DWRN")
        self.Mark1out = QtWidgets.QTextEdit(self.frame)
        self.Mark1out.setGeometry(QtCore.QRect(210, 120, 561, 51))
        self.Mark1out.setObjectName("Mark1out")
        self.Mark2out = QtWidgets.QTextEdit(self.frame)
        self.Mark2out.setGeometry(QtCore.QRect(210, 190, 561, 51))
        self.Mark2out.setObjectName("Mark2out")
        self.Mark3out = QtWidgets.QTextEdit(self.frame)
        self.Mark3out.setGeometry(QtCore.QRect(210, 260, 561, 51))
        self.Mark3out.setObjectName("Mark3out")
        self.Mark4out = QtWidgets.QTextEdit(self.frame)
        self.Mark4out.setGeometry(QtCore.QRect(210, 330, 561, 51))
        self.Mark4out.setObjectName("Mark4out")
        self.Mark5out = QtWidgets.QTextEdit(self.frame)
        self.Mark5out.setGeometry(QtCore.QRect(210, 400, 561, 51))
        self.Mark5out.setObjectName("Mark5out")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dataset_path.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dataset path:</p></body></html>"))
        self.dataset_path_apply.setText(_translate("MainWindow", "Apply"))
        self.Mark1text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mark 1.0:</p></body></html>"))
        self.NM1.setText(_translate("MainWindow", "Next"))
        self.Mark2text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mark 2.0:</p></body></html>"))
        self.NM2.setText(_translate("MainWindow", "Next"))
        self.Mark3text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mark 3.0:</p></body></html>"))
        self.NM3.setText(_translate("MainWindow", "Next"))
        self.Mark4text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mark 4.0:</p></body></html>"))
        self.NM4.setText(_translate("MainWindow", "Next"))
        self.Mark5text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mark 5.0:</p></body></html>"))
        self.NM5.setText(_translate("MainWindow", "Next"))
        self.DTC.setText(_translate("MainWindow", "Dataset to csv"))
        self.CD.setText(_translate("MainWindow", "Copy dataset"))
        self.DWRN.setText(_translate("MainWindow", "Dataset with rand names"))
        self.Mark1out.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Mark2out.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Mark3out.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Mark4out.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Mark5out.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

"/home/ivanc/Documents/Python/application_programming_first_lab_and_dataset/dataset"

def read_path():
    global check_way
    global fullWay
    if (os.path.exists(ui.dataset_path_input.text()+"/1") == False):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("файлы не найдены!\nВведите путь еще раз")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        check_way = False
    else:
        check_way = True
        fullWay = ui.dataset_path_input.text()
        
def dataset_to_csv():
    
    paths_to_files = DTC.get_paths_to_files(fullWay)
    DTC.write_as_csv(paths_to_files)
    
    
    if (os.path.exists("./dataset_csv_first.csv")): 
        pass
    else: 
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("CVS файл не создан")
        msg.setIcon(QMessageBox.Warning)
        #check_DTS = False
        msg.exec_()
    
    make_it()
    
def dataset_copy():
    
    paths_to_files = CD.get_paths_to_files(fullWay)
    new_dataset_path = CD.copy_dataset(fullWay)
    CD.write_as_csv(new_dataset_path, paths_to_files)
    
    if (os.path.exists("./dataset_csv_copy.csv")): 
        pass
    else: 
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("CVS файл не создан")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    
    make_it()
    
def dataset_copy_random():
    CDR.create_copy(fullWay)
    path_new_dataset = CDR.path_n_d()
    paths_to_files = CDR.get_paths_to_files(path_new_dataset)
    CDR.write_as_csv(path_new_dataset, paths_to_files)

    make_it()

def make_it():
    global it_NM1
    global it_NM2
    global it_NM3
    global it_NM4
    global it_NM5
    
    it_NM1 = it.SimpleIterator("./dataset_csv_first.csv", "1")
    it_NM2 = it.SimpleIterator("./dataset_csv_first.csv", "2")
    it_NM3 = it.SimpleIterator("./dataset_csv_first.csv", "3")
    it_NM4 = it.SimpleIterator("./dataset_csv_first.csv", "4")
    it_NM5 = it.SimpleIterator("./dataset_csv_first.csv", "5")
    
def case_NM1():
    
    with open(next(it_NM1), "r", encoding="utf-8") as file:
        text = file.read()
        ui.Mark1out.setText(text)
        
def case_NM2():
    
    with open(next(it_NM2), "r", encoding="utf-8") as file:
        text = file.read()
        ui.Mark2out.setText(text)

def case_NM3():
    
    with open(next(it_NM3), "r", encoding="utf-8") as file:
        text = file.read()
        ui.Mark3out.setText(text)
        
def case_NM4():
    
    with open(next(it_NM4), "r", encoding="utf-8") as file:
        text = file.read()
        ui.Mark4out.setText(text)
        
def case_NM5():
    
    with open(next(it_NM5), "r", encoding="utf-8") as file:
        text = file.read()
        ui.Mark5out.setText(text)
    
if __name__ == "__main__":
    
    fullWay= str()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    ui.dataset_path_apply.clicked.connect(read_path)
    
    ui.DTC.clicked.connect(dataset_to_csv)
    ui.CD.clicked.connect(dataset_copy)
    ui.DWRN.clicked.connect(dataset_copy_random)
    
    ui.NM1.clicked.connect(case_NM1)
    ui.NM2.clicked.connect(case_NM2)
    ui.NM3.clicked.connect(case_NM3)
    ui.NM4.clicked.connect(case_NM4)
    ui.NM5.clicked.connect(case_NM5)
    
    sys.exit(app.exec_())