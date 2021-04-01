def interclasare(l1, l2):
    l3 = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    while i < len(l1):
        l3.append(l1[i])
        i += 1

    while j < len(l2):
        l3.append(l2[j])
        j += 1

    return l3


def test_interclasare():
    assert interclasare([], []) == []
    li = [1]
    assert interclasare(li, []) == li
    li = [1, 2, 3, 4]
    assert interclasare(li, li) == [1, 1, 2, 2, 3, 3, 4, 4]
    assert interclasare([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def main():
    l1 = [0, 1, 3]
    l2 = [2, 4, 6, 8, 10, 12, 13]
    print(interclasare(l1, l2))


main()
