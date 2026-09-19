''''''
class Employee:
    a = 1
    @classmethod
    def show(cls): # insted of self we use cls bcz of classmethod
        print(f"The class attribute of a is {cls.a}")
    
    @property
    def name(self):
        return self.ename # f"{self.fname} {self.lname}""
    
    @name.setter
    def name(self,value):
        self.ename = value

        # self.fname = value.split(" ")[0]
        # self.lname = value.split(" ")[1]

p = Employee()
p.a=45

p.name = "Pallavi Ramachandra"
print(p.name)
# print(e.fname, e.lname)
p.show()