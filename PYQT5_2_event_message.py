import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('Push me!', self)
        btn1.move(50, 50)
        btn1.setToolTip('누르면 반응합니다.')
        btn1.clicked.connect(QCoreApplication.instance().quit)
        self.resize(500, 500)
        self.setWindowTitle('프로그램 공부 입니다.')
        self.show()
    def closeEvent(self, QCloseEvent):
        # 예스,노를 만들고 맨뒤 노는 기본값 ex 막 엔터누르면 no가 눌림
        ans = QMessageBox.question(self, '종료입니다.', '종료하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())