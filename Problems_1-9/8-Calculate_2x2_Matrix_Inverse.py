def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    determinant = a * d - b * c
    inverse = [[d, -b], [-c, a]]
    for row in range(len(inverse)):
        for col in range(len(inverse[0])):
            inverse[row][col] /= determinant
    return inverse