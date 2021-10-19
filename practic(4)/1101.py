for i in range(127):
    print(f'\'{chr(i)}\' 10: {i}, 2: {bin(i)[2:]}, 8:{oct(i)[2:]}, 16:{hex(i)[2:]}')