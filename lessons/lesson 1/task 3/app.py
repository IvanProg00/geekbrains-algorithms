def cubs(k, n):
    return rec_cubs(0, k, n)


def rec_cubs(depth, k, n):
    if depth == k:
        return 1

    count = 0

    for _ in range(1, n + 1):
        count += rec_cubs(depth + 1, k, n)

    return count


result = cubs(4, 6)
print(result)
