class Tankstelle():
    def __init__(self, name, benzinpreis, land, koordinate):
        self.name = name
        self.benzinpreis = benzinpreis
        self.land = land
        self.koordinate = koordinate

    def __str__(self):
        return f"Name: {self.name}, Benzinpreis: {str(self.benzinpreis)}, Land: {self.land}, Koordinate X: {self.koordinate[0]}, Koordinate Y: {self.koordinate[1]}"

avia = Tankstelle("AVIA", 1.893 , "Deutschland", (1000000, 200000))
print(avia)