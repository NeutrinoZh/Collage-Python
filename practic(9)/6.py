def bitwise_sort(array):
    array = [str(i) for i in array]
    k = len(max(array, key=int))

    array = list(map(lambda x: '0' * (k - len(x)) + x, array))

    for l in reversed(range(k)):
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                if array[j][l] < array[min][l]:
                    min = j
            array[min], array[i] = array[i], array[min]

    return [int(i) for i in array]

array = [29, 457, 657, 839, 36, 720, 355]
array = bitwise_sort(array)
print(array)