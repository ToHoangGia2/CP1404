CURRENT_YEAR=2025

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



def test():
    guitar = Guitar("Guitar", 1977, 10)
    print(guitar)

test()