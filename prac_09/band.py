class Band:
    def __init__(self, name=""):
        self.name = name
        self.members = []

    def add(self, member):
        self.members.append(member)