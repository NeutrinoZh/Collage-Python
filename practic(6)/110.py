# ІНДЗ 1
class QHofstadter:
    def __init__(self, len):
        self.q = [1, 1]
        self.n = 0
        self.len = len

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.len:
            raise StopIteration

        if self.n >= 2:
            val = self.q[self.n - self.q[self.n - 1]] + self.q[self.n - self.q[self.n - 2]] 
            self.q.append(val)

        self.n += 1
        return self.q[self.n - 1]
try:
    num = int(input('num:'))
    
    iter = QHofstadter(num)
    l = 0
    for i in iter: l = i
    print(l)
    
except:
    print('Это не число!')