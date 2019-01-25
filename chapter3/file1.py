
# you can import a module using import keyword
import random
import math

"""Algorithm
welcome the player to the game and explain it
pick a random number between 1 and 100
ask the player for a guess
set the number of guesses to 1
while the player’s guess does not equal the number
if the guess is greater than the number
tell the player to guess lower
otherwise
tell the player to guess higher
get a new guess from the player
increase the number of guesses by 1
congratulate the player on guessing the number
let the player know how many guesses it took
"""

def game_play():
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    if username =='admin' and password =='admin':
        print('login success!')
        explain_game()
        number_guess()
    elif username =='admin' and password =='admin':
        print('login success with some exceptions.')
        explain_game()
        number_guess()
    else:
        print('sorry, login failed!')

# creating a funtion to explain the game.
def explain_game():
    print('System will generate a number b/w 1-100')
    print('input a number to know you have guessed the right one.')
    print('if you guess way lesser or higher the system will ask u to guess close to the number.')
    print('when u guess it correct, system will display how much the user took to guess the number.')
# creating a function for the game core.
def number_guess():
    # using randint func can allow user to select number from 1 to 100.
    secret_number = random.randint(1,100)
    guess = 0
    user_guess = ""
    while not user_guess:
        user_guess = int(input('input a number b/w 1-100'))
        print(user_guess)
        while user_guess != secret_number:
            if user_guess > secret_number:
                guess += 1
                print('guess a lower number!')
                user_guess = ""
                break
            elif user_guess < secret_number:
                guess += 1
                print('guess a higher number!')
                user_guess = ""
                break
            else:
                pass
                # when u have no statement to make but still need a loop can use pass as a place holder.
        if user_guess == secret_number:
            print('correct guess: '+str(guess))
#game_play()
# Challenge
"""
Write a program that flips a coin 100 times and then tells you
the number of heads and tails.
"""
def flip_coin():
    counter = 0
    heads = 0
    tails = 1
    while counter <= 100:
        value = random.randrange(2)
        if value == 0:
            heads += 1
        else:
            tails += 1
        counter += 1
    print(heads)
    print(tails)
#flip_coin()

"""
Here’s a bigger challenge. Write the pseudocode for a program
where the player and the computer trade places in the number
guessing game. That is, the player picks a random number
between 1 and 100 that the computer has to guess. Before you
start, think about how you guess. If all goes well, try coding the
game.
"""
# 1. user inputs the secret number
# 2. Ask the computer to guess the number.
# 3. Verify how much attempts the computer is taking to guess.

def game_root():
    secret_number = ""
    while not secret_number:
        user_guess = int(input('USER -> enter the secret number b/w 1-100 : '))
        while user_guess > 0 and user_guess <=100:
            secret_number = user_guess
            break
    guess = 0
    comp_guess = ""
    while not comp_guess:
        comp_guess = random.randint(1,100)
        while comp_guess != secret_number:
            if comp_guess > secret_number:
                guess += 1
                print('guess a lower number!')
                comp_guess = ""
                break
            elif comp_guess < secret_number:
                guess += 1
                print('guess a higher number!')
                comp_guess = ""
                break
            else:
                pass
        if comp_guess == secret_number:
            print('correct guess: '+str(guess))

game_root()



