class Form:
      def fläche(self):
        return 0
    
class Rechteck(Form):
    def __init__(self, länge, breite):
        self.länge = länge
        self.breite = breite
        
    def fläche(self):
        return self.länge * self.breite

