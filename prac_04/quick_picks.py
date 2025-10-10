from random import *

NUMBERS_EACH_LINE = 6
MINIMUM = 1
MAXIMUM = 45

valid = True
while valid:
    try:
        user_input = int(input("How many quick picks? "))
        if user_input > 0:
            valid = False
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Please enter a valid number.")

for i in range(user_input):
    LIST_OF_NUMBERS = []
    for j in range(NUMBERS_EACH_LINE):
        random_number = randint(MINIMUM, MAXIMUM)
        while random_number in LIST_OF_NUMBERS:
            random_number = randint(MINIMUM, MAXIMUM)
        LIST_OF_NUMBERS.append(random_number)
    LIST_OF_NUMBERS.sort()

    print(" ".join(f"{number:3}" for number in LIST_OF_NUMBERS))
