def first(max, i = 1):
    prev = 0
    while i < max:
        i += 1
        prev = 2 * prev + 1
        yield prev

iter = first(5)
for i in iter:
    print(i)

def second(max, i = 1):
    prev = 0
    while i < max:
        i += 1
        prev = 2 * prev - 1
        yield prev

iter = second(5)
for i in iter:
    print(i)