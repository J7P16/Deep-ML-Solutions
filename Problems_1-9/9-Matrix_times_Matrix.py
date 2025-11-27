def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if (len(a[0]) != len(b)):
        return -1
        
    matmul = []
    for r in range(len(a)):
        matmul_row = []
        for c in range(len(b[0])):
            dot_product = 0
            for i in range(len(b)):
                dot_product += a[r][i] * b[i][c]
            matmul_row.append(dot_product)
        matmul.append(matmul_row)
    return matmul