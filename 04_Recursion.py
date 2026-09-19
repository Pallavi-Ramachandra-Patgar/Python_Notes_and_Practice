''' 
Recursion is a function use a methametical formula as function
it is used to dirctly use a mathematical formula as function'''

def factorial(n):
    if(n==1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of this number is: {factorial(n)}")

''

