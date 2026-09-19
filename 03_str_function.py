# STRING FUCNTION
# 01 len() function- this function returns the length of the string
name = "Pallavi"
print(len(name)) # output 7

# 02 String.endswith("avi")-This function _tells wheather the variable string ends with "avi" or not
#if string is "Pallavi", it returns true for "avi" since Harry ends with avi.
MyString = "Pallavi"
a=MyString.endswith("avi") # output True
b=MyString.startswith("Pal") # output True
print(a)
print(b)

#03 sting.count("c") - counts the total number of occurences of any charecter.
string = "Ramachandra"
d = string.count("a")
print(d) #output 4 bcz it count how many a is prenset in Ramachandra

#04 sting.capitalize()- This function capitalize the first charecter of a given string
s = "indu"
q = string.capitalize() # output Indu
r = string.upper() # output INDU
t = string.lower() # output indu
print(q) 
print(r)
print(t)

#05 sting.find(world) - This function finds a word and return the index of first occurence of that word 
#in the string 
X = "Pallavi Cute"
index = X.find("Cute")
print(index) # output 5

#06 string.replace(old word, new word)- This function replace the old word with new word in the entire sting
Z = "Pallavi is good"
Y = Z.replace("good", "smart")
print(Y) #output Pallavi is smart

