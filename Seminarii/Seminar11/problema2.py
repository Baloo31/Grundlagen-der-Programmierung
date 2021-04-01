def sorted_li(li):
    nrz, nru, nrd = 0, 0, 0
    for el in li:
        if el == 0:
            nrz += 1
        elif el == 1:
            nru += 1
        else:
            nrd += 1
    k = 0
    while nrz != 0:
        li[k] = 0
        nrz -= 1
        k += 1
    while nru != 0:
        li[k] = 1
        nru -= 1
        k += 1
    while nrd != 0:
        li[k] = 2
        nrd -= 1
        k += 1
    return li


def main():
    li = [1, 1, 0, 1, 2, 1, 2, 0, 2, 1, 0, 0, 0, 1, 1, 2, 2, 2, 0, 0]
    print(sorted_li(li))


main()
