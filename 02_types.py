'''Type Defination in python:Type hints are added using the colon(:)syntax for 
variable and the -> syntax for function return types. '''

# variable type hint
n : int = 25

#Function type hint
def greeting(name:str) ->str:
    return f"Hello,{name}!"

#Usage
print(greeting("Alice")) #o/p: Hello,Alice!