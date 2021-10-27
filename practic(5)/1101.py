# OOP 4 (0,7)

class Queue:
    queue = [None]*100
    tail = 0
    head = 0

    def enqueue(self, el):
        self.queue[self.tail] = el
        self.tail += 1

    def dequeue(self):
        x = self.queue[self.head]
        self.head += 1
        return x


q = Queue()

q.enqueue('eat')
q.enqueue('sleep')
q.enqueue('code')

print(q.dequeue()) # 'eat'
print(q.dequeue()) # 'sleep'
print(q.dequeue()) # 'code'