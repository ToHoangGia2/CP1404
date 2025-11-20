from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_cost = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
                #print("current taxi: {}".format(current_taxi.name))
            except IndexError:
                print("Invalid taxi choice")



        elif choice == "d":
            print("WIP")

        else:
            print("Invalid choice")

        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()




main()