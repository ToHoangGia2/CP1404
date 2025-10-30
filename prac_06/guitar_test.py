from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 2000.1)

print(f"{guitar.name} get_age() - Expected {103}. Got {guitar.get_age()}")
print(f"{another.name} get_age() - Expected {12}. Got {another.get_age()}")
print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
print(f"{another.name} is_vintage() - Expected {False}. Got {another.is_vintage()}")
