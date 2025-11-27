def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    covariance_matrix = []
    for feature1 in vectors:
        mean = sum(feature1) / len(feature1)
        covariance_matrix_row = []
        for feature2 in vectors:
            covariance = 0
            for i in range(len(feature1)):
                covariance += (feature1[i] - mean) * (feature2[i] - mean)
            covariance_matrix_row.append(covariance / (len(feature1) - 1 ))
        covariance_matrix.append(covariance_matrix_row)
    return covariance_matrix