from tkinter import *
from tkinter.messagebox import showerror
import copy
import time

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

FIELD_SIZE = 30
CELL_SIZE = WINDOW_WIDTH / FIELD_SIZE

maze = [
    [0 for j in range(FIELD_SIZE)] for i in range(FIELD_SIZE)
]

WALL = 1
PATH = 2

START_POINT = [0, 0]
FINISH_POINT = [FIELD_SIZE - 1, FIELD_SIZE - 1]

click = False

def loop(func):
    root = Tk()
    root.title('Maze')
    root.resizable(width=False, height=False)
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

    c = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_WIDTH, bg='white')
    c.pack()

    def calculate():
        global maze
        path = func(maze)

        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE):
                x = j * CELL_SIZE
                y = i * CELL_SIZE

                fill = 'white'
                if   i ==  START_POINT[0] and j ==  START_POINT[1]: fill = 'blue'
                elif i == FINISH_POINT[0] and j == FINISH_POINT[1]: fill = 'red'
                elif path[i][j] == WALL: fill = 'black'
                elif path[i][j] == PATH: fill = 'orange'   

                c.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=fill)

    def click_left(event):
        x = int(event.y / CELL_SIZE)
        y = int(event.x / CELL_SIZE)

        if 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE:
            if maze[x][y] == WALL:
                maze[x][y] = 0
            elif maze[x][y] == 0:
                maze[x][y] = WALL

        calculate()

    def click_right(event):
        x = int(event.y / CELL_SIZE)
        y = int(event.x / CELL_SIZE)

        if 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE:
            global click
            click = not click

            if click:
                global START_POINT
                START_POINT = [x, y]
            else:
                global FINISH_POINT
                FINISH_POINT = [x, y]

        calculate()

    calculate()

    root.bind('<Button-1>', click_left)
    root.bind('<Button-3>', click_right)
    root.mainloop()

def main(org_maze):
    maze = copy.deepcopy(org_maze)

    def is_valid(i, j):
        if not (0 <= i < FIELD_SIZE and 0 <= j < FIELD_SIZE):
            return False
        return (maze[i][j] != WALL and maze[i][j] != PATH)

    def find_maze_path(x, y):
        if x == FINISH_POINT[0] and y == FINISH_POINT[1]:
            return True

        shift_x = [-1,  0, 0, 1]
        shift_y = [ 0, -1, 1, 0]

        for k in range(4):
            nx = x + shift_x[k]
            ny = y + shift_y[k]

            if is_valid(nx, ny):
                if maze[nx][ny] == 0:
                    maze[nx][ny] = PATH

                if find_maze_path(nx, ny):
                    return True
                
                if maze[nx][ny] == PATH:
                    maze[nx][ny] = 0

        return False

    t = time.time()

    if find_maze_path(START_POINT[0], START_POINT[1]):
        print(f'Completed successfully in {round(time.time() - t, 2)} seconds')
        return maze
    else:
        print(f'No solution found. Spent {round(time.time() - t, 2)} seconds')
        return org_maze

loop(main)