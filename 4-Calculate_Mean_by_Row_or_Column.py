def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if (mode == "row"):
        for r in range(len(matrix)):
            mean = 0
            for c in range(len(matrix[0])):
                mean += matrix[r][c]
            means.append(mean / len(matrix[0]))
    elif (mode == "column"):
        for c in range(len(matrix[0])):
            mean = 0
            for r in range(len(matrix)):
                mean += matrix[r][c]
            means.append(mean / len(matrix))
    return means