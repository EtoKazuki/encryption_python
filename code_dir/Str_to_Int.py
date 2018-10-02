# -*- coding: utf-8 -*-


# 文字列の平文を数値化する
def str_to_int(chr):
    list_ord = []
    str_list = list(chr)  # 文字列をリストに格納
    for s in str_list:
        ord_chr = ord(s)
        list_ord.append(ord_chr)

    return list_ord


# 数値化した平文を文字列に直す
def int_to_str(num_list):
    chr_list = []
    for i in num_list:
        ori_chr = chr(i)
        chr_list.append(ori_chr)

    maped_list = map(str, chr_list)
    original_message = "".join(maped_list)

    print(original_message)
    return original_message
