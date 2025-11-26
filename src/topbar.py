from PyQt6.QtWidgets import QToolBar, QWidget, QLabel, QSizePolicy
from PyQt6.QtGui import QFont, QAction, QActionGroup, QIcon
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from styles import topbar

class TopBar(QToolBar):
    navigationRequested = pyqtSignal(str)
    themeToggleRequested = pyqtSignal() 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setMovable(False)
        self.setStyleSheet(topbar)

        title = QLabel("rasppy")
        title.setFont(QFont("Arial", 14))
        self.addWidget(title)

        self.pageswitches = QActionGroup(self)
        self.pageswitches.setExclusive(True)

        self.drumpad_btn = QAction("Drumpad", self)
        self.drumpad_btn.setCheckable(True)
        self.drumpad_btn.setChecked(True)
        self.drumpad_btn.triggered.connect(lambda event: print("Drumpad"))
        self.pageswitches.addAction(self.drumpad_btn)
        self.addAction(self.drumpad_btn)

        self.record_btn = QAction("Record", self)
        self.record_btn.setIcon(QIcon("src/resources/icons/record-icon.svg"))
        self.record_btn.setCheckable(True)
        self.pageswitches.addAction(self.record_btn)
        try:
            self.record_btn.toggled.connect(self.enableRecordBtn)
        except Exception as e:
            print(e)
        self.addAction(self.record_btn)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.addWidget(spacer)

        theme_button = self.addAction("Theme")
        theme_button.triggered.connect(self._handle_theme_toggle)

        close_button = self.addAction("x")
        close_button.setToolTip("Close")
        close_button.triggered.connect(self._handle_close)

    def _handle_close(self):
        if self.parent is not None:
            self.parent.close()

    def _handle_theme_toggle(self):
        self.themeToggleRequested.emit()
