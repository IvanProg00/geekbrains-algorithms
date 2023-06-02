def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)

arr = [8, 4, -2, 4, 1, 6]
bubble_sort(arr)
print(arr)
