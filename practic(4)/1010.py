visitors = []
while True:
    try:
        age = int(input('Возраст:'))
        if age == 0: break
        visitors.append(age)
    except ValueError:
        print('Некорректные данные')

price = 0
for visitor in visitors:
    if visitor < 3:
        pass
    elif visitor > 3 and visitor < 12:
        price += 16
    elif visitor > 60:
        price += 18
    else:
        price += 25

if len(visitors) >= 10:
    price *= 0.9

print(price)