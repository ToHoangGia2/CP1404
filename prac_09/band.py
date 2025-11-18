class Band:
    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.name} ({self.members})"



    def add(self, member):
        self.members.append(member)