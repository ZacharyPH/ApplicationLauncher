import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QMessageBox)


class Dialog(QDialog):
    @staticmethod
    def slot_method():
        print('slot method called.')

    def __init__(self):
        super().__init__()

        button = QPushButton("Click")
        button.clicked.connect(self.slot_method)

        main_layout = QVBoxLayout()
        main_layout.addWidget(button)

        self.setLayout(main_layout)
        self.setWindowTitle("Button Example - pythonspot.com")


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Application Launcher"
        self.left = 35
        self.top = 50
        self.w = 640
        self.h = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.w, self.h)
        button = QPushButton("Button", self)
        button.setToolTip("Push Me!")
        button.move(300, 170)
        button.clicked.connect(self.click)
        self.show()

    @pyqtSlot()
    def click(self):
        print("Button clicked!")
        # Dialog().exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # App init
    ex = App()
    sys.exit(app.exec_())  # Looks like this returns 0 if the app runs successfully

# TODO: Signals and Slots: https://pythonspot.com/pyqt5-signals-and-slots/
