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


def main():
    myBass = Bass("Wall Singer", "Black Bass")

    print(myBass)

    roberto = Llama("Roberto", "alpaca", "midday")
    print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')


main()
