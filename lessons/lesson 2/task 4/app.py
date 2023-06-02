def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)


def sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        sort(arr, low, p - 1)
        sort(arr, p + 1, high)


def partition(arr, low, high) -> int:
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i


arr = [5, 4, 3, 2, 1]
quick_sort(arr)
print(arr)

arr = [8, 4, -2, 4, 1, 6]
quick_sort(arr)
print(arr)
