def counting_sort(a):
    k = max(a) + 1
    c = [0]*k
    
    for i in a:
        c[i] += 1

    for i in range(1, k):
        c[i] += c[i - 1]

    b = [0]*(len(a))

    for j in reversed(range(len(a))):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] = c[a[j]] - 1

    return b

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
array = counting_sort(array)
print(array)