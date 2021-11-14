def quick_sort(array, p, r):
    def partition(p, r):
        x = array[p]
        i = p
        
        for j in range(p + 1, r + 1):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]        
        array[p], array[i] = array[i], array[p]

        return i

    if p < r:
        x = partition(p, r)
        quick_sort(array, p, x - 1)
        quick_sort(array, x + 1, r)
    return array

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
array = quick_sort(array, 0, len(array) - 1)
print(array)