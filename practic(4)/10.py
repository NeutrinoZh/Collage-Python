import time

def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


#----------------------------------------#

def test():
    arr = [99, 4, 7, 1, 8, 10, 8, 0]

    print(" ", arr)
    insertionSort(arr)
    print(" ", arr)

def speedTest(n):
    arr = [ i for i in range(n) ]

    start_time = time.time()
    insertionSort(arr)
    end_time = time.time()

    print(" time:", f"{end_time - start_time} seconds. num: {n}")    

#----------------------------------------#

print("Test:")
test()

print("Speed test:")
speedTest(5000)   # 0
speedTest(10000)  # 0.0009
speedTest(100000) # 0.01