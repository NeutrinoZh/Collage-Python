from tkinter import *
from random import randint
from math import sqrt
from itertools import combinations

def main(func): 
    root = Tk()
    root.title('TSP')
    root.resizable(width=False, height=False)
    root.geometry('800x650')
    c = Canvas(root, width=800, height=600, bg='white')
    c.pack()

    def calculate():
        c.delete("all")

        RADIUS = 8
        points = [(randint(50, 750), randint(50, 550)) for _ in range(10)]

        for point in points:
            c.create_oval(point[0], point[1], point[0] + RADIUS, point[1] + RADIUS, fill='black')

        results = func(points)
        for i in range(len(results) - 1):
            a = results[i]
            b = results[i + 1]
            c.create_line(points[a][0] + RADIUS/2, points[a][1] + RADIUS/2,
                          points[b][0] + RADIUS/2, points[b][1] + RADIUS/2,
                          arrow='last', fill='blue', width=2)


    btn = Button(root, width=800, height=50, text="calculate", command=calculate)
    btn.pack(side=BOTTOM)

    root.mainloop()

def dist(a, b):
    return sqrt(pow(b[0]-a[0], 2) + pow(b[1]-a[1], 2))

def TSP(points):
    A = {}
    for i in range(len(points) - 1):
        A[(frozenset([0, i + 1]), i + 1)] = ( dist(points[0], points[i + 1]), [0, i + 1] )

    n = len(points)
    for i in range(2, n):
        B = {}
        for S in [frozenset(C) | {0} for C in combinations(range(1, n), i)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + dist(points[k], points[j]), A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k != j])
        A = B

    res = min([(A[d][0] + dist(points[0], points[d[1]]), A[d][1]) for d in iter(A)])
    res[1].append(0)
    return res[1]

if __name__ == '__main__':
    main(TSP)