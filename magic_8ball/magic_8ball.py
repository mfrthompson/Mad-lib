
def magic_8ball():

    import random
    import sys

    ans = True

    while ans:
        question = input("What would you like to know? (Press enter to end the program.)")

        answers = random.randint(1, 6)

        if question == "":
            sys.exit()
        elif answers == 1:
            print("Fat Chance!")
        elif answers == 2:
            print("Maybe...")
        elif answers == 3:
            print("I guess there is such a thing as stupid questions.")
        elif answers == 4:
            print("Yes!")
        elif answers == 5:
            print("No!")
        elif answers == 6:
            print("If you work really hard!")


magic_8ball()
