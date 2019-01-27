# Nesting sequence
"""
can have sequence of any data type
for ex: a list may have tuples and a list too
"""
list1 = [(1,2,),[3,4,5]]
# indexing nested sequence
print(list1[0])
# taking the first element of tuple
print(list1[0][0])
# sequencing is possible too    
print(list1[1][0:2])

# Unpacking a seq
# no of var should equal to no of values passed on
# can be of any data type.
name, age = ('arun',27)
print(name)
print(age)

# Creating Dictionaries
"""
Dictionaries are Key value pair 
Keys are unique and values are not 
Keys are immutable but the values can be mutable. 
"""
# creating a empty dictionary
dict1 = {}
print(dict1)
# adding key:value pair into the dictionary
dict1['key1'] = [1,2,3]
dict1['key2'] = ('arun',27)

print(dict1)

# indexing and slicing is possible in dictionary
print(dict1['key1'][1])
# prints key2 values in reverse.
print(dict1['key2'][::-1])

# Replace a key:value pair
dict1['key1'] = ['one','two']
print(dict1)
# deleting one of the value from #key-1
"""
When the value type is Tuple - cannot delete as Tuple doesn't support Delete.
because Tuple are immutable.
"""
del dict1['key1'][1]
print(dict1)

"""
Dictionary in-built methods
get()
keys()
values()
items()
"""




