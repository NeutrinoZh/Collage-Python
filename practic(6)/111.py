
#-----------------------------------------------#
# Decorators

def my_decorator(func_to_decorate):
    def wrapper():
        print('before func')
        func_to_decorate()
        print('after func')
    return wrapper

@my_decorator
def foo():
    print('Hello, World!')

foo()

#-----------------------------------------------#
# Memoization

def memoize(f): 
    memo = {} 
    def helper(x): 
        if x not in memo:             
            memo[x] = f( x ) 
        return memo[x] 
    return helper 

@memoize
def fib(n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else:
        return fib(n - 1) + fib(n - 2)  


#-----------------------------------------------#
# Сurrying

greet_curried = lambda gretting: lambda name: print(f'{gretting}, {name}!')

greet_hello = greet_curried('Hello')

greet_hello('Zhenya')
greet_hello('Vanya')

greet_curried('Hi')('Vlad')

#-----------------------------------------------#

from functools import partial

def greet(greeting, name):
    print(f'{greeting}, {name}!')

newfunc = partial(greet, greeting='Hello')
newfunc(name='Zhenya')
newfunc(name='Maksim')