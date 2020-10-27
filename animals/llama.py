from .animal import Animal
from datetime import date
from movements import Walking


class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        # super().__init__(name, species, food, chip_num)
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.walking = False
        self.shift = shift
