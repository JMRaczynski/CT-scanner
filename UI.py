# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from skimage import io, color


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(400, 510, 75, 23))
        self.startButton.setObjectName("startButton")
        self.chooseImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseImageButton.setGeometry(QtCore.QRect(170, 300, 75, 23))
        self.chooseImageButton.setObjectName("chooseImageButton")
        self.inputImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputImageLabel.setGeometry(QtCore.QRect(130, 40, 81, 16))
        self.inputImageLabel.setObjectName("inputImageLabel")
        self.sinogramLabel = QtWidgets.QLabel(self.centralwidget)
        self.sinogramLabel.setGeometry(QtCore.QRect(440, 40, 51, 16))
        self.sinogramLabel.setObjectName("sinogramLabel")
        self.outputImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputImageLabel.setGeometry(QtCore.QRect(710, 40, 81, 16))
        self.outputImageLabel.setObjectName("outputImageLabel")
        self.inputImage = QtWidgets.QLabel(self.centralwidget)
        self.inputImage.setGeometry(QtCore.QRect(50, 80, 251, 191))
        self.inputImage.setFrameShape(QtWidgets.QFrame.Box)
        self.inputImage.setText("")
        self.inputImage.setObjectName("inputImage")
        self.sinogram = QtWidgets.QLabel(self.centralwidget)
        self.sinogram.setGeometry(QtCore.QRect(340, 80, 251, 191))
        self.sinogram.setFrameShape(QtWidgets.QFrame.Box)
        self.sinogram.setText("")
        self.sinogram.setObjectName("sinogram")
        self.outputImage = QtWidgets.QLabel(self.centralwidget)
        self.outputImage.setGeometry(QtCore.QRect(630, 80, 251, 191))
        self.outputImage.setFrameShape(QtWidgets.QFrame.Box)
        self.outputImage.setText("")
        self.outputImage.setObjectName("outputImage")
        self.progressSlider = QtWidgets.QSlider(self.centralwidget)
        self.progressSlider.setGeometry(QtCore.QRect(170, 460, 111, 22))
        self.progressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progressSlider.setObjectName("progressSlider")
        self.chooseImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseImageLabel.setGeometry(QtCore.QRect(60, 300, 81, 21))
        self.chooseImageLabel.setObjectName("chooseImageLabel")
        self.alphaStepTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.alphaStepTextfield.setGeometry(QtCore.QRect(170, 340, 113, 20))
        self.alphaStepTextfield.setObjectName("alphaStepTextfield")
        self.numOfDetectorsTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.numOfDetectorsTextfield.setGeometry(QtCore.QRect(170, 370, 113, 20))
        self.numOfDetectorsTextfield.setObjectName("numOfDetectorsTextfield")
        self.angularRangeTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.angularRangeTextfield.setGeometry(QtCore.QRect(170, 400, 113, 20))
        self.angularRangeTextfield.setObjectName("angularRangeTextfield")
        self.alphaStepLabel = QtWidgets.QLabel(self.centralwidget)
        self.alphaStepLabel.setGeometry(QtCore.QRect(60, 340, 81, 16))
        self.alphaStepLabel.setObjectName("alphaStepLabel")
        self.numOfDetectorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numOfDetectorsLabel.setGeometry(QtCore.QRect(60, 370, 91, 16))
        self.numOfDetectorsLabel.setObjectName("numOfDetectorsLabel")
        self.angularRangeLabel = QtWidgets.QLabel(self.centralwidget)
        self.angularRangeLabel.setGeometry(QtCore.QRect(60, 400, 101, 16))
        self.angularRangeLabel.setObjectName("angularRangeLabel")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(60, 460, 47, 13))
        self.progressLabel.setObjectName("progressLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(620, 380, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.filterCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.filterCheckbox.setGeometry(QtCore.QRect(170, 430, 70, 17))
        self.filterCheckbox.setObjectName("filterCheckbox")
        self.commentsTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.commentsTextField.setGeometry(QtCore.QRect(620, 420, 251, 71))
        self.commentsTextField.setObjectName("commentsTextField")
        self.patientInfoTextfield = QtWidgets.QTextEdit(self.centralwidget)
        self.patientInfoTextfield.setGeometry(QtCore.QRect(620, 290, 251, 71))
        self.patientInfoTextfield.setObjectName("patientInfoTextfield")
        self.patientInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientInfoLabel.setGeometry(QtCore.QRect(476, 320, 111, 20))
        self.patientInfoLabel.setObjectName("patientInfoLabel")
        self.examinationDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.examinationDateLabel.setGeometry(QtCore.QRect(480, 380, 71, 16))
        self.examinationDateLabel.setObjectName("examinationDateLabel")
        self.commentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.commentsLabel.setGeometry(QtCore.QRect(480, 450, 61, 16))
        self.commentsLabel.setObjectName("commentsLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.chooseImageButton.clicked.connect(self.setImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.chooseImageButton.setText(_translate("MainWindow", "Przeglądaj.."))
        self.inputImageLabel.setText(_translate("MainWindow", "Obraz wejściowy"))
        self.sinogramLabel.setText(_translate("MainWindow", "Sinogram"))
        self.outputImageLabel.setText(_translate("MainWindow", "Obraz wynikowy"))
        self.chooseImageLabel.setText(_translate("MainWindow", "Wybierz obraz"))
        self.alphaStepLabel.setText(_translate("MainWindow", "Krok delta-alfa"))
        self.numOfDetectorsLabel.setText(_translate("MainWindow", "Liczba detektorów"))
        self.angularRangeLabel.setText(_translate("MainWindow", "Rozpiętość kątowa"))
        self.progressLabel.setText(_translate("MainWindow", "Postęp"))
        self.filterCheckbox.setText(_translate("MainWindow", "Filtrowanie"))
        self.patientInfoLabel.setText(_translate("MainWindow", "Informacje o pacjencie"))
        self.examinationDateLabel.setText(_translate("MainWindow", "Data badania"))
        self.commentsLabel.setText(_translate("MainWindow", "Komentarze"))


    def setImage(self):
        self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Wybierz obraz", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.imagePath:
            pixmap = QtGui.QPixmap(self.imagePath)
            pixmap = pixmap.scaled(self.inputImage.width(), self.inputImage.height(), QtCore.Qt.KeepAspectRatio)
            self.inputImage.setPixmap(pixmap)
            self.inputImage.setAlignment(QtCore.Qt.AlignCenter)
            generateSinogram(self.imagePath)


def generateSinogram(imagePath):
    img = io.imread(imagePath)
    img = color.rgb2gray(img)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
