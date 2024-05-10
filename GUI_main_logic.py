import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from string_to_dict import create_dict_list, create_list_from_file
from get_ipv4s_from_log import get_ipv4s_from_log
from create_SSH_log_journal import create_journal as cre

from SSH_log_browser import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.fillList()

    def connectSignalsSlots(self):
        ...

    # def findAndReplace(self):
    #     dialog = FindReplaceDialog(self)
    #     dialog.exec()

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

# class FindReplaceDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         loadUi("ui/find_replace.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())