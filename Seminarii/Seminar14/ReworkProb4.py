def prima_ap(l, left, right, nr):
    if l[0] == nr:
        return 0
    if left > right:
        return -1
    mij = (left + right) // 2
    if l[mij] == nr and l[mij-1] != nr:
        return mij
    if nr <= l[mij]:
        return prima_ap(l, left, mij-1, nr)
    return prima_ap(l, mij+1, right, nr)


def ultima_ap(l, left, right, nr):
    if l[len(l) - 1] == nr:
        return len(l) - 1
    if left > right:
        return -1
    mij = (left + right) // 2
    if l[mij] == nr and l[mij+1] != nr:
        return mij
    if nr < l[mij]:
        return ultima_ap(l, left, mij-1, nr)
    return ultima_ap(l, mij+1, right, nr)


def sir(li, nr):
    stanga = prima_ap(li, 0, len(li), nr)
    dreapta = ultima_ap(li, 0, len(li), nr)
    if stanga == -1 or dreapta == -1:
        return "Nu exista un sir de {}".format(nr)
    return dreapta - stanga + 1


def main():
    li = [0, 0, 0, 0, 0, 1, 1, 1, 1, 3, 4]
    print(sir(li, 1))


main()
