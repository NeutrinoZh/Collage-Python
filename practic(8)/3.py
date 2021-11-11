def odd_even_sort(array):
    for i in range(len(array)):
        for j in range(i & 1, len(array) - 1, 2):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
odd_even_sort(array)
print(array)