import math
import numpy
from typing import List
from scipy.optimize import linear_sum_assignment

class Character:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


def main():
    # Initialize groups
    reds, blues = init_characters()

    # Find pairings using the Hungarian Algorithm
    pairing_distance_array = create_array(reds, blues)
    row_ind, col_ind = linear_sum_assignment(pairing_distance_array)

    # Output pairings
    for i, red in enumerate(reds):
        print(red.name + " x " + blues[col_ind[i]].name)


def init_characters():
    reds = list()
    reds.append(Character("Midoriya", [4, 5, 3, 4]))
    reds.append(Character("Todoroki", [2, 3, 1, 4]))
    reds.append(Character("Bakugo", [5, 1, 1, 3]))
    reds.append(Character("Kirishima", [5, 4, 3, 2]))
    reds.append(Character("Shoji", [1, 4, 1, 3]))
    reds.append(Character("Kaminari", [4, 2, 4, 1]))
    reds.append(Character("Iida", [4, 4, 1, 4]))

    blues = list()
    blues.append(Character("Uraraka", [4, 5, 3, 2]))
    blues.append(Character("Asui", [2, 4, 2, 4]))
    blues.append(Character("Yaoyorozu", [2, 3, 2, 5]))
    blues.append(Character("Ashido", [5, 1, 4, 2]))
    blues.append(Character("Hagakure", [4, 3, 4, 2]))
    blues.append(Character("Kyouka", [3, 2, 2, 2]))
    blues.append(Character("Hatsume", [5, 1, 3, 5]))

    return reds, blues


# Create numpy array representing attribute distances between each red and blue
def create_array(reds: List[Character], blues: List[Character]):
    array = []
    for r, red in enumerate(reds):
        array.append([])

        for blue in blues:
            distance = math.dist(red.attributes, blue.attributes)
            array[r].append(distance)

    return numpy.array(array)


def create_character(name, energy, kindness, humor, int):
    attribs = [energy, kindness, humor, int]
    return Character(name, attribs)


def getScore(character1: Character, character2: Character):
    max_diff = 0
    sum_diff = 0
    for attrib in character1.attributes:
        value1 = character1.attributes[attrib]
        value2 = character2.attributes[attrib]

        diff = abs(value1 - value2)
        sum_diff += diff

        if diff > max_diff:
            max_diff = diff

    avg_diff = sum_diff / len(character1.attributes)

    total = avg_diff + max_diff
    return total


if __name__ == '__main__':
    main()
