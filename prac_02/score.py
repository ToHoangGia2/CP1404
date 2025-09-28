from random import *

def main():
    """this function will get score and print the determined score"""
    score = float(input("Enter your score: "))
    print(determine_score(score))
    random_score = randint(0, 100)
    print(f"random score ({random_score}) is: {determine_score(random_score)}")

def determine_score(score):
    """this function will return the determined score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()