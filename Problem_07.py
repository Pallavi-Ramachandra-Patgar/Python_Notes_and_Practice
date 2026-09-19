'''Write a python function to remove a givem word from a list ad strip it at the 
same time'''
def rem(l,word):
    n =[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
        
l = ["Shubham","Shivam","Ramchandra","Indumati","Vamshi","amruta"]
print(rem(l,"am"))

#o/p : ['Shubh', 'Shiv', 'Ramchandr', 'Indumati', 'Vamshi', 'rut']
