while True:
    noise = float(input('Гучність шуму:'))
    
    if noise == 0:
        break
    elif noise < 40:
        print('Тиха кімната')
    elif noise < 70:
        print('Тиха кімната/Будильник')
    elif noise == 70:
        print('Будильник')
    elif noise < 106:
        print('Будильник/Бензова газонокосилка')
    elif noise == 106:
        print('Бензова газонокосилка')
    elif noise < 130:
        print('Бензова газонокосилка/Відбійний молоток')
    else:
        print('Відбійний молоток')