'''Write a python program using function to convert Celsius to Fahrenheit'''
#Formula c/5 = (f-32)/9

a = int(input("Enter temprature in F: "))
b = 5*(a-32)/9
print(b)

#using function u
def f_to_c(f):
    return(5*(f-32)/9)
f = int(input("Enter a temprature in F: "))
c = f_to_c(f)
print(f"{round(c,2)} degree C")
