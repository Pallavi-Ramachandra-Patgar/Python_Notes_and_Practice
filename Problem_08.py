''' Write a python function to print multiplication table of given number'''
def multiply(n):
    for i in range(1 , 11):
        print(f"{n} x {i} ={n*i}")

multiply(4)

#Another way
a = int(input("Enter a number:"))
for i in range (1,11):
    print(f"{a} x {i} ={a*i}")




