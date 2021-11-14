from time import process_time
from itertools import count

def karatsuba_mult(x, y):
    x = [int(i) for i in x if i.isdigit()]
    y = [int(i) for i in y if i.isdigit()]

    n = max(len(x), len(y))

    while n & (n - 1):
        n += 1


    num_zeros = n * 2 - (len(x) + len(y) + 1)

    def extend(v):
        v = v[::-1]
        v.extend([0 for i in range((n - len(v)))])
        v = v[::-1]
        return v

    x = extend(x)
    y = extend(y)

    def finalize(a):
        while True:
            one = True
            for i in range(1, len(a)):
                num = a[i] // 10
                a[i - 1] += num
                a[i] %= 10

                one = one and (num == 0)
            
            if one:
                break
        return a
    def deleteZeros(a):
        return list(filter(lambda i, c=count(0, 1): next(c) >= num_zeros, a))
    def to_str(a):
        a = [str(i) for i in a]
        return ''.join(a)

    def native_mult(x, y):
        assert type(x) == list,  'type(x) != list'
        assert type(y) == list,  'type(y) != list'
        assert len(x) == len(y), 'len(x) != len(y)'

        n = len(x)
        if not n:
            return []
        
        def mult():
            result = [0]*(2*n)
            for i in range(n):
                for j in range(n):
                    result[i + j] += x[i] * y[j]
            return result
        
        result = mult()
        result = finalize(result)
        return result
    def karatsuba(x, y):
        n = len(x)
        if n <= 32:
            return native_mult(x, y)

        result = [0]*(2*n)
        k = n // 2

        xr = [x[i] for i in range(0, k)]
        xl = [x[i] for i in range(k, len(x))]
        yr = [y[i] for i in range(0, k)]
        yl = [y[i] for i in range(k, len(y))]

        p1 = karatsuba(xl, yl)
        p2 = karatsuba(xr, yr)

        xlr = [0]*k
        ylr = [0]*k

        for i in range(k):
            xlr[i] = xl[i] + xr[i]
            ylr[i] = yl[i] + yr[i]
        
        p3 = karatsuba(xlr, ylr)

        for i in range(n):
            p3[i] -= p2[i] + p1[i]

        for i in range(n):
            result[i] = p2[i]

        for i in range(n, 2 * n):
            result[i] = p1[i - n]

        for i in range(k, n + k):
            result[i] += p3[i - k]

        return result
        
    result = finalize(karatsuba(x, y))
    result = deleteZeros(result)
    result.pop()
    return to_str(result)

def read(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except:
        print('Could not open file in path:', path)

a, b = read('a.txt'), read('b.txt')

try:
    t = process_time()
    print(karatsuba_mult(a, b))
    print('time:', process_time() - t)
except AssertionError as e:
    print(e)