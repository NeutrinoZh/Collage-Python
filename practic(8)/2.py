def gnome_sort(array):
    i = 1
    j = 2
    while i < len(array):
        if array[i - 1] < array[i]:
            i = j
            j += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
gnome_sort(array)
print(array)