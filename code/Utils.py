import math
Seed=937162211

def rnd(n, nPlaces=3):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult

def rand(lo=0,hi=1):
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647
"""
function rand(lo,hi) --> n; a float "x" lo<=x < x
  lo, hi = lo or 0, hi or 1
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647 end
"""