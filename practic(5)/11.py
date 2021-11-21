# 6 (0,3)

import time

BUTTONS = {
    '0': ' ',
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}


def foo(text):
    result = ''
    for ch in text:
        for button, letters in BUTTONS.items():
            if ch in letters:
                result.join(button * (letters.index(ch) + 1))   

start_time = time.process_time()
for i in range(1000000):
    foo('Hello World!')
print(time.process_time() - start_time)