import math


def rnd(n, nPlaces=3):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult
