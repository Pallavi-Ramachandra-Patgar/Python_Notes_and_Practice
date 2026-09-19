'''if else and elif statements are a multyway decision taken by our program due to certain 
condition in our code.'''

#Syntax:
'''
if(condition1):
    print("Yes")     it will print when if condtion match 
elif(condition2):
    print("No")      it will print when if condtion not match 
else:
    print("Maybe")   it will print when both if and elif contion not match
'''

#if elif else ladder
a = int(input("Enter your age: "))
if(a>=18):
    print("Your are above the age of concent")
elif(a<0):
    print("You are entering the an invalid age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:
    print("Your are below the age of concent")

b=-22 #here i already gave a number
if(b>=18):
    print("Greater")
elif(b<=0):
    print("Invalid number")
else:
    print("Lower")

'''
Relational operator or Comparison operator:
These are used to evaluate condtions inside the if statement.
ex: ==:equals.
    >=:greater than/equal to
    <=:less than/ equal to
'''

'''Logical Operator:
aand-true if both operands are true else false
or -true if atleast one operand is true or else false.
not-converts true to false and false to true
'''

'''
Note:
There can be any number of elif statements.
Last else is executed only if all the conditions inside elifs fail.
'''