import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QGridLayout, QListWidget, QListWidgetItem, QDesktopWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']
        self.current_index = 0
        self.filtered_items = self.items[:]

        self.initUI()

    def initUI(self):
        self.path_input = QLineEdit(self)
        self.path_input.setPlaceholderText('Enter path here')
        open_button = QPushButton('Open', self)
        open_button.clicked.connect(self.open_path)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(open_button)

        self.filter_input1 = QLineEdit(self)
        self.filter_input1.setPlaceholderText('Filter 1')
        self.filter_input1.textChanged.connect(self.apply_filter)
        self.filter_input2 = QLineEdit(self)
        self.filter_input2.setPlaceholderText('Filter 2')
        self.filter_input2.textChanged.connect(self.apply_filter)

        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.filter_input1)
        filter_layout.addWidget(self.filter_input2)

        prev_button = QPushButton('Previous', self)
        prev_button.clicked.connect(self.previous)
        next_button = QPushButton('Next', self)
        next_button.clicked.connect(self.next)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(prev_button)
        nav_layout.addWidget(next_button)

        self.list_widget = QListWidget()
        self.list_widget.setFixedWidth(800)
        self.populate_list()

        self.labels_grid = QGridLayout()
        self.populate_labels()

        main_layout = QVBoxLayout()
        main_layout.addLayout(path_layout)
        main_layout.addLayout(filter_layout)
        main_layout.addLayout(nav_layout)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.list_widget)
        top_layout.addLayout(self.labels_grid)
        main_layout.addLayout(top_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Qt GUI')
        self.setGeometry(400, 400, 1200, 800)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.show()

    def populate_list(self):
        self.list_widget.clear()
        for item in self.filtered_items:
            item_widget = QListWidgetItem(item)
            self.list_widget.addItem(item_widget)

        self.list_widget.currentItemChanged.connect(self.update_labels)

    def update_labels(self, current, previous):
        if current is not None:
            selected_item = current.text()
            for i in range(min(12, len(selected_item))):
                label_name = f"Label {i+1}"
                label = QLabel(f"{label_name}: {selected_item[i]}", self)
                self.labels_grid.addWidget(label, i, 0)

    def populate_labels(self):
        for i in range(12):
            label_name = f"Label {i+1}"
            label = QLabel(label_name, self)
            self.labels_grid.addWidget(label, i, 0)

    def previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.populate_labels()

    def next(self):
        if self.current_index + 1 < len(self.filtered_items):
            self.current_index += 1
            self.populate_labels()

    def apply_filter(self):
        filter1 = self.filter_input1.text().lower()
        filter2 = self.filter_input2.text().lower()

        self.filtered_items = [item for item in self.items if filter1 in item.lower() and filter2 in item.lower()]
        self.populate_list()

    def open_path(self):
        path = self.path_input.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
