from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMenu
from PyQt6.QtCore import Qt
import sys

class Pad(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(150, 150)
        self.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
        """)

class DrumPad(QWidget):
    pads = []
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.pads = []
    
    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10)

        for row in range(4):
            for col in range(4):
                pad_num = row * 4 + col + 1
                pad = Pad()
                pad.setText("Pad {num}".format(num = pad_num))
                pad.clicked.connect(lambda x, n=pad_num: self.pad_clicked(n))
                layout.addWidget(pad, row, col)
                self.pads.append([pad, pad_num])

        self.setLayout(layout)

    def pad_clicked(self, pad_number):
        print("Pad{} clicked!".format(pad_number))