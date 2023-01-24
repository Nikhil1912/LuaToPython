import sys

import TestEngine
from Sym import Sym
from Num import Num
from Utils import rnd


def eg_check_syms(the):
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    assert 'a' == sym.mid() and 1.379 == rnd(sym.div())


def eg_check_nums(the):
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    assert 11 / 7 == num.mid() and 0.787 == rnd(num.div())

def eg_the(the):
    print(the)
    pass