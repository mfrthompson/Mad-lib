import random
import sys


def dice_roll():
    try:
        side_dice = int(input("Would you like to roll the 4, 6, 8, 10, 12,or 20 sided dice?"))
        roll_amt = int(input("How many times would you like the dice to roll?"))
    except ValueError:
        print("Numbers only please")
        sys.exit()
    for _ in range(roll_amt):
        print(random.randint(1, side_dice))


dice_roll()

