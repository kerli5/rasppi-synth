from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import pyqtSignal
from drumpad import DrumPad
from topbar import TopBar
from styles import STYLESHEET
import sys
from drumpad import DrumPad
from styles import STYLESHEET, ALT_STYLESHEET, topbar, ALT_TOPBAR


page_indices = {
    'drumpad': 0
}

class Raspsynth(QMainWindow):
    navigationRequested = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        try:
            print("Program is working.")
            # window params
            self.setWindowTitle("rasppy v0.0.1")
            ##self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self.setStyleSheet(STYLESHEET)
            self.setGeometry(20, 20, 1080, 720)
            # central widget
            self.widget = QStackedWidget()
            self.setCentralWidget(self.widget)

            # pages
            drumpad_widget = DrumPad(self)
            self.widget.addWidget(drumpad_widget)

            # top bar (toolbar)
            self.topbar = TopBar(self)
            self.addToolBar(self.topbar)

            self.topbar.navigationRequested.connect(self.setPage)

            self.topbar.themeToggleRequested.connect(self.toggleTheme)

            self.setPage('drumpad')
        except Exception as e:
            print("Something went wrong.", e)

    def setPage(self, page_name: str):
        idx = page_indices.get(page_name, 0)
        self.widget.setCurrentIndex(idx)

    def toggleTheme(self):
        # compare current stylesheet and swap
        if self.styleSheet() == STYLESHEET:
            self.setStyleSheet(ALT_STYLESHEET)
            self.topbar.setStyleSheet(ALT_TOPBAR)
        else:
            self.setStyleSheet(STYLESHEET)
            self.topbar.setStyleSheet(topbar)

def main():
    app = QApplication(sys.argv)
    window = Raspsynth()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()