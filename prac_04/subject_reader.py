"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
lines = []

def main():
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked
        #print("----------")
        lines.append(parts)
    input_file.close()
    return lines

def display_subjects(data):
    """This function will display the subjects data """
    for i in data:
        print(f"{i[0]:5} is taught by {i[1]:14} and has {i[2]:5} students")

main()