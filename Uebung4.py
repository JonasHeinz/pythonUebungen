import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Fenster-Titel definieren:
        self.setWindowTitle("Uebung 5")
        # Layout erstellen:
        layout = QFormLayout()
        
        menubar = self.menuBar() # Die Menubar des Fensters erhalten
        filemenu = menubar.addMenu("File") # "File"-Menu erstellen
        self.save = QAction("Save", self) # Eine weitere Action defininieren
        self.quit = QAction("Quit", self) # Eine dritte Action defininieren

        filemenu.addAction(self.save) # Eine weitere Action hinzufügen
        filemenu.addAction(self.quit) # Eine weitere Action hinzufügen
        
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button = QPushButton("Speichern")

        # Buttons dem Layout hinzufügen
        layout.addRow("Vorname: ",self.vorname)
        layout.addRow("Name: ", self.name)
        layout.addRow("Geburtstag: ", self.geburtstag)
        layout.addRow("Adresse: ", self.adresse)
        layout.addRow("PLZ: ", self.plz)
        layout.addRow("Ort: ", self.ort)
        layout.addRow("Land: ", self.land)
        layout.addRow(self.button)
        
        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)
        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)
        # Fenster anzeigen
        self.show()

        self.save.triggered.connect(self.button_clicked)
        self.button.clicked.connect(self.button_clicked)
        self.quit.triggered.connect(self.menu_quit)

    def menu_quit(self):
        self.close() 
    def button_clicked(self):
        f = open("myfile.txt", "x")
        f.write(f"{self.vorname.text()}, {self.name.text()}, {self.geburtstag.text()}, {self.adresse.text()}, {self.plz.text()}, {self.ort.text()}, {self.land.currentText()}")
        f.close()


def main():
    app = QApplication(sys.argv) # Qt Applikation erstellen
    mainwindow = MyWindow() # Instanz Fenster erstellen
    app.exec() # Applikations-Loop starten
if __name__ == '__main__':
    main()
