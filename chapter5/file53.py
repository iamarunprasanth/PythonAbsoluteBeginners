
# Challenges
"""
Create a program that prints a list of words in random order.
The program should print all the words and not repeat any.
"""

# words = ['one','two','three','four']
# import random
# nos = []
# while len(nos)!= len(words):
#     position = random.randrange(len(words))
#     if words[position] not in nos:
#         print(words[position])
#         nos.append(words[position])
#
"""
Write a Character Creator program for a role-playing game. The
player should be given a pool of 30 points to spend on four
attributes: Strength, Health, Wisdom, and Dexterity. The
player should be able to spend points from the pool on any
attribute and should also be able to take points from an
attribute and put them back into the pool.
"""

print('Hi, My name is " ARUN "')
points = 30
strength = 0
health = 0
wisdom = 0
dexterity = 0
choices = ['points','strength','health','wisdom','dexterity']
choice = None
while not choice:
    print("choices "
          "0 -> View current stats \n"
          "1 -> strength \n"
          "2 -> health \n"
          "3 -> wisdom \n"
          "4 -> dexterity \n")
    choice = int(input('enter your choice: '))
    while choices[choice] in choices:
        if str(choices[choice]).lower() == 'strength':
            user_prompt = input('input I/D to increase/decrease strength: ')
            if user_prompt[0].lower() == 'i':
                strength_increase = int(input('enter the value to increase: '))
                if strength_increase <= points:
                    strength += strength_increase
                    points -= strength_increase
                    choice = None
                else:
                    print('failed')
            elif user_prompt[0].lower() == 'd':
                strength_decrease = int(input('enter the value to decrease: '))
                if strength > strength_decrease:
                    strength -= strength_decrease
                    points += strength_decrease
                    choice = None
                continue
            break
        else:
            continue



