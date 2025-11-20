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
            current_taxi = choose_taxi(taxis)
            #print("current taxi: {}".format(current_taxi.name))

        elif choice == "d":
            if current_taxi != None:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_cost += trip_cost
                except ValueError:
                    print("Invalid distance")
            else:
                print("You need to choose taxi before you can drive")

        else:
            print("Invalid choice")

        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
        return current_taxi
    except (ValueError, IndexError):
        print("Invalid taxi choice")


main()