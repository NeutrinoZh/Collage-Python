str = input('string:')
result = [ str[len(str) - i - 1] for i in range(len(str)) ]
print(''.join(result))