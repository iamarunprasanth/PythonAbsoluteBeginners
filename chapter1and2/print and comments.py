
# single line comment
"""
multi line comment
"""

# print function
print("hello world!")
"""
print func automatically adds new line when executed. to avoid - can be modified via end keyword.
"""
print('something',end=" ")

# Chapter -1 Challenges
"""
1. Create an error of your very own by entering your favorite ice
cream flavor in interactive mode. Then, make up for your
misdeed and enter a statement that prints the name of your
favorite ice cream.

"""
print('vanilla')

"""
2. Write and save a program that prints out your name and waits
for the user to press the Enter key before the program ends.
Then, run the program by double-clicking its icon

"""
print('arun')
input('\n press enter key to exit')

"""
3. Write a program that prints your favorite quote. It should give
credit to the person who said it on the next line.

"""

print('quote1')
print('by arun')

# Chapter -2
# triple-quoted string.
print("""
GAME OVER
""")
"""
Sequence Description
\\ Backslash. Prints one backslash.
\' Single quote. Prints a single quote.
\" Double quote. Prints a double quote.
\a Bell. Sounds the system bell.
\n Newline. Moves cursor to beginning of next line.
\t Horizontal tab. Moves cursor forward one tab stop.
"""
# Line Continuation Character "\"
print('THis is in line 1 '\
      'and this is in line 2')


print("If a 2000 pound pregnant hippo gives birth to a 100 pound calf,")
print("but then eats 50 pounds of food, how much does she weigh?")
input("Press the enter key to find out.")
print("2000 - 100 + 50 =", 2000 - 100 + 50)

# getting user input using the input() func
name = input('enter username')
print('username is :' +name)

"""
Method Description
upper() Returns the uppercase version of the string.
lower() Returns the lowercase version of the string.
swapcase() Returns a new string where the case of each letter is switched.
Uppercase becomes lowercase and lowercase becomes uppercase.
capitalize() Returns a new string where the first letter is capitalized and the rest
are lowercase.
title() Returns a new string where the first letter of each word is capitalized
and all others are lowercase.
strip() Returns a string where all the white space (tabs, spaces, and newlines)
at the beginning and end is removed.
replace(old, new [,max]) Returns a string where occurrences of the string old are replaced with
the string new. The optional max limits the number of replacements.
"""

# Chapter -2 Challenge (really challenge)
"""
1. Write a Tipper program where the user enters a restaurant
bill total. The program should then display two amounts: a
15 percent tip and a 20 percent tip.
"""

def bill_with_tip():
    amount1 = int(input('enter bill-1: '))
    amount2 = int(input('enter bill-2: '))

    print('Amount-1',amount1*0.015)
    print('Amount-2',amount2*0.20)

"""
2. Write a Car Salesman program where the user enters the base
price of a car. The program should add on a bunch of extra fees
such as tax, license, dealer prep, and destination charge. Make
tax and license a percent of the base price. The other fees
should be set values. Display the actual price of the car once
all the extras are applied.
"""

def car_sales():
    basePrice = int(input('please input base price of the car: '))
    tax = basePrice * 0.10
    license = 5
    dealer_prep = 10
    destination_charge = 20
    import random
    other_fees = random.randrange(100)
    print('Actual price of car: ',basePrice-tax-license-dealer_prep-destination_charge-other_fees)
    input('press enter key to exit program')
    print('THANK U')

car_sales()