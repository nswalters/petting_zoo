from Animal import Animal
from datetime import date


class GardenSnake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = False

    def feed(self):
        return f'{self.name} ate {self.food} with one swallow on {date.today().strftime("%m/%d/%Y")}'
