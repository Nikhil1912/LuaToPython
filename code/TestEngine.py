# Referenced : https://www.youtube.com/watch?v=aDTCnAfmyZA

import Tests
from inspect import getmembers, isfunction

tests = [t for t in getmembers(Tests) if isfunction(t[1]) and t[0].startswith("eg_")]


def run(the):
    fails = 0
    for test in tests:
        t_name, t_func = test
        try:
            t_func(the)
            print(f"PASS : {t_name}")
        except AssertionError:
            print(f"FAIL : {t_name}")
            fails += 1

    return fails
