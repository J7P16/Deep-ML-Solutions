def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
    if (len(matrix) == 2):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else: 
        determinant = 0
        for col in range(len(matrix[0])):
            determinant += (-1) ** col * matrix[0][col] * determinant_4x4(sub_matrix(matrix, col))
        return determinant

def sub_matrix(matrix: list[list[int|float]], col: int) -> list[list[int|float]]:
    sub_matrix = []
    for r in range(1, len(matrix)):
        sub_matrix_row = []
        for c in range(len(matrix[0])):
            if (c != col):
                sub_matrix_row.append(matrix[r][c])
        sub_matrix.append(sub_matrix_row)
    return sub_matrix