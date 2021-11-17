import time
from itertools import count

def native_mult(x, y):
    assert type(x) == str, 'type(x) != str'
    assert type(y) == str, 'type(y) != str'

    if not (len(x) and len(y)):
        return ''

    x = [int(i) for i in x if i.isdigit()]
    y = [int(i) for i in y if i.isdigit()]

    n = max(len(x), len(y))
    num_zeros = abs(len(x) - len(y)) - 1

    def extend(v):
        v = v[::-1]
        v.extend([0 for i in range((n - len(v)))])
        v = v[::-1]
        return v

    x = extend(x)
    y = extend(y)

    def mult(x, y):
        n = max(len(x), len(y))

        def multiplication():
            result = [None]*(2*n)

            for i in range(n):
                for j in range(n):
                    if result[i + j] == None:
                        result[i + j] = 0
                    result[i + j] += x[i] * y[j]

            return list(filter(lambda v: v != None, result))

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

            return result

        def deleteZeros(a):
            return list(filter(lambda i, c=count(0, 1): next(c) >= num_zeros, a))
            
        def to_str(a):
            a = [str(i) for i in a]
            return ''.join(a)

        result = multiplication()
        result = finalize(result)
        result = deleteZeros(result)
        return to_str(result)

    return mult(x, y)

def read(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except:
        print('Could not open file in path:', path)

a, b = read('a.txt'), read('b.txt')

try:
    t = time.process_time()
    print(native_mult(a, b))
    print('time:', time.process_time() - t)
except AssertionError as e:
    print(e)