import re

try:
    pos = input('Позиція:')
    if not re.match(r'^[abcdefgh][12345678]$', pos):
        raise Exception('Это не позиция на шах.доске')
    
    x = ord(pos[0]) - ord('a') + 1
    y = int(pos[1])
    
    px = x % 2 == 0
    py = y % 2 == 0

    if px:
        if py: print('Черная')
        else:  print('Белая')
    else:
        if py: print('Белая')
        else:  print('Черная')
except Exception as e:
    print(e)