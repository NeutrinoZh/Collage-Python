from tkinter import *
from random import randint

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
OFFSET = 50

def loop(func): 
    root = Tk()
    root.title('Convex Hull Graham')
    root.resizable(width=False, height=False)
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    c = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT-50, bg='white')
    c.pack()

    def calculate():
        c.delete("all")

        RADIUS = 7
        points = [(randint(OFFSET, WINDOW_WIDTH-OFFSET), randint(OFFSET, WINDOW_HEIGHT-OFFSET-50)) for i in range(50)]
        
        for point in points:
            c.create_oval(point[0], point[1], point[0] + RADIUS, point[1] + RADIUS, fill='black')

        results = func(points)
        for i in range(len(results)):
            a = results[i]
            b = results[i + 1] if i < len(results) - 1 else results[0]
            c.create_line(points[a][0] + RADIUS/2, points[a][1] + RADIUS/2, points[b][0] + RADIUS/2, points[b][1] + RADIUS/2)

    
    btn = Button(root, width=800, height=50, text="calculate", command=calculate)
    btn.pack(side=BOTTOM)

    root.mainloop()

#--------------------------------------------------------------------------#

def rotate(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) -  (c[0] - b[0]) * (b[1] - a[1])

def main(org_points):
    index = lambda obj: org_points.index(obj)
    points = org_points.copy()
    results = [i for i in range(len(points))]

    min = points[0]
    for p in reversed(points):
        if p[0] < min[0]:
            min = p
        elif p[0] == min[0] and p[1] < min[1]:
            min = p

    min = index(min)
    results[0], results[min] = min, 0

    for i in range(2, len(points)):
        j = i
        while j > 1 and rotate(points[results[0]], points[results[j - 1]], points[results[j]]) < 0:
            results[j], results[j - 1] = results[j - 1], results[j]
            j -= 1

    stack = [ results[0], results[1] ]

    for i in range(2, len(points)):
        while rotate(points[stack[-2]], points[stack[-1]], points[results[i]]) < 0:
            del stack[-1]
        stack.append(results[i])

    return stack

loop(main)