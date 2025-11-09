from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'
CURRENT_YEAR = 2025

def main():
    """display all guitars in file"""
    guitars = load_guitars()
    guitars.sort()

    display_guitars(guitars)

    add_new_guitar()

    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)


def add_new_guitar():
    """add a new guitar"""
    with open(FILENAME, 'a') as out_file:
        name = input('\nEnter a guitar name if you want to add\nEnter guitar name: ')
        while name != "":
            year = get_valid_year()
            cost = get_valid_cost()
            new_guitar = Guitar(name, year, cost)
            print(f"{new_guitar.name},{new_guitar.year},{new_guitar.cost}", file=out_file)
            name = input('\nEnter a guitar name if you want to add\nEnter guitar name: ')


def get_valid_year():
    """prompt user for year and return it"""
    is_valid = False
    while not is_valid:
        try:
            year = int(input("Year of guitar: "))
            while year < 0 or year > CURRENT_YEAR:
                print("please enter a valid year")
                year = int(input("Year of guitar: "))
            is_valid = True
        except ValueError:
            print("please enter a valid number")
    return year


def get_valid_cost():
    """prompt user for cost and return it"""
    is_valid = False
    while not is_valid:
        try:
            cost = float(input("Cost of guitar: "))
            while cost < 0:
                print("please enter a valid year")
                cost = float(input("Cost of guitar: "))
            is_valid = True
        except ValueError:
            print("please enter a valid number")
    return cost


def display_guitars(guitars):
    """display guitars"""
    max_name_length = max(len(guitar.name) for guitar in guitars)
    for guitar in guitars:
        print(f"{guitar.name:{max_name_length + 3}}{guitar.year:6}{guitar.cost}")


def load_guitars():
    """load guitars to a list and return that list"""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    in_file.close()
    return guitars


if __name__ == '__main__':
    main()