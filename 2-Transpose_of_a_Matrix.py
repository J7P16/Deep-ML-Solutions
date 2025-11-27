def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    transpose = []
    for c in range(len(a[0])):
        transpose_row = []
        for r in range(len(a)):
            transpose_row.append(a[r][c])
        transpose.append(transpose_row)
    return transpose