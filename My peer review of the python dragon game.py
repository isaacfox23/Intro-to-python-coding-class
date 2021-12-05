# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review

#This is a typical part of any program
# Author: Isaac
# Creation Date: December 3rd, 2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time


def displayIntro():
    print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.\n''')
    #print(), is not needed you can just add \n up above at the end of the print statement


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        #print('Which cave will you go into? (1 or 2)\n')
        cave = input('Which cave will you go into? (1 or 2)\n')
        #cave = input() This is not needed, the print and input statements can be combined with n\
# return caves is not defined in this case so it needs to be cave because that is defined up above in the variable
    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    # sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    # sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    #print() this print() is not neccessary just put \n at the end of the above line
    # sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    #    else:
        #print
        #'Gobbles you down in one bite!'
    #Here you need to fix the paranthese with the print statement also fix it up with the print statement
    else:
        print('Gobbles you down in one bite!')


playAgain = 'yes'
# You need an == instead of just =, wrong syntax ///while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    #caveNumber = choosecave(), choosecave is wrong it should be chooseCave() to call the correct function, Spelling wrong
    caveNumber = chooseCave()
    checkCave(caveNumber)

    #print('Do you want to play again? (yes or no)') not needed if you just combine input and print statement
    playAgain = input('Do you want to play again?(yes or no)\n')
    # This if playAgain == "no": is not necessary because the loop already ends when the no option is entered
    #if playAgain == "no":
        #Spelled playing wrong///print("Thanks for planing")
        #print("Thanks for playing") needs to be dropped outside of the loop
print("Thanks for playing")


