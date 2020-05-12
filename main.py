import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


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
        button.move(100, 70)
        button.clicked.connect(self.click)
        self.show()

    @pyqtSlot()
    def click(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # App init
    ex = App()
    sys.exit(app.exec_())  # Looks like this returns 0 if the app runs sucessfully

# TODO: Signals and Slot: https://pythonspot.com/pyqt5-signals-and-slots/
