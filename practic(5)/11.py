# 6 (0,3)

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

text = input('text:').upper()
result = ''
for ch in text:
    for button, letters in BUTTONS.items():
        if ch in letters:
            result += button * (letters.index(ch) + 1)
print(result)