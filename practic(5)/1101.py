# OOP 4 (0,7)

class Queue:
    queue = []

    def put(self, el):
        self.queue.append(el)

    def get(self):
        temp = self.queue[0]
        del self.queue[0]
        return temp


q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

print(q.get()) # 'eat'
print(q.get()) # 'sleep'
print(q.get()) # 'code'