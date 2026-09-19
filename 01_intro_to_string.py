# String is data type in python . It is immuatble ( immutable means we can't change once we write)

#write string in diff diff way

a = 'harry' # Single quote string
b = "harry" # Double quote string
c = '''harry''' # Triple quote string

# Index of string : The index in a string start from 0 
# "  P  A  L  S  H  I "  here the string length of this string is 5
#    0  1  2  3  4  5    ( index )
#   -6 -5 -4 -3 -2 -1    ( reverse index)

# length of string 
name = "Pallavi"
print(len(name))

# SLICING OF STRING
# SYNTAX OF SLICING: sl = name[ind_start:ind_end] 
# ind_ start : first index include , ind_end : last index not included
name1 = "Pallavi"
nameshort = name1[0:5] # start from index 0 but it exclude index 5 and it will give output Palla
print(nameshort)
