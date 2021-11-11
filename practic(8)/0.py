def bubble_sort(array):
    length = len(array) - 1
    for i in range(0, length):
        for j in range(length, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
bubble_sort(array)
print(array)