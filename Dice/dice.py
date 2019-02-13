
from random import *


def dice():
    num_dice = input("Hello! Would you like to roll 1 or 2 dice?")
    side_dice = input("Ok, would you like to roll the 4, 6, 8, 10, 12,or 20 sided dice?")
    if(side_dice == "4" and num_dice == "1"):
        print(randint(1, 6))
    elif(side_dice == "4" and num_dice == "2"):
        print(randint(1, 6))
        print(randint(1, 6))
    elif(side_dice == "6" and num_dice == "1"):
        print(randint(1, 6))
    elif(side_dice == "6" and num_dice == "2"):
        print(randint(1, 6))
        print(randint(1, 6))
    elif(side_dice == "8" and num_dice == "1"):
        print(randint(1, 6))
    elif(side_dice == "8" and num_dice == "2"):
        print(randint(1, 6))
        print(randint(1, 6))
    elif(side_dice == "10" and num_dice == "1"):
        print(randint(1, 6))
    elif(side_dice == "10" and num_dice == "2"):
        print(randint(1, 6))
        print(randint(1, 6))
    elif(side_dice == "12" and num_dice == "1"):
        print(randint(1, 6))
    elif(side_dice == "12" and num_dice == "2"):
        print(randint(1, 6))
        print(randint(1, 6))
    elif(side_dice == "20" and num_dice == "1"):
        print(randint(1, 6))
    elif(side_dice == "20" and num_dice == "2"):
        print(randint(1, 6))
        print(randint(1, 6))

dice()

