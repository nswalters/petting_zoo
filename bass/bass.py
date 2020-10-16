from datetime import date


class Bass:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

    def __str__(self):
        return f"My name is {self.name} and I am a {self.species}"
