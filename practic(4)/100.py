sum = 0
i = 0

while True:
    number = float(input())
    if number == 0:
        break
    else:
        sum += number
        i += 1

if sum != 0:
    average = sum / i
    print(average)