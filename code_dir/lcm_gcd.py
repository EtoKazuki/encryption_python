# -*- coding: utf-8 -*-


# 最大公約数を求める
def gcd(_a, _b):
    a = abs(_a)
    b = abs(_b)
    if(a == 0 or b == 0):
        return 0
    if(a >= b):
        r = a % b
        if(r == 0):
            return b
        else:
            return gcd(b, r)
    else:
        r = b % a
        if(r == 0):
            return a
        else:
            return gcd(a, r)


# 最小公倍数を求める
def lcm(a, b):
    return a * b // gcd(a, b)
