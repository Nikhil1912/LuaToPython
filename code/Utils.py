import math


def rnd(n, nPlaces=3):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult

def rand(lo=0,hi=1,Seed=937162211):
    #Seed=937162211
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647,Seed

def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi))

