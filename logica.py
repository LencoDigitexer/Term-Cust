import os

asd = []

PU = "/data/data/com.termux/files/usr/share/Term-Cust/Base/PS1/PU"

for a, b, c in os.walk(PU):
    asd.append(b)

if len(asd[0]) == 0:
    print('''
Список слотов пуст.
Выйдите назад и создайте новый слот''')
else:
    for i in asd[0]:
        c = str(asd[0].index(i) + 1)
        print("[ {} ] - {}".format(c, i))
    print("Выберите слот для запуска")

    a = input()
    if a in [str(i) for i in range(1, len(asd[0]) + 1)]:
        cop = (asd[0][int(a) - 1]) + "/.bashrc"
        os.system("cp /data/data/com.termux/files/usr/share/Term-Cust/Base/PS1/PU/" + cop + " /data/data/com.termux/files/usr/share/Term-Cust/Base/PS1/PU")
    else:
        print("ошибка")