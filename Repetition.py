#1) Unterschied zwischen Aggregation und Komposition

#-->Aggregation bezieht sich auf eine "hat-ein" Beziehung, bei der ein Objekt Teil eines anderen sein kann, während Komposition eine engere "ist-ein-Bestandteil-von" Beziehung darstellt, bei der ein Objekt ohne sein übergeordnetes Objekt nicht existieren kann.

class Studenten():
      def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        
class Kurs():
    def __init__(self, name):
        self.name = name
        self.lehrer = []

    def addLehrer (self, lehrer):
        self.lehrer.append(lehrer)


kantiSargans = Kurs("Mathe")
kantiSargans.addLehrer(Studenten("Frank", "Müller"))

print(kantiSargans.lehrer[0].vorname)

class Zimmer():
      def __init__(self, zimmerNr):
          self.zimmerNr = zimmerNr

class Haus():
    def __init__(self, hausNr, zimmer1Nr):
        self.hausNr = hausNr
        self.zimmer1 = Zimmer(zimmer1Nr)

haus1 = Haus(2,3)

print(haus1.hausNr)

#2 Was sind magische Funktionen

#Magische Methoden sind spezielle Python-Methoden, die von Doppelunterstrichen umgeben sind und es ermöglichen, das Verhalten von Klassen in Bezug auf Python-spezifische Operationen zu definieren, wie Instanziierung, String-Konvertierung oder Arithmetik.


class Stadt():
    def __init__(self, name, einwohnerzahl, land, kontinent, koordinate):
        self.name = name
        self.einwohnerzahl = einwohnerzahl
        self.land = land
        self.kontinent = kontinent
        self.koordinate = koordinate

    def __str__(self):
        return f"{self.name},{self.einwohnerzahl}, {self.land}, {self.kontinent}, {self.koordinate}"


hamburg = Stadt("Hamburg", 100000, "Deutschland", "200",1)
print(hamburg)
