import sys
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        # H는 가로
        sld = QSlider(Qt.Horizontal, self)

        # 세로로 쌓는 Vbox 레이아웃 선언
        vBox = QVBoxLayout()
        # vBox에 위젯 추가
        vBox.addWidget(lcd)
        vBox.addWidget(sld)

        self.setLayout(vBox)
        # 슬라이더 값이 변경되면 연결 될 슬롯 설정?(lcd.display)=QLCDNumber에 정의가 돼어있을듯
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('ICN')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())