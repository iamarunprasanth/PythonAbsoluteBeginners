# List
"""
Lists are unlike Tuples can store multiple datatype.
The main diff is Lists are mutable.
can support all the features Tuples supports.
and has some very flexible in-built methods.
"""
# creating an empty list
list1 = []
# Adding few items to the list
list1.append(1)
list1.append('two')
# printing list
print(list1)
# Changing an element at position 0
list1[0] = 'one'
list1.append(3)
print(list1)
# iterating the list
for item in list1:
    print(item, end=" ")
    print()

# Indexing over list
print('After indexing \t' + str(list1[2]))
print('After indexing \t' + str(list1[-2]))

# Slicing over list
print(list1[0:2])
# slicing doesn't complain abt the list size as we have only 3 elements starting from 0-1-2
print(list1[-1:3])
# concatenating list
list1[0] = list1[0] + 'one'
print(list1)

# List mutability
list1[1] = 'not two'
print(list1, end= "")

# Some list methods
"""
Method Description
append(value) Adds value to end of a list.
sort() Sorts the elements, smallest value first. Optionally, you can pass a Boolean
value to the parameter reverse. If you pass True, the list will be sorted with the
largest value first.
reverse() Reverses the order of a list.
count(value) Returns the number of occurrences of value.
index(value) Returns the first position number of where value occurs.
insert(i, value) Inserts value at position i.
pop([i]) Returns value at position i and removes value from the list. Providing the
position number i is optional. Without it, the last element in the list is removed
and returned.
remove(value) Removes the first occurrence of value from the list.
"""
# sort list - will sort if the list has same datatype elements.
list2 = [4,5,63,1,0,5,5,5,5,5,5,5,5]
print(list2)
# to sort in descending order, else takes ascending as default
list2.sort(reverse=True)
print(list2)

# Reverse list -> Reverses the order of the list
list2.reverse()
print(list2)

# count list
print(list2.count(4))

# index of list
print(list2.index(5))
# insert list
list2.insert(5,'five')
print(list2)
# pop list  -> default pops the last element
print(list2.pop())
print(list2.pop(5))
print(list2)
# Remove list -> removes the first occurrence of the value.
print(list2.remove(5))
print(list2)


