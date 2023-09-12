import re
from enum import Enum


class GeoPoliticalZone(Enum):
    NORTH_CENTRAL = "Benue", "FCT", "Kogi", "Nassarawa", "Niger", "Plateau"
    NORTH_EAST = "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yoba"
    NORTH_WEST = "Kaduna", "Katsina", "Kano", "Sokoto", "Jigawa", "Zamfara"
    SOUTH_SOUTH = "Akwa_ibom", "Bayelsa", "Delta", "Edo", "Rivers"
    SOUTH_WEST = "Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"
    SOUTH_EAST = "Abia", "Anambra", "Ebonyi" "Enugu", "Imo"


def user():
    state = input("Enter a State:  ")
    if not re.search("^(?!$)\D+$", state):
        print("invalid input")
    elif state != GeoPoliticalZone:
        print("Not a State")
        if state.capitalize() in GeoPoliticalZone.NORTH_CENTRAL.value:
            print("The GeoPoliticalZone is NORTH CENTRAL")
        elif state.capitalize() in GeoPoliticalZone.NORTH_EAST.value:
            print("The GeoPoliticalZone is NORTH EAST")
        elif state.capitalize() in GeoPoliticalZone.NORTH_WEST.value:
            print("The GeoPoliticalZone is NORTH WEST")
        elif state.capitalize() in GeoPoliticalZone.SOUTH_SOUTH.value:
            print("The GeoPoliticalZone is SOUTH SOUTH")
        elif state.capitalize() in GeoPoliticalZone.SOUTH_WEST.value:
            print("The GeoPoliticalZone is SOUTH WEST")
        elif state.capitalize() in GeoPoliticalZone.SOUTH_EAST.value:
            print("The GeoPoliticalZone is SOUTH WEST")
        else:
            print("Your input is not a State")
            user()


if __name__ == "__main__":
    user()
