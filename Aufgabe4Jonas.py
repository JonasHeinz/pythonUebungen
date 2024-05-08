import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

class MyWindow(QMainWindow): 
    def __init__(self):      
        super().__init__()   
    
        layout = QFormLayout()

        self.txtCelsius = QDoubleSpinBox()
        self.lblFahrenheit = QLabel()
        self.button = QPushButton("Umrechnen")

        layout.addRow("Celsius:", self.txtCelsius)
        layout.addRow("Wert in Fahrenheit:", self.lblFahrenheit)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.umrechnung)


        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Konverter")  # Fenster-Titel setzen 
        self.show()  # Fenster anzeigen/sichtbar machen 

    def umrechnung(self):
        celsius = float(self.txtCelsius.text().replace(",", "."))
        fahrenheit = (celsius * 1.8) + 32
        self.lblFahrenheit.setText(f"{fahrenheit}")
      
 
def main(): 
    app = QApplication(sys.argv)  # Qt Applikation erstellen 
    mainwindow = MyWindow()       # Instanz Fenster erstellen 
    app.exec()  
    
if __name__ == '__main__': 
    main() 