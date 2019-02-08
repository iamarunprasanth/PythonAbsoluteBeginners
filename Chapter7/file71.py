#Files and Exceptions

# Reading from a text file

"""
Mode Description
"r" Read from a text file. If the file doesn’t exist, Python will complain with an error.
"w" Write to a text file. If the file exists, its contents are overwritten. If the file doesn’t exist,
it’s created.
"a" Append a text file. If the file exists, new data is appended to it. If the file doesn’t exist, it’s
created.
"r+" Read from and write to a text file. If the file doesn’t exist, Python will complain with an error.
"w+" Write to and read from a text file. If the file exists, its contents are overwritten. If the file
doesn’t exist, it’s created.
"a+" Append and read from a text file. If the file exists, new data is appended to it. If the file
doesn’t exist, it’s created.
"""
"""
Method Description
close() Closes the file. A closed file cannot be read from or written to until opened
again.
read([size]) Reads size characters from a file and returns them as a string. If size is not
specified, the method returns all of the characters from the current position
to the end of the file.
readline([size]) Reads size characters from the current line in a file and returns them as a
string. If size is not specified, the method returns all of the characters from
the current position to the end of the line.
readlines() Reads all of the lines in a file and returns them as elements in a list.
write(output) Writes the string output to a file.
writelines(output) Writes the strings in the list output to a file.

"""

file = open("sample.txt",'r')

print(file.read(1))
# after read(1) the cursor will point to the 2nd character to point to starting palce use
file.seek(0)
print(file.readline(1))
print(file.read())
print(file.readline())
# looping thru
for line in file:
    print(line)
print(file.readlines())
"""
Both read and readlines prints entire file. but the diff is readlines() method will return
each line in list type. so each line of the file is considered as an element in the list
"""
# write to a file
file1 = open("sample.txt",'w')
file1.write('I am from line 1')
file1.write('I am from line 2')
# likewise writelines() method will write an list of elements to the file.
# for ex:
list1 = ['Iam from 1 \n', 'Iam from 2 \n']
file1.writelines(list1)

import pickle, shelve

# pickle is used to read/write data of following type to file.
"""
• Numbers
• Strings
• Tuples
• Lists
• Dictionaries
"""
"""
Mode Description
"rb" Read from a binary file. If the file doesn’t exist, Python will complain with an error.
"wb" Write to a binary file. If the file exists, its contents are overwritten. If the file doesn’t exist,
it’s created.
"ab" Append a binary file. If the file exists, new data is appended to it. If the file doesn’t exist, it’s
created.
"rb+" Read from and write to a binary file. If the file doesn’t exist, Python will complain with an
error.
"wb+" Write to and read from a binary file. If the file exists, its contents are overwritten. If the file
doesn’t exist, it’s created.
"ab+" Append and read from a binary file. If the file exists, new data is appended to it. If the file
doesn’t exist, it’s created.

"""

list2 = ['one']
list3 = [1,2,434,54]
f = open('picke1.dat','wb')
pickle.dump(list1,f)
pickle.dump(list2,f)
pickle.dump(list3,f)
pickle.dump(list1,f,True)
f.close()
f = open('picke1.dat','rb+')
new1 = pickle.load(f)
new2 = pickle.load(f)
new3 = pickle.load(f)
print('adasd;'+str(new1))

# shelve - is used when u want to randomly pick some data from the file as stores as in dictionary format.
"""
Mode Description
"c" Open a file for reading or writing. If the file doesn’t exist, it’s created.
"n" Create a new file for reading or writing. If the file exists, its contents are overwritten.
"r" Read from a file. If the file doesn’t exist, Python will complain with an error.
"w" Write to a file. If the file doesn’t exist, Python will complain with an error.
"""
s = shelve.open('pickle2.dat','c')
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s.sync()
print(s['variety'][0][1])

# Exceptions
try:
    open('file1.txt','r')
   #num = float(input("Enter a number: "))
except TypeError:
    print("Something went wrong!")

