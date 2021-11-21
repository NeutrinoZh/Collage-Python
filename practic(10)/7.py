import math
from tkinter import *
import os

WIDTH = 200

def main(func): 
    root = Tk()
    root.title('Text Justification Problem')
    root.resizable(width=False, height=False)
    root.geometry('300x620')
    c = Canvas(root, width=WIDTH, height=500, bg='white')
    c.pack()


    text = Text(root, width=300)
    text.pack(side=BOTTOM)

    def calculate():
        c.delete('all')

        results = func(text.get(0.0, END))
        for i, line in enumerate(results):
            c.create_text(WIDTH/2, 50 + i * 15, text=line)

        root.after(1, calculate)

    calculate()
    root.mainloop()

def foo(text):
    width = 20

    words = text[:-1].split(' ')

    lines = ['']
    i = 0

    for word in words:
        if len(lines[i]) + len(word) < width:
            lines[i] += word + ' '
        else:
            i += 1
            lines.append(word + ' ')

    return lines

if __name__ == '__main__':
    main(foo)