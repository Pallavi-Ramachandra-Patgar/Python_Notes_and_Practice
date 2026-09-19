'''Write __str__() method to print the vector as follows:
7i +8j +10k Assume vector of 3 dimention 3 for this problem'''
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    def __mul__(self, other):
        result = self.x * other.x, self.y * other.y, self.z * other.z
        return result
    def __str__(self):
        return f"({self.x}i,{self.y}j,{self.z}k)"
    
#Test the implimentation
V1 = Vector(1,2,3)
V2 = Vector(4,5,6)
V3 = Vector(7,8,9)

print(V1 + V2)
print(V1 * V2)

print(V1 + V3)
print(V1 * V3)
    