import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    X, y = np.array(X), np.array(y)
    theta = (np.linalg.inv(X.T @ X)) @ X.T @ y
    return np.round(theta, 4)