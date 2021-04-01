def entfernen(vek):  # Entfernen der Zahlen die sich wiederholen.
    i = 0
    while i < len(vek) - 1:
        j = i + 1
        while j < len(vek):
            if vek[i] == vek[j]:
                vek.pop(j)
                j = j - 1
            j += 1
        i = i + 1


def reverse_number(x):  # Umkehrung eines Zahles
    x = int(str(x)[::-1])
    return x


def losung_2(liste):  # Anzahl der Zahlenpaare
    anzahl = 0
    for i in range(len(liste)):
        if reverse_number(liste[i]) in liste and liste[i] > 9 and (reverse_number(liste[i]) != liste[i]):
            anzahl += 1
    return anzahl // 2


def sort(vek):
    for i in range(len(vek) - 1):
        for j in range(i + 1, len(vek)):
            if vek[i] < vek[j]:
                aux = vek[i]
                vek[i] = vek[j]
                vek[j] = aux


def konkat(vek):
    kon = ''
    for i in range(len(vek)):
        kon = kon + str(vek[i])
    return int(kon)


def verschlusseln(vek):  # wir verschlusseln die liste mit "+"
    kript_el = vek[0]
    for i in range(len(vek)):
        vek[i] = vek[i] + kript_el


def transform(a, b):  # Umwandelt die Operanden in Zahlen um
    if a == "x":
        return b // 10 % 10
    elif a == "y":
        return b % 10
    else:
        return int(a)


def operation(s, x):  # Untersucht ob ein Element der Liste die Bedingung erfullt
    if s[1] == "=":
        rez = s[0]
        a = s[2]
        b = s[4]
        op = s[3]
    else:
        rez = s[4]
        a = s[0]
        b = s[2]
        op = s[1]
    a = transform(a, x)
    b = transform(b, x)
    rez = transform(rez, x)
    if op == "/":
        return rez == a/b
    if op == "*":
        return rez == a*b
    if op == "+":
        return rez == a+b
    if op == "-":
        return rez == a-b


def losung_5(vek):  # liest die Zeichen und durchquert die Liste
    s = "y-x=3"
    for i in range(len(vek)):
        if operation(s, vek[i]):
            print(vek[i])


def erste_ziff(zahl):  # Bestimmt die erste Ziffer einer Zahl
    if zahl < 10:
        return 0
    else:
        aux = zahl
        while aux > 9:
            aux = aux//10
        return aux


def len_teil_fol(vek):
    pos_init_max = -1
    pos_fin_max = -1
    lange = 0
    zahlvar = 0
    while zahlvar < len(vek) - 1:
        pos_init = zahlvar
        while zahlvar < len(vek) - 1 and (vek[zahlvar] % 10) == erste_ziff(vek[zahlvar+1]):
            zahlvar += 1
        pos_fin = zahlvar
        if (pos_fin - pos_init) > lange:
            pos_init_max = pos_init
            pos_fin_max = pos_fin
            lange = pos_fin - pos_init
        zahlvar += 1
    if lange == 0:
        print('es gibt keine entsprechende Teilfolge')
    else:
        print(vek[pos_init_max:pos_fin_max+1])


def ggt(var_a, var_b):
    while var_a != var_b:
        if var_a >= var_b:
            var_a = var_a - var_b
        else:
            var_b = var_b - var_a
    return var_a


def kgv(var_a, var_b):
    return var_a * var_b // ggt(var_a, var_b)


def ub_7(vek, indexf, indext,):
    if indexf >= indext:
        return 0
    else:
        allg_kgv = kgv(vek[indexf], vek[indexf + 1])
        for i in range(indexf + 2, indext):
            allg_kgv = kgv(allg_kgv, vek[i])
        return allg_kgv


def main():
    vek = [11, 11, 14, 49, 11, 22, 33, 44, 56, 78, 67, 96, 69, 69, 33, 21, 41, 90, 9]
    print("0. Exit")
    print("1. Entfernen")
    print("2. Anz sym Paaren")
    print("3. Konktenation")
    print("4. Verschlusseln")
    print("5. Beziehung")
    print("6. Domino Teilfolge")
    print("7. Kgv")
    x = int(input("Option:"))
    while x != 0:
        if x == 1:
            entfernen(vek)
            print(vek)
            x = int(input("Option:"))
        elif x == 2:
            print(losung_2(vek))
            x = int(input("Option:"))
        elif x == 3:
            sort(vek)
            print(konkat(vek))
            x = int(input("Option:"))
        elif x == 4:
            print(vek)
            verschlusseln(vek)
            print(vek)
            x = int(input("Option:"))
        elif x == 5:
            losung_5(vek)
            x = int(input("Option:"))
        elif x == 6:
            print(vek)
            len_teil_fol(vek)
            x = int(input("Option:"))
        elif x == 7:
            print(vek)
            print(ub_7(vek, 2, 6))
            x = int(input("Option:"))


main()
