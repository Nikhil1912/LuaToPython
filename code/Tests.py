import TestEngine
from Sym import Sym
from Num import Num
from Utils import rnd


def eg_check_syms():
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    assert 'a' == sym.mid() and 1.379 == rnd(sym.div())


def eg_check_nums():
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    assert 11 / 7 == num.mid() and 0.787 == rnd(num.div())


if __name__ == "__main__":
    TestEngine.run()
