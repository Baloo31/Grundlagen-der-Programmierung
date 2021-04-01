def anz_1(li, idx):
    if li[idx] == 1:
        return 1 + anz_1(li, idx + 1)
    elif li[idx] > 1:
        return 0
    return anz_1(li, idx + 1)


def anz_1_2(li, left, right):
    if left >= right:
        return 0
    m = (left+right) // 2
    if li[m] == 1:
        return anz_1_2(li, left, m) + anz_1_2(li, m+1, right) + 1
    return anz_1_2(li, left, m) + anz_1_2(li, m+1, right)


def main():
    print(anz_1([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3], 0))
    l1 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    print(anz_1_2(l1, 0, len(l1)))


main()
