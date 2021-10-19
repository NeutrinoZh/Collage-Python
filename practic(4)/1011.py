
animals = [
    'Мавпа',
    'Півень',
    'Собака',
    'Свиня',
    'Щур',
    'Бик',
    'Тигр',
    'Кролик',
    'Дракон',
    'Змія',
    'Кінь',
    'Коза'
]

try:
    year = int(input('Год:')) % 12
    print(animals[year])
except ValueError:
    print('Это не год!')