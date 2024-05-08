import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
 

class MyWindow(QMainWindow): 
    def __init__(self):     
        super().__init__() 
    
        layout = QFormLayout()

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Hello World")   
        self.show()  

 
def main(): 
    app = QApplication(sys.argv) 
    mainwindow = MyWindow()       
    app.exec()  
    
if __name__ == '__main__': 
    main() 