from tkinter import *
import time

# Размеры окна
WINDOW_SIZE = 800 

# Традиционная шахматная доска, описанная в правилах ФИДЕ, представляет собой поле 8×8
FIELD_SIZE = 8
# Размер клетки
CELL_SIZE = WINDOW_SIZE / FIELD_SIZE

START_POINT = [0, 0]

def loop(func):
    root = Tk()
    root.title('Knight’s Tour Problem')
    root.resizable(width=False, height=False)
    root.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}')
    
    c = Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg='white')
    c.pack()

    numbers = func()

    try:
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE):
                x = j * CELL_SIZE
                y = i * CELL_SIZE

                if (i + j & 1) & 1: 
                    c.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill='orange')
                
                c.create_text(x + CELL_SIZE/2, y + CELL_SIZE/2, text=str(numbers[i][j]))
    except IndexError as e:
        c.create_text(100, 50, text=str(e))

    root.mainloop()

#---------------------------------------------------#

max_step = 0

def main():
    # Иницилизируем двумерный массив FIELD_SIZExFIELD_SIZE значением -1.
    results = [[-1 for j in range(FIELD_SIZE)] for i in range(FIELD_SIZE) ]

    shift_x = [2, 1, -1, -2, -2, -1,  1,  2]	
    shift_y = [1, 2,  2,  1, -1, -2, -2, -1]

    results[START_POINT[0]][START_POINT[1]] = 0

    def is_valid(i, j):
        if not (0 <= i < FIELD_SIZE and 0 <= j < FIELD_SIZE):
            return False
        return (results[i][j] == -1)

    def knight_tour(i, j, step):
        global max_step
        if step > max_step:
            max_step = step
            print(f'{max_step} of {FIELD_SIZE*FIELD_SIZE} steps found')

        if step == FIELD_SIZE * FIELD_SIZE:
            return True
        
        # Проверяем всё ходы (у коня их 8)
        for k in range(8): 
            next_i = i + shift_x[k]
            next_j = j + shift_y[k]

            if is_valid(next_i, next_j):
                results[next_i][next_j] = step
                
                if knight_tour(next_i, next_j, step + 1):
                    return True
                
                results[next_i][next_j] = -1
        
        return False

    t = time.time()
    if knight_tour(START_POINT[0], START_POINT[1], 1):
        print(f'Completed successfully in {round(time.time() - t, 2)} seconds')
    else:
        print(f'No solution found. Spent {round(time.time() - t, 2)} seconds')
    return results

loop(main)