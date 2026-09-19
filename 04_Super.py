'''Super Method: super() method is used to access the methods of a super class 
in the derived class'''
class Employee:
    def __init__(self):
        print("Costructor of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Costructor of Programmer")
    b = 2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Costructor of Manager")
    c = 3

# o = Employee 
# print(o.a) #o/p:1

# o = Programmer() 
# print(o.a,o.b) # o/p: 1,2

o = Manager()  
print(o.a,o.b,o.c) # o/p :1,2,3
