import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
 
# Fenster-Klasse: wird von QWindow vererbt 
class MyWindow(QMainWindow): 
    def __init__(self):      # Konstruktor 
        super().__init__()   # Konstruktor Basis-Klasse 
    
        layout = QFormLayout()

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Hello World")  # Fenster-Titel setzen 
        self.show()  # Fenster anzeigen/sichtbar machen 

 
def main(): 
    app = QApplication(sys.argv)  # Qt Applikation erstellen 
    mainwindow = MyWindow()       # Instanz Fenster erstellen 
    app.exec()  
    
if __name__ == '__main__': 
    main() 