from .animal import Animal
from datetime import date


class Chicken(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = False
        self.shift = shift
