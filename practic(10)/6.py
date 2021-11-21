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
            print(line)
        os.system('cls')

        root.after(1, calculate)

    calculate()
    root.mainloop()

def foo(text):
    width = 20

    words = text[:-1].split(' ')

    if len(words) < 2:
        return words

    cost = [ [0]*len(words) for _ in range(len(words))]

    for i in range(len(words)):
        cost[i][i] = width - len(words[i])
        for j in range(i + 1, len(words)):
            cost[i][j] = cost[i][j - 1] - len(words[j]) - 1
    
    for i in range(len(words)):
        for j in range(i, len(words)):
            if cost[i][j] < 0:
                cost[i][j] = math.inf
            else:
                cost[i][j] = int(pow(cost[i][j], 2))

    minCost = [0]*len(words)
    results = [0]*len(words)

    for i in reversed(range(0, len(words))):
        minCost[i] = cost[i][len(words) - 1]
        results[i] = len(words)

        for j in range(len(words) - 1, i, -1):
            if cost[i][j - 1] == math.inf:
                continue
            if minCost[i] > minCost[j] + cost[i][j - 1] or (minCost[i] == math.inf and minCost[j] == math.inf):
                if minCost[i] == math.inf:
                    minCost[i] = -math.inf
                else:
                    minCost[i] = minCost[j] + cost[i][j - 1]
                results[i] = j


    lines = []

    i = 0
    while True:
        j = results[i]

        lines.append('')
        for k in range(i, j):
            lines[-1] += words[k] + ' '
        i = j

        if j >= len(words):
            break

    return lines

if __name__ == '__main__':
    main(foo)