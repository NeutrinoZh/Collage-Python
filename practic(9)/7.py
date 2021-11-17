from tkinter import *

coordinates = []
solution = []

def create_dot(event):
    x = event.x
    y = event.y
    r = 5
    my_canvas.create_oval(x+r,y+r,x-r,y-r,fill='black')
    coordinates.append((x,y))


def clear(event):
    my_canvas.delete('all')
    coordinates.clear()
    solution.clear()


def get_coordinate_side(A,B,coordinate):
    x1, y1 = A
    x2, y2 = B
    x, y = coordinate
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    f = a*x + b*y + c
    if f < 0:
        return 'right'
    elif f > 0:
        return 'left'
    else:
        return 'on-the-line'


def find_hull(partition,A,B):
    if len(partition) == 0:
        return
    else:
        x1, y1 = A
        x2, y2 = B
        a = y2 - y1
        b = x1 - x2
        c = x2*y1 - x1*y2
        farthest_dist = -1
        C = None
        for coordinate in partition:
            x, y = coordinate
            f = abs(a*x + b*y + c)
            if f>farthest_dist:
                f = farthest_dist
                C = coordinate
        x,y = C
        
        solution.remove((A,B))
        solution.append((A,C))
        solution.append((C,B))
        
        partition.remove(C)
        ACright = []
        for coordinate in partition:
            coordinate_side = get_coordinate_side(A,C,coordinate)
            if coordinate_side == 'right':
                ACright.append(coordinate)
        CBright = []
        for coordinate in partition:
            coordinate_side = get_coordinate_side(C,B,coordinate)
            if coordinate_side == 'right':
                CBright.append(coordinate)
                
         
        find_hull(ACright,A,C)
        find_hull(CBright,C,B)


def convex_hull(event):
    sorted_coordinates = sorted(coordinates , key=lambda k: [k[0], k[1]])

    A = sorted_coordinates[0]
    B = sorted_coordinates[-1]

    ABright = []
    BAright = []
    for coordinate in sorted_coordinates:
        coordinate_side = get_coordinate_side(A,B,coordinate)
        if coordinate_side == 'right':
            ABright.append(coordinate)
        elif coordinate_side == 'left':
            BAright.append(coordinate)
        else:
            pass

    solution.append((A,B))
    solution.append((B,A))
    
    x1,y1 = A
    x2,y2 = B

    find_hull(ABright,A,B)
    find_hull(BAright,B,A)

    for line in solution:
        (x1,y1),(x2,y2) = line
        my_canvas.create_line(x1,y1,x2,y2,width=2,fill='blue')


if __name__ == '__main__':
    my_window = Tk()
    my_canvas = Canvas(my_window, width=500, height=500, background='white')
    my_canvas.bind('<Button-1>',create_dot)
    my_canvas.bind('<Button-3>',convex_hull)
    my_canvas.bind('<Button-2>',clear)
    my_canvas.grid(row=0,column=0)
    my_window.mainloop()