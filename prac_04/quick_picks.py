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