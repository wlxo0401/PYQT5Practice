import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('CANCEL')

        hBox = QHBoxLayout()
        # 버튼 두개가 차지 하지 않고있는 공간 만큼 늘어난다?
        hBox.addStretch(1)
        hBox.addWidget(okButton)
        hBox.addWidget(cancelButton)

        vBox = QVBoxLayout()
        vBox.addStretch(1)
        vBox.addLayout(hBox)

        self.setLayout(vBox)


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('ICN')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

        