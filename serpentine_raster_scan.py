import numpy as np


def serpentine_scan(scan_matrix):
    scan = []
    col = len(scan_matrix[1])
    fil = len(scan_matrix)
    diagonals = [scan_matrix[::-1, :].diagonal(i) for i in range(-fil, col)]
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

"""Future implementations : 
read . jpg as array and scan it 
import matplotlib.image as img
image = img.imread(file_name)
Now the image would be a 3D numpy array

print image.shape

"""