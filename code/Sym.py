import math
from collections import defaultdict

class Sym:
    def __init__(self):
        self.n = 0
        self.has = defaultdict(int)
        self.most = 0
        self.mode = None

    def add(self, x):
        if x != '?':
            self.n += 1
            self.has[x] += 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self, x):       # Don't know why x is passed as a parameter
        return self.mode

    def div(self, x):       # Don't know why x is passed as a parameter

        def fun(p):
            return p*math.log(p, 2)

        e = 0
        for n in self.has.values():
            e += fun(n/self.n)

        return -e