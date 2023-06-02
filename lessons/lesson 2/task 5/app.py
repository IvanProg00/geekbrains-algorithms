def merge_sort(arr):
    sort(arr, 0, len(arr) - 1)


def sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        sort(arr, mid + 1, high)
        sort(arr, low, mid)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = mid - low + 1
    right = high - mid

    left_arr = [arr[low + i] for i in range(left)]
    right_arr = [arr[mid + 1 + i] for i in range(right)]

    i = 0
    j = 0
    pos = low

    while i < left and j < right:
        if left_arr[i] <= right_arr[j]:
            arr[pos] = left_arr[i]
            i += 1
        else:
            arr[pos] = right_arr[j]
            j += 1
        pos += 1

    for i in range(i, left):
        arr[pos] = left_arr[i]
        pos += 1

    for j in range(j, right):
        arr[pos] = right_arr[j]
        pos += 1


arr = [5, 4, 3, 2, 1]
merge_sort(arr)
print(arr)

arr = [8, 4, -2, 4, 1, 6]
merge_sort(arr)
print(arr)
