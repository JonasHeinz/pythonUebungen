import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse

def parse(str):
    return urllib.parse.quote(str)

countries = ["Schweiz", "Deutschland", "Österreich"]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Fenster-Titel definieren:
        self.setWindowTitle("Uebung 5")
        # Layout erstellen:
        layout = QFormLayout()
        
        menubar = self.menuBar() # Die Menubar des Fensters erhalten
        filemenu = menubar.addMenu("File") # "File"-Menu erstellen
  
        self.view = QAction("View", self)
        self.save = QAction("Save", self) # Eine weitere Action defininieren
        self.quit = QAction("Quit", self)
        self.load = QAction("Load", self)

        menubar.addAction(self.view)
        
        filemenu.addAction(self.save) # Eine weitere Action hinzufügen
        filemenu.addAction(self.quit) 
        filemenu.addAction(self.load) 
        
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(countries)
        
        self.loadButton = QPushButton("Laden")
        self.showMapButton = QPushButton("Auf Karte anzeigen")
        self.saveButton = QPushButton("Speichern")
        
        # Buttons dem Layout hinzufügen
        layout.addRow("Vorname: ",self.vorname)
        layout.addRow("Name: ", self.name)
        layout.addRow("Geburtstag: ", self.geburtstag)
        layout.addRow("Adresse: ", self.adresse)
        layout.addRow("PLZ: ", self.plz)
        layout.addRow("Ort: ", self.ort)
        layout.addRow("Land: ", self.land)
        layout.addRow(self.loadButton)
        layout.addRow(self.showMapButton)
        layout.addRow(self.saveButton)
        
        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)
        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)
        # Fenster anzeigen
        self.show()

        self.save.triggered.connect(self.save_clicked)
        self.saveButton.clicked.connect(self.save_clicked)
        self.quit.triggered.connect(self.menu_quit)
        self.loadButton.clicked.connect(self.load_clicked)
        self.load.triggered.connect(self.load_clicked)
        self.view.triggered.connect(self.view_clicked)
        self.showMapButton.clicked.connect(self.view_clicked)
        
    def load_clicked(self):
        path, format = QFileDialog.getOpenFileName(self, "Open",  "", "Text (*.txt)")
        if(path):
            file = open(str(path), "r", encoding="utf-8")
                
            reader = file.read()
            personalien = reader.split(",")

            self.vorname.setText(personalien[0])
            self.name.setText(personalien[1])
            dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
            self.geburtstag.setDate(QDate.fromString(personalien[2], dformat))
            self.adresse.setText(personalien[3])
            self.plz.setText(personalien[4])
            self.ort.setText(personalien[5])
            self.land.setCurrentIndex(countries.index(personalien[6]))
            
    def view_clicked(self):
        QDesktopServices.openUrl(QUrl(f"https://www.google.ch/maps/place/{parse(self.adresse.text())}+{parse(self.plz.text())}+{parse(self.ort.text())}+{parse(self.land.currentText())}")) 
          
    def menu_quit(self):
        self.close() 
        
    def save_clicked(self):
        path, format = QFileDialog.getSaveFileName(self, "Save",  "", "Text (*.txt)")
        if(path):
            f = open(path, "x")
            f.write(f"{self.vorname.text()},{self.name.text()},{self.geburtstag.text()},{self.adresse.text()},{self.plz.text()},{self.ort.text()},{self.land.currentText()}")
            f.close()


def main():
    app = QApplication(sys.argv) # Qt Applikation erstellen
    mainwindow = MyWindow() # Instanz Fenster erstellen
    app.exec() # Applikations-Loop starten
if __name__ == '__main__':
    main()
