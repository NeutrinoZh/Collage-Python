
def printMatrix(matrix):
    for row in matrix:
        text = ''
        for el in row:
            text += f"{el} "
        print(text)

#------------------------------------------------#

matrix = [
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
    [4, 645, 7, 65, 685, 246, 463, 4],
]

printMatrix(matrix)