import random
import sys


def dice_roll():
    try:
        side_dice = int(input("Would you like to roll the 4, 6, 8, 10, 12,or 20 sided dice?"))
    except ValueError:
        print("Numbers only please")
        sys.exit()
    try:
        roll_amt = int(input("How many times would you like the dice to roll?"))
    except ValueError:
        print("Numbers only please")
        sys.exit()

    for _ in range(roll_amt):
        print(random.randint(1, side_dice))


dice_roll()

