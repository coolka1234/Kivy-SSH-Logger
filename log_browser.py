# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 558)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 558))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 558))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pathInput = QtWidgets.QTextEdit(self.centralwidget)
        self.pathInput.setGeometry(QtCore.QRect(10, 10, 831, 31))
        self.pathInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pathInput.setObjectName("pathInput")
        self.PathButton = QtWidgets.QPushButton(self.centralwidget)
        self.PathButton.setGeometry(QtCore.QRect(850, 10, 141, 31))
        self.PathButton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.PathButton.setObjectName("PathButton")
        self.listOfLogs = QtWidgets.QListWidget(self.centralwidget)
        self.listOfLogs.setGeometry(QtCore.QRect(10, 120, 541, 381))
        font = QtGui.QFont()
        font.setFamily("Verdana Pro")
        font.setPointSize(11)
        self.listOfLogs.setFont(font)
        self.listOfLogs.setObjectName("listOfLogs")
        self.labelDateFrom = QtWidgets.QLabel(self.centralwidget)
        self.labelDateFrom.setGeometry(QtCore.QRect(10, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.labelDateFrom.setFont(font)
        self.labelDateFrom.setObjectName("labelDateFrom")
        self.labelDateEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelDateEnd.setGeometry(QtCore.QRect(230, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.labelDateEnd.setFont(font)
        self.labelDateEnd.setObjectName("labelDateEnd")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 120, 131, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDateRemoteHostL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelDateRemoteHostL.setFont(font)
        self.labelDateRemoteHostL.setObjectName("labelDateRemoteHostL")
        self.verticalLayout.addWidget(self.labelDateRemoteHostL)
        self.labelDateL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelDateL.setFont(font)
        self.labelDateL.setObjectName("labelDateL")
        self.verticalLayout.addWidget(self.labelDateL)
        self.labelTimeL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelTimeL.setFont(font)
        self.labelTimeL.setObjectName("labelTimeL")
        self.verticalLayout.addWidget(self.labelTimeL)
        self.labelTimezoneL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelTimezoneL.setFont(font)
        self.labelTimezoneL.setObjectName("labelTimezoneL")
        self.verticalLayout.addWidget(self.labelTimezoneL)
        self.labelStatusCodeL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelStatusCodeL.setFont(font)
        self.labelStatusCodeL.setObjectName("labelStatusCodeL")
        self.verticalLayout.addWidget(self.labelStatusCodeL)
        self.labelMethodL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelMethodL.setFont(font)
        self.labelMethodL.setObjectName("labelMethodL")
        self.verticalLayout.addWidget(self.labelMethodL)
        self.labelResourceL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelResourceL.setFont(font)
        self.labelResourceL.setObjectName("labelResourceL")
        self.verticalLayout.addWidget(self.labelResourceL)
        self.labelSizeL = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelSizeL.setFont(font)
        self.labelSizeL.setObjectName("labelSizeL")
        self.verticalLayout.addWidget(self.labelSizeL)
        self.pushButtonPrev = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPrev.setGeometry(QtCore.QRect(10, 510, 131, 41))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(860, 510, 131, 41))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(230, 70, 161, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(700, 120, 291, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelRemoteHost = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelRemoteHost.setFont(font)
        self.labelRemoteHost.setText("")
        self.labelRemoteHost.setObjectName("labelRemoteHost")
        self.verticalLayout_2.addWidget(self.labelRemoteHost)
        self.labelDate = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelDate.setFont(font)
        self.labelDate.setText("")
        self.labelDate.setObjectName("labelDate")
        self.verticalLayout_2.addWidget(self.labelDate)
        self.labelTime = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelTime.setFont(font)
        self.labelTime.setText("")
        self.labelTime.setObjectName("labelTime")
        self.verticalLayout_2.addWidget(self.labelTime)
        self.labelTimezone = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelTimezone.setFont(font)
        self.labelTimezone.setText("")
        self.labelTimezone.setObjectName("labelTimezone")
        self.verticalLayout_2.addWidget(self.labelTimezone)
        self.labelStatusCode = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelStatusCode.setFont(font)
        self.labelStatusCode.setText("")
        self.labelStatusCode.setObjectName("labelStatusCode")
        self.verticalLayout_2.addWidget(self.labelStatusCode)
        self.labelMethod = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelMethod.setFont(font)
        self.labelMethod.setText("")
        self.labelMethod.setObjectName("labelMethod")
        self.verticalLayout_2.addWidget(self.labelMethod)
        self.labelResource = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelResource.setFont(font)
        self.labelResource.setText("")
        self.labelResource.setObjectName("labelResource")
        self.verticalLayout_2.addWidget(self.labelResource)
        self.labelSize = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.labelSize.setFont(font)
        self.labelSize.setText("")
        self.labelSize.setObjectName("labelSize")
        self.verticalLayout_2.addWidget(self.labelSize)
        self.comboBoxSSHOrHTTP = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSSHOrHTTP.setGeometry(QtCore.QRect(850, 70, 141, 31))
        self.comboBoxSSHOrHTTP.setObjectName("comboBoxSSHOrHTTP")
        self.labelDateEnd_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelDateEnd_2.setGeometry(QtCore.QRect(850, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.labelDateEnd_2.setFont(font)
        self.labelDateEnd_2.setObjectName("labelDateEnd_2")
        self.pushButtonFilterDates = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFilterDates.setGeometry(QtCore.QRect(410, 70, 81, 31))
        self.pushButtonFilterDates.setObjectName("pushButtonFilterDates")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log Browser"))
        self.pathInput.setPlaceholderText(_translate("MainWindow", "Input path..."))
        self.PathButton.setText(_translate("MainWindow", "Open file"))
        self.labelDateFrom.setText(_translate("MainWindow", "From:"))
        self.labelDateEnd.setText(_translate("MainWindow", "To:"))
        self.labelDateRemoteHostL.setText(_translate("MainWindow", "Remote Host:"))
        self.labelDateL.setText(_translate("MainWindow", "Date:"))
        self.labelTimeL.setText(_translate("MainWindow", "Time:"))
        self.labelTimezoneL.setText(_translate("MainWindow", "Timezone:"))
        self.labelStatusCodeL.setText(_translate("MainWindow", "Status Code:"))
        self.labelMethodL.setText(_translate("MainWindow", "Method:"))
        self.labelResourceL.setText(_translate("MainWindow", "Resource:"))
        self.labelSizeL.setText(_translate("MainWindow", "Size:"))
        self.pushButtonPrev.setText(_translate("MainWindow", "Previous"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))
        self.labelDateEnd_2.setText(_translate("MainWindow", "Log type:"))
        self.pushButtonFilterDates.setText(_translate("MainWindow", "Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
