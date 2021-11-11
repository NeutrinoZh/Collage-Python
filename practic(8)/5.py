from tkinter import *
from random import randint

def loop(func): 
    root = Tk()
    root.title('Convex Hull Jarvis')
    root.resizable(width=False, height=False)
    root.geometry('800x650')
    c = Canvas(root, width=800, height=600, bg='white')
    c.pack()

    def calculate():
        c.delete("all")

        RADIUS = 7
        points = [(randint(50, 750), randint(50, 550)) for i in range(50)]
        
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

def determinantSignum(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) -  (c[0] - b[0]) * (b[1] - a[1]) >= 0

def main(points):
    results = []
    points2 = points.copy()

    min = points[0]
    for p in reversed(points2):
        if p[0] < min[0]:
            min = p
        elif p[0] == min[0] and p[1] < min[1]:
            min = p

    del points2[points2.index(min)]
    results.append(points.index(min))

    currentPoint = min

    while True:
        nextPoint = min
        for p in reversed(points2):
            if determinantSignum(nextPoint, currentPoint, p):
                nextPoint = p

        if nextPoint != min:
            del points2[points2.index(nextPoint)]
            results.append(points.index(nextPoint))
            currentPoint = nextPoint

        if nextPoint == min:
            break

    return results

loop(main)