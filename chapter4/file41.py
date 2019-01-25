#using for loop
message = input('input: ')
# this type of access called sequential access
for letter in message:
    print(letter)

#Direct access using indexing
string1 = "palindorome"
print(string1[0])
#
# # iterate using range func
for numb in range(len(string1)):
    print(string1[numb])
# iterate in reverse form
for numb in range(len(string1)-1,0-1,-1):
    print(string1[numb])

# while reverse indexing starts from -1 from last char of the string
print(string1[-2])
print(string1[-11])
# strings are immutable can't be changed.
msg = 'arun'
msg[0] = 'l' # this is not allowed - TypeError: 'str' object does not support item assignment
print(msg[0])
# slicing
word = 'things'
# word[start(inclusive):end(exclusive)]
print(word[0:3])

"""     0   1   2   3   4   5    
        T   H   I   N   G   S
        -6  -5   -4  -3  -2  -1    

"""
# slicing can be done even reverse
print(word[-4:4])
# print(word[-4:2]) -> will print empty string as it looks for the next immediate right digit.

# short-hand slicing
# prints every digit
print(word[:])
# prints in reverse.
print(word[::-1])
# Tuples
"""
Tuples are similar to strings but can store multiple data types
It is immutable, and has all features available in strings
"""
# creating empty tuple.
tup = ()

tup = ('one','two',3,4)

# iterating over the tuple
for item in tup:
    print(item)

# indexing tuple
print('----------')
print(tup[-1])

# slicing tuple with step value as 2
print(tup[:4:2])
# CHALLENGES
import random

"""
Write a program that counts for the user. Let the user enter the
starting number, the ending number, and the amount by which
to count.

"""
def func1(start,end,step=1):
    for i in range(start,end,step):
        print(i)

#func1(0,5,2)

"""
Create a program that gets a message from the user and then
prints it out backwards
"""
def func2():
    string = input('type word')
    while string:
        print(string[::-1])
        # to counter infinite loop.
        break
"""
Improve “Word Jumble” so that each word is paired with a hint.
The player should be able to see the hint if he or she is stuck.
Add a scoring system that rewards players who solve a jumble
without asking for the hint.
"""
def jumble(word):
    import random
    jumble = ""
    while len(jumble) != len(word):
        random_position = random.randrange(len(word))
        if word[random_position] not in jumble:
            jumble += word[random_position]
    return jumble



def play_func3():
    words = ('mobilizer','condition','whack','deodarant')
    position = random.randrange(len(words))
    print('The jumbled word is: ' +jumble(words[position]))
    user_guess = ""
    count = 0
    while user_guess != words[position]:
        user_guess = input('input your guess: ')
        count += 1
        if count > 3:
            user_response = input('would u need a hint? : ')
            if user_response[0].lower() in 'y':
                print('fuck off!')
                count = 0
        print('try again.')
    print('congrats! you found the word in '+str(count)+' attempts ')



"""
Create a game where the computer picks a random word and
the player has to guess that word. The computer tells the
player how many letters are in the word. Then the player gets
five chances to ask if a letter is in the word. The computer can
only respond with “yes” or “no”. Then, the player must guess
the word.
"""
