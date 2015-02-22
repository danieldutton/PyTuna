from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from audio import notes

class Console(QDialog):

    """Description of class here"""
       
    def __init__(self):
        
        app = QApplication(sys.argv)
        QDialog.__init__(self)
        
        self.size_dialog()
        self.layout = QVBoxLayout()
        self.label = QLabel("Hello")
        self.combo = QComboBox()
        self.playButton = QPushButton("Play")
        self.exitButton = QPushButton("Stop")
        self.do_shit()
        
        app.exec_()

    def size_dialog(self):
        self.setMinimumSize(200, 200)
        self.setMaximumSize(200, 200)
        self.resize(200, 200)

    def do_shit(self):
        print("Application Starting")
               
        self.init_labels()  
        self.init_combobox()
        self.init_buttons()   
        self.init_layout()
        self.show()

    def init_labels(self):
        pass
        
    def init_combobox(self):        
        self.combo.addItems(notes.Notes.get_guitar_notes_six_string())

    def init_buttons(self):       
        self.playButton.clicked.connect(self.clicker)
        #self.exitButton.clicked.connnect()

    def init_layout(self):
        self.layout.addWidget(self.label)       
        self.layout.addWidget(self.combo)        
        self.layout.addWidget(self.playButton)        
        self.layout.addWidget(self.exitButton)

        self.setLayout(self.layout)

    def clicker(self):
        print("played")







