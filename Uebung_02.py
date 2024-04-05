
class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
    
    def add(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)         
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z +other.z)
    
    def __add__(self, other):
        return self.add(other)
    def __radd__(self, other):
       return self.add(other)

    def sub(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)         
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __sub__(self, other):
        return self.sub(other)
    def __rsub__(self, other):
       return self.sub(other)


    def mul(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)         
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __mul__(self, other):
        return self.mul(other)
    def __rmul__(self, other):
       return self.mul(other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3((self.y * other.z)-(self.z * other.y), (self.z * other.x)-(self.x * other.z), (self.x * other.y)-(self.y * other.x))

    #mul, sub, truediv, floordiv,
    
a = Vector3(3,4,2)
b = Vector3(2,1,0)

print(a)
print(a.dot(b))





