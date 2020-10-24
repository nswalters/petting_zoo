from datetime import date


class Cow:
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = False
        self.shift = shift
        self.food = food
        self.__chip_num = chip_num  # privately scoped attribute

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f"My name is {self.name} and I am a {self.species}"

    @property  # the getter
    def chip_number(self):
        return self.__chip_num

    @chip_number.setter  # the setter
    def chip_number(self, number):
        pass
