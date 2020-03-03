import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    # Qwidget에 해당하는 상위 객체를 생성
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('클릭', self)
        # btn1 버튼의 사이즈 조절하는데 sizeHint를 하면 글씨?에 따른 사이즈조절
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip('툴팁입니다. <b>안녕하세요</b>')
        btn1.move(20, 30)
        self.setGeometry(800,300,500,500)
        self.setWindowTitle('첫 번째 학습시간.')
        self.show()



app = QApplication(sys.argv)

window = Exam()
# 프로그램을 깔끔하게 종료한다?
# app.exec 이벤트 처리를 위한 메인루프? 클릭,드래그,입력 등등 app.exec가 끝나면 sys.exit가 실행된다.
sys.exit(app.exec_())

