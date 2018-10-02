# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from os import path
import re
from Str_to_Int import *
from code import *
import math
from random import randint
import numpy as np


# 暗号化するためのクラス
class Application_for_encryption(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 暗号化するための手法一覧
        self.fil_label = tk.Label(root, text="ファイルパス")
        self.fil_label.pack(side=tk.LEFT)
        self.entry = tk.Entry(root, bd=1)
        self.entry.pack(side=tk.LEFT)

        self.label = tk.Label(self, text="暗号手法一覧")
        self.label.pack(side="top")

        self.button_rsa = tk.Button(self)
        self.button_rsa["text"] = "RSA"
        self.button_rsa["command"] = self.push_rsa
        self.button_rsa.pack(side="top")

        self.button_el = tk.Button(self)
        self.button_el["text"] = "ElGamal"
        self.button_el["command"] = self.push_Elgamal
        self.button_el.pack(side="top")

        self.button_rabin = tk.Button(self)
        self.button_rabin["text"] = "Rabin"
        self.button_rabin["command"] = self.push_Rabin
        self.button_rabin.pack(side="top")

        # 復号化するときの一覧
        self.label = tk.Label(self, text="復号化一覧")
        self.label.pack(side="top", pady=10)

        self.button_composite_rsa = tk.Button(self)
        self.button_composite_rsa["text"] = "RSA復号化"
        self.button_composite_rsa["command"] = self.push_composite_rsa
        self.button_composite_rsa.pack(side="top")

        self.button_composite_el = tk.Button(self)
        self.button_composite_el["text"] = "ElGamal復号化"
        self.button_composite_el["command"] = self.push_composite_Elgamal
        self.button_composite_el.pack(side="top")

        self.label = tk.Label(self, text="終了ボタン")
        self.label.pack(side="top", pady=10)

        self.quit = tk.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # RSAが押された時
    def push_rsa(self):

        # 平文を取得
        value = str(self.entry.get())
        text = self.find_file(value)
        int_text_list = str_to_int(text)

        # 素数生成
        prime_list = self.prime_generator()
        while(True):
            p = randint(0, len(prime_list)-1)
            q = randint(0, len(prime_list)-1)
            if(p != q):
                break

        # 暗号化
        print("選ばれた素数は{}と{}です".format(prime_list[p], prime_list[q]))
        self.pri = Prime(prime_list[p], prime_list[q])
        self.pri.seek_N()
        self.pri.seek_L()
        E = self.pri.seek_E()
        D = self.pri.seek_D()
        encry_str = ""
        for num in int_text_list:
            num = self.pri.encryption(int(num))
            encry_str += str(num)+","
        print("公開鍵は{}と{}".format(E, self.pri.N))
        print("秘密鍵は{}と{}".format(D, self.pri.N))
        print("")

        # ファイル書き込み
        file_name = "rsa"
        self.write_file(encry_str, value, file_name)

    # ElGamalが押された時
    def push_Elgamal(self):
        # 平文を取得
        value = str(self.entry.get())
        text = self.find_file(value)
        int_text_list = str_to_int(text)

        # 素数生成
        prime_list = self.prime_generator()
        p = randint(0, len(prime_list)-1)

        # 暗号化
        self.el = ElGamal(prime_list[p])
        self.el.seek_root()
        self.el.seek_key()
        encry_str = ""
        for num in int_text_list:
            c1, c2 = self.el.encryption(int(num))
            encry_str += str(c1)+","+str(c2)+","
        print("公開鍵は{}".format(self.el.public))
        print("秘密鍵は{}".format(self.el.private))

        # ファイル書き込み
        file_name = "elgamal"
        self.write_file(encry_str, value, file_name)

    # Rabinが押された時
    def push_Rabin(self):
        # 平文を取得
        value = str(self.entry.get())
        text = self.find_file(value)
        int_text_list = str_to_int(text)

        # 素数生成
        prime_list = self.prime_generator_rabin()
        p = prime_list[0]
        q = prime_list[1]

        # 暗号化
        self.ra = Rabin(p, q)
        self.ra.prime_conform()
        encry_str = ""
        for num in int_text_list:
            num = self.ra.encryption(int(num))
            encry_str += str(num)+","
        print("秘密鍵は{}と{}".format(self.ra.p, self.ra.q))
        print("公開鍵は{}".format(self.ra.N))

        # 暗号化した文をファイル書き込み
        file_name = "rabin"
        self.write_file(encry_str, value, file_name)

    # RSA復号化が押されたとき
    def push_composite_rsa(self):
        ori_int_list = []
        value = str(self.entry.get())
        text = self.find_file(value)
        text_list = text.rsplit(",")
        del text_list[-1]
        for i in text_list:
            ori_int = self.pri.composite(int(i))
            ori_int_list.append(ori_int)
        ori_message = int_to_str(ori_int_list)
        return ori_message

    # Elgamal復号が押されたとき
    def push_composite_Elgamal(self):
        ori_int_list = []
        value = str(self.entry.get())
        text = self.find_file(value)
        text_list = text.rsplit(",")
        del text_list[-1]
        for i in range(int(len(text_list)/2)):
            ori_int = self.el.composite(int(text_list[2*i]), int(text_list[2*i+1]))
            ori_int_list.append(ori_int)
        ori_message = int_to_str(ori_int_list)
        return ori_message

    # Rabin復号が押されたとき
    def push_composite_Rabin(self):
        ori_int_list1 = []

        value = str(self.entry.get())
        text = self.find_file(value)
        text_list = text.rsplit(",")
        del text_list[-1]
        for i in text_list:
            ori_int1 = self.ra.composite(int(i))
            ori_int_list1.append(int(ori_int1))

        ori_message1 = int_to_str(ori_int_list1)

        return ori_message1

    # ファイル存在するかどうか調べる
    # あったらファイルを開いて文字列を代入
    def find_file(self, file_path):
        if(path.exists(file_path) is True):
            with open(file_path, mode="r") as f:
                text = f.read()
            return text
        else:
            print("This file is not exists")

    def write_file(self, text, file_path, file_name):
        base_dir_pair = path.split(file_path)
        new_path = base_dir_pair[0]+"/{}_encryption.txt".format(file_name)
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(text)

    def write_rabin_file(self, text, file_path, file_name):
        base_dir_pair = path.split(file_path)
        new_path = base_dir_pair[0]+"/{}_encryption.txt".format(file_name)
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(text)

    def prime_generator(self):
        min_len = 1000
        max_len = 10000
        pri_list = []
        for pri_n in range(min_len, max_len):
            if(self.is_prime(pri_n, k=50) == True):
                pri_list.append(pri_n)
            else:
                continue
            if(len(pri_list) == 10):
                return pri_list

    def prime_generator_rabin(self):
        min_len = 1000
        max_len = 10000
        pri_list = []
        for pri_n in range(min_len, max_len):
            if((self.is_prime(pri_n, k=50) == True) & (pri_n % 4 == 3)):
                pri_list.append(pri_n)
            else:
                continue
            if(len(pri_list) == 2):
                return pri_list

    def is_prime(self, q, k=50):
        q = abs(q)
        # 計算するまでもなく判定できるものははじく
        if q == 2:
            return True
        if (q < 2) or (q & 1) == 0:
            return False

        # n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
        d = (q-1) >> 1
        while d & 1 == 0:
            d >>= 1

        # 判定をk回繰り返す
        for i in range(k):
            a = randint(1, q-1)
            t = d
            y = pow(a, t, q)
            # [0,s-1]の範囲すべてをチェック
            while t != q-1 and y != 1 and y != q-1:
                y = pow(y, 2, q)
                t <<= 1
            if (y != q-1) and (t & 1) == 0:
                return False
        return True


root = tk.Tk()
root.geometry("500x500")
app1 = Application_for_encryption(master=root)
app1.mainloop()
