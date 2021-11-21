import os

def backpack(items: list, W: int = 80) -> list:
    assert type(items) == list, 'type(items) != list'
    assert type(W) == int, 'type(W) != int'

    ratio = sorted([
        (i, price / weight) for i, (price, weight) in enumerate(items)
    ], key=lambda x: x[1], reverse=True)

    results = []
    free = W

    i = 0
    while i < len(ratio):
        item = items[ratio[i][0]]
        if free > item[1]:
            results.append(item)
            free -= item[1]
        i += 1

    return results

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