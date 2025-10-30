class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        """add value to self"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if self is a dynamic language"""
        return self.typing == "Dynamic"

    def __str__(self):
        """return a string of the language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, {self.year}"