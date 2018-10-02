# -*- coding: utf-8 -*-
from random import randint


def prime(e, L):
    def xgcd(b, n):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while n != 0:
            q, b, n = b // n, n, b % n
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return b, x0, y0
    g, x, _ = xgcd(self.E, self.L)
    d = x % self.L
    self.D = d
    return d


if __name__ == "__main__":
    print(prime(7, 55565444880))
