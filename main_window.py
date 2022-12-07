import txt_to_csv_first as DTC
import txt_to_csv_second as CD
import txt_to_csv_third as CDR

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("backgroud-color: #222222e")
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
        self.Mark1output = QtWidgets.QLineEdit(self.frame)
        self.Mark1output.setGeometry(QtCore.QRect(210, 120, 561, 51))
        self.Mark1output.setObjectName("Mark1output")
        self.NM1 = QtWidgets.QPushButton(self.frame)
        self.NM1.setGeometry(QtCore.QRect(780, 120, 89, 25))
        self.NM1.setObjectName("NM1")
        self.Mark2text = QtWidgets.QTextEdit(self.frame)
        self.Mark2text.setGeometry(QtCore.QRect(90, 190, 111, 31))
        self.Mark2text.setObjectName("Mark2text")
        self.Mark2output = QtWidgets.QLineEdit(self.frame)
        self.Mark2output.setGeometry(QtCore.QRect(210, 190, 561, 51))
        self.Mark2output.setObjectName("Mark2output")
        self.NM2 = QtWidgets.QPushButton(self.frame)
        self.NM2.setGeometry(QtCore.QRect(780, 190, 89, 25))
        self.NM2.setObjectName("NM2")
        self.Mark3text = QtWidgets.QTextEdit(self.frame)
        self.Mark3text.setGeometry(QtCore.QRect(90, 260, 111, 31))
        self.Mark3text.setObjectName("Mark3text")
        self.Mark3output = QtWidgets.QLineEdit(self.frame)
        self.Mark3output.setGeometry(QtCore.QRect(210, 260, 561, 51))
        self.Mark3output.setObjectName("Mark3output")
        self.NM3 = QtWidgets.QPushButton(self.frame)
        self.NM3.setGeometry(QtCore.QRect(780, 260, 89, 25))
        self.NM3.setObjectName("NM3")
        self.Mark4text = QtWidgets.QTextEdit(self.frame)
        self.Mark4text.setGeometry(QtCore.QRect(90, 330, 111, 31))
        self.Mark4text.setObjectName("Mark4text")
        self.mark4output = QtWidgets.QLineEdit(self.frame)
        self.mark4output.setGeometry(QtCore.QRect(210, 330, 561, 51))
        self.mark4output.setObjectName("mark4output")
        self.NM4 = QtWidgets.QPushButton(self.frame)
        self.NM4.setGeometry(QtCore.QRect(780, 330, 89, 25))
        self.NM4.setObjectName("NM4")
        self.Mark5text = QtWidgets.QTextEdit(self.frame)
        self.Mark5text.setGeometry(QtCore.QRect(90, 400, 111, 31))
        self.Mark5text.setObjectName("Mark5text")
        self.Mark5output = QtWidgets.QLineEdit(self.frame)
        self.Mark5output.setGeometry(QtCore.QRect(210, 400, 561, 51))
        self.Mark5output.setObjectName("Mark5output")
        self.NM5 = QtWidgets.QPushButton(self.frame)
        self.NM5.setGeometry(QtCore.QRect(780, 400, 89, 25))
        self.NM5.setObjectName("NM5")
        self.DTC = QtWidgets.QPushButton(self.frame)
        self.DTC.setGeometry(QtCore.QRect(120, 570, 191, 25))
        self.DTC.setObjectName("DTC")
        self.CD = QtWidgets.QPushButton(self.frame)
        self.CD.setGeometry(QtCore.QRect(400, 570, 191, 25))
        self.CD.setObjectName("CD")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(650, 570, 191, 25))
        self.pushButton_15.setObjectName("pushButton_15")
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
        self.pushButton_15.setText(_translate("MainWindow", "Dataset with rand names"))

def read_path() -> bool:
        if (os.path.exists(ui.dataset_path_input.text()+"/1") == False):
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("файлы не найдены!\nВведите путь еще раз")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                check_way = False
                return False, ""
        else:
                check_way = True
                fullWay = ui.dataset_path_input.text()
                return True,fullWay

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    path = str()
    isPath = False

    isPath, path = ui.dataset_path_apply.clicked.connect(read_path)

    #ui.DTC.clicked.connect(DTC)

    sys.exit(app.exec_())