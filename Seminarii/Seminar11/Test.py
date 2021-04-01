def datlesen(datei):
    dat = open(datei, 'r')
    summe = 0
    g = -1
    for i in dat:
        g += 1
        linie = i.strip(' \n').split(' ')
        if ((g+1) % 3 == 0) and linie[0][0] != '.':
            return "FEHLER"
        lange = 0
        for j in range(len(linie)):
            # print(linie[j])
            if linie[j].isnumeric():
                summe = summe + int(linie[j])
            else:
                q = 0
                while q < len(linie[j]):
                    if linie[j][q] in '^&|_.':
                        break
                    q += 1
                if q == len(linie[j]):
                    lange += len(linie[j])
        # print(lange)
        if lange > 123:
            return "FEHLER"
    if summe != 0 and not(prim(summe)):
        return "FEHLER"
    # print(summe)
    return "OK"


def prim(nr):
    if nr <= 1:
        return False

    if nr <= 3:
        return True

    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


def test_prim():
    assert prim(0) == False
    assert prim(1) == False
    assert prim(2) == True
    assert prim(5) == True
    assert prim(4) == False
    assert prim(100) == False
    assert prim(101) == True


def main():
    test_prim()
    print(datlesen('uba.txt'))


main()
