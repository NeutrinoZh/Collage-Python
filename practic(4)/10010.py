def my_pow(x, n):
    if n == 0: return 1
    if n > 0:  return x * my_pow(x, n - 1)
    raise ValueError('n < 0')
    
try:
    a = my_pow(-2, 3)
    print(a)
except ValueError as e:
    print('Error:', e)