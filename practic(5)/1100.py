# OOP 3 (0,7)
import os

text = ''

try:
    f = open('main.cpp', 'r')
    text = f.read()
    f.close()
except Exception as e:
    print('Не удалось прочитать файл:', e)
    os.abort()


class Stack:
    stack = []
    top = 0

    def push(self, el):
        self.top += 1
        self.stack[self.top] = el

    def pop(self):
        if self.top <= 0:
            raise "ERROR"
        self.top -= 1
        return self.stack[self.top]

    def empty(self):
        return self.top

stack = Stack()

num = 0
for ch in text:
    if ch == '{': num += 1
    elif ch == '}': 
        if num == 0: raise 'Error'
        else: num -= 1

if stack.empty():
    print('Сorrect code')
else:
    print('Invalid code')

os.system('pause')

if text.count('{') == text.count('}'):
    print('Сorrect code')
else:
    print('Invalid code')

os.system('pause')