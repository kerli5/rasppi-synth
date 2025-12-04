from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import pyqtSignal
from styles import STYLESHEET, ALT_STYLESHEET, topbar, ALT_TOPBAR
from drumpad import DrumPad
from topbar import TopBar
import sys
import os


##env variables
os.environ['GPIOZERO_PIN_FACTORY']='mock' ##for use in dev



page_indices = {
    'drumpad': 0
}

class Raspsynth(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            print("Program is working.")
            # window params
            self.setWindowTitle("rasppy v0.0.1")
            ##self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self.setStyleSheet(STYLESHEET)
            self.setGeometry(20, 20, 300, 300)
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

            self.topbar.volumeChanged.connect(self.updateVolume)

            self.setPage('drumpad')
        except Exception as e:
            print("Something went wrong.", e)

    def updateVolume(self, value:int):
        volume = max(0.0, min(1.0, value / 100))
        current = self.widget.currentWidget()
        if hasattr(current, 'pads'):
            for pad, _ in current.pads:
                if hasattr(pad, 'audio') and hasattr(pad.audio, 'set_volume'):
                    pad.audio.set_volume(volume)


    def setPage(self, page_name: str):
        idx = page_indices.get(page_name, 0)
        self.widget.setCurrentIndex(idx)

    def toggleTheme(self):
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