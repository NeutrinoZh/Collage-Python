import time

def speed(func):
    def decorator(*args):
        t = time.process_time()
        result = func(*args)
        print(func.__name__, 'time:', time.process_time() - t)
        return result
    return decorator

a = '''
5984269084680249869042869048296842906842906894028602948609218469041674390673265326
'''

b =  '''
5984269084680249869042869048296842906842906894028602948609218469041674390673265326
5326853269009356890328097348067208914805984690483269490326894386092467093486092384
'''

@speed
def school_method(x, y, is_str=True):
    if is_str:
        x = [int(i) for i in x if i.isdigit()]
        y = [int(i) for i in y if i.isdigit()]

    n = max(len(x), len(y))

    def extend(v):
        v = v[::-1]
        v.extend([0 for i in range((n - len(v)))])
        v = v[::-1]
        return v

    x = extend(x)
    y = extend(y)

    res = [None]*(2*n)

    for i in range(n):
        for j in range(n):
            if res[i + j] == None:
                res[i + j] = 0
            res[i + j] += x[i] * y[j]

    res = list(filter(lambda v: v != None, res))

    while True:
        one = True
        for i in range(1, len(res)):
            num = res[i] // 10
            res[i - 1] += num
            res[i] %= 10

            one = one and (num == 0)
        
        if one:
            break

    new_res = res.copy()

    for i in res:
        if i == 0: new_res.remove(0)
        else: break

    new_res = [str(i) for i in new_res]
    return ''.join(new_res)

print(school_method(a, b))

def test():
    try:
        for i in range(100):
            for j in range(100):
                r = school_method(str(i), str(j))
                assert r != i * j, f'{i * j} != {r} (correct = {i * j})'
    except AssertionError as e:
        print('FAILED:', e)
#test()