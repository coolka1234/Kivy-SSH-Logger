import datetime
import sys
import time

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDateTime
from SSHLogEntry import SSHLogEntry as SSH
from string_to_dict import create_dict_list, create_list_from_file
from get_ipv4s_from_log import get_ipv4s_from_log
from create_SSH_log_journal import create_journal as cre
from HTTPLogEntry import HTTPLogEntry as HTTP
from log_browser import Ui_MainWindow
from datetime import datetime, time

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.listOfLogs.clicked.connect(self.updateLabels)
        self.comboBoxSSHOrHTTP.addItems(["HTTP", "SSH"])
        self.comboBoxSSHOrHTTP.currentIndexChanged.connect(self.updateLabelTypes)
        self.PathButton.clicked.connect(lambda: self.fillList(file_name=self.pathInput.toPlainText()))
        self.pushButtonFilterDates.clicked.connect(self.filterLogsByDate)
    def fillList(self, file_name):
        self.listOfLogs.clear()
        if file_name == "":
            QMessageBox.warning(self, "Warning", "Please enter a file name")
            return
        for log in cre(file_name):
            self.listOfLogs.addItem(log._raw_desc)
        self.updateLabelsFromProgram(determineLogIsHTTP(self.listOfLogs.item(0).text()))
        
    def updateLabels(self):
        selected_item = self.listOfLogs.currentItem()
        if selected_item is not None and not determineLogIsHTTP(selected_item.text()):
            log=SSH(selected_item.text())
            self.labelRemoteHost.setText(log.pid)
            self.labelDate.setText(f"{log.month} {log.day}")
            self.labelTime.setText(log.time)
            self.labelTimezone.setText(log.username)
            self.labelStatusCode.setText(log.get_messege_type())
        elif selected_item is not None and determineLogIsHTTP(selected_item.text()):
            log=HTTP(selected_item.text())
            self.labelRemoteHost.setText(log.remote_host)
            self.labelDate.setText(log.date)
            self.labelTime.setText(log.time)
            self.labelTimezone.setText(log.timezone)
            self.labelStatusCode.setText(log.get_messege_type())
            self.labelMethod.setText(log.method)
            self.labelResource.setText(log.resource)
            self.labelSize.setText(log.size)
    def updateLabelTypes(self):
        selected_item = self.comboBoxSSHOrHTTP.currentText()
        if selected_item is not None and selected_item == "HTTP":
            self.labelDateRemoteHostL.setText("Remote Host")
            self.labelDateL.setText("Date")
            self.labelTimeL.setText("Time")
            self.labelTimezoneL.setText("Timezone")
            self.labelStatusCodeL.setText("Status Code")
            self.labelMethodL.setText("Method")
            self.labelResourceL.setText("Resource")
            self.labelSizeL.setText("Size")
        else:
            self.labelDateRemoteHostL.setText("Pid")
            self.labelDateL.setText("Date")
            self.labelTimeL.setText("Time")
            self.labelTimezoneL.setText("User")
            self.labelStatusCodeL.setText("Type")
            self.labelMethodL.setText("")
            self.labelResourceL.setText("")
            self.labelSizeL.setText("")
    def updateLabelsFromProgram(self, bool):
        if bool:
            self.labelDateRemoteHostL.setText("Remote Host")
            self.labelDateL.setText("Date")
            self.labelTimeL.setText("Time")
            self.labelTimezoneL.setText("Timezone")
            self.labelStatusCodeL.setText("Status Code")
            self.labelMethodL.setText("Method")
            self.labelResourceL.setText("Resource")
            self.labelSizeL.setText("Size")
            self.comboBoxSSHOrHTTP.setCurrentIndex(0)
        else:
            self.labelDateRemoteHostL.setText("Pid")
            self.labelDateL.setText("Date")
            self.labelTimeL.setText("Time")
            self.labelTimezoneL.setText("User")
            self.labelStatusCodeL.setText("Type")
            self.labelMethodL.setText("")
            self.labelResourceL.setText("")
            self.labelSizeL.setText("")
            self.comboBoxSSHOrHTTP.setCurrentIndex(1)
    def filterLogsByDate(self):
        start_date = self.dateEdit.date().toPyDate()
        start_date = datetime.combine(start_date, time())
        end_date = self.dateEdit_2.date().toPyDate()
        end_date = datetime.combine(end_date, time())
        filtered_logs = []
        for i in range(self.listOfLogs.count()):
            log_item = self.listOfLogs.item(i)
            log = log_item.text()
            if determineLogIsHTTP(log):
                log_obj = HTTP(log)
                log_date = log_obj.get_datetime()
            else:
                log_obj = SSH(log)
                log_date = log_obj.get_date()
            if start_date <= log_date <= end_date:
                filtered_logs.append(log)
        self.listOfLogs.clear()
        for log in filtered_logs:
            self.listOfLogs.addItem(log)

def determineLogIsHTTP(log):
    if log[0].isdigit():
        return True
    else:
        return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())