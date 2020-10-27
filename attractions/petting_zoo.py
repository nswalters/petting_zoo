from .attraction import Attraction
from movements import Walking


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    # Duck Typing Check
    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')
