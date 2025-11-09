from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'

def main():
    """a"""
    guitars = load_guitars()
    guitars.sort()

    display_guitars(guitars)


def display_guitars(guitars):
    max_name_length = max(len(guitar.name) for guitar in guitars)
    for guitar in guitars:
        print(f"{guitar.name:{max_name_length + 3}}{guitar.year:6}{guitar.cost}")


def load_guitars():
    guitars = []
    with open(FILENAME) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
    return guitars


if __name__ == '__main__':
    main()