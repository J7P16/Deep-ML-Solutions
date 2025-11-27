def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    determinant = a * d - b * c
    lambda1 = (trace + (trace ** 2 - 4 * determinant) ** 0.5) / 2
    lambda2 = (trace - (trace ** 2 - 4 * determinant) ** 0.5) / 2
    eigenvalues = [lambda1, lambda2]
    return eigenvalues