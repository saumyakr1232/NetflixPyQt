import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5 import  QtCore
from PyQt5.QtGui import QIcon

from pages.MainWindow import LandingPage
from pages.SearchWindow import SearchWindow
from pages.LoginPage import LoginPage

from pages.PageWindow import PageWindow





class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.resize(int(self.width * .8), int(self.height * .8))
        self.setWindowIcon(QIcon('netflix-logo-png-2574-64x64.ico'))
        # self.setStyleSheet('background-color:grey')
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}
        self.register(LandingPage(), "main")
        self.register(SearchWindow(), "search")
        self.register(LoginPage(), "loginPage")

        self.goto("main")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())





def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
