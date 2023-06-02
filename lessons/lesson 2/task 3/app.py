def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [5, 4, 3, 2, 1]
insertion_sort(arr)
print(arr)

arr = [8, 4, -2, 4, 1, 6]
insertion_sort(arr)
print(arr)
