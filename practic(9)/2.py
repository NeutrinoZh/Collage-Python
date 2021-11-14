def heap_sort(array):
    length = len(array)

    def heapify(array, length, i):
        largest = i
        
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < length and array[i] < array[left]:
            largest = left

        if right < length and array[largest] < array[right]:
            largest = right
        
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, length, largest)

    
    for i in reversed(range(1, length // 2 )):
        heapify(array, length, i)

    for i in reversed(range(1, length)):
        array[i], array[0] = array[0], array[i]    
        heapify(array, i, 0)

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
heap_sort(array)
print(array)