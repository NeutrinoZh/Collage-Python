try:
    radiation = int(input('radiation:'))

    if 0 < radiation < 3 * pow(10, 9):
        print('Радіохвилі')
    elif radiation < 3 * pow(10, 12):
        print('Мікрохвилі')
    elif radiation < 4.3 * pow(10, 14):
        print('Інфрачервоне світло')
    elif radiation < 7.5 * pow(10, 14):
        print('Видиме світло ')
    elif radiation < 3 * pow(10, 17):
        print('Ультрафіолет')
    elif radiation < 3 * pow(10, 19):
        print('Рентгенівські промені')
    else:
        print('Гамма-промені')
except:
    print("Не.кор данние")