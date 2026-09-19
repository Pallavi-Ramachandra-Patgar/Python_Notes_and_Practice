'''Class Method: A class method is a method which is bound to the class and not the 
object of the class 
@classmethod decorator is used to create a class method'''
class Employee:
    a = 1
    @classmethod
    def show(cls): # insted of self we use cls bcz of classmethod
        print(f"The class attribute of a is {cls.a}")

p = Employee()
p.a=45
p.show() #o/p : 1 bcz of using classmethod


