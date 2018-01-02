sya = int(input("借金>"))
riritu = int(input("年利率(%)>"))
hennsai = int(input("返済額>"))
count = 0


while True:
    count += 1
    if sya <= hennsai:
        sya = int(((sya*riritu/100)/12 + sya))
        sumhen = hennsai*(count-1)+sya
        print(count,"月: 返済額",sya,"円 これで完済。 返済総額:",sumhen,"円")
        break
    sya = int(((sya*riritu/100)/12 + sya) - hennsai)
    print(count,"月:返済額",hennsai,"円 残り",sya,"円")
