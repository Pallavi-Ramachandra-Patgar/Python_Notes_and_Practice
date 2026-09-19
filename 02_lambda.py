'''Lambda Function: It is an expression using lambda keyword
syntax:
lambda argumnets:expression
'''
# def square(n):
#     return n*n

#Example

square = lambda x:x*x
print(square(5))

sum = lambda a,b,c:a+b+c
print(sum(1,2,3))

'''Join Method:Create a string from iterable objects'''
#Example
a = ["Pallavi","Shivam","Gaurav"]
final = "::".join(a)
print(final)

B = ["Pallavi","Shivam","Gaurav"]
last = "__".join(B)
print(last)

'''Format Method(String):Formates the values inside the string into a 
desired output
Syntax:
"{} is good {}".formate("Pallavi","Girl") o/p:Pallavi is good Girl
{} is good {0}".formate("Pallavi","Girl") o/p:Girl is a good Pallavi''' 
#Example
P = "{} is good {}".format("Pallavi","Girl")
print(P)
Q = "{1} Good Morning {0}".format("Shivam","Hey")
print(Q)

