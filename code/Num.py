import math


class Num:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf

    def add(self, n):
        if n != '?':
            self.n += 1
            d = n - self.mu
            self.mu += (d/self.n)     # Might have to replace with integer division
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
            
    def mid(self):
        #returns mean
        return self.mu

    def div(self):
        #returns standard devaition
        return 0 if self.m2 < 0 or self.n < 2 else pow(self.m2/(self.n - 1), 0.5)
