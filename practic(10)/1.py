import os

def backpack(items: list, W: int = 10) -> list:
    n = len(items)

    V = [
        [0 for j in range(W + 1)] for i in range(n + 1) 
    ]

    for i in range(n + 1):
        for j in range(W + 1):
            if items[i - 1][1] <= j:
                a = items[i - 1][0] + V[i - 1][j - items[i - 1][1]]
                V[i][j] = max(a, V[i - 1][j])
            else:
                V[i][j] = V[i - 1][j]

    occupied = V[n][W]
    capacity = W
    result = []

    for i in reversed(range(n)):
        if occupied <= 0:
            break
        
        if occupied == V[i - 1][capacity]:
            continue
        else:
            result.append(items[i - 1])
            occupied -= items[i - 1][0]
            capacity -= items[i - 1][1]

    return result

def main() -> None:
    items = []
    weight = 0

    # input items
    print('add items:')
    while True:
        try:
            price  = int(input('price:'))
            weight = int(input('weight:'))
            
            items.append((price, weight))
        except ValueError as e:
            print('incorrect data!', e)

        os.system('cls')
        if input('continue? (y/n)').upper() != 'Y':
            break
    os.system('cls')

    # input weight
    while True:
        try:
            weight = int(input('backpack capacity:'))
            break
        except ValueError as e:
            os.system('cls')
            print('incorrect data!', e)
    os.system('cls')

    print('backpack:')

    total_price = 0
    total_weight = 0
    for item in backpack(items, weight):
        print(f'\t(price={item[0]}, weight={item[1]})')
        
        total_price += item[0]
        total_weight += item[1]
    
    print(f'{"-"*10}')

    print('total price:', total_price)
    print(f'weight: {total_weight}/{weight}')

if __name__ == "__main__":
    main()
    print('\n')
    os.system('pause')