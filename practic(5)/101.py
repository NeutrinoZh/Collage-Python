# 10 (0,4)
import random
import os

CARDS = [
    u"\U0001F352",
    u"\U0001F514",
    u"\U0001F34B",
    u"\U0001F34A",
    u"\u2606",
    u"\U0001F480"
]

money = 100

while True:
    print(f'Money: {money}')
    cmd = input('Please enter "play" to try your luck. Or "exit" to finish the game.\n')
    os.system('cls')

    if cmd == 'exit': 
        print('Thanks for playing!')
        break
    
    if cmd != 'play':
        print('Sorry I don\'t understand you')
        continue
    
    if money < 5:
        print('You don\'t have enough money(5)!')
        continue

    money -= 5

    luck = [
        CARDS[random.randint(0, len(CARDS) - 1)],
        CARDS[random.randint(0, len(CARDS) - 1)],
        CARDS[random.randint(0, len(CARDS) - 1)]
    ]

    same = (luck[0] == luck[1]) + (luck[1] == luck[2]) + (luck[0] == luck[2])
    
    if same == 2:
        money += 10
    elif same == 3:
        money += 25
    
    if luck[0] == CARDS[1] and luck[1] == CARDS[1] and luck[2] == CARDS[1]:
        money += 75

    if luck[0] == CARDS[5] and luck[1] == CARDS[5] and luck[2] == CARDS[5]:
        money = 0

    print(luck)