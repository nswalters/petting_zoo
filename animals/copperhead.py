from .animal import Animal
from datetime import date


class CopperHead(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = False
