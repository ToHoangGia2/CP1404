CURRENT_YEAR=2025
APPROVED_AGE=50

class Guitar:
    def __init__(self,name="", year=0, cost=0):
        """define value"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return a string output"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """return age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """return True if the guitar is vintage"""
        return self.get_age() >= APPROVED_AGE

def test():
    guitar = Guitar("Guitar", 1977, 10)
    print(guitar)
    print(guitar.get_age())
    print(guitar.is_vintage())

test()