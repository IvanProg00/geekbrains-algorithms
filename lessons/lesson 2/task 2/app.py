def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]



arr = [5, 4, 3, 2, 1]
selection_sort(arr)
print(arr)

arr = [8, 4, -2, 4, 1, 6]
selection_sort(arr)
print(arr)
