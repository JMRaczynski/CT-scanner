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
import numpy as np
import sys
import random
import pydicom
import datetime
from skimage.exposure import rescale_intensity


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(400, 560, 75, 23))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startProcessing)
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
        self.alphaStepTextfield.setText("1")
        self.numOfDetectorsTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.numOfDetectorsTextfield.setGeometry(QtCore.QRect(170, 370, 113, 20))
        self.numOfDetectorsTextfield.setObjectName("numOfDetectorsTextfield")
        self.numOfDetectorsTextfield.setText("180")
        self.angularRangeTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.angularRangeTextfield.setGeometry(QtCore.QRect(170, 400, 113, 20))
        self.angularRangeTextfield.setObjectName("angularRangeTextfield")
        self.angularRangeTextfield.setText("180")
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
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.filterCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.filterCheckbox.setGeometry(QtCore.QRect(170, 430, 70, 17))
        self.filterCheckbox.setObjectName("filterCheckbox")
        self.commentsTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.commentsTextField.setGeometry(QtCore.QRect(620, 410, 251, 85))
        self.commentsTextField.setObjectName("idTextField")
        self.idTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.idTextField.setGeometry(QtCore.QRect(620, 500, 251, 25))
        self.idTextField.setObjectName("idTextField")
        self.patientNameTextfield = QtWidgets.QTextEdit(self.centralwidget)
        self.patientNameTextfield.setGeometry(QtCore.QRect(620, 290, 251, 25))
        self.patientNameTextfield.setObjectName("patientNameTextfield")
        self.sexLabel = QtWidgets.QLabel(self.centralwidget)
        self.sexLabel.setGeometry(QtCore.QRect(480, 350, 111, 20))
        self.sexLabel.setObjectName("sexLabel")
        self.sexCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.sexCheckbox.setGeometry(QtCore.QRect(620, 350, 70, 17))
        self.sexCheckbox.setObjectName("sexCheckbox")
        self.patientNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientNameLabel.setGeometry(QtCore.QRect(480, 290, 111, 20))
        self.patientNameLabel.setObjectName("patientNameLabel")
        self.patientSurnameTextfield = QtWidgets.QTextEdit(self.centralwidget)
        self.patientSurnameTextfield.setGeometry(QtCore.QRect(620, 320, 251, 25))
        self.patientSurnameTextfield.setObjectName("patientSurnameTextfield")
        self.patientSurnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientSurnameLabel.setGeometry(QtCore.QRect(480, 320, 111, 20))
        self.patientSurnameLabel.setObjectName("patientSurnameLabel")
        self.examinationDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.examinationDateLabel.setGeometry(QtCore.QRect(480, 380, 71, 20))
        self.examinationDateLabel.setObjectName("examinationDateLabel")
        self.commentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.commentsLabel.setGeometry(QtCore.QRect(480, 410, 61, 16))
        self.commentsLabel.setObjectName("commentsLabel")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(480, 500, 61, 16))
        self.idLabel.setObjectName("idLabel")
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
        self.patientNameLabel.setText(_translate("MainWindow", "Imię pacjenta"))
        self.patientSurnameLabel.setText(_translate("MainWindow", "Nazwisko pacjenta"))
        self.sexLabel.setText(_translate("MainWindow", "Mężczyzna"))
        self.examinationDateLabel.setText(_translate("MainWindow", "Data badania"))
        self.commentsLabel.setText(_translate("MainWindow", "Komentarz"))
        self.idLabel.setText(_translate("MainWindow", "ID Pacjenta"))


    def setImage(self):
        self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Wybierz obraz", "",
                                                                  "Image Files (*.png *.jpg *.jpeg *.bmp);; Dicom Files (*.dcm)")
        if self.imagePath:
            if not self.imagePath.endswith(".dcm"):
                pixmap = QtGui.QPixmap(self.imagePath)
                pixmap = pixmap.scaled(self.inputImage.width(), self.inputImage.height(), QtCore.Qt.KeepAspectRatio)
                self.inputImage.setPixmap(pixmap)
                self.inputImage.setAlignment(QtCore.Qt.AlignCenter)
            else:
                patientName = None
                patientSex = None
                studyDate = None
                comment = None
                patientID = None
                ds = pydicom.dcmread(self.imagePath)
                try:
                    patientID = str(ds.PatientID)
                except AttributeError:
                    pass
                try:
                    patientName = str(ds.PatientName)
                except AttributeError:
                    pass
                try:
                    studyDate = str(ds.StudyDate)
                except AttributeError:
                    pass
                try:
                    patientSex = str(ds.PatientSex)
                except AttributeError:
                    pass
                try:
                    comment = str(ds.ImageComments)
                except AttributeError:
                    pass
                if patientID:
                    self.idTextField.setText(patientID)
                if patientName:
                    self.patientNameTextfield.setText(str(patientName)[0:str(patientName).index(" ")])
                    self.patientSurnameTextfield.setText(str(patientName)[str(patientName).index(" ")+1:])
                if patientSex:
                    if patientSex == "M" or patientSex == None:
                        self.sexCheckbox.setChecked(True)
                if studyDate:
                    self.dateEdit.setDate(QtCore.QDate(int(studyDate[0:4]), int(studyDate[4:6]), int(studyDate[6:8])))
                else:
                    self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
                if comment:
                    self.commentsTextField.setText(comment)

                image = ds.pixel_array
                image = np.multiply(image, 255.0 / np.max(image))
                image = image.astype('uint8')
                io.imsave("dicom.png", image)
                pixmap = QtGui.QPixmap("dicom.png")
                pixmap = pixmap.scaled(self.inputImage.width(), self.inputImage.height(), QtCore.Qt.KeepAspectRatio)
                self.inputImage.setPixmap(pixmap)
                self.inputImage.setAlignment(QtCore.Qt.AlignCenter)

    def showSinogram(self, width):
        img = QtGui.QImage(self.sinogramPath)
        img2 = img.copy(0, 0, int(img.width() * width / 10), img.height())
        pixmap = QtGui.QPixmap(img2)
        pixmap = pixmap.scaled(self.sinogram.width(), self.sinogram.height(), QtCore.Qt.KeepAspectRatio)
        self.sinogram.setPixmap(pixmap)
        self.sinogram.setAlignment(QtCore.Qt.AlignLeft)
        self.showReconstructed(width)


    def showReconstructed(self, iteration):
        img = QtGui.QImage("rec" + str(iteration) + ".png")
        pixmap = QtGui.QPixmap(img)
        pixmap = pixmap.scaled(self.outputImage.width(), self.outputImage.height(), QtCore.Qt.KeepAspectRatio)
        self.outputImage.setPixmap(pixmap)
        self.outputImage.setAlignment(QtCore.Qt.AlignLeft)


    def startProcessing(self):
        self.processImage(float(self.alphaStepTextfield.text()), int(self.numOfDetectorsTextfield.text()),
                              int(self.angularRangeTextfield.text()))


    def normalizeImage(self, image):
        maxx = np.amax(image)
        minn = np.amin(image)
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = (image[i][j] - minn) / (maxx - minn)
        return image

    def processImage(self, step, numOfDetectors, angleRange):
        img = io.imread(self.imagePath)
        img = color.rgb2gray(img)
        img = resize(img, (180, 180))
        m = len(img[0]) // 2
        n = len(img) // 2
        sinogram = np.zeros((numOfDetectors, int(180 / step)))
        radius = ((len(img) ** 2 + len(img[0]) ** 2) ** 0.5) / 2  # okrąg opisany na obrazku
        for k in np.arange(1, 180.1, step):             # generacja sinogramu
            angles = np.linspace(k, k + angleRange, numOfDetectors)
            detectorAngles = np.copy(angles)
            detectorAngles = np.flip(detectorAngles)
            detectorAngles += 180
            if numOfDetectors % 2 == 0: # emitery i detektory strzelają promieniami w takim kierunku, aby środkowy promień przechodził przez środek okręgu
                a = sin(radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2)) / cos(radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2))
            else:
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
            #print(k, a)
            for i, angle in enumerate(angles):
                emiterX = int(round(radius * cos(radians(angle))))
                emiterY = int(round(radius * sin(radians(angle))))
                detectorX = int(round(radius * cos(radians(detectorAngles[i]))))
                detectorY = int(round(radius * sin(radians(detectorAngles[i]))))
                b = emiterY - a * emiterX
                deltax = detectorX - emiterX
                deltay = detectorY - emiterY
                error = 0
                if a <= -1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = emiterX
                    for y in range(emiterY, detectorY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            x = x + 1
                            error -= 1
                elif -1 < a < 0:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    y = emiterY
                    for x in range(emiterX, detectorX + 1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif 0 < a < 1:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    error = 0
                    y = detectorY
                    for x in range(detectorX, emiterX + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif a >= 1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = detectorX
                    for y in range(detectorY, emiterY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            x = x - 1
                            error -= 1

        if self.filterCheckbox.isChecked():  # filtracja sinogramu
            mask = [1]
            for i in range(1, 21):
                if i % 2 == 0:
                    toAdd = 0
                else:
                    toAdd = -4 / pi ** 2 / i ** 2
                mask.insert(0, toAdd)
                mask.append(toAdd)
            print(mask)

            sinogram = self.normalizeImage(sinogram)

            for i in range(len(sinogram[0])):
                for j in range(len(sinogram)):
                    acc = 0
                    for k in range(-20, 21):
                        if 0 <= j + k < len(sinogram):
                            acc += sinogram[j + k][i] * mask[k + 20]
                    sinogram[j][i] = max(0, acc)

        io.imsave("sinogram.png", resize(sinogram, (191, 251)))
        self.sinogramPath = "sinogram.png"
        self.progressSlider.setMinimum(0)
        self.progressSlider.setMaximum(10)
        self.progressSlider.setSingleStep(1)
        self.progressSlider.valueChanged.connect(self.showSinogram)

        reconstructedImage = np.zeros((len(img), len(img[0])))              # rekonstrukcja obrazu
        for k in np.arange(1, 181, step):
            angles = np.linspace(k, k + angleRange, numOfDetectors)
            detectorAngles = np.copy(angles)
            detectorAngles = np.flip(detectorAngles)
            detectorAngles += 180
            if numOfDetectors % 2 == 0:
                a = sin(radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2)) / cos(
                    radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2))
            else:
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
            print(k, a)
            for i, angle in enumerate(angles):
                emiterX = int(round(radius * cos(radians(angle))))
                emiterY = int(round(radius * sin(radians(angle))))
                detectorX = int(round(radius * cos(radians(detectorAngles[i]))))
                detectorY = int(round(radius * sin(radians(detectorAngles[i]))))
                b = emiterY - a * emiterX
                deltax = detectorX - emiterX
                deltay = detectorY - emiterY
                error = 0
                if a <= -1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = emiterX
                    for y in range(emiterY, detectorY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step)]
                        error += deltaerr
                        if error >= 0.5:
                            x = x + 1
                            error -= 1
                elif -1 < a < 0:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    y = emiterY
                    for x in range(emiterX, detectorX + 1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step)]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif 0 < a < 1:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    error = 0
                    y = detectorY
                    for x in range(detectorX, emiterX + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step)]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif a >= 1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = detectorX
                    for y in range(detectorY, emiterY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step)]
                        error += deltaerr
                        if error >= 0.5:
                            x = x - 1
                            error -= 1
            if k // 18 != (k - step) // 18:
                io.imsave("rec" + str(int(k // 18)) + ".png", reconstructedImage)

        # KONIEC REKONSTRUKCJI

        self.reconstructedPath = "rec10.png"

        reconstructedImage = self.normalizeImage(reconstructedImage)
        lo, hi = np.percentile(reconstructedImage, (2, 98))
        reconstructedImage = rescale_intensity(reconstructedImage, in_range=(lo, hi))
        io.imsave(self.reconstructedPath, reconstructedImage)

        img = self.normalizeImage(img)
        rmse = 0
        for i in range(len(img)):
            for j in range(len(img[i])):
                rmse += (img[i][j] - reconstructedImage[i][j]) ** 2
        rmse /= img.shape[0] * img.shape[1]
        rmse **= 0.5
        print(rmse)


        #reconstructedImage = reconstructedImage.astype(np.int64)
        #reconstructedImage -= np.amin(reconstructedImage)
        reconstructedImage = (reconstructedImage / np.amax(reconstructedImage)) * 255
        reconstructedImage = reconstructedImage.astype(np.int16)

        file_meta = pydicom.dataset.Dataset()
        file_meta.MediaStorageSOPClassUID = pydicom.uid.generate_uid()
        file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
        file_meta.ImplementationClassUID = pydicom.uid.generate_uid()
        file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian

        patientID = self.idTextField.toPlainText()
        filename = self.dateEdit.date().toString('yyyyMMdd') + patientID + str(random.randrange(100))
        ds = pydicom.dataset.FileDataset(filename + ".dcm", {}, file_meta=file_meta, preamble=b"\0" * 128)
        ds.PatientID = patientID
        ds.PatientName = self.patientNameTextfield.toPlainText() + " " + self.patientSurnameTextfield.toPlainText()
        ds.StudyDate = self.dateEdit.date().toString('yyyyMMdd')
        ds.StudyID = str(ds.StudyDate) + ds.PatientID
        ds.ImageComment = self.commentsTextField.toPlainText()
        if self.sexCheckbox.isChecked():
            ds.PatientSex = "M"
        else:
            ds.PatientSex = "F"

        ds.SeriesInstanceUID = pydicom.uid.generate_uid()
        ds.StudyInstanceUID = pydicom.uid.generate_uid()
        ds.FrameOfReferenceUID = pydicom.uid.generate_uid()
        ds.SOPClassUID = pydicom.uid.generate_uid()
        ds.SOPInstanceUID = pydicom.uid.generate_uid()

        ds.Modality = "CT"
        ds.ImagesInAcquisition = "1"
        ds.InstanceNumber = 1
        ds.PixelData = reconstructedImage.tobytes()
        ds.BitsAllocated = 16
        ds.Rows = len(reconstructedImage)
        ds.Columns = len(reconstructedImage[0])
        ds.PixelRepresentation = 0
        ds.SamplesPerPixel = 1
        ds.BitsStored = 16
        ds.HighBit = 15
        ds.PhotometricInterpretation = "MONOCHROME2"
        ds.SmallestImagePixelValue = b'\\x00\\x00'
        ds.LargestImagePixelValue = b'\\xff\\xff'

        ds.is_little_endian = True
        ds.is_implicit_VR = True
        dt = datetime.datetime.now()
        ds.ContentDate = dt.strftime('%Y%m%d')
        timeStr = dt.strftime('%H%M%S.%f')
        ds.ContentTime = timeStr
        ds.save_as(filename + ".dcm")
        ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRBigEndian
        ds.is_little_endian = False
        ds.is_implicit_VR = False
        ds.save_as(filename + ".dcm")






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
