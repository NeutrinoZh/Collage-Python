import re

numbers = input('numbers:')

if re.match(r'^[A-Z]{3} [\d]{3}$', numbers):
    print('Старая')
elif re.match(r'^[\d]{4} [A-Z]{3}$', numbers):
    print('Новая')
else:
    print('Такой нету')