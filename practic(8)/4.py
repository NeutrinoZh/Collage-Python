def shell_sort(array):
    d = len(array) / 2
    while d >= 1:
        int_d = int(d)
        for i in range(int_d, len(array)):
            j = i
            while (j >= int_d) and (array[j - int_d] > array[j]):
                array[j], array[j - int_d] = array[j - int_d], array[j]
                j -= int_d
        d = d / 2
    
array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
shell_sort(array)
print(array)