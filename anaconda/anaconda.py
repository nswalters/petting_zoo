from datetime import date


class Anaconda:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = False
        self.food = food

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f"My name is {self.name} and I am a {self.species}"
