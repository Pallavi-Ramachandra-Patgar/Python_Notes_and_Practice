'''Multilevel Inheritence: when a child class become a parent for another child class
   Parent ---> Child 1 ---> Child 2'''
 #Syntax 
class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

o = Employee 
print(o.a) #o/p:1

o = Programmer() 
print(o.a,o.b) # o/p: 1,2

o = Manager()  
print(o.a,o.b,o.c) # o/p :1,2,3
