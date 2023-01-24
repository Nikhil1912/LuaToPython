import sys

import TestEngine
from Sym import Sym
from Num import Num
from Utils import rnd,rand


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

def eg_check_rands(the):
    num1=Num()
    num2=Num()
    Seed=the['seed']
    for i in (1,1001):
        x,Seed = rand(0,1,Seed)
        num1.add(x)
    Seed=the['seed']
    for i in (1,1001):
        x,Seed = rand(0,1,Seed)
        num2.add(x)
    m1=rnd(num1.mid(),10)
    m2=rnd(num2.mid(),10)
    assert m1==m2 and .5==rnd(m1,1)
    
    """
    Seed=the.seed; for i=1,10^3 do num1:add( rand(0,1) ) end
  Seed=the.seed; for i=1,10^3 do num2:add( rand(0,1) ) end
  local m1,m2 = rnd(num1:mid(),10), rnd(num2:mid(),10)
  return m1==m2 and .5 == rnd(m1,1) end )
    """

