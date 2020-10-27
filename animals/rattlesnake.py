from .animal import Animal
from datetime import date
from movements import Slithering


class RattleSnake(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        self.slithering = False
