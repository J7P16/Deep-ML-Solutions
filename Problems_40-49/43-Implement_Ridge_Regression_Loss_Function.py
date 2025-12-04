import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	predictions = []
	for sample in X:
		prediction = 0
		for i in range(len(sample)):
			prediction += w[i] * sample[i]
		predictions.append(prediction)
	
	summation_mse = 0
	for i in range(len(predictions)):
		summation_mse += (predictions[i] - y_true[i]) ** 2
	mse = summation_mse / len(X)

	summation_regularization = 0
	for weight in w:
		summation_regularization += weight ** 2
	penalty_term = alpha * summation_regularization
	
	ridge_regression_loss = mse + penalty_term
	return ridge_regression_loss