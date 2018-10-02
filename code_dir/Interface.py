# -*- coding: utf-8 -*-

from code import Prime
from code import ElGamal


p = input("素数を入力してください")
q = input("素数を入力してください")

# pri = Prime(p, q)
el = ElGamal(q)

'''
print(pri.seek_L())
print(pri.seek_E())
print(pri.seek_D())
print(pri.N)

# print(pri.output())
'''
print(el.seek_root())
