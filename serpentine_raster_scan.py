import numpy as np


def serpentine_scan(matrix):
    scan = []
    col = len(matrix[1])
    fil = len(matrix)
    diagonals = [matrix[::-1, :].diagonal(i) for i in range(-fil, col)]
    for n in diagonals:
        for sample in n:
            scan.append(sample)
    return scan


matrix = np.array(
    [[-2, 5, 3, 2],
     [9, -6, 5, 1],
     [3, 2, 7, 3],
     [-1, 8, -4, 8]])

print(serpentine_scan(matrix))

