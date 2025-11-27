import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    
    # you can just submit "return np.array(a).reshape(new_shape).tolist()"

    # here's my scratch solution (without numpy)
    if (len(a) * len(a[0]) != new_shape[0] * new_shape[1]):
        return []

    reshaped_matrix, reshaped_matrix_row = [], []
    r, c = 0, 0
    while (r < len(a)):
        reshaped_matrix_row.append(a[r][c])
        c += 1
        if (c == len(a[0])):
            c = 0
            r += 1
        if (len(reshaped_matrix_row) % new_shape[1] == 0):
            reshaped_matrix.append(reshaped_matrix_row)
            reshaped_matrix_row = []
    return reshaped_matrix