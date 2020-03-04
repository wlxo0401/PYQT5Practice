import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication
class Exam(QMainWindow):
    # Qwidget에 해당하는 상위 객체를 생성
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage('안녕하세요.')


        # 메뉴바를 생성
        menu = self.menuBar()
        # 그룹들을 생성
        menu_file = menu.addMenu('File')
        menu_file.setStatusTip('파일 메뉴를 봅니다.')

        menu_second = menu.addMenu('Second')
        menu_second.setStatusTip('두번째 메뉴를 봅니다.')

        menu_third = menu.addMenu('Third')
        menu_third.setStatusTip('세번째 메뉴를 봅니다.')

        menu_view = menu.addMenu('View')
        menu_view.setStatusTip('View메뉴입니다.')

        # 사이드 메뉴 생성     
        file_new = QMenu('New', self)
   

        # 메뉴 객체 생성
        file_exit = QAction('Exit', self) 

        new_file = QAction('New File', self)
        new_file.setStatusTip('파일을 생성합니다.')
        
        view_stat = QAction('상태표시줄', self, checkable = True)
        view_stat.setChecked(True)       
        # 단축기등록
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 종료됩니다.')


        # 기능
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        view_stat.triggered.connect(self.tglStat)

        # 메뉴 추가
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)
        file_new.addAction(new_file)
        menu_view.addAction(view_stat)



        self.resize(450, 400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QcontextMenuEvent):
        cm = QMenu(self)
        quit = cm.addAction('Quit')
        action = cm.exec_(self.mapToGlobal(QcontextMenuEvent.pos()))
        if action == quit:
            qApp.quit()



app = QApplication(sys.argv)

window = Exam()
# 프로그램을 깔끔하게 종료한다?
# app.exec 이벤트 처리를 위한 메인루프? 클릭,드래그,입력 등등 app.exec가 끝나면 sys.exit가 실행된다.
sys.exit(app.exec_())