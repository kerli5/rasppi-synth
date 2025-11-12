from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class DrumPad(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10)

        for row in range(2):
            for col in range(4):
                ##naming pads
                btn = QPushButton("Pad" + str(row * 4 + col + 1))
                btn.setFixedSize(100, 100)
                btn.setStyleSheet("""
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
                #calls the pad_clicked() function.
                #which button number it was.
                btn.clicked.connect(lambda _, b=row * 4 + col + 1: self.pad_clicked(b))
                layout.addWidget(btn, row, col)

        self.setLayout(layout)

    def pad_clicked(self, pad_number):
        print("Pad" + str(pad_number) + "clicked!")
