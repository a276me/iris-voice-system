import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
    #设图标
mainWin =  MainWin()
#ui = untitled.Ui_MainWindow()
#ui.setupUi(mainWin)
mainWin.show()
sys.exit(app.exec_())