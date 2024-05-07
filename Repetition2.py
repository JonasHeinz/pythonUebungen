import sys 
from PyQt5.QtWidgets import * 
 
# Fenster-Klasse: wird von QWindow vererbt 
class MyWindow(QMainWindow): 
    def __init__(self):      # Konstruktor 
        super().__init__()   # Konstruktor Basis-Klasse 
    
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        label =QLabel("Ist dieses Datum in Ordnung?")
        btnJa = QPushButton("Ja")
        btnNein = QPushButton("Nein")
        btnAbbrechen = QPushButton("Abbrechen")
    
    
        calendar = QCalendarWidget()

        hlayout.addWidget(btnJa)
        hlayout.addWidget(btnNein)
        hlayout.addWidget(btnAbbrechen)
        
        vlayout.addWidget(calendar)
        vlayout.addWidget(label)

        vlayout.addLayout(hlayout)

        center = QWidget()
        center.setLayout(vlayout)
        self.setCentralWidget(center) 
        
        self.setWindowTitle("Hello World")  # Fenster-Titel setzen 
        self.show()  # Fenster anzeigen/sichtbar machen 
      
 
def main(): 
    app = QApplication(sys.argv)  # Qt Applikation erstellen 
    mainwindow = MyWindow()       # Instanz Fenster erstellen 
    app.exec()  
    
if __name__ == '__main__': 
    main() 