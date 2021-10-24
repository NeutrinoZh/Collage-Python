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

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0

stack = Stack()

for ch in text:
    if ch == '{':
        stack.push(ch)
    elif ch == '}':
        stack.pop()

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