'''Inheritence:It is a way of creating from an existing class'''

#Syntax
'''class Employeee: # Base class
    #Code
class Programmer(Employee): #Derived or child class
    #Code'''
#We can also use the method and attribute of employee in Programm object
#We can overwrite or add new attributes and methods in Programmer class

#Example
class Employee(): # This is called base class or parent class
    def Employee(self):
        company = "Velankani Software Private Limited"
        print(f" The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee): # This is called Derived or inheritent class or child class
    company = "AGS"
    def showlanguage(self):
        print(f"she is third party employee{self.name} and she is working as{self.role}")

a = Employee()
b = Programmer()
print(a.company,b.company)

'''Types of Inheritence:
Single Inheritence
Multiple Inheritence
Multilevel Inheritence'''

#Single Inheritence: Single inheritence occurs when child class inherits only a 
# single parent class
#  Base ---> Derived

