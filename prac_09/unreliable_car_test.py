from prac_09.unreliable_car import UnreliableCar

def main():
    car1 = UnreliableCar("used_car", 1000, 30)
    car2 = UnreliableCar("new_car", 1000, 80)
    
    for i in range (1,30):
        print(i)
        print(f"{car1.name} drove: {car1.drive(i)}km")
        print(f"{car2.name} drove: {car2.drive(i)}km")

    print("")
    print(f"{car1.name} has: {car1.fuel}fuel left")
    print(f"{car2.name} has: {car2.fuel}fuel left")

main()
