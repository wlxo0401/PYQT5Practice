import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('btn1', self)
        btn2 = QPushButton('btn2', self)
        btn3 = QPushButton('bddd', self)
        
        btn1.move(30, 50)
        btn2.move(150, 50)
        btn3.move(270, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)

        self.statusBar()


        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('ICN')
        self.show()
        
    # 나자신을 넘겨 받아서 
    def buttonClicked(self):
        # sender 메소드는 함수를 호출한 개체를 가지고 온다.
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())