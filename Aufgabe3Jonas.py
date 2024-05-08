import sys 
from PyQt5.QtWidgets import * 

 

class MyWindow(QMainWindow): 
    def __init__(self):     
        super().__init__() 
    
        layout = QFormLayout()

        self.txtThema = QLineEdit()
        self.txtOrt = QLineEdit()
        self.date = QCalendarWidget()
        self.von = QTimeEdit()
        self.bis = QTimeEdit()
        self.von.setDisplayFormat("HH:mm:ss")
        self.bis.setDisplayFormat("HH:mm:ss")
        self.ganzTägig = QCheckBox("Ganztägiges Event")
        self.button = QPushButton("Ok")

        layout.addRow("Thema:", self.txtThema)
        layout.addRow("Ort", self.txtOrt)
        layout.addRow("Datum:", self.date)
        layout.addRow("Von:", self.von)
        layout.addRow("Bis:", self.bis)
        layout.addRow(self.ganzTägig)
        layout.addRow(self.button)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Termin Festlegen")   
        self.show()  

 
def main(): 
    app = QApplication(sys.argv) 
    mainwindow = MyWindow()       
    app.exec()  
    
if __name__ == '__main__': 
    main() 