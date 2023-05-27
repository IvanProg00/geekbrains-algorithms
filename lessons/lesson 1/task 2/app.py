def simple(n):  # O(n^2)
    res = []

    for i in range(2, n + 1):
        simple = True

        j = 2
        while j * j <= i:
            if i % j == 0:
                simple = False
                break
            j += 1

        if simple:
            res.append(i)

    return res


result = simple(100)
print(result)
