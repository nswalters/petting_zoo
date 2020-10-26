from Animal import Animal
from datetime import date


class Goose(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(self, name, species, food, chip_num)
        self.swimming = False
