from prac_06.guitar import Guitar

def main():
    guitars =[]

    print("My guitars!")
    name = input("Name: ")
    while name !="":
        year = get_number("Year: ",False)
        cost = get_number("Cost: $",True)
        new_guitar = Guitar(name,year,cost)
        guitars.append(new_guitar)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


def get_number(text, allow_float):
    """prompt user for number input then check it"""
    valid = True
    while valid:
        try:
            number = float(input(text)) if allow_float else int(input(text))
            if number > 0:
                valid = False
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Please enter a valid number")


main()
