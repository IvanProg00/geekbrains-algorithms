def sum1(n): # O(n)
    count = 0
    for i in range(1, n + 1):
        count += i
    return count


def sum2(n): # O(1)
    return n * (n + 1) // 2


n = 10

result1 = sum1(n)
print(result1)

result2 = sum2(n)
print(result2)
