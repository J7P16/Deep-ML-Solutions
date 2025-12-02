import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	if (Y is None):
		Y = X
	X, Y = np.array(X), np.array(Y)
	X_features, Y_features = X.T, Y.T

	correlation_matrix = []
	for feature1 in X_features:
		meanX, stdX = np.mean(feature1), np.std(feature1)
		correlation_matrix_row = []
		for feature2 in Y_features:
			meanY, stdY = np.mean(feature2), np.std(feature2)
			covariance = np.sum((feature1 - meanX) * (feature2 - meanY)) / len(feature1)
			correlation_matrix_row.append(covariance / (stdX * stdY))
		correlation_matrix.append(correlation_matrix_row)
	return correlation_matrix