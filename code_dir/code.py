# -*- coding: utf-8 -*-


from lcm_gcd import gcd, lcm
from numpy.random import randint


class Prime:
    def __init__(self, _p, _q):
        self.p = int(_p)
        self.q = int(_q)

    def seek_N(self):
            self.N = self.p * self.q

    def seek_L(self):
            self.L = lcm(self.p - 1, self.q - 1)
            return self.L

    def seek_E(self):
        for e in range(2, self.L):
            if (gcd(e, self.L) == 1):
                self.E = e
                return self.E

    def seek_D(self):
        for d in range(2, self.L):
            if(((self.E * d) % self.L) == 1):
                self.D = d
                break
        return self.D

    # 暗号化
    def encryption(self, text_num):
        self.code_num = (text_num ** self.E) % self.N
        return self.code_num

    # 復号化
    def composite(self, coded_num):
        origin_num = (coded_num ** self.D) % self.N
        return origin_num


class ElGamal:
    def __init__(self, _p):
        self.p = int(_p)

    def prime(self, _n):
        _n = int(_n)
        for p in range(2, _n):
            if _n % p == 0:
                print(str(_n) + "は合成数")
                return False
        return True

    # 原始根を求める
    def seek_root(self):
        if((self.prime(self.p) is True) & (self.p > 3)):
            for r in range(1, self.p):
                root_list = []
                correct_list = [x for x in range(1, self.p)]
                for p_pow in range(1, self.p):
                    root_mod = (r**p_pow) % self.p
                    root_list.append(root_mod)
                if(sorted(root_list) == sorted(correct_list)):
                    self.r = r
                    return self.r

    # 鍵発行
    def seek_key(self):
        self.private = randint(0, self.p-1)  # 秘密鍵
        self.public = self.r ** self.private   # 公開鍵

    # 暗号化
    def encryption(self, message):
        ran = randint(0, self.p-1)
        self.c1 = self.r ** ran
        self.c2 = ((self.public ** ran) * message)
        return self.c1, self.c2

    # 復号化
    def composite(self, c1, c2):
        self.ori_message = c2/(c1 ** self.private)
        return int(self.ori_message)


# ラビン暗号
class Rabin():
    def __init__(self, _p, _q):
        self.p = int(_p)
        self.q = int(_q)

    # 入力された数が素数か調べる
    def prime(self, _n):
        _n = int(_n)
        for p in range(2, _n):
            if _n % p == 0:
                print(str(_n) + "は合成数")
                return False
        return True

    def prime_conform(self):
        p_can = self.prime(self.p)
        q_can = self.prime(self.q)

        if(p_can & q_can):
            self.N = self.p * self.q
            return True
        else:
            print("素数を入力してください")
            return False

    # 暗号化
    def encryption(self, message):
        self.ex = (message ** 2) % self.N
        return self.ex

    # 復号化
    def composite(self, coded_num):
        x_1 = ((coded_num) ** 1/2) % self.N

        return x_1
