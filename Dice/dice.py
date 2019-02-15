import random
import sys


def size():
    try:
        side_dice = int(input("Would you like to roll the 4, 6, 8, 10, 12,or 20 sided dice?"))
        return side_dice
    except ValueError:
        print("Numbers only please")
        size()


def amount():
    try:
        roll_amt = int(input("How many times would you like to roll the dice?"))
        return roll_amt
    except ValueError:
        print("Numbers only please")
        amount()


def main():
    side_dice = size()
    roll_amt = amount()
    for _ in range(roll_amt):
        print(random.randint(1, side_dice))
    cont = input("Would you like to roll again? Y/N")
    if cont.lower() == "y":
        main()
    elif cont.lower() == "n":
        sys.exit()


main()

