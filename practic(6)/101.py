from random import randint

def main():
    VODAFONE = ['050', '066', '095', '099']
    KYIVSTAR = ['067', '068', '096', '097', '098']
    LIFECELL = ['063', '093', '073', '077']
    PHONES = [*VODAFONE, *KYIVSTAR, *LIFECELL]
    
    def random_user(user):
        return f'{PHONES[randint(0, len(PHONES) - 1)]}0000000'

    users = list(map(random_user, [None]*10))

    print(users)

    vodafone = list(filter(lambda number: number[:3] in VODAFONE, users))
    kievstar = list(filter(lambda number: number[:3] in KYIVSTAR, users))
    lifecell = list(filter(lambda number: number[:3] in LIFECELL, users))

    print('VODAFONE:\n', vodafone)
    print('KYIVSTAR:\n', kievstar)
    print('LIFECELL:\n', lifecell)

main()