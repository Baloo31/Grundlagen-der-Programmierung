def verifica(li, suma):
    difset = set()
    for i in range(len(li)):
        difset.add(li[i])
        dif = suma - li[i]
        for j in range(i+1, len(li)):
            if dif - li[j] in difset:
                return li[i], li[j], dif-li[j]
    return None


def main():
    li = [15]
    print(verifica(li, 45))
    li = [4, 3, 1, 0, 44]
    print(verifica(li, 45))
    li = [1, 2, 3, 4, 5, 10, 30]
    print(verifica(li, 45))


main()
