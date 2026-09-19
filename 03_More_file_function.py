f = open("file.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()

'''o/p :['Hi Pallavi Good Morning have a great day \n', 'You are doing well\n', 
'Try hard untile you get what you want\n', 
'I am damn sure you will get good job with good salary']
 <class 'list'>'''

f = open("file.txt")
line1 = f.readline()
print(line1,type(line1))
line2 = f.readline()
print(line2,type(line2))
line3 = f.readline()
print(line3,type(line3))
line4 = f.readline()
print(line4,type(line4))
f.close()

'''o/p
Hi Pallavi Good Morning have a great day 
 <class 'str'>
You are doing well
 <class 'str'>
Try hard untile you get what you want
 <class 'str'>
I am damn sure you will get good job with good salary <class 'str'>
'''

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()

#Mode of opening file 
'''
r - open for read
w - open for writing
+ - open for updating
a - open for apending
rb will open for read in binary mode
rt will open for read in text mode'''

#With statment:You don't have to explicity close the file
with open("myfile.txt")as f:
    print(f.read())
