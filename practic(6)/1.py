# 2 (0,3)

class MyIterator:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.counter

iter = MyIterator()
for i in iter:
    print(i)