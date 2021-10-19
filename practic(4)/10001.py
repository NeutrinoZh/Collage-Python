
try:
    year = int(input('Year:'))

    if year % 400 == 0:
        print('Високосний')
    elif year % 100 == 0:
        print('Невисокосний')
    elif year % 4 == 0:
        print('Високосний')
    else:
        print('Невисокосний')
except:
    print('Не.кор данние')