import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x, x_new = np.zeros(len(A)), np.zeros(len(A))
    for iterations in range(n):
        for i in range(len(A)):
            summation = 0
            for j in range(len(A[0])):
                if (i != j):
                    summation += A[i][j] * x[j]
            x_new[i] = (b[i] - summation) / A[i][i]
        for i in range(len(x_new)):
            x[i] = x_new[i]
    return x