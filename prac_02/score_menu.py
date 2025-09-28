MENU ="(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    score = ""
    user_choice = input("Enter your choice: ").upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = int(input("Enter your score: "))
            while score < 0 or score > 100:
                print("Enter a valid score between 0 and 100 inclusive")
                score = int(input("Enter your score: "))

        elif user_choice == "P":
            if score == "":
                print("There is no score")
            elif score < 0 or score > 100:
                print("Invalid score")
            elif score >= 90:
                print("Excellent")
            elif score >= 50:
                print("Passable")
            else:
                print("Bad")

        elif user_choice == "S":
            if score == "":
                print("There is no score")
            else:
                print(score * "*")

        else:
            print("Invalid choice")

        user_choice = input("Enter your choice: ").upper()

    print("Thank you!")


main()