'''Operator overloading in python can be overloaded using dunder methods
These methods are called when a given operator is used on the objects
Operators in python can be overloaded using the following methods:
p1+p2 p1.__add__(p2)
p1-p2 p1.__sub__(p2)
p1*p2 p1.__mul__(p2)
p1/p2 p1.__truediv__(p2)
p1//p2 p1.__floorediv__(p2)'''

class number():
    def __init__(self,n):
        self.n = n
    def __add__(self, num):
        return self.n+ num.n
    
n = number(1)
m = number(2)
print(n+m)

# str__() used to set what we gets displayed upon calling str(obj)
# __len__() used to set displayed upon calling. __len__() or len(obj)

