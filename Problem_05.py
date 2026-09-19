'''Write a program to mine a log file and find out wheather it contains 'python' '''
with open("log.txt","r") as f:
   content= f.read()
if ("python" in content):
   print("Yes python is present")
else:
   ("python is not present")
   