from animals import Bass, Llama, Horse, Cow, GardenSnake, Goose, RattleSnake, Duck
from attractions import PettingZoo, SnakePit, Wetlands


def main():

    varmint_village = PettingZoo(
        "Varmint Village", "cute and fuzzy critters to cuddle")
    slither_inn = SnakePit('Slither Inn', "stupendous snakes of all sizes")
    bubbling_brook = Wetlands('Bubbling Brook', "feathery and wet critters")

    dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
    snappy = RattleSnake("Snappy", "American RattleSnake", "frogs", 1044)
    donald = Duck("Donald", "Animated Duck", "Duck Food", 123)

    varmint_village.add_animal_pythonic(dolly)
    varmint_village.add_animal_pythonic(snappy)

    slither_inn.add_animal_pythonic(dolly)
    slither_inn.add_animal_pythonic(snappy)

    bubbling_brook.add_animal_pythonic(donald)
    bubbling_brook.add_animal_pythonic(snappy)

    # # swimmers
    # myBass = Bass("Wall Singer", "Black Bass", "Bass Nibbles", 123)
    # bubbling_brook.add_animal(myBass)

    # # walkers
    # miss_fuzz = Llama("Miss Fuzz", "domestic llama",
    #                   "morning", "Llama Chow", 456)
    # print(miss_fuzz.feed())
    # varmint_village.add_animal(miss_fuzz)

    # giddy_up = Horse("Giddy Up", "Friendly Mustang",
    #                  "afternoon", "Horse Chow", 789)
    # print(giddy_up.feed())
    # varmint_village.add_animal(giddy_up)

    # moo_moo = Cow("Betsy", "Holstein", "morning", "Cow Chow", 12345)
    # print(moo_moo.feed())
    # print(moo_moo.chip_number)
    # varmint_village.add_animal(moo_moo)

    # # slither-ers??
    # slimy_stan = GardenSnake(
    #     "Slimy Stan", "Slimy Garden Snake", "mice", 2222)
    # print(slimy_stan.feed())
    # slither_inn.add_animal(slimy_stan)

    # print("******")
    # varmint_village.get_animals()
    # print("******")
    # slither_inn.get_animals()
    # print("******")
    # bubbling_brook.get_animals()

    # print("******")
    # print("******")
    # print("LAST VARMINT: ", varmint_village.last_critter_added)

    # print("******")
    # print("******")
    # print("LAST SLITHER: ", slither_inn.last_critter_added)

    # print("******")
    # print("******")
    # print("LAST BUBBLING: ", bubbling_brook.last_critter_added)


main()
