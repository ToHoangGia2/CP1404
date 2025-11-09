from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'

def main():
    """a"""
    guitars = []
    with open(FILENAME) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)

    max_name_length = max(len(guitar.name) for guitar in guitars)

    guitars.sort()

    for guitar in guitars:
        print(f"{guitar.name:{max_name_length + 3}}{guitar.year:6}{guitar.cost}")


if __name__ == '__main__':
    main()