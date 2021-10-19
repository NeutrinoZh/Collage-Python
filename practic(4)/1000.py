
try:
    number = input('Введіть число:')

    if not number.isdigit():
        raise Exception("Це не число!")

    sum = 0
    for ch in number:
        sum += int(ch)
    
    print(f'Результат: {sum}')
except Exception as e:
    print(e)