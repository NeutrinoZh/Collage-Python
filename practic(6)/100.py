import time

def speed(func):
    def decorator():
        t = time.process_time()
        func()
        print(func.__name__, 'time:', time.process_time() - t)
    return decorator

print()

#-----------------------------------------------------------------#

def mymap(func, *args):
    if not args:
        raise TypeError('Слишком мало аргументов')
    iters = [iter(arg) for arg in args]
    for i in args[0]:
        yield func(*[next(it) for it in iters])


@speed
def mymap_test():
    my_pets = [chr(i) for i in range(100000)]
    uppered_pets = list(mymap(str.upper, my_pets))
    return uppered_pets

@speed
def map_test():
    my_pets = [chr(i) for i in range(100000)]
    uppered_pets = list(map(str.upper, my_pets))
    return uppered_pets

map_test()
mymap_test()
print()

#-----------------------------------------------------------------#

def myfilter(func, args):
    for iter in args:
        if func(iter):
            yield iter

@speed
def filter_test():
    scores = [i for i in range(100000)]
    return list(filter(lambda x: x > 75, scores))

@speed
def myfilter_test():
    scores = [i for i in range(100000)]
    return list(myfilter(lambda x: x > 75, scores))

filter_test()
myfilter_test()
print()

#-----------------------------------------------------------------#

from functools import reduce

def myreduce(func, args):
    arg = 0
    for iter in args:
        arg = func(iter, arg)
    return arg

@speed
def myreduce_test():
    numbers = [i for i in range(100000)]
    return myreduce(lambda x, y: x + y, numbers)

@speed
def reduce_test():
    numbers = [i for i in range(100000)]
    return reduce(lambda x, y: x + y, numbers)

reduce_test()
myreduce_test()
print()