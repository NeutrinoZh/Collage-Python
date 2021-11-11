def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
selection_sort(array)
print(array)