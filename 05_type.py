# Type() function and Typecasting :

#type() function is  used to find data type of the given variable in python 

a = 15 
t = type(a) # class int bcz 15 is integer 
print(t)

b = 1.3 
X  = type(b) # class float bcz 1.3 is floating point number or decimal number 
print(X)

c = "Ramachandra"
Y = type(c) # class string bcz "Ramachandra" is string type which is prent in double quote 
print(Y)

# CONVERTION 
d = "31.5" # this is in string data type bcz it is in double quote 
Z = float(d) # now that string will convert into float 
Q = type (Z) # output is float insted of string 
print(Q)