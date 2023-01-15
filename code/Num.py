import math


class Num:
    def __init__(self):
        self.n = self.mu = self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf

    def add(self, n):
        if n != '?':
            self.n += 1
            d = n - self.mu
            self.mu += d/self.n     # Might have to replace with integer division
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.m2 < 0 or self.n < 2 else pow(self.m2/(self.n - 1), 0.5)
