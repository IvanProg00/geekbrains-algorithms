def binary_search(arr, val):
    left = 0
    right = len(arr)

    while left < right:
        m = (left + right) // 2

        if arr[m] == val:
            return m
        elif arr[m] < val:
            left = m + 1
        else:
            right = m
    return -1


arr = [-2, 4, 5, 8, 12, 18, 24]
print(binary_search(arr, 4))  # 1
print(binary_search(arr, 8))  # 3
print(binary_search(arr, 18))  # 5
print(binary_search(arr, 24))  # 6
print(binary_search(arr, -2))  # 0
print(binary_search(arr, 7))  # -1
