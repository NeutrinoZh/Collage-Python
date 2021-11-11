from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showerror
import copy
import time
import threading 
import json


WINDOW_SIZE = 700 
FIELD_SIZE = 9
CELL_SIZE = WINDOW_SIZE / FIELD_SIZE

task = None
_cache_ = {}

try:
    file = open("_cache_.json", "r")
    _cache_ = json.load(file)
    file.close()
except:
    pass

def loop(func):
    root = Tk()
    root.title('Sudoku')
    root.resizable(width=False, height=False)
    root.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE+50}')
    
    c = Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg='white')
    c.pack()

    def calculate():
        path_to_file = fd.askopenfilename(title='Open a file') 
        
        try:
            file = open(path_to_file, 'r')
            
            sudoku = json.load(file)['sudoku']

            assert type(sudoku) == list
            assert len(sudoku) == FIELD_SIZE
            for i in sudoku:
                assert type(i) == list
                assert len(i) == FIELD_SIZE

            file.close()
        except:
            showerror(title='Error', message='The file is damaged or the format is not supported.')
            return

        def progress(num):
            c.delete('all')
            c.create_text(WINDOW_SIZE/2, 50, text=f'{num} of {FIELD_SIZE*FIELD_SIZE} cells found', fill='black', font="Verdana 12")
            c.update()

        if path_to_file in _cache_:
            numbers = _cache_[path_to_file]
        else:
            numbers = func(sudoku, progress)
            _cache_[path_to_file] = copy.deepcopy(numbers)

        c.delete('all')

        try:
            for i in range(FIELD_SIZE):
                for j in range(FIELD_SIZE):
                    x = j * CELL_SIZE
                    y = i * CELL_SIZE

                    c.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE)

                    if numbers[i][j] != 0:
                        if sudoku[i][j] != 0 and numbers[i][j] != sudoku[i][j]:
                            raise ValueError(f'Sudoku is damaged: numbers[{i}][{j}] = {numbers[i][j]}, sudoku[{i}][{j}] = {sudoku[i][j]}')
                        if numbers[i][j] == sudoku[i][j]:
                            c.create_text(x + CELL_SIZE/2, y + CELL_SIZE/2, font="Verdana 12", fill="red", text=str(numbers[i][j]))
                        else:
                            c.create_text(x + CELL_SIZE/2, y + CELL_SIZE/2, fill="black", font="Verdana 10", text=str(numbers[i][j]))

                    if (i % 3 + j % 3) == 0:
                        c.create_rectangle(x, y, x + CELL_SIZE * 3, y + CELL_SIZE * 3, width=5)
        except Exception as e:
            showerror(title='Error', message=str(e))

    def run():
        global task
        if task == None:
            task = threading.Thread(name='Thread', target=calculate)
            task.start()
        elif not task.is_alive():
            task = None
            run()
    
    btn = Button(root, width=800, height=50, text="calculate", command=run)
    btn.pack(side=BOTTOM)

    root.mainloop()

    if task != None and task.is_alive():
        task.join()

    with open("_cache_.json", "w") as write_file:
        json.dump(_cache_, write_file)

#---------------------------------------------------#

max_cell = 0

def main(field, progress):
    field = copy.deepcopy(field)

    global max_cell
    max_cell = 0

    progress(max_cell)

    def is_valid(i, j, num):
        if num in field[i]:
            return False
        
        for k in field:
            if k[j] == num:
                return False
        
        block_i = 3 * (i // 3)
        block_j = 3 * (j // 3)

        for x in range(3):
            for y in range(3):
                rx = block_i + x
                ry = block_j + y

                if rx == i and ry == j:
                    continue
                    
                if field[rx][ry] == num:
                    return False

        return True

    def next(next_i, next_j):
        try:
            while True:
                next_i = (next_i + 1) % FIELD_SIZE
                next_j = next_j + (not next_i)

                if field[next_i][next_j] == 0:
                    return next_i, next_j              
        except IndexError:
            return None, None

    def sudoku(i, j):
        global max_cell
        cell = i % FIELD_SIZE + FIELD_SIZE * j
        if cell > max_cell:
            max_cell = cell
            progress(max_cell)

        for k in range(1, 10):
            if is_valid(i, j, k):
                field[i][j] = k

                next_i, next_j = next(i, j)

                if next_i == None:
                    return True

                if sudoku(next_i, next_j):
                    return True

                field[i][j] = 0

        return False
    
    t = time.time()
    i, j = next(-1, -1)

    if i == None or sudoku(i, j):
        print(f'Completed successfully in {round(time.time() - t, 2)} seconds')
    else:
        print(f'No solution found. Spent {round(time.time() - t, 2)} seconds')

    return field

loop(main)