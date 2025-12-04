from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMenu
from audio import AudioPlayer
import tkinter
from gpiozero import Button
from tkinter import filedialog
from topbar import TopBar
import os

matrix_size = 2

def getProjectBPM():
    return TopBar().bpmslider.value()

class Pad(QPushButton):
    def __init__(self, number = None, path = None, parent = None, loop:bool = False, bpm:int = None):
        super().__init__(parent)
        self.path = path
        self.pad_num = number
        self.loop = loop

        self.bpm = getProjectBPM()
        self.audio = AudioPlayer(self.bpm, self.loop)

        self.gpio = Button(self.pad_num + 1)

        self.setFixedSize(150, 150) ## panna drumpad style style sisse


        if self.pad_num is not None:
            self.setText(f"Pad {self.pad_num}")

        self.clicked.connect(self.audio.play_audio)


    def play_audio(self):
        self.audio.play_audio()

    def contextMenuEvent(self, a0): ## a0 -> event if its not working
        menu = QMenu(self)
        
        pad_changeState = menu.addMenu("Pad state")
        pad_modify = menu.addAction("Modify")
        pad_reset = menu.addAction("Reset")

        trigger_state = pad_changeState.addAction("Trigger")
        loop_state = pad_changeState.addAction("Loop")

        action = menu.exec(a0.globalPos())

        if action == pad_modify:
            self.modifyMusicFile()
        elif action == pad_reset:
            self.resetMusicFile()

        ##submenu actions
        if action == trigger_state:
            self.changeStateTrigger()
        elif action == loop_state:
            self.changeStateLoop()

    def changeStateTrigger(self):
        self.loop = False
        print(f"Looping:{self.loop}")
    def changeStateLoop(self):
        self.loop = True
        print(f"Looping:{self.loop}")

    def modifyMusicFile(self):
        tkinter.Tk().withdraw()
        self.path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .mp3"),   ("All Files", "*.*")))
        if self.path != "":
            file_name = os.path.split(self.path)[1]
            self.audio.load_audio(self.path)
            print(f"Path:{self.path}")
            self.setText(file_name)
    def resetMusicFile(self):
        if self.path is not None:
            self.path = None
            self.setText(f"Pad {self.pad_num}")

class DrumPad(QWidget):
    pads = []
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
    
    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10) 
        for row in range(matrix_size):
            for col in range(matrix_size):
                pad_num = row * matrix_size + col + 1
                pad = Pad(pad_num)
                layout.addWidget(pad, row, col)
                self.pads.append([pad, pad_num])

        self.setLayout(layout)
