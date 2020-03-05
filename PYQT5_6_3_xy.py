import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = 'x : {0}, y : {1}'.format(x,y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop) #AlignTop 정렬
        # 마우스 포인터를 하겠다. 평소에는 꺼있음.
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('ICN')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = 'x : {0}, y : {1}'.format(x,y)
        self.label.setText(text)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())