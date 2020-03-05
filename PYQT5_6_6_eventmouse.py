import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        
        self.c = Communicate()
        self.c.closeApp.connect(self.close)


        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('ICN')
        self.show()
        
    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())