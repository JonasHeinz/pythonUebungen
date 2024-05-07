import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
 
# Fenster-Klasse: wird von QWindow vererbt 
class MyWindow(QMainWindow): 
    def __init__(self):      # Konstruktor 
        super().__init__()   # Konstruktor Basis-Klasse 
    
        layout = QFormLayout()

        self.txtFranken = QLineEdit()
        self.lblEuro = QLabel()
        self.button = QPushButton("Umrechnen")

        layout.addRow("Schweizer Franken", self.txtFranken)
        layout.addRow("Euro:", self.lblEuro)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.umrechnung)


        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Hello World")  # Fenster-Titel setzen 
        self.show()  # Fenster anzeigen/sichtbar machen 

    def umrechnung(self):
        chf = float(self.txtFranken.text())
        euro = chf * 0.876
        euro_rounded = round(euro, 2)
        self.lblEuro.setText(f"{euro_rounded}")
      
 
def main(): 
    app = QApplication(sys.argv)  # Qt Applikation erstellen 
    mainwindow = MyWindow()       # Instanz Fenster erstellen 
    app.exec()  
    
if __name__ == '__main__': 
    main() 