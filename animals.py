from bass import Bass
from chicken import Chicken
from copperhead import CopperHead
from coralsnake import CoralSnake
from cow import Cow
from duck import Duck
from gardensnake import GardenSnake
from goat import Goat
from goose import Goose
from horse import Horse
from llama import Llama
from rattlesnake import RattleSnake
from swan import Swan
from turtle import Turtle

from attractions import PettingZoo, SnakePit, Wetlands


def main():

    varmint_village = PettingZoo("Varmint Village")
    slither_inn = SnakePit('Slither Inn')
    bubbling_brook = Wetlands('Bubbling Brook')

    # swimmers
    myBass = Bass("Wall Singer", "Black Bass", "Bass Nibbles")
    bubbling_brook.add_animal(myBass)

    # walkers
    miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
    print(miss_fuzz.feed())
    varmint_village.add_animal(miss_fuzz)

    giddy_up = Horse("Giddy Up", "Friendly Mustang", "afternoon", "Horse Chow")
    print(giddy_up.feed())
    varmint_village.add_animal(giddy_up)

    # slither-ers??
    slimy_stan = GardenSnake(
        "Slimy Stan", "Slimy Garden Snake", "mice")
    print(slimy_stan.feed())
    slither_inn.add_animal(slimy_stan)

    print("******")
    varmint_village.get_animals()
    print("******")
    slither_inn.get_animals()
    print("******")
    bubbling_brook.get_animals()


main()
