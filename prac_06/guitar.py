class Guitar:
    def __init__(self,name="", year=0, cost=0):
        """define value"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

def test():
    guitar = Guitar("Guitar", 20, 10)
    print(guitar)

test()