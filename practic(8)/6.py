from tkinter import *
from random import randint

def loop(func): 
    root = Tk()
    root.title('Convex Hull Brute Force')
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
        for i in range(0, len(results) - 1, 2):
            a = results[i]
            b = results[i + 1] if i < len(results) - 1 else results[0]
            c.create_line(points[a][0] + RADIUS/2, points[a][1] + RADIUS/2, points[b][0] + RADIUS/2, points[b][1] + RADIUS/2)

    btn = Button(root, width=800, height=50, text="calculate", command=calculate)
    btn.pack(side=BOTTOM)

    root.mainloop()

#--------------------------------------------------------------------------#

def determinantSignum(a, b, c):
    d = (b[0] - a[0]) * (c[1] - b[1]) -  (c[0] - b[0]) * (b[1] - a[1])
    
    if d > 0: d = 1
    elif d < 1: d = -1
    else: d = 0 

    return d

def main(points):
    results = []
    
    for p1 in points:
        for p2 in points:
            if p1 == p2: continue

            side = None
            for p3 in points:
                if p3 == p1 or p3 == p2: continue

                currentSide = determinantSignum(p1, p2, p3)
                if side == None:
                    side = currentSide
                elif side != currentSide:
                    side = None
                    break
            
            if side != None:
                results.append(points.index(p1))
                results.append(points.index(p2))

    return results

loop(main)