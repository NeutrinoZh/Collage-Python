def printMatrix(matrix):
    for row in matrix:
        text = ''
        for el in row:
            text += f"{el} "
        print(text)

def encryption(msg, w):
    if len(msg) == 0: return

    h = int(len(msg) / w) + 1

    matrix = [
        ['*' for j in range(w)] for i in range(h)
    ]

    i = 0
    for y in range(h):
       for x in range(w):
            if i < len(msg):
                matrix[y][x] = msg[i]
            i += 1

    result = ''
    for j in range(w):
        for i in range(j, len(msg), w):
            x = i % w
            y = int(i / w)
            if matrix[y][x] != '*':
                result += matrix[y][x]

    return result

def decryption(msg, w):
    if len(msg) == 0: return

    result = ''
    result += msg[0] 
    msg = msg[1:]

    a = int(len(msg) / w)

    shift = (len(msg) + 1) % w
    j = 0

    for i in range(len(msg)):
        j += a
        if i % w < shift:
            j += 1
        j = j % len(msg)

        if j - 1 < len(msg):
            result += msg[j - 1]
 
    return result

def test():
    msg = 'Hello_World_My_names'
    nmsg = encryption(msg, 6)
    nmsg = decryption(nmsg, 6)

    if nmsg != msg:
        print("ERROR")
    
test()

def crypt(msg):
    print(f"'{msg}' => '{ encryption(msg, 6)} '")

crypt('My name is awesome. Today I want tell you about my life.')