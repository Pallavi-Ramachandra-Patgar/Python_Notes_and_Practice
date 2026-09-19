#Mulptiple Inheritence: It occurs when the child class inherits from more than 
# one parent classes
'''Parent 1   Parent 2
         Child 
         '''

#Example 
class Employee(): # This is called base class or parent class
    company = "Velankani Software Private Limited"
    name = "Default name"
    def Employee(self):
        print(f"The name of the Employee is {self.name} and the Companey is {self.company}")

class Coder:
    language = "Python"
    def printlanguages(self):
        print(f"Out of all the languages here is your languague:{self.language}")

class Programmer(Employee,Coder): # This is called Derived or inheritent class or child class
    company = "AGS"
    role = "Default role"
    def showlanguage(self):
        print(f"she is third party employee of {self.company} and she is working as {self.role}")

a = Employee()
b = Programmer()



b.Employee()
b.showlanguage()
b.printlanguages()