class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals(self):
        print(f"{self.attraction_name} is where you'll find {self.description}, like:")
        for animal in self.animals:
            print(
                f'\t* {animal.name} the {animal.species}')


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "stupendous snakes of all sizes"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals(self):
        print(f"{self.attraction_name} is where you'll find {self.description}, like:")
        for animal in self.animals:
            print(
                f'\t* {animal.name} the {animal.species}')


class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "feathery and wet critters"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals(self):
        print(f"{self.attraction_name} is where you'll find {self.description}, like:")
        for animal in self.animals:
            print(
                f'\t* {animal.name} the {animal.species}')
