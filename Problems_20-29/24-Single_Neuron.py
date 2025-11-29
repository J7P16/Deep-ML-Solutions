import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    # calculate probabilities from sigmoid
    probabilities = []
    for data in features:
        weighted_sum = 0
        for i in range(len(data)):
            weighted_sum += weights[i] * data[i]
        sigmoid_input = weighted_sum + bias
        probability = round(1 / (1 + math.e ** -sigmoid_input), 4)
        probabilities.append(probability)
    
    # calculate mean squared error
    summation = 0
    for i in range(len(probabilities)):
        summation += (probabilities[i] - labels[i]) ** 2
    mse = round(summation / len(probabilities), 4)
    
    return probabilities, mse