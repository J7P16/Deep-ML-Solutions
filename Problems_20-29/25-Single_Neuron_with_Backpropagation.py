import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	updated_weights, updated_bias = initial_weights, initial_bias
	mse_values = []

	for epoch in range(epochs):
		# forward pass
		predictions = []
		for sample in features:
			z = 0
			for i in range(len(sample)):
				z += initial_weights[i] * sample[i]
			z += initial_bias
			sigmoid_output = 1 / (1 + np.exp(-z))
			predictions.append(sigmoid_output)

		# loss calculation
		summation = 0
		for i in range(len(predictions)):
			summation += (predictions[i] - labels[i]) ** 2
		mse = summation / len(features)
		mse_values.append(mse)
		
		# backward pass for weights
		for j in range(len(features[0])):
			summation = 0
			for i in range(len(features)):
				summation += (predictions[i] - labels[i]) * (predictions[i] * (1 - predictions[i])) * (features[i][j])
			weight_gradient = (2 * summation) / len(features)

			# gradient descent for weights
			new_weight = initial_weights[j] - learning_rate * weight_gradient
			updated_weights[j] = new_weight
		
		# backward pass for bias
		summation = 0
		for i in range(len(features)):
			summation += (predictions[i] - labels[i]) * (predictions[i] * (1 - predictions[i]))
		bias_gradient = (2 * summation) / len(features)

		# gradient descent for bias
		updated_bias = initial_bias - learning_rate * bias_gradient

		# update parameters
		for i in range(len(initial_weights)):
			initial_weights[i] = updated_weights[i]
		initial_bias = updated_bias
	
	# round to nearest 4 decimals
	updated_weights = np.round(updated_weights, 4).tolist()
	updated_bias = round(updated_bias, 4)
	mse_values = np.round(mse_values, 4).tolist()

	return updated_weights, updated_bias, mse_values