from random import *

inputOne = int(input("Enter the number 1 to play: "))
number = 0

while number < 21 and inputOne == 1:
    number += randint(1, 11)
    print("Your number is", number)
    if number > 21:
        print("You lose")
        break
    elif number == 21: 
        print("You win")
        break
    inputOne = int(input("Enter the number 1 to play again: "))
else:
    print("Game over")

