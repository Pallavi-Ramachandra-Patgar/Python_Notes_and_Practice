try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("I am inside else")

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
finally: # it will run always 
    print("I am inside else")