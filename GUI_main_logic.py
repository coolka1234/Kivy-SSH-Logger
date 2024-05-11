import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from SSHLogEntry import SSHLogEntry as SSH
from string_to_dict import create_dict_list, create_list_from_file
from get_ipv4s_from_log import get_ipv4s_from_log
from create_SSH_log_journal import create_journal as cre

from log_browser import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.fillList()
        self.listOfLogs.clicked.connect(self.updateLabels)
        self.comboBoxSSHOrHTTP.addItems(["SSH", "HTTP"])
        self.comboBoxSSHOrHTTP.currentIndexChanged.connect(self.updateLabelTypes)
        
    def connectSignalsSlots(self):
        ...


    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )
    def fillList(self):
        self.listOfLogs.clear()
        for log in cre("SSH_log_test.log"):
            self.listOfLogs.addItem(log._raw_desc)
    def updateLabels(self):
        selected_item = self.listOfLogs.currentItem()
        if selected_item is not None:
            log=SSH(selected_item.text())
            self.labelRemoteHost.setText(log.get_ipv4s())
            self.labelDate.setText(f"{log.month} {log.day}")
            self.labelTime.setText(log.time)
        else:
            self.labelDescription.setText("")
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
            self.labelMethodL.setText("Description")
            self.labelResourceL.setText("")
            self.labelSizeL.setText("")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())