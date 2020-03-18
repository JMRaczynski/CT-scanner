# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from skimage import io, color
from skimage.transform import rescale, resize
from math import pi, radians, cos, sin, ceil
from time import sleep
import numpy as np
import sys


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
            self.generateSinogram(int(self.alphaStepTextfield.text()), int(self.numOfDetectorsTextfield.text()), int(self.angularRangeTextfield.text()))

    def showSinogram(self, width):
        img = QtGui.QImage(self.sinogramPath)
        img2 = img.copy(0, 0, width, img.height())
        pixmap = QtGui.QPixmap(img2)
        pixmap = pixmap.scaled(self.sinogram.width(), self.sinogram.height(), QtCore.Qt.KeepAspectRatio)
        self.sinogram.setPixmap(pixmap)
        self.sinogram.setAlignment(QtCore.Qt.AlignLeft)


    def generateSinogram(self, step, numOfDetectors, angleRange):
        img = io.imread(self.imagePath)
        img = color.rgb2gray(img)
        if max(len(img), len(img[0])) > 1000:
            factor = 0.125
        else:
            factor = 0.25
        img = rescale(img, factor, anti_aliasing=False)
        m = len(img[0]) // 2
        n = len(img) // 2
        romax = ceil((len(img) ** 2 + len(img[0]) ** 2) ** 0.5)
        sinogram = np.zeros((numOfDetectors, 180//step))
        print(len(sinogram), len(sinogram[0]))
        radius = round(romax / 2)
        radius2 = ((len(img) ** 2 + len(img[0]) ** 2) ** 0.5) / 2
        for k in range(1, 180, step):
            if k < 46:
                angles = np.linspace(k, k + angleRange, numOfDetectors)
                a = sin(radians(angles[numOfDetectors//2])) / cos(radians(angles[numOfDetectors//2]))
                for i, angle in enumerate(angles):
                    emiterX = radius2 * cos(radians(angle))
                    emiterY = radius2 * sin(radians(angle))
                    b = emiterY - a*emiterX
                    #ymax = min(int(round(-a * m + b)), n - 1)
                    #ymin = max(int(round(a * m + b)), -n)
                    for y in range(-n, n-1):
                        x = (y - b) / a
                        xfloor = x // 1
                        xup = x - xfloor
                        xlow = 1 - xup
                        x = xfloor
                        x = max(x, -m)
                        x = min(x, m - 2)
                        x = int(x)
                        sinogram[i][(180 - k) // step - 1] += xlow * img[y + n][x + m]
                        sinogram[i][(180 - k) // step - 1] += xup * img[y + n][x + m + 1]
                """for detector in range(1, romax):
                    distance = detector - radius
                    b = distance / sin(rads)
                    ymax = min(round(-a*m + b), n - 1)
                    ymin = max(round(a*m + b), -n)
                    for y in range(ymin, ymax):
                        x = (y-b) / a
                        xfloor = x // 1
                        xup = x - xfloor
                        xlow = 1 - xup
                        x = xfloor
                        x = max(x, -m)
                        x = min(x, m -2)
                        x = int(x)
                        if k == 1:
                            print(romax - detector)
                        sinogram[(romax - detector) - 1][(180 - k)//step - 1] += xlow * img[y + n][x + m]
                        sinogram[(romax - detector) - 1][(180 - k)//step - 1] += xup * img[y + n][x + m + 1]"""
            elif k < 91:
                rads = radians(k)
                angles = np.linspace(k, k + angleRange, numOfDetectors)
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
                for i, angle in enumerate(angles):
                    emiterX = radius2 * cos(radians(angle))
                    emiterY = radius2 * sin(radians(angle))
                    b = emiterY - a * emiterX
                    #xmax = min(round((-n - b) / a), m - 1)
                    #xmin = max(round((n - b) / a), -m)
                    for x in range(-m, m - 1):
                        y = a * x + b
                        yfloor = y // 1
                        yup = y - yfloor
                        ylow = 1 - yup
                        y = yfloor
                        y = max(y, -n)
                        y = min(y, n - 2)
                        y = int(y)
                        sinogram[i][(180 - k) // step - 1] += ylow * img[y + n][x + m]
                        sinogram[i][(180 - k) // step - 1] += yup * img[y + n + 1][x + m]
                """for detector in range(1, romax):
                    distance = detector - radius
                    b = distance / sin(rads)
                    xmax = min(round((-n - b) / a), m - 1)
                    xmin = max(round((n - b) / a), -m)
                    for x in range(xmin, xmax):
                        y = a * x + b
                        yfloor = y // 1
                        yup = y - yfloor
                        ylow = 1 - yup
                        y = yfloor
                        y = max(y, -n)
                        y = min(y, n - 2)
                        y = int(y)
                        sinogram[(romax - detector) - 1][(180 - k) // step - 1] += ylow * img[y + n][x + m]
                        sinogram[(romax - detector) - 1][(180 - k) // step - 1] += yup * img[y + n + 1][x + m]"""
            elif k < 136:
                angles = np.linspace(k, k + angleRange, numOfDetectors)
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
                for i, angle in enumerate(angles):
                    emiterX = radius2 * cos(radians(angle))
                    emiterY = radius2 * sin(radians(angle))
                    b = emiterY - a * emiterX
                    #xmax = min(round((n - b) / a), m - 1)
                    #xmin = max(round((-n - b) / a), -m)
                    for x in range(-m, m - 1):
                        y = a * x + b
                        yfloor = y // 1
                        yup = y - yfloor
                        ylow = 1 - yup
                        y = yfloor
                        y = max(y, -n)
                        y = min(y, n - 2)
                        y = int(y)
                        sinogram[i][(180 - k) // step - 1] += ylow * img[y + n][x + m]
                        sinogram[i][(180 - k) // step - 1] += yup * img[y + n + 1][x + m]
                """for detector in range(1, romax):
                    distance = detector - radius
                    b = distance / sin(rads)
                    xmax = min(round((n - b) / a), m - 1)
                    xmin = max(round((-n - b) / a), -m)
                    for x in range(xmin, xmax):
                        y = a * x + b
                        yfloor = y // 1
                        yup = y - yfloor
                        ylow = 1 - yup
                        y = yfloor
                        y = max(y, -n)
                        y = min(y, n - 2)
                        y = int(y)
                        sinogram[(romax - detector) - 1][(180 - k) // step - 1] += ylow * img[y + n][x + m]
                        sinogram[(romax - detector) - 1][(180 - k) // step - 1] += yup * img[y + n + 1][x + m]"""
            elif k < 180:
                angles = np.linspace(k, k + angleRange, numOfDetectors)
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
                for i, angle in enumerate(angles):
                    emiterX = radius2 * cos(radians(angle))
                    emiterY = radius2 * sin(radians(angle))
                    b = emiterY - a * emiterX
                    #ymax = min(int(round(a * m + b)), n - 1)
                    #ymin = max(int(round(-a * m + b)), -n)
                    for y in range(-n, n - 1):
                        x = (y - b) / a
                        xfloor = x // 1
                        xup = x - xfloor
                        xlow = 1 - xup
                        x = xfloor
                        x = max(x, -m)
                        x = min(x, m - 2)
                        x = int(x)
                        sinogram[i][(180 - k) // step - 1] += xlow * img[y + n][x + m]
                        sinogram[i][(180 - k) // step - 1] += xup * img[y + n][x + m + 1]
                """for detector in range(1, romax):
                    distance = detector - radius
                    b = distance / sin(rads)
                    ymax = min(round(a * m + b), n - 1)
                    ymin = max(round(-a * m + b), -n)
                    for y in range(ymin, ymax):
                        x = (y - b) / a
                        xfloor = x // 1
                        xup = x - xfloor
                        xlow = 1 - xup
                        x = xfloor
                        x = max(x, -m)
                        x = min(x, m - 2)
                        x = int(x)
                        sinogram[(romax - detector) - 1][(180 - k) // step - 1] += xlow * img[y + n][x + m]
                        sinogram[(romax - detector) - 1][(180 - k) // step - 1] += xup * img[y + n][x + m + 1]"""
        sinogram = resize(sinogram, (191, 251))
        io.imsave("sinogram.png", sinogram)
        self.sinogramPath = "sinogram.png"
        self.progressSlider.setMinimum(0)
        self.progressSlider.setMaximum(251)
        self.progressSlider.setSingleStep(1)
        self.progressSlider.valueChanged.connect(self.showSinogram)




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
