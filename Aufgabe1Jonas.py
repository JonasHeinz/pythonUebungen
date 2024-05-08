class Ort():
    def __init__(self, name, x, y, einwohner):
        self.name = name
        self.x = x
        self.y = y
        self.einwohner = einwohner

    def __str__(self):
        return f"Name: {self.name}, X: {self.x}, Y: {self.y}, Einwohner: {self.einwohner}"

    def __lt__(self, other):
        return self.einwohner < other.einwohner

    def __gt__(self, other):
        return self.einwohner > other.einwohner

    def __eq__(self, other):
        return self.einwohner == other.einwohner

basel = Ort("basel",7.5886, 47.5596, 100000)
zürich = Ort("zürich",8.5417, 47.3769, 200000)

if zürich > basel:
    print("Zürich hat eine grössere Population als Basel")