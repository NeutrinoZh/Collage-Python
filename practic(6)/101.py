VODAFONE = ['050', '066', '095', '099']
KYIVSTAR = ['067', '068', '096', '097', '098']
LIFECELL = ['063', '093', '073', '077']

def random_users(num):
    import random
    PHONES = [*VODAFONE, *KYIVSTAR, *LIFECELL]
    for i in range(num):
        number = f'{PHONES[random.randint(0, len(PHONES) - 1)]}0000000'
        yield f'name{i}', number

users = {
    name: number for name, number in random_users(500)
}

def main():   
    for name, number in users.items():
        operator = number[:3]

        if operator in VODAFONE: operator = 'VOFADONE'
        elif operator in KYIVSTAR: operator = 'KYIVSTAR'
        elif operator in LIFECELL: operator = 'LIFECELL'

        print(name, number, operator)

main()