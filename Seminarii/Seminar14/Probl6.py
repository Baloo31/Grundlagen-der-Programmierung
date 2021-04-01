def max_recursiv(l, left, right):
    if left == right:
        return l[left]
    mij = (left + right) // 2
    max1 = max_recursiv(l, left, mij - 1)
    max2 = max_recursiv(l, mij + 1, right)
    return max1 if max1 > max2 else max2


li = [1, 2, 3, 4, 5, 6]
print(max_recursiv(li, 0, len(li) - 1))
