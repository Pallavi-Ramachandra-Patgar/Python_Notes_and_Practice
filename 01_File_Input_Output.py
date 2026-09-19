'''The random-access memory is volatile, and all its contents are lost 
once a program terminate in order to persist the data forever, we use files'''

'''A file is data stored in a storage device.A python program can talk to the file
by reading content from it and writing content to it'''

'''
Programmer         <---> Write code --->FILE
(computer program           Read    <---
written in python)'''
'''Ram = Volatile : where the memory temprorily load RAM is a fast 
 HDD = Non Volatile'''

'''TYPE OF FILE
There are two type:
1. Text file(.text , .c etc)
2.Binary files(.log, .data, ect)'''

''' EXAMPLE:
f = open("file.text")   # here we created file.text 
data = f.read()         # to read the file.text we used f.read()
print(data)             # whatever present in file.text it will print
f.close()               # once we read the file we have to close 
''' 

