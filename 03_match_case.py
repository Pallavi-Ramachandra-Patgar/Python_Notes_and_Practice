''''''
def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown satus"

print(http_status(200)) #o/p Ok
print(http_status(404)) #o/p Not Found
print(http_status(500)) #o/p Internal Server Error
print(http_status(201 )) #o/p Unknown status 

'''Merge Dictionary: | is used for merging and updating dictionaries'''
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}
merged = dict1|dict2
print(merged) #o/p {'a': 1, 'b': 2, 'c': 3, 'd': 4}
