import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
 

class MyWindow(QMainWindow): 
    def __init__(self):     
        super().__init__() 

        layoutV = QVBoxLayout()
        layoutH = QHBoxLayout()

        self.inputLabel = QLabel("File:")
        self.txtInput = QLineEdit()
        self.selectButton = QPushButton("Select File...")
        self.outputLabel = QLabel()

        layoutH.addWidget(self.inputLabel)
        layoutH.addWidget(self.txtInput)
        layoutH.addWidget(self.selectButton)
        layoutV.addLayout(layoutH)
        layoutV.addWidget(self.outputLabel)

        self.selectButton.clicked.connect(self.select_clicked)
        self.txtInput.textChanged.connect(self.text_changed)

        center = QWidget()
        center.setLayout(layoutV)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Speichern...")   
        self.show() 

    def text_changed(self):
        self.outputLabel.setText(f"{self.txtInput.text()}")

    def select_clicked(self):
        path, format = QFileDialog.getOpenFileName(self, "Open",  "", "Text (*.txt)")
        print(path)
        if(path):
            self.outputLabel.setText(f"{path}")
            self.txtInput.setText(f"{path}")
    
 
def main(): 
    app = QApplication(sys.argv) 
    mainwindow = MyWindow()       
    app.exec()  
    
if __name__ == '__main__': 
    main() 