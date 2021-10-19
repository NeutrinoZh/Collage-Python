while True:
    try:
        home = input("Місце проживання: (Будинок, Квартира або Гуртожиток):")
        time = int(input("Час у дома:"))

        if home == 'Будинок':
            if time >= 18:
                print("Порося")
            elif time >= 10 and time < 18:
                print("Собака")
            else:
                print("Змія")
        elif home == 'Квартира':
            if time >= 10:
                print("Кішка")
            else:
                print("Хом'як")
        elif home == 'Гуртожиток':
            if time >= 6:
                print("Рибки")
            else:
                print("Мурашник")
        else:
            print("Хз що за місце")
    except:
        print("error")