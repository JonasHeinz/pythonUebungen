import math

def distanz(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

class Figur:
    def __init__(self, name):
        self.name = name
    def Umfang(self):
        return 0
    def __str__(self):
        return self.name

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({str(self.x)}, {str(self.y)})"

        
class Kreis(Figur):
    def __init__(self, mittelpunkt: Point, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius
    def Umfang(self):
        return self.radius * 2 * math.pi

    def __str__(self):
        return f"{self.name} M={self.mittelpunkt} r={str(self.radius)}"

class Dreieck(Figur):
    def __init__(self, A: Point, B: Point, C: Point):
        super().__init__("Dreieck")
        self.A = A
        self.B = B
        self.C = C
    
    def Umfang(self):
        ab = distanz(self.A, self.B)
        bc = distanz(self.B, self.C)
        ca = distanz(self.C, self.A)
        return ab + bc + ca
 
    def __str__(self):
        return f"{self.name} A={str(self.A)} B={str(self.B)} C={str(self.C)}"


class Rechteck(Figur):
    def __init__(self, A: Point, C: Point):
        super().__init__("Rechteck")
        self.A = A
        self.C = C
        
    def Umfang(self):
        return abs(abs(self.C.x-self.A.x)*2 + abs(self.C.y-self.A.y)*2)

    def __str__(self):
        return f"{self.name} {self.A} - {self.C}"


class Polygon(Figur):
    def __init__(self, points: list[Point]):
        super().__init__("Polygon")
        self.points = points
    def Umfang(self):
        if len(self.points) >= 3:
            umfang = 0
            last = self.points[len(self.points)-1]   
            for point in self.points:
                umfang += distanz(point, last)
                last = point
            return umfang
        else:
            print("Es braucht mindestens 3 Punkte")
            
        return abs(abs(self.C.x-self.A.x)*2 + abs(self.C.y-self.A.y)*2)

    def __str__(self):
        pointsStr = ""
        for i in range (len(self.points)):
            pointsStr+=f"P{i+1}:{self.points[i]} "
                      
        return f"{self.name} {pointsStr}"
    
P1 = Point(1, 3)
P2 = Point(4, 5)
P3 = Point(2.4, 2)
print(Polygon([P1, P2, P3]).Umfang())
print(Kreis(P1, 3))
print(Dreieck(P1, P2, P3))
print(Rechteck(P1, P2))
print(Polygon([P1, P2, P3]))